#!/usr/bin/env python3
"""
Test ESPN NFL API - Scoreboard Endpoint
Requires Python 3.10+
"""

import json
import pytest
import requests
import os
from datetime import datetime

from models.site_api.espn_nfl_api_client import Client
from models.site_api.espn_nfl_api_client.api.default.get_nfl_scoreboard import sync
from models.site_api.espn_nfl_api_client.models.error_response import ErrorResponse
from models.site_api.espn_nfl_api_client.models.scoreboard import Scoreboard
from models.site_api.espn_nfl_api_client.types import UNSET

from models.site_api.espn_nfl_api_client.api.default.get_mlb_scoreboard import (
    sync as get_mlb_scoreboard,
)
from models.site_api.espn_nfl_api_client.models.mlb_scoreboard_response import (
    MlbScoreboardResponse,
)

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


def validate_schema_response(data: Scoreboard) -> bool:
    """Validate if response matches expected schema structure."""
    required_attrs = ["leagues", "season", "week", "events"]
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
    if (
        getattr(league, "id", UNSET) is UNSET
        or getattr(league, "name", UNSET) is UNSET
        or getattr(league, "season", UNSET) is UNSET
    ):
        print("Invalid league structure: missing required keys")
        return False

    # Check events
    events = data.events
    if not events:
        print("No events found or events list is empty")
        return False

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


def format_scoreboard(data: Scoreboard) -> str:
    """Format scoreboard data for display."""
    if not data.leagues or not data.events:
        return "Invalid data format: missing leagues or events"

    league = data.leagues[0]
    season_info = data.season
    week_info = data.week

    output = []
    output.append("=== ESPN NFL Scoreboard ===")
    output.append(f"League: {league.name}")
    output.append(f"Season: {season_info.year} (Type: {season_info.type})")
    output.append(f"Week: {week_info.number}")

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


@pytest.mark.api
def test_mlb_scoreboard(site_api_client, ensure_json_output_dir):
    """Test the MLB scoreboard endpoint and print the full formatted scoreboard for today's games, including active games."""
    today = datetime.now().strftime("%Y%m%d")
    response = get_mlb_scoreboard(client=site_api_client, dates=today)

    assert isinstance(response, MlbScoreboardResponse), (
        "Response should be a MlbScoreboardResponse"
    )

    # Check for leagues and events
    assert response.leagues, "Response should have leagues data"
    assert response.events, "Response should have events data"

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

    # Save processed response
    with open(f"{ensure_json_output_dir}/mlb_scoreboard_processed.json", "w") as f:
        json.dump(response.to_dict(), f, indent=2)
    print(
        f"✓ Processed MLB scoreboard saved to {ensure_json_output_dir}/mlb_scoreboard_processed.json"
    )


@pytest.mark.api
def test_get_nfl_scoreboard(site_api_client, ensure_json_output_dir):
    """Test the ESPN NFL Scoreboard API."""
    # Test using the generated client
    scoreboard_data = sync(client=site_api_client)

    assert not isinstance(scoreboard_data, ErrorResponse), (
        f"API returned an error response: {scoreboard_data.error.message if hasattr(scoreboard_data, 'error') and scoreboard_data.error and hasattr(scoreboard_data.error, 'message') else str(scoreboard_data)}"
    )
    assert isinstance(scoreboard_data, Scoreboard), (
        "Failed to fetch scoreboard data using client or unexpected response type"
    )

    # Validate schema
    assert validate_schema_response(scoreboard_data), (
        "Response does not match expected schema structure"
    )

    # Display formatted summary
    print("\n" + format_scoreboard(scoreboard_data))

    # Save full response for analysis
    with open(
        f"{ensure_json_output_dir}/nfl_scoreboard_response_processed.json", "w"
    ) as f:
        json.dump(scoreboard_data.to_dict(), f, indent=2)
    print(
        f"\nFull processed response saved to {ensure_json_output_dir}/nfl_scoreboard_response_processed.json"
    )


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
