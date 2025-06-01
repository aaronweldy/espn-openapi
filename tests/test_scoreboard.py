#!/usr/bin/env python3
"""
Test ESPN API - Scoreboard Endpoints
Includes tests for generic scoreboard endpoint and sport-specific night football endpoints
"""

import json
import pytest
import logging
from datetime import datetime

from models.site_api.espn_nfl_api_client.api.default import get_scoreboard
from models.site_api.espn_nfl_api_client.models.error_response import ErrorResponse
from models.site_api.espn_nfl_api_client.models.generic_scoreboard_response import (
    GenericScoreboardResponse,
)
from models.site_api.espn_nfl_api_client.models.get_scoreboard_sport import (
    GetScoreboardSport,
)
from models.site_api.espn_nfl_api_client.models.get_scoreboard_seasontype import (
    GetScoreboardSeasontype,
)
from models.site_api.espn_nfl_api_client.types import UNSET

from models.site_api.espn_nfl_api_client.api.default.get_monday_night_football import (
    sync as mnf_sync,
)
from models.site_api.espn_nfl_api_client.models.monday_night_football_response import (
    MondayNightFootballResponse,
)

from models.site_api.espn_nfl_api_client.api.default.get_thursday_night_football import (
    sync as tnf_sync,
)
from models.site_api.espn_nfl_api_client.models.thursday_night_football_response import (
    ThursdayNightFootballResponse,
)

from models.site_api.espn_nfl_api_client.api.default.get_sunday_night_football import (
    sync as snf_sync,
)
from models.site_api.espn_nfl_api_client.models.sunday_night_football_response import (
    SundayNightFootballResponse,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def validate_schema_response(data: GenericScoreboardResponse) -> bool:
    """Validate if response matches expected schema structure."""
    required_attrs = ["leagues", "events"]
    for attr in required_attrs:
        if getattr(data, attr, UNSET) is UNSET:
            print(f"Missing required attribute: {attr}")
            return False

    # Check leagues
    leagues = data.leagues
    if not leagues:
        print("No leagues found or leagues list is empty")
        return False

    league = leagues[0]
    if getattr(league, "id", UNSET) is UNSET or getattr(league, "name", UNSET) is UNSET:
        print("Invalid league structure: missing required keys")
        return False

    # Check events
    events = data.events
    if events:
        # Check at least one event exists
        event = events[0]
        if (
            getattr(event, "id", UNSET) is UNSET
            or getattr(event, "date", UNSET) is UNSET
            or getattr(event, "competitions", UNSET) is UNSET
        ):
            print("Invalid event structure: missing required keys")
            return False

    return True


def format_scoreboard(data: GenericScoreboardResponse, sport: str, league: str) -> str:
    """Format scoreboard data for display."""
    if not data.leagues or not data.events:
        return "Invalid data format: missing leagues or events"

    league_obj = data.leagues[0]

    output = []
    output.append(f"=== ESPN {league.upper()} Scoreboard ===")
    output.append(f"League: {league_obj.name}")

    if data.season:
        output.append(f"Season: {data.season.year} (Type: {data.season.type})")

    if data.week:
        output.append(f"Week: {data.week.number}")

    output.append("\n--- Games ---")
    for event in data.events:
        output.append(f"\nGame: {event.name}")
        output.append(f"Date: {event.date}")

        if not event.competitions:
            output.append("No competition data available")
            continue

        competition = event.competitions[0]
        competitors = competition.competitors
        if not competitors:
            output.append("No competitors found")
            continue

        # Find home and away teams
        away_team = next(
            (c for c in competitors if c.home_away == "away"),
            None,
        )
        home_team = next(
            (c for c in competitors if c.home_away == "home"),
            None,
        )

        if home_team and away_team and home_team.team and away_team.team:
            output.append(
                f"Teams: {away_team.team.display_name} ({away_team.score}) @ {home_team.team.display_name} ({home_team.score})"
            )

        # Game status
        status_desc = "Unknown"
        if competition.status and competition.status.type:
            status_desc = competition.status.type.description or "Unknown"
        output.append(f"Status: {status_desc}")

        # Venue info if available
        if competition.venue and competition.venue.full_name:
            venue_name = competition.venue.full_name
            output.append(f"Venue: {venue_name}")

    return "\n".join(output)


# =============================================================================
# Parameterized tests for all sports
# =============================================================================


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,sport_enum,league,has_week,has_day",
    [
        ("football", GetScoreboardSport.FOOTBALL, "nfl", True, False),
        ("baseball", GetScoreboardSport.BASEBALL, "mlb", False, True),
        ("basketball", GetScoreboardSport.BASKETBALL, "nba", False, True),
        ("hockey", GetScoreboardSport.HOCKEY, "nhl", False, False),
        ("soccer", GetScoreboardSport.SOCCER, "eng.1", False, False),
        ("soccer", GetScoreboardSport.SOCCER, "usa.1", False, False),
    ],
)
def test_get_scoreboard(
    site_api_client,
    ensure_json_output_dir,
    sport,
    sport_enum,
    league,
    has_week,
    has_day,
):
    """Test the generic scoreboard endpoint for different sports."""
    today = datetime.now().strftime("%Y%m%d")

    # Call the generic endpoint
    response = get_scoreboard.sync_detailed(
        client=site_api_client, sport=sport_enum, league=league, dates=today
    )

    assert response.status_code == 200, (
        f"Expected status code 200 for {sport}/{league}, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, GenericScoreboardResponse), (
        f"Response should parse to GenericScoreboardResponse for {sport}/{league}"
    )

    # Common validations
    assert result.leagues, f"{sport}/{league} should have leagues"
    assert len(result.leagues) > 0, f"{sport}/{league} should have at least one league"

    league_obj = result.leagues[0]
    assert league_obj.name, f"{sport}/{league} league should have a name"

    # Sport-specific validations
    if has_week and result.week is not UNSET:
        week_num = result.week.number if result.week else "N/A"
        logger.info(f"{sport}/{league} - Week: {week_num}")

    if has_day and result.day is not UNSET:
        day_date = result.day.date if result.day else "N/A"
        logger.info(f"{sport}/{league} - Day: {day_date}")

    # Check events
    if result.events:
        logger.info(f"{sport}/{league} - Found {len(result.events)} games")

        # Log first 3 games
        for event in result.events[:3]:
            if event.name:
                logger.info(f"  Game: {event.name}")

            if event.competitions:
                comp = event.competitions[0]
                if comp.competitors:
                    teams = []
                    scores = []
                    for c in comp.competitors:
                        if c.team and c.team.display_name:
                            teams.append(c.team.display_name)
                            scores.append(str(c.score) if c.score else "0")

                    if teams:
                        logger.info(f"    Teams: {' vs '.join(teams)}")
                        logger.info(f"    Scores: {' - '.join(scores)}")

                    # Check status
                    if comp.status and comp.status.type:
                        status_desc = comp.status.type.description or "Unknown"
                        logger.info(f"    Status: {status_desc}")
    else:
        logger.info(f"{sport}/{league} - No games scheduled for {today}")

    # Save the response
    filename = f"{league}_scoreboard_processed.json"
    with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
        json.dump(result.to_dict(), f, indent=2)

    logger.info(f"✓ {sport}/{league} scoreboard saved to {filename}")


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,sport_enum,league",
    [
        ("football", GetScoreboardSport.FOOTBALL, "college-football"),
        ("basketball", GetScoreboardSport.BASKETBALL, "mens-college-basketball"),
        ("basketball", GetScoreboardSport.BASKETBALL, "womens-college-basketball"),
        ("basketball", GetScoreboardSport.BASKETBALL, "wnba"),
    ],
)
def test_get_other_sports_scoreboard(site_api_client, sport, sport_enum, league):
    """Test scoreboard for other sports/leagues."""
    response = get_scoreboard.sync_detailed(
        client=site_api_client, sport=sport_enum, league=league
    )

    assert response.status_code == 200, (
        f"Expected status code 200 for {sport}/{league}, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, GenericScoreboardResponse), (
        f"Response should parse to GenericScoreboardResponse for {sport}/{league}"
    )

    logger.info(
        f"{sport}/{league} - Found {len(result.events) if result.events else 0} games"
    )


# =============================================================================
# Sport-specific detailed tests
# =============================================================================


@pytest.mark.api
def test_get_nfl_scoreboard(site_api_client, ensure_json_output_dir):
    """Test the ESPN NFL Scoreboard API with detailed output."""
    # Test using the generated client
    scoreboard_data = get_scoreboard.sync(
        client=site_api_client, sport=GetScoreboardSport.FOOTBALL, league="nfl"
    )

    assert not isinstance(scoreboard_data, ErrorResponse), (
        f"API returned an error response: {scoreboard_data.error.message if hasattr(scoreboard_data, 'error') and scoreboard_data.error and hasattr(scoreboard_data.error, 'message') else str(scoreboard_data)}"
    )
    assert isinstance(scoreboard_data, GenericScoreboardResponse), (
        "Failed to fetch scoreboard data using client or unexpected response type"
    )

    # Validate schema
    assert validate_schema_response(scoreboard_data), (
        "Response does not match expected schema structure"
    )

    # Display formatted summary
    print("\n" + format_scoreboard(scoreboard_data, "football", "nfl"))

    # Save full response for analysis
    with open(
        f"{ensure_json_output_dir}/nfl_scoreboard_response_processed.json", "w"
    ) as f:
        json.dump(scoreboard_data.to_dict(), f, indent=2)
    print(
        f"\nFull processed response saved to {ensure_json_output_dir}/nfl_scoreboard_response_processed.json"
    )


@pytest.mark.api
def test_get_nfl_scoreboard_with_week(site_api_client, ensure_json_output_dir):
    """Test NFL scoreboard with week parameter."""
    response = get_scoreboard.sync_detailed(
        client=site_api_client,
        sport=GetScoreboardSport.FOOTBALL,
        league="nfl",
        week=1,
        seasontype=GetScoreboardSeasontype.VALUE_2,  # Regular season
    )

    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, GenericScoreboardResponse), (
        "Response should parse to GenericScoreboardResponse"
    )

    # NFL should have week info
    assert result.week, "NFL scoreboard should have week information"
    assert result.season, "NFL scoreboard should have season information"

    logger.info(
        f"NFL Week {result.week.number if result.week else 'N/A'} - "
        f"Found {len(result.events) if result.events else 0} games"
    )


@pytest.mark.api
def test_mlb_scoreboard_detailed(site_api_client, ensure_json_output_dir):
    """Test the MLB scoreboard endpoint with detailed game information."""
    today = datetime.now().strftime("%Y%m%d")
    response = get_scoreboard.sync(
        client=site_api_client,
        sport=GetScoreboardSport.BASEBALL,
        league="mlb",
        dates=today,
    )

    assert isinstance(response, GenericScoreboardResponse), (
        "Response should be a GenericScoreboardResponse"
    )

    # Check for leagues and events
    assert response.leagues, "Response should have leagues data"
    assert response.events is not None, "Response should have events data"

    league = response.leagues[0]
    print(f"League: {getattr(league, 'name', '[no name]')}")
    print("\n--- MLB Games Today ---")

    game_count = 0
    for event in response.events:
        game_count += 1
        print(f"\nGame: {getattr(event, 'name', '[no name]')}")
        print(f"Date: {getattr(event, 'date', '[no date]')}")

        if event.competitions:
            comp = event.competitions[0]
            competitors = getattr(comp, "competitors", [])
            teams = []
            scores = []
            for c in competitors:
                team_name = getattr(
                    getattr(c, "team", None), "display_name", "[no team]"
                )
                score = getattr(c, "score", "?")
                teams.append(team_name)
                scores.append(score)

            print(f"Teams: {' vs '.join(teams)} | Scores: {', '.join(scores)}")

            # Print game status
            status = getattr(comp, "status", None)
            status_type = getattr(status, "type", None) if status else None
            state = getattr(status_type, "state", None) if status_type else None
            desc = getattr(status_type, "description", None) if status_type else None
            print(f"Status: {desc or '[no status]'}")

            if state == "in":
                print("  → Game is IN PROGRESS!")
            elif state == "post":
                print("  → Game is FINAL.")
            elif state == "pre":
                print("  → Game has not started yet.")

    print(f"\nTotal MLB games today: {game_count}")


@pytest.mark.api
def test_nhl_scoreboard_detailed(site_api_client, ensure_json_output_dir):
    """Test the NHL scoreboard endpoint with detailed game information."""
    today = datetime.now().strftime("%Y%m%d")
    response = get_scoreboard.sync(
        client=site_api_client,
        sport=GetScoreboardSport.HOCKEY,
        league="nhl",
        dates=today,
    )

    assert isinstance(response, GenericScoreboardResponse), (
        "Response should be a GenericScoreboardResponse"
    )

    # Check for leagues and events
    assert response.leagues, "Response should have leagues data"
    assert response.events is not None, "Response should have events data"

    league = response.leagues[0]
    print(f"League: {getattr(league, 'name', '[no name]')}")
    print("\n--- NHL Games Today ---")

    game_count = 0
    for event in response.events:
        game_count += 1
        print(f"\nGame: {getattr(event, 'name', '[no name]')}")
        print(f"Date: {getattr(event, 'date', '[no date]')}")

        if hasattr(event, "competitions") and event.competitions:
            comp = event.competitions[0]
            competitors = getattr(comp, "competitors", [])
            teams = []
            scores = []
            for c in competitors:
                team_name = getattr(
                    getattr(c, "team", None), "display_name", "[no team]"
                )
                score = getattr(c, "score", "?")
                teams.append(team_name)
                scores.append(score)

            print(f"Teams: {' vs '.join(teams)} | Scores: {', '.join(scores)}")

            # Print game status
            status = getattr(comp, "status", None)
            status_type = getattr(status, "type", None) if status else None
            state = getattr(status_type, "state", None) if status_type else None
            desc = getattr(status_type, "description", None) if status_type else None
            print(f"Status: {desc or '[no status]'}")

            if state == "in":
                print("  → Game is IN PROGRESS!")
            elif state == "post":
                print("  → Game is FINAL.")
            elif state == "pre":
                print("  → Game has not started yet.")

    print(f"\nTotal NHL games today: {game_count}")


# =============================================================================
# NFL Night Football specific endpoints
# =============================================================================


@pytest.mark.api
def test_monday_night_football(site_api_client, ensure_json_output_dir):
    """Test the Monday Night Football API endpoint."""
    response = mnf_sync(client=site_api_client)

    assert isinstance(response, MondayNightFootballResponse), (
        "Response should be a MondayNightFootballResponse"
    )
    assert response.leagues, "Response should have leagues data"
    assert response.season, "Response should have season data"
    assert response.events is not None, (
        "Response should have events data (even if empty)"
    )

    print(
        f"\nMonday Night Football: {response.leagues[0].name} - Events: {len(response.events)}"
    )

    if response.events:
        print(f"First MNF Event: {response.events[0].name}")

        # Save processed response
        with open(
            f"{ensure_json_output_dir}/monday_night_football_processed.json", "w"
        ) as f:
            json.dump(response.to_dict(), f, indent=2)
        print(
            f"✓ Processed MNF data saved to {ensure_json_output_dir}/monday_night_football_processed.json"
        )


@pytest.mark.api
def test_thursday_night_football(site_api_client, ensure_json_output_dir):
    """Test the Thursday Night Football API endpoint."""
    response = tnf_sync(client=site_api_client)

    assert isinstance(response, ThursdayNightFootballResponse), (
        "Response should be a ThursdayNightFootballResponse"
    )
    assert response.leagues, "Response should have leagues data"
    assert response.season, "Response should have season data"
    assert response.events is not None, (
        "Response should have events data (even if empty)"
    )

    print(
        f"\nThursday Night Football: {response.leagues[0].name} - Events: {len(response.events)}"
    )

    if response.events:
        print(f"First TNF Event: {response.events[0].name}")

        # Save processed response
        with open(
            f"{ensure_json_output_dir}/thursday_night_football_processed.json", "w"
        ) as f:
            json.dump(response.to_dict(), f, indent=2)
        print(
            f"✓ Processed TNF data saved to {ensure_json_output_dir}/thursday_night_football_processed.json"
        )


@pytest.mark.api
def test_sunday_night_football(site_api_client, ensure_json_output_dir):
    """Test the Sunday Night Football API endpoint."""
    response = snf_sync(client=site_api_client)

    assert isinstance(response, SundayNightFootballResponse), (
        "Response should be a SundayNightFootballResponse"
    )
    assert response.leagues, "Response should have leagues data"
    assert response.season, "Response should have season data"
    assert response.events is not None, (
        "Response should have events data (even if empty)"
    )

    print(
        f"\nSunday Night Football: {response.leagues[0].name} - Events: {len(response.events)}"
    )

    if response.events:
        print(f"First SNF Event: {response.events[0].name}")

        # Save processed response
        with open(
            f"{ensure_json_output_dir}/sunday_night_football_processed.json", "w"
        ) as f:
            json.dump(response.to_dict(), f, indent=2)
        print(
            f"✓ Processed SNF data saved to {ensure_json_output_dir}/sunday_night_football_processed.json"
        )
