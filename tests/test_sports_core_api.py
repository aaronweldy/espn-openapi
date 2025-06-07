#!/usr/bin/env python3
"""
Test ESPN Sports Core API endpoints
Requires Python 3.10+
"""

import json
import pytest
import logging

from models.sports_core_api.espn_sports_core_api_client.models.sport_enum import (
    SportEnum,
)
from models.sports_core_api.espn_sports_core_api_client.models.league_enum import (
    LeagueEnum,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_athlete_details import (
    sync as get_athlete_details,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_athlete_statistics import (
    sync as get_athlete_statistics,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_athlete_statistics_log import (
    sync as get_athlete_statistics_log,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_league_calendar import (
    sync as get_league_calendar,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_league_venues import (
    sync as get_league_venues,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_league_franchises import (
    sync as get_league_franchises,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_league_seasons import (
    sync as get_league_seasons,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_league_season_weeks import (
    sync as get_league_season_weeks,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_league_events import (
    sync as get_league_events,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_league_event_details import (
    sync as get_league_event_details,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_team_injuries import (
    sync as get_team_injuries,
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
from models.sports_core_api.espn_sports_core_api_client.models.calendar_list_response import (
    CalendarListResponse,
)
from models.sports_core_api.espn_sports_core_api_client.models.team import Team
from models.sports_core_api.espn_sports_core_api_client.models.reference import (
    Reference,
)
from models.sports_core_api.espn_sports_core_api_client.models.paginated_reference_list_response import (
    PaginatedReferenceListResponse,
)
from models.sports_core_api.espn_sports_core_api_client.models.event_detail import (
    EventDetail,
)
from models.sports_core_api.espn_sports_core_api_client.types import UNSET
from models.sports_core_api.espn_sports_core_api_client.api.default.get_nfl_leaders import (
    sync as get_nfl_leaders,
)
from models.sports_core_api.espn_sports_core_api_client.models.nfl_leaders_response import (
    NflLeadersResponse,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_nfl_season_team import (
    sync as get_nfl_season_team,
)
from models.sports_core_api.espn_sports_core_api_client.models.core_nfl_season_team_response import (
    CoreNflSeasonTeamResponse,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_nfl_season_type_leaders import (
    sync as get_nfl_season_type_leaders,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_nfl_draft import (
    sync as get_nfl_draft,
)
from models.sports_core_api.espn_sports_core_api_client.models.nfl_draft_response import (
    NflDraftResponse,
)
from models.sports_core_api.espn_sports_core_api_client.models.get_league_season_weeks_season_type import (
    GetLeagueSeasonWeeksSeasonType,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_competition_detail import (
    sync as get_competition_detail,
)
from models.sports_core_api.espn_sports_core_api_client.models.competition_detail import (
    CompetitionDetail,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_competition_situation import (
    sync as get_competition_situation,
)
from models.sports_core_api.espn_sports_core_api_client.models.competition_situation_response import (
    CompetitionSituationResponse,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_competition_status import (
    sync as get_competition_status,
)
from models.sports_core_api.espn_sports_core_api_client.models.competition_status import (
    CompetitionStatus,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_competition_odds import (
    sync as get_competition_odds,
)
from models.sports_core_api.espn_sports_core_api_client.models.odds_response import (
    OddsResponse,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_competition_broadcasts import (
    sync as get_competition_broadcasts,
)
from models.sports_core_api.espn_sports_core_api_client.models.competition_broadcasts_response import (
    CompetitionBroadcastsResponse,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_competition_officials import (
    sync as get_competition_officials,
)
from models.sports_core_api.espn_sports_core_api_client.models.competition_officials_response import (
    CompetitionOfficialsResponse,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_competition_leaders import (
    sync as get_competition_leaders,
)
from models.sports_core_api.espn_sports_core_api_client.models.competition_leaders_response import (
    CompetitionLeadersResponse,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_competition_athlete_statistics import (
    sync as get_competition_athlete_statistics,
)
from models.sports_core_api.espn_sports_core_api_client.models.competition_athlete_statistics_response import (
    CompetitionAthleteStatisticsResponse,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_mlb_athlete_details import (
    sync as get_mlb_athlete_details,
)
from models.sports_core_api.espn_sports_core_api_client.models.mlb_athlete_details_response import (
    MlbAthleteDetailsResponse,
)


# Example athlete ID for testing
EXAMPLE_ATHLETE_ID = "3139477"  # Patrick Mahomes
EXAMPLE_MLB_ATHLETE_ID = "33192"  # Shohei Ohtani


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
    output = []
    output.append("=== ESPN Athlete Statistics ===")

    # Athlete reference
    athlete_ref = data.athlete
    if athlete_ref and athlete_ref.ref:
        output.append(f"Athlete Reference: {athlete_ref.ref}")

    # Splits and categories
    if data.splits and data.splits.categories:
        for category in data.splits.categories:
            # Skip empty categories
            if not category.stats:
                continue

            output.append(f"\n--- {category.name} ---")
            for stat in category.stats:
                display_value = (
                    stat.display_value
                    if hasattr(stat, "display_value")
                    and stat.display_value is not UNSET
                    else str(stat.value)
                )
                output.append(f"{stat.name}: {display_value}")

    return "\n".join(output)


def format_athlete_statistics_log(data: AthleteStatisticsLogResponse) -> str:
    """Format athlete statistics log for display."""
    output = []
    output.append("=== ESPN Athlete Statistics Log ===")

    # Check for entries
    if not data.entries:
        output.append("No statistics log entries found")
        return "\n".join(output)

    # Process each entry
    for i, entry in enumerate(data.entries):
        if i >= 5:  # Limit to 5 entries for readability
            output.append(f"\n... and {len(data.entries) - 5} more entries")
            break

        # Season info
        if entry.season and entry.season.ref:
            output.append(f"\n--- Entry {i + 1} (Season: {entry.season.ref}) ---")
        else:
            output.append(f"\n--- Entry {i + 1} ---")

        # Process statistics type entries
        if entry.statistics:
            for type_entry in entry.statistics:
                if type_entry.type:
                    # The type is a string, not an object with a name attribute
                    output.append(f"Type: {type_entry.type}")

                if type_entry.statistics and type_entry.statistics.ref:
                    output.append(f"Statistics Reference: {type_entry.statistics.ref}")

    return "\n".join(output)


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league,athlete_id",
    [
        (SportEnum.FOOTBALL, LeagueEnum.NFL, "14876"),  # Ryan Tannehill
        (SportEnum.BASKETBALL, LeagueEnum.NBA, "4011"),  # Ricky Rubio
        (SportEnum.BASEBALL, LeagueEnum.MLB, "6514"),  # Chris Young
        (SportEnum.HOCKEY, LeagueEnum.NHL, "3024816"),  # Austin Czarnik
    ],
)
def test_athlete_details(
    sports_core_api_client, ensure_json_output_dir, sport, league, athlete_id
):
    """Test fetching and parsing athlete details for multiple sports/leagues."""
    response = get_athlete_details(
        sport=sport,
        league=league,
        athlete_id=athlete_id,
        client=sports_core_api_client,
    )
    assert isinstance(response, AthleteDetailsResponse), (
        "Response should parse to AthleteDetailsResponse"
    )
    assert validate_athlete_details_response(response), (
        "Response does not match expected schema structure"
    )
    logging.info(
        f"Athlete: {response.full_name} ({response.id}) [{sport.value}/{league.value}]"
    )
    with open(
        f"{ensure_json_output_dir}/athlete_{sport.value}_{league.value}_{athlete_id}_details_processed.json",
        "w",
    ) as f:
        json.dump(response.to_dict(), f, indent=2)


@pytest.mark.api
def test_athlete_statistics(
    sports_core_api_client, ensure_json_output_dir, athlete_id: str = EXAMPLE_ATHLETE_ID
):
    """Test fetching and parsing NFL athlete statistics."""
    response = get_athlete_statistics(
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        athlete_id=athlete_id,
        client=sports_core_api_client,
    )
    assert isinstance(response, AthleteStatisticsResponse), (
        "Response should parse to AthleteStatisticsResponse"
    )
    assert validate_athlete_statistics_response(response), (
        "Response does not match expected schema structure"
    )
    logging.info(f"NFL Athlete Statistics for {athlete_id} fetched.")
    with open(
        f"{ensure_json_output_dir}/athlete_{athlete_id}_statistics_processed.json", "w"
    ) as f:
        json.dump(response.to_dict(), f, indent=2)


@pytest.mark.api
def test_athlete_statistics_log(
    sports_core_api_client, ensure_json_output_dir, athlete_id: str = EXAMPLE_ATHLETE_ID
):
    """Test fetching and parsing NFL athlete statistics log."""
    response = get_athlete_statistics_log(
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        athlete_id=athlete_id,
        client=sports_core_api_client,
    )
    assert isinstance(response, AthleteStatisticsLogResponse), (
        "Response should parse to AthleteStatisticsLogResponse"
    )
    assert validate_athlete_statistics_log_response(response), (
        "Response does not match expected schema structure"
    )
    logging.info(f"NFL Athlete Statistics Log for {athlete_id} fetched.")
    with open(
        f"{ensure_json_output_dir}/athlete_{athlete_id}_statistics_log_processed.json",
        "w",
    ) as f:
        json.dump(response.to_dict(), f, indent=2)


@pytest.mark.api
def test_league_calendar(
    sports_core_api_client,
    ensure_json_output_dir,
    sport: str = "football",
    league: str = "nfl",
):
    """Tests fetching the league calendar."""
    response = get_league_calendar(
        sport=SportEnum(sport),
        league=LeagueEnum(league),
        client=sports_core_api_client,
    )

    assert isinstance(response, CalendarListResponse), (
        "Response should parse to CalendarListResponse"
    )

    # Save the processed response
    with open(f"{ensure_json_output_dir}/league_{league}_calendar.json", "w") as f:
        json.dump(response.to_dict(), f, indent=2)

    # Verify basic structure
    assert response.items, "Response should contain items field"
    assert response.count > 0, "Calendar count should be > 0"


@pytest.mark.api
def test_league_venues(
    sports_core_api_client,
    ensure_json_output_dir,
    sport: str = "football",
    league: str = "nfl",
):
    """Tests fetching the league venues."""
    response = get_league_venues(
        sport=SportEnum(sport),
        league=LeagueEnum(league),
        client=sports_core_api_client,
    )

    assert isinstance(response, CalendarListResponse), (
        "Response should parse to CalendarListResponse"
    )

    # Save the processed response
    with open(f"{ensure_json_output_dir}/league_{league}_venues.json", "w") as f:
        json.dump(response.to_dict(), f, indent=2)

    # Verify basic structure
    assert response.items, "Response should contain items field"
    assert response.count > 0, "Venues count should be > 0"


@pytest.mark.api
def test_league_franchises(
    sports_core_api_client,
    ensure_json_output_dir,
    sport: str = "football",
    league: str = "nfl",
):
    """Tests fetching the league franchises."""
    response = get_league_franchises(
        sport=SportEnum(sport),
        league=LeagueEnum(league),
        client=sports_core_api_client,
    )

    assert isinstance(response, CalendarListResponse), (
        "Response should parse to CalendarListResponse"
    )

    # Save the processed response
    with open(f"{ensure_json_output_dir}/league_{league}_franchises.json", "w") as f:
        json.dump(response.to_dict(), f, indent=2)

    # Verify basic structure
    assert response.items, "Response should contain items field"
    assert response.count > 0, "Franchises count should be > 0"


@pytest.mark.api
def test_league_seasons(
    sports_core_api_client,
    ensure_json_output_dir,
    sport: str = "football",
    league: str = "nfl",
):
    """Tests fetching the league seasons."""
    response = get_league_seasons(
        sport=SportEnum(sport),
        league=LeagueEnum(league),
        client=sports_core_api_client,
    )

    assert isinstance(response, CalendarListResponse), (
        "Response should parse to CalendarListResponse"
    )

    # Save the processed response
    with open(f"{ensure_json_output_dir}/league_{league}_seasons.json", "w") as f:
        json.dump(response.to_dict(), f, indent=2)

    # Verify basic structure
    assert response.items, "Response should contain items field"
    assert response.count > 0, "Seasons count should be > 0"


@pytest.mark.api
def test_league_season_weeks(
    sports_core_api_client,
    ensure_json_output_dir,
    sport: str = "football",
    league: str = "nfl",
    year: int = 2024,
    season_type: int = 2,
):
    """Tests fetching the league season weeks."""
    response = get_league_season_weeks(
        sport=SportEnum(sport),
        league=LeagueEnum(league),
        year=year,
        season_type=GetLeagueSeasonWeeksSeasonType(season_type),
        client=sports_core_api_client,
    )

    assert isinstance(response, PaginatedReferenceListResponse), (
        "Response should parse to PaginatedReferenceListResponse"
    )

    # Save the processed response
    with open(
        f"{ensure_json_output_dir}/league_{league}_season_{year}_type_{season_type}_weeks.json",
        "w",
    ) as f:
        json.dump(response.to_dict(), f, indent=2)

    # Verify basic structure
    assert response.items, "Response should contain items field"
    assert response.count > 0, "Weeks count should be > 0"


@pytest.mark.api
def test_league_events(
    sports_core_api_client,
    ensure_json_output_dir,
    sport: str = "football",
    league: str = "nfl",
    week: int = 1,
    season: int = 2025,
    seasontypes: str = "2",
):
    """Tests fetching league events."""
    response = get_league_events(
        sport=SportEnum(sport),
        league=LeagueEnum(league),
        week=week,
        season=season,
        seasontypes=seasontypes,
        client=sports_core_api_client,
    )

    assert isinstance(response, PaginatedReferenceListResponse), (
        "Response should parse to PaginatedReferenceListResponse"
    )

    # Save the processed response
    with open(
        f"{ensure_json_output_dir}/league_{league}_events_week_{week}_season_{season}.json",
        "w",
    ) as f:
        json.dump(response.to_dict(), f, indent=2)

    # Verify basic structure
    assert response.items, "Response should contain items field"
    assert response.count >= 0, "Events count should be >= 0"


@pytest.mark.api
def test_league_event_details(
    sports_core_api_client,
    ensure_json_output_dir,
    sport: SportEnum = SportEnum.FOOTBALL,
    league: LeagueEnum = LeagueEnum.NFL,
    event_id: str = "401772510",
):
    """Tests fetching event details."""
    response = get_league_event_details(
        sport=sport,
        league=league,
        event_id=event_id,
        client=sports_core_api_client,
    )

    assert isinstance(response, EventDetail), "Response should parse to EventDetail"

    # Save the processed response
    with open(f"{ensure_json_output_dir}/event_{event_id}_details.json", "w") as f:
        json.dump(response.to_dict(), f, indent=2)

    # Verify basic structure
    assert response.id == event_id, f"Event ID mismatch: {response.id} != {event_id}"
    assert response.competitions, "Response should contain competitions field"


@pytest.mark.api
def test_nfl_league_leaders(
    sports_core_api_client, ensure_json_output_dir, limit: int = 5
):
    """Tests fetching NFL league leaders."""
    response = get_nfl_leaders(
        client=sports_core_api_client,
        limit=limit,
    )

    assert isinstance(response, NflLeadersResponse), (
        "Response should parse to NflLeadersResponse"
    )

    # Verify basic structure
    assert response.categories, "Response should contain categories field"

    # Save the processed response
    with open(f"{ensure_json_output_dir}/nfl_leaders_processed.json", "w") as f:
        json.dump(response.to_dict(), f, indent=2)


@pytest.mark.api
def test_nfl_season_team(
    sports_core_api_client,
    ensure_json_output_dir,
    year: int = 2024,
    team_id: str = "12",
):
    """Tests fetching NFL season team data."""
    response = get_nfl_season_team(
        client=sports_core_api_client,
        year=year,
        team_id=team_id,
    )

    assert isinstance(response, CoreNflSeasonTeamResponse), (
        "Response should parse to CoreNflSeasonTeamResponse"
    )

    # Save the processed response
    with open(
        f"{ensure_json_output_dir}/nfl_season_team_{team_id}_{year}_processed.json", "w"
    ) as f:
        json.dump(response.to_dict(), f, indent=2)


@pytest.mark.api
def test_nfl_team_injuries(
    sports_core_api_client, ensure_json_output_dir, team_id: str = "1"
):
    """Tests fetching NFL team injuries."""
    response = get_team_injuries(
        sport="football",
        league="nfl",
        team_id=team_id,
        client=sports_core_api_client,
    )

    assert isinstance(response, PaginatedReferenceListResponse), (
        "Response should parse to PaginatedReferenceListResponse"
    )

    # Save the processed response
    with open(f"{ensure_json_output_dir}/nfl_team_{team_id}_injuries.json", "w") as f:
        json.dump(response.to_dict(), f, indent=2)

    assert response.items is not None, "Response should contain items field"

    # Display summary if items exist
    if response.items:
        print(f"\nFound {len(response.items)} injured players for team {team_id}")

        for i, injury_ref in enumerate(response.items[:5]):  # Limit to first 5
            if i >= 5:  # Safety check
                print(f"... and {len(response.items) - 5} more injured players")
                break

            if injury_ref.ref:
                # Instead of making a direct request, we could use another API call
                # if there's a specific client method for fetching injury details
                # For now, just display the reference
                print(f"\nInjury Reference: {injury_ref.ref}")
    else:
        print(f"\nNo injured players found for team {team_id}")


@pytest.mark.api
def test_nfl_season_type_leaders(
    sports_core_api_client,
    ensure_json_output_dir,
    year: int = 2023,
    seasontype: int = 2,
    limit: int = 5,
):
    """Tests fetching NFL season type leaders."""
    response = get_nfl_season_type_leaders(
        client=sports_core_api_client,
        year=year,
        seasontype=seasontype,
        limit=limit,
    )

    assert isinstance(response, NflLeadersResponse), (
        "Response should parse to NflLeadersResponse"
    )

    # Verify basic structure
    assert response.categories, "Response should contain categories field"

    # Save the processed response
    with open(
        f"{ensure_json_output_dir}/nfl_season_type_leaders_{year}_{seasontype}_processed.json",
        "w",
    ) as f:
        json.dump(response.to_dict(), f, indent=2)


@pytest.mark.api
def test_nfl_draft(sports_core_api_client, ensure_json_output_dir, year: int = 2023):
    """Tests fetching NFL draft data."""
    response = get_nfl_draft(
        client=sports_core_api_client,
        year=year,
    )

    assert isinstance(response, NflDraftResponse), (
        "Response should parse to NflDraftResponse"
    )

    # Save the processed response
    with open(f"{ensure_json_output_dir}/nfl_draft_{year}_processed.json", "w") as f:
        json.dump(response.to_dict(), f, indent=2)


@pytest.mark.api
def test_competition_detail(sports_core_api_client, ensure_json_output_dir):
    """Test the competition detail endpoint for a known NFL event/competition."""
    sport = SportEnum.FOOTBALL
    league = LeagueEnum.NFL
    event_id = "401547417"
    competition_id = "401547417"

    result = get_competition_detail(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        client=sports_core_api_client,
    )

    assert isinstance(result, CompetitionDetail), (
        f"Expected CompetitionDetail, got {type(result)}"
    )
    assert result.id == competition_id, (
        f"Competition ID mismatch: {result.id} != {competition_id}"
    )
    assert result.venue, "Venue should be present"
    assert result.competitors, "Competitors should be present"
    assert result.status, "Status should be present"
    assert result.links, "Links should be present"

    # Save the response for inspection
    with open(f"json_output/competition_{competition_id}.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)


@pytest.mark.api
def test_competition_situation(sports_core_api_client):
    """Test the competition situation endpoint with a valid NFL event/competition."""
    sport = SportEnum.FOOTBALL
    league = LeagueEnum.NFL
    event_id = "401220403"
    competition_id = "401220403"
    result = get_competition_situation(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        client=sports_core_api_client,
    )
    assert isinstance(result, CompetitionSituationResponse), (
        f"Expected CompetitionSituationResponse, got {type(result)}"
    )
    assert result.ref, "Missing $ref in response"
    assert result.last_play, "Missing last_play in response"
    assert isinstance(result.down, int), "down should be int"
    assert isinstance(result.yard_line, int), "yard_line should be int"
    assert isinstance(result.distance, int), "distance should be int"
    assert isinstance(result.is_red_zone, bool), "is_red_zone should be bool"
    assert isinstance(result.home_timeouts, int), "home_timeouts should be int"
    assert isinstance(result.away_timeouts, int), "away_timeouts should be int"


@pytest.mark.api
def test_competition_status(sports_core_api_client):
    """Test the /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/status endpoint."""
    sport = SportEnum.FOOTBALL
    league = LeagueEnum.NFL
    event_id = "401326638"
    competition_id = "401326638"
    result = get_competition_status(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        client=sports_core_api_client,
    )
    assert isinstance(result, CompetitionStatus), (
        f"Expected CompetitionStatus, got {type(result)}"
    )
    assert result.ref, "Missing $ref in CompetitionStatus"
    assert result.clock is not None, "Missing clock in CompetitionStatus"
    assert result.display_clock, "Missing display_clock in CompetitionStatus"
    assert result.period is not None, "Missing period in CompetitionStatus"
    assert result.type, "Missing type in CompetitionStatus"
    assert result.type.id, "Missing id in CompetitionStatus.type"
    assert result.type.name, "Missing name in CompetitionStatus.type"
    assert result.type.state, "Missing state in CompetitionStatus.type"
    assert result.type.description, "Missing description in CompetitionStatus.type"
    assert result.type.detail, "Missing detail in CompetitionStatus.type"
    assert result.type.short_detail, "Missing short_detail in CompetitionStatus.type"


@pytest.mark.api
def test_competition_odds(sports_core_api_client):
    """Test the /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/odds endpoint."""
    sport = SportEnum.FOOTBALL
    league = LeagueEnum.NFL
    event_id = "401220181"
    competition_id = "401220181"
    response = get_competition_odds(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        client=sports_core_api_client,
    )
    assert response is not None, "No response returned from get_competition_odds"
    assert isinstance(response, OddsResponse), (
        f"Response should be OddsResponse, got {type(response)}"
    )
    assert response.items, "OddsResponse.items should not be empty"


@pytest.mark.api
def test_competition_broadcasts(sports_core_api_client, ensure_json_output_dir):
    """Test the /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/broadcasts endpoint."""
    sport = SportEnum.FOOTBALL
    league = LeagueEnum.NFL
    event_id = "401547417"
    competition_id = "401547417"
    response = get_competition_broadcasts(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        client=sports_core_api_client,
    )
    assert isinstance(response, CompetitionBroadcastsResponse), (
        f"Expected CompetitionBroadcastsResponse, got {type(response)}"
    )
    assert response.items, "BroadcastsResponse.items should not be empty"
    # Save the response for inspection
    with open(f"json_output/competition_{competition_id}_broadcasts.json", "w") as f:
        json.dump(response.to_dict(), f, indent=2)


@pytest.mark.api
def test_competition_officials(sports_core_api_client, ensure_json_output_dir):
    """Test the /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/officials endpoint."""
    sport = SportEnum.FOOTBALL
    league = LeagueEnum.NFL
    event_id = "401547417"
    competition_id = "401547417"
    response = get_competition_officials(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        client=sports_core_api_client,
    )
    assert isinstance(response, CompetitionOfficialsResponse), (
        f"Expected CompetitionOfficialsResponse, got {type(response)}"
    )
    assert response.items, "OfficialsResponse.items should not be empty"
    # Save the response for inspection
    with open(f"json_output/competition_{competition_id}_officials.json", "w") as f:
        json.dump(response.to_dict(), f, indent=2)


@pytest.mark.api
def test_competition_leaders(sports_core_api_client, ensure_json_output_dir):
    """Test the /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/leaders endpoint."""
    sport = SportEnum.FOOTBALL
    league = LeagueEnum.NFL
    event_id = "401547417"
    competition_id = "401547417"
    response = get_competition_leaders(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        client=sports_core_api_client,
    )
    assert isinstance(response, CompetitionLeadersResponse), (
        f"Expected CompetitionLeadersResponse, got {type(response)}"
    )
    assert response.categories, "LeadersResponse.categories should not be empty"
    # Save the response for inspection
    with open(f"json_output/competition_{competition_id}_leaders.json", "w") as f:
        json.dump(response.to_dict(), f, indent=2)


@pytest.mark.api
def test_competition_athlete_statistics(sports_core_api_client, ensure_json_output_dir):
    """Test the /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/competitors/{competitor_id}/roster/{athlete_id}/statistics/{page} endpoint."""
    sport = SportEnum.FOOTBALL
    league = LeagueEnum.NFL
    event_id = "401547417"
    competition_id = "401547417"
    competitor_id = "1"
    athlete_id = "4426502"
    page = 0

    response = get_competition_athlete_statistics(
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        competitor_id=competitor_id,
        athlete_id=athlete_id,
        page=page,
        client=sports_core_api_client,
    )

    assert isinstance(response, CompetitionAthleteStatisticsResponse), (
        f"Expected CompetitionAthleteStatisticsResponse, got {type(response)}"
    )
    assert response.splits, "Response should contain splits"
    assert response.splits.categories, "Splits should contain categories"

    # Save the response for inspection
    with open(
        f"json_output/competition_{competition_id}_athlete_{athlete_id}_statistics_{page}.json",
        "w",
    ) as f:
        json.dump(response.to_dict(), f, indent=2)


@pytest.mark.api
def test_mlb_athlete_details(sports_core_api_client, ensure_json_output_dir):
    """Test fetching and parsing MLB athlete details (Shohei Ohtani)."""
    athlete_id = EXAMPLE_MLB_ATHLETE_ID
    response = get_mlb_athlete_details(
        athlete_id=athlete_id,
        client=sports_core_api_client,
    )
    assert isinstance(response, MlbAthleteDetailsResponse), (
        "Response should parse to MlbAthleteDetailsResponse"
    )
    logging.info(f"MLB Athlete: {response.full_name} ({response.id})")
    with open(
        f"{ensure_json_output_dir}/mlb_athlete_{athlete_id}_details_processed.json", "w"
    ) as f:
        json.dump(response.to_dict(), f, indent=2)


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league",
    [
        ("football", "nfl"),
        ("baseball", "mlb"),
        ("basketball", "nba"),
        ("hockey", "nhl"),
        ("soccer", "uefa.champions"),
    ],
)
def test_positions_list(sports_core_api_client, ensure_json_output_dir, sport, league):
    """Test fetching and parsing the positions list endpoint for various sports/leagues."""
    from models.sports_core_api.espn_sports_core_api_client.api.default.get_positions_list import (
        sync_detailed as get_positions_list_sync_detailed,
    )
    from models.sports_core_api.espn_sports_core_api_client.models.positions_list_response import (
        PositionsListResponse,
    )

    limit = 10
    response = get_positions_list_sync_detailed(
        sport=sport,
        league=league,
        client=sports_core_api_client,
        limit=limit,
    )
    if response.status_code != 200:
        print(f"Status code: {response.status_code}")
        print(f"Response content: {response.content}")
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}. Response content: {response.content}"
    )
    result = response.parsed
    if not isinstance(result, PositionsListResponse):
        print(f"Parsed result type: {type(result)}")
        print(f"Parsed result: {result}")
    assert isinstance(result, PositionsListResponse), (
        f"Response should parse to PositionsListResponse, got {type(result)}"
    )

    # Save processed response for analysis
    out_path = f"{ensure_json_output_dir}/{sport}_{league}_positions_processed.json"
    with open(out_path, "w") as f:
        import json

        json.dump(result.to_dict(), f, indent=2)
    print(f"✓ Processed response saved to {out_path}")
