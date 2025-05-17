#!/usr/bin/env python3
"""
Test ESPN Sports Core API endpoints
Requires Python 3.10+
"""

import json
import os
import traceback
from typing import Any, Dict, Optional

import requests
from models.sports_core_api.espn_sports_core_api_client import Client
from models.sports_core_api.espn_sports_core_api_client.api.default.get_nfl_athlete_details import (
    sync as get_athlete_details,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_nfl_athlete_statistics import (
    sync as get_athlete_statistics,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_nfl_athlete_statistics_log import (
    sync as get_athlete_statistics_log,
)
from models.sports_core_api.espn_sports_core_api_client.models.error_response import (
    ErrorResponse,
)
from models.sports_core_api.espn_sports_core_api_client.models.athlete_details_response import (
    AthleteDetailsResponse,
)
from models.sports_core_api.espn_sports_core_api_client.models.athlete_statistics_response import (
    AthleteStatisticsResponse,
)
from models.sports_core_api.espn_sports_core_api_client.models.athlete_statistics_log_response import (
    AthleteStatisticsLogResponse,
)
from models.sports_core_api.espn_sports_core_api_client.models.team import Team
from models.sports_core_api.espn_sports_core_api_client.models.reference import (
    Reference,
)
from models.sports_core_api.espn_sports_core_api_client.types import UNSET
from models.sports_core_api.espn_sports_core_api_client.api.default.get_nfl_leaders import (
    sync as get_nfl_leaders,
)
from models.sports_core_api.espn_sports_core_api_client.models.nfl_leaders_response import (
    NflLeadersResponse,
)
from models.sports_core_api.espn_sports_core_api_client.models.nfl_leaders_category import (
    NflLeadersCategory,
)
from models.sports_core_api.espn_sports_core_api_client.models.nfl_leader import (
    NflLeader,
)


# Example athlete ID for testing
EXAMPLE_ATHLETE_ID = "3139477"  # Patrick Mahomes


def validate_athlete_details_response(data: AthleteDetailsResponse) -> bool:
    """Validate if athlete details response matches expected schema structure."""
    # Required fields for the main Athlete object
    required_attrs = ["id", "uid", "full_name", "position"]
    for attr in required_attrs:
        # Use snake_case for attribute access in Python models
        py_attr = attr.replace("fullName", "full_name")
        if getattr(data, py_attr, UNSET) is UNSET:
            print(f"Missing required athlete attribute: {py_attr}")
            return False

    # Check position
    position = data.position
    if not position or getattr(position, "name", UNSET) is UNSET:
        print("Invalid position structure: missing name")
        return False

    # Check team if present (team is just a reference here)
    if data.team and getattr(data.team, "ref", UNSET) is UNSET:
        print("Invalid team reference structure: missing $ref")
        return False

    return True


def validate_athlete_statistics_response(data: AthleteStatisticsResponse) -> bool:
    """Validate if athlete statistics response matches expected schema structure."""
    if (
        getattr(data, "athlete", UNSET) is UNSET
        or getattr(data, "splits", UNSET)
        is UNSET  # Check for splits instead of categories
    ):
        print("Missing required attributes: athlete or splits")
        return False

    # Check athlete reference
    athlete_ref = data.athlete
    if not athlete_ref or getattr(athlete_ref, "ref", UNSET) is UNSET:  # Check for $ref
        print("Invalid athlete reference structure: missing $ref")
        return False

    # Check splits and categories
    splits = data.splits
    if not splits or getattr(splits, "categories", UNSET) is UNSET:
        print("Invalid splits structure: missing categories")
        return False

    if not splits.categories:
        print("No categories found or categories list is empty")
        # This might be acceptable in some cases, return True
        return True

    category = splits.categories[0]
    if (
        getattr(category, "name", UNSET) is UNSET
        or getattr(category, "stats", UNSET) is UNSET
    ):
        print("Invalid category structure: missing name or stats")
        return False

    # Check statistics (now 'stats')
    if not category.stats:
        print("No statistics found in category")
        return False

    stat = category.stats[0]
    if getattr(stat, "name", UNSET) is UNSET or getattr(stat, "value", UNSET) is UNSET:
        print("Invalid statistic structure: missing name or value")
        return False

    return True


def validate_athlete_statistics_log_response(
    data: AthleteStatisticsLogResponse,
) -> bool:
    """Validate if athlete statistics log response matches expected schema structure."""
    # Athlete is no longer expected at the top level
    if getattr(data, "entries", UNSET) is UNSET:
        print("Missing required attributes: entries")
        return False

    # Check entries
    if not data.entries:
        # This might be acceptable for some athletes with no statistics log
        print("No entries found or entries list is empty")
        return True

    entry = data.entries[0]
    # Event is not present, check for season and statistics refs
    if (
        getattr(entry, "season", UNSET) is UNSET
        or getattr(entry, "statistics", UNSET) is UNSET
    ):
        print("Invalid entry structure: missing season or statistics")
        return False

    # Check season reference
    season_ref = entry.season
    if not season_ref or getattr(season_ref, "ref", UNSET) is UNSET:
        print("Invalid season structure: missing $ref")
        return False

    # Check statistics array
    if not entry.statistics:
        print("No statistics references found in entry")
        return False

    # Check first statistics type entry reference
    stats_type_entry = entry.statistics[0]
    if (
        getattr(stats_type_entry, "type", UNSET) is UNSET
        or getattr(stats_type_entry, "statistics", UNSET) is UNSET
    ):
        print(
            "Invalid StatisticsTypeEntry structure: missing type or statistics reference"
        )
        return False

    # Check statistics reference itself
    stats_ref = stats_type_entry.statistics
    if not stats_ref or getattr(stats_ref, "ref", UNSET) is UNSET:
        print("Invalid StatisticsReference structure: missing $ref")
        return False

    return True


def format_athlete_details(data: AthleteDetailsResponse) -> str:
    """Format athlete details for display."""
    output = []
    output.append("=== ESPN Athlete Details ===")
    output.append(f"Name: {data.full_name}")

    if data.position:
        output.append(f"Position: {data.position.name} ({data.position.abbreviation})")

    if data.team:
        # Check if team is a full Team object or just a Reference
        if isinstance(data.team, Team) and data.team.display_name:
            output.append(f"Team: {data.team.display_name}")
        elif isinstance(data.team, Reference) and data.team.ref:
            output.append(f"Team Reference: {data.team.ref}")
        else:
            # Handle unexpected case or missing data gracefully
            output.append("Team: Info Unavailable")

    if data.jersey:
        output.append(f"Jersey: #{data.jersey}")

    if data.height and data.weight:
        output.append(f"Height/Weight: {data.display_height} / {data.display_weight}")

    if data.date_of_birth:
        output.append(f"Date of Birth: {data.date_of_birth}")

    if data.age:
        output.append(f"Age: {data.age}")

    if data.experience and data.experience.display_value:
        output.append(f"Experience: {data.experience.display_value}")

    return "\n".join(output)


def format_athlete_statistics(data: AthleteStatisticsResponse) -> str:
    """Format athlete statistics for display."""
    # Check splits instead of categories at the top level
    if not data.athlete or not data.splits or not data.splits.categories:
        return "Invalid data format: missing athlete or categories in splits"

    output = []
    output.append("=== ESPN Athlete Statistics ===")
    # Athlete is now a reference, so display its $ref URL
    if data.athlete and data.athlete.ref:
        output.append(f"Athlete Reference: {data.athlete.ref}")
    else:
        output.append("Athlete Reference: Not available")

    # Season is optional now
    if data.season:
        season_type = (
            "Regular Season"
            if data.season.type == 2
            else "Postseason"
            if data.season.type == 3
            else "Preseason"
        )
        output.append(f"Season: {data.season.year} ({season_type})")

    # Iterate through categories within splits
    for category in data.splits.categories:
        output.append(f"\n=== {category.display_name} ===")

        # Use 'stats' instead of 'statistics'
        if not category.stats:
            output.append("No statistics available")
            continue

        # Display statistics in a tabular format
        for stat in category.stats:
            if stat.display_name and stat.display_value:
                output.append(f"{stat.display_name}: {stat.display_value}")

    return "\n".join(output)


def format_athlete_statistics_log(data: AthleteStatisticsLogResponse) -> str:
    """Format athlete statistics log for display."""
    # Athlete is no longer expected at the top level
    # if not data.athlete:
    #     return "Invalid data format: missing athlete"

    output = []
    output.append("=== ESPN Athlete Statistics Log ===")
    # Output the main reference URL instead of athlete name
    if data.ref:
        output.append(f"Log Reference: {data.ref}")
    # output.append(f"Athlete: {data.athlete.display_name}") # Removed

    if not data.entries:
        output.append("\nNo statistics log entries available")
        return "\n".join(output)

    # Display summary of entries, focusing on the references
    output.append("\nLog Entries (Season and Stat Refs):")
    for i, entry in enumerate(data.entries[:5]):  # Limit for brevity
        if not entry.season or not entry.season.ref:
            continue

        season_ref = entry.season.ref
        output.append(f"\nEntry {i + 1}:")
        output.append(f"  Season Ref: {season_ref}")

        # Display the stat references within the entry
        if entry.statistics:
            output.append("  Statistics Refs:")
            for stat_entry in entry.statistics:
                if (
                    stat_entry.type
                    and stat_entry.statistics
                    and stat_entry.statistics.ref
                ):
                    output.append(
                        f"    Type: {stat_entry.type}, Ref: {stat_entry.statistics.ref}"
                    )
        else:
            output.append("  No statistics references found for this entry.")

    # Note: Detailed event info and stats are not directly available here.
    # The original formatting code that accessed entry.event and detailed stats
    # is removed as it's incompatible with the actual API structure.
    # To get details, one would need to follow the $ref links.

    return "\n".join(output)


def fetch_direct(url: str) -> Optional[Dict[str, Any]]:
    """Fetch data directly using requests to bypass model issues."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    print(f"Error fetching {url}: {response.status_code}")
    return None


def test_athlete_details(athlete_id: str = EXAMPLE_ATHLETE_ID):
    """Test athlete details endpoint."""
    print("\nTesting NFL Athlete Details endpoint")
    print("-" * 50)

    client = Client(base_url="https://sports.core.api.espn.com")

    # Direct request as fallback
    direct_url = f"https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes/{athlete_id}"
    athlete_json = fetch_direct(direct_url)

    if not athlete_json:
        print("✗ Failed to fetch athlete details directly")
        return False

    # Save the raw JSON for analysis
    with open(f"json_output/nfl_athlete_{athlete_id}_direct.json", "w") as f:
        json.dump(athlete_json, f, indent=2)

    print("✓ Successfully fetched athlete details directly")

    # Try using the generated client
    try:
        athlete_data = get_athlete_details(athlete_id=athlete_id, client=client)

        if isinstance(athlete_data, ErrorResponse):
            print("✗ API returned an error response:")
            print(
                athlete_data.error.message
                if hasattr(athlete_data, "error")
                and athlete_data.error
                and hasattr(athlete_data.error, "message")
                else str(athlete_data)
            )
            return False
        elif isinstance(athlete_data, AthleteDetailsResponse):
            # Validate schema
            if validate_athlete_details_response(athlete_data):
                print("✓ Response matches expected schema structure")
            else:
                print("✗ Response does not match expected schema structure")
                return False

            # Display formatted summary
            print("\n" + format_athlete_details(athlete_data))

            # Save full response for analysis
            with open(f"json_output/nfl_athlete_{athlete_id}_processed.json", "w") as f:
                json.dump(athlete_data.to_dict(), f, indent=2)
            print(
                f"✓ Processed response saved to json_output/nfl_athlete_{athlete_id}_processed.json"
            )

            return True
        else:
            print("✗ Failed to fetch athlete details using client")
            return False
    except Exception as e:
        print(f"✗ Error using generated client: {str(e)}")
        print(traceback.format_exc())
        return False


def test_athlete_statistics(athlete_id: str = EXAMPLE_ATHLETE_ID):
    """Test athlete statistics endpoint."""
    print("\nTesting NFL Athlete Statistics endpoint")
    print("-" * 50)

    client = Client(base_url="https://sports.core.api.espn.com")

    # Direct request as fallback
    direct_url = f"https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes/{athlete_id}/statistics"
    stats_json = fetch_direct(direct_url)

    if not stats_json:
        print("✗ Failed to fetch athlete statistics directly")
        return False

    # Save the raw JSON for analysis
    with open(f"json_output/nfl_athlete_{athlete_id}_stats_direct.json", "w") as f:
        json.dump(stats_json, f, indent=2)

    print("✓ Successfully fetched athlete statistics directly")

    # Try using the generated client
    try:
        stats_data = get_athlete_statistics(athlete_id=athlete_id, client=client)

        if isinstance(stats_data, ErrorResponse):
            print("✗ API returned an error response:")
            print(
                stats_data.error.message
                if hasattr(stats_data, "error")
                and stats_data.error
                and hasattr(stats_data.error, "message")
                else str(stats_data)
            )
            return False
        elif isinstance(stats_data, AthleteStatisticsResponse):
            # Validate schema
            if validate_athlete_statistics_response(stats_data):
                print("✓ Response matches expected schema structure")
            else:
                print("✗ Response does not match expected schema structure")
                return False

            # Display formatted summary
            print("\n" + format_athlete_statistics(stats_data))

            # Save full response for analysis
            with open(
                f"json_output/nfl_athlete_{athlete_id}_stats_processed.json", "w"
            ) as f:
                json.dump(stats_data.to_dict(), f, indent=2)
            print(
                f"✓ Processed response saved to json_output/nfl_athlete_{athlete_id}_stats_processed.json"
            )

            return True
        else:
            print("✗ Failed to fetch athlete statistics using client")
            return False
    except Exception as e:
        print(f"✗ Error using generated client: {str(e)}")
        print(traceback.format_exc())
        return False


def test_athlete_statistics_log(athlete_id: str = EXAMPLE_ATHLETE_ID):
    """Test athlete statistics log endpoint."""
    print("\nTesting NFL Athlete Statistics Log endpoint")
    print("-" * 50)

    client = Client(base_url="https://sports.core.api.espn.com")

    # Direct request as fallback
    direct_url = f"https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes/{athlete_id}/statisticslog"
    log_json = fetch_direct(direct_url)

    if not log_json:
        print("✗ Failed to fetch athlete statistics log directly")
        return False

    # Save the raw JSON for analysis
    with open(f"json_output/nfl_athlete_{athlete_id}_log_direct.json", "w") as f:
        json.dump(log_json, f, indent=2)

    print("✓ Successfully fetched athlete statistics log directly")

    # Try using the generated client
    try:
        log_data = get_athlete_statistics_log(athlete_id=athlete_id, client=client)

        if isinstance(log_data, ErrorResponse):
            print("✗ API returned an error response:")
            print(
                log_data.error.message
                if hasattr(log_data, "error")
                and log_data.error
                and hasattr(log_data.error, "message")
                else str(log_data)
            )
            return False
        elif isinstance(log_data, AthleteStatisticsLogResponse):
            # Validate schema
            if validate_athlete_statistics_log_response(log_data):
                print("✓ Response matches expected schema structure")
            else:
                print("✗ Response does not match expected schema structure")
                return False

            # Display formatted summary
            print("\n" + format_athlete_statistics_log(log_data))

            # Save full response for analysis
            with open(
                f"json_output/nfl_athlete_{athlete_id}_log_processed.json", "w"
            ) as f:
                json.dump(log_data.to_dict(), f, indent=2)
            print(
                f"✓ Processed response saved to json_output/nfl_athlete_{athlete_id}_log_processed.json"
            )

            return True
        else:
            print("✗ Failed to fetch athlete statistics log using client")
            return False
    except Exception as e:
        print(f"✗ Error using generated client: {str(e)}")
        print(traceback.format_exc())
        return False


def test_league_calendar(sport: str = "football", league: str = "nfl"):
    from models.sports_core_api.espn_sports_core_api_client import Client
    from models.sports_core_api.espn_sports_core_api_client.api.default.get_league_calendar import (
        sync as get_league_calendar,
    )
    from models.sports_core_api.espn_sports_core_api_client.models.calendar_list_response import (
        CalendarListResponse,
    )
    from models.sports_core_api.espn_sports_core_api_client.models.reference import (
        Reference,
    )
    from models.sports_core_api.espn_sports_core_api_client.models.error_response import (
        ErrorResponse,
    )
    from models.sports_core_api.espn_sports_core_api_client.types import UNSET

    client = Client(base_url="https://sports.core.api.espn.com")
    response = get_league_calendar(sport=sport, league=league, client=client)
    assert response is not None, "No response returned from calendar endpoint"
    assert isinstance(response, CalendarListResponse), (
        f"Unexpected response type: {type(response)}"
    )
    assert response.count > 0, "Calendar count should be > 0"
    assert isinstance(response.items, list), "Items should be a list"
    for item in response.items:
        assert isinstance(item, Reference), f"Item is not a Reference: {type(item)}"
        assert item.ref.startswith("http"), (
            f"Reference $ref does not look like a URL: {item.ref}"
        )
    print(f"Calendar test passed: {response.count} items found.")


def test_league_venues(sport: str = "football", league: str = "nfl"):
    from models.sports_core_api.espn_sports_core_api_client import Client
    from models.sports_core_api.espn_sports_core_api_client.api.default.get_league_venues import (
        sync as get_league_venues,
    )
    from models.sports_core_api.espn_sports_core_api_client.models.calendar_list_response import (
        CalendarListResponse,
    )
    from models.sports_core_api.espn_sports_core_api_client.models.reference import (
        Reference,
    )

    client = Client(base_url="https://sports.core.api.espn.com")
    response = get_league_venues(sport=sport, league=league, client=client)
    assert response is not None, "No response returned from venues endpoint"
    assert isinstance(response, CalendarListResponse), (
        f"Unexpected response type: {type(response)}"
    )
    assert response.count > 0, "Venues count should be > 0"
    for item in response.items:
        assert isinstance(item, Reference), f"Item is not a Reference: {type(item)}"
        assert item.ref.startswith("http"), (
            f"Reference $ref does not look like a URL: {item.ref}"
        )
    print(f"Venues test passed: {response.count} items found.")


def test_league_franchises(sport: str = "football", league: str = "nfl"):
    from models.sports_core_api.espn_sports_core_api_client import Client
    from models.sports_core_api.espn_sports_core_api_client.api.default.get_league_franchises import (
        sync as get_league_franchises,
    )
    from models.sports_core_api.espn_sports_core_api_client.models.calendar_list_response import (
        CalendarListResponse,
    )
    from models.sports_core_api.espn_sports_core_api_client.models.reference import (
        Reference,
    )

    client = Client(base_url="https://sports.core.api.espn.com")
    response = get_league_franchises(sport=sport, league=league, client=client)
    assert response is not None, "No response returned from franchises endpoint"
    assert isinstance(response, CalendarListResponse), (
        f"Unexpected response type: {type(response)}"
    )
    assert response.count > 0, "Franchises count should be > 0"
    for item in response.items:
        assert isinstance(item, Reference), f"Item is not a Reference: {type(item)}"
        assert item.ref.startswith("http"), (
            f"Reference $ref does not look like a URL: {item.ref}"
        )
    print(f"Franchises test passed: {response.count} items found.")


def test_league_seasons(sport: str = "football", league: str = "nfl"):
    from models.sports_core_api.espn_sports_core_api_client import Client
    from models.sports_core_api.espn_sports_core_api_client.api.default.get_league_seasons import (
        sync as get_league_seasons,
    )
    from models.sports_core_api.espn_sports_core_api_client.models.calendar_list_response import (
        CalendarListResponse,
    )
    from models.sports_core_api.espn_sports_core_api_client.models.reference import (
        Reference,
    )

    client = Client(base_url="https://sports.core.api.espn.com")
    response = get_league_seasons(sport=sport, league=league, client=client)
    assert response is not None, "No response returned from seasons endpoint"
    assert isinstance(response, CalendarListResponse), (
        f"Unexpected response type: {type(response)}"
    )
    assert response.count > 0, "Seasons count should be > 0"
    for item in response.items:
        assert isinstance(item, Reference), f"Item is not a Reference: {type(item)}"
        assert item.ref.startswith("http"), (
            f"Reference $ref does not look like a URL: {item.ref}"
        )
    print(f"Seasons test passed: {response.count} items found.")


def test_league_season_weeks(
    sport: str = "football", league: str = "nfl", year: int = 2024, season_type: int = 2
):
    from models.sports_core_api.espn_sports_core_api_client import Client
    from models.sports_core_api.espn_sports_core_api_client.api.default.get_league_season_weeks import (
        sync as get_league_season_weeks,
    )
    from models.sports_core_api.espn_sports_core_api_client.models.paginated_reference_list_response import (
        PaginatedReferenceListResponse,
    )
    from models.sports_core_api.espn_sports_core_api_client.models.reference import (
        Reference,
    )
    from models.sports_core_api.espn_sports_core_api_client.models.get_league_season_weeks_season_type import (
        GetLeagueSeasonWeeksSeasonType,
    )

    client = Client(base_url="https://sports.core.api.espn.com")
    response = get_league_season_weeks(
        sport=sport,
        league=league,
        year=year,
        season_type=GetLeagueSeasonWeeksSeasonType(season_type),
        client=client,
    )
    assert response is not None, "No response returned from weeks endpoint"
    assert isinstance(response, PaginatedReferenceListResponse), (
        f"Unexpected response type: {type(response)}"
    )
    assert response.count > 0, "Weeks count should be > 0"
    for item in response.items:
        assert isinstance(item, Reference), f"Item is not a Reference: {type(item)}"
        assert item.ref.startswith("http"), (
            f"Reference $ref does not look like a URL: {item.ref}"
        )
    print(f"Weeks test passed: {response.count} items found.")


def test_league_events(
    sport: str = "football",
    league: str = "nfl",
    week: int = 1,
    season: int = 2025,
    seasontypes: str = "2",
):
    from models.sports_core_api.espn_sports_core_api_client import Client
    from models.sports_core_api.espn_sports_core_api_client.api.default.get_league_events import (
        sync as get_league_events,
    )
    from models.sports_core_api.espn_sports_core_api_client.models.paginated_reference_list_response import (
        PaginatedReferenceListResponse,
    )
    from models.sports_core_api.espn_sports_core_api_client.models.reference import (
        Reference,
    )

    client = Client(base_url="https://sports.core.api.espn.com")
    response = get_league_events(
        sport=sport,
        league=league,
        week=week,
        season=season,
        seasontypes=seasontypes,
        client=client,
    )
    assert response is not None, "No response returned from events endpoint"
    assert isinstance(response, PaginatedReferenceListResponse), (
        f"Unexpected response type: {type(response)}"
    )
    assert response.count > 0, "Events count should be > 0"
    for item in response.items:
        assert isinstance(item, Reference), f"Item is not a Reference: {type(item)}"
        assert item.ref.startswith("http"), (
            f"Reference $ref does not look like a URL: {item.ref}"
        )
    print(f"Events test passed: {response.count} items found.")


def test_league_event_details(
    sport: str = "football", league: str = "nfl", event_id: str = "401772510"
):
    from models.sports_core_api.espn_sports_core_api_client import Client
    from models.sports_core_api.espn_sports_core_api_client.api.default.get_league_event_details import (
        sync as get_league_event_details,
    )
    from models.sports_core_api.espn_sports_core_api_client.models.event_detail import (
        EventDetail,
    )

    client = Client(base_url="https://sports.core.api.espn.com")
    response = get_league_event_details(
        sport=sport,
        league=league,
        event_id=event_id,
        client=client,
    )
    assert response is not None, "No response returned from event details endpoint"
    assert isinstance(response, EventDetail), (
        f"Unexpected response type: {type(response)}"
    )
    assert response.id == event_id, f"Event ID mismatch: {response.id} != {event_id}"
    assert response.date, "Event date missing"
    assert response.competitions, "Event competitions missing"
    print(
        f"Event details test passed: {response.id} {response.name if hasattr(response, 'name') else ''}"
    )


def test_nfl_league_leaders(limit: int = 5):
    """Test the NFL league leaders endpoint and validate the response structure."""
    client = Client(base_url="https://sports.core.api.espn.com")
    data = get_nfl_leaders(client=client, limit=limit)
    assert isinstance(data, NflLeadersResponse), (
        f"Expected NflLeadersResponse, got {type(data)}"
    )
    print(f"NFL Leaders: {data.name} ({data.type}) - {len(data.categories)} categories")
    assert data.categories, "No categories returned in leaders response"
    first_cat = data.categories[0]
    assert isinstance(first_cat, NflLeadersCategory), (
        "First category is not NflLeadersCategory"
    )
    print(
        f"  Category: {first_cat.display_name} ({first_cat.abbreviation}) - {len(first_cat.leaders)} leaders"
    )
    assert first_cat.leaders, "No leaders in first category"
    first_leader = first_cat.leaders[0]
    assert isinstance(first_leader, NflLeader), "First leader is not NflLeader"
    print(
        f"    Leader: {first_leader.display_value} ({first_leader.value}) - Active: {first_leader.active}"
    )
    print(f"    Athlete ref: {first_leader.athlete.ref}")
    print(f"    Statistics ref: {first_leader.statistics.ref}")


def main():
    """Main function to test ESPN Sports Core API endpoints."""
    print("===== ESPN Sports Core API Test Script =====")

    # Create output directory if it doesn't exist
    os.makedirs("json_output", exist_ok=True)

    results = []

    # Test athlete details endpoint
    athlete_details_result = test_athlete_details()
    results.append(("NFL Athlete Details", athlete_details_result))

    # Test athlete statistics endpoint
    athlete_stats_result = test_athlete_statistics()
    results.append(("NFL Athlete Statistics", athlete_stats_result))

    # Test athlete statistics log endpoint
    athlete_log_result = test_athlete_statistics_log()
    results.append(("NFL Athlete Statistics Log", athlete_log_result))

    # Test league calendar endpoint
    test_league_calendar()

    # Test league venues endpoint
    test_league_venues()

    # Test league franchises endpoint
    test_league_franchises()

    # Test league seasons endpoint
    test_league_seasons()

    # Test league season weeks endpoint
    test_league_season_weeks()

    # Test league events endpoint
    test_league_events()

    # Test league event details endpoint
    test_league_event_details()

    # Test NFL league leaders endpoint
    test_nfl_league_leaders()

    # Summary
    print("\n===== Test Results Summary =====")
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{test_name}: {status}")


if __name__ == "__main__":
    main()
