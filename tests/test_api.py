#!/usr/bin/env python3
"""
Test ESPN NFL API - Game Summary Endpoint
Requires Python 3.10+
"""

import json
import pytest
from typing import cast, Dict, Any, List
import httpx
from datetime import datetime

from models.site_api.espn_nfl_api_client import Client
from models.site_api.espn_nfl_api_client.api.default.get_nfl_game_summary import sync
from models.site_api.espn_nfl_api_client.models.error_response import ErrorResponse
from models.site_api.espn_nfl_api_client.models.game_summary import GameSummary
from models.site_api.espn_nfl_api_client.types import UNSET

from models.site_web_api.espn_site_web_api_client.api.default.get_nfl_athlete_game_log import (
    sync_detailed as get_athlete_gamelog,
)
from models.site_web_api.espn_site_web_api_client.client import (
    Client as SiteWebApiClient,
)
from models.site_web_api.espn_site_web_api_client.models.athlete_game_log_response import (
    AthleteGameLogResponse,
)
from models.site_web_api.espn_site_web_api_client.models.game_event import GameEvent

from models.sports_core_api.espn_sports_core_api_client.client import (
    Client as CoreApiClient,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_nfl_competition_drives import (
    sync as get_nfl_competition_drives,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_nfl_competition_plays import (
    sync as get_nfl_competition_plays,
)
from models.sports_core_api.espn_sports_core_api_client.models.drives_list_response import (
    DrivesListResponse,
)
from models.sports_core_api.espn_sports_core_api_client.models.plays_list_response import (
    PlaysListResponse,
)
from models.sports_core_api.espn_sports_core_api_client.models.error_response import (
    ErrorResponse as CoreErrorResponse,
)


def validate_schema_response(data: GameSummary) -> bool:
    """Validate if response matches expected schema structure."""
    required_attrs = ["header", "game_info", "boxscore"]
    for attr in required_attrs:
        if getattr(data, attr, UNSET) is UNSET:
            return False
    header = data.header
    if not header:
        return False
    if not header.id or not header.uid or not header.season or not header.competitions:
        return False

    competitions = header.competitions
    if not competitions:
        return False

    competition = competitions[0]
    if not competition.competitors:
        return False
    return True


def format_game_summary(data: GameSummary) -> str:
    """Format game summary data for display."""
    if data.header is UNSET:
        return "Invalid data format: header is UNSET"
    header = data.header
    if not header:
        return "Invalid data format: header is empty"

    competitions = header.competitions or []
    if not competitions:
        return "Invalid competition data: header.competitions is empty"
    competition = competitions[0]
    competitors_on_competition = competition.competitors or []
    if not competitors_on_competition:
        return "Invalid competition data: no competitors found"

    competitors_list = competitors_on_competition
    away_team = next(
        (
            c
            for c in competitors_list
            if c.home_away is not UNSET and c.home_away == "away"
        ),
        None,
    )
    home_team = next(
        (
            c
            for c in competitors_list
            if c.home_away is not UNSET and c.home_away == "home"
        ),
        None,
    )

    if (
        away_team is None
        or home_team is None
        or away_team.team is UNSET
        or home_team.team is UNSET
    ):
        return "Could not determine home/away teams or team data is UNSET"

    output = []
    output.append("=== ESPN NFL Game Summary ===")
    game_id = header.id or "N/A"
    output.append(f"Game ID: {game_id}")

    game_date = competition.date or "N/A"
    output.append(f"Date: {game_date}")

    output.append("\n--- Teams ---")
    away_team_display_name = away_team.team.display_name or "Unknown"
    away_team_score = away_team.score or "N/A"
    output.append(f"{away_team_display_name} (Away): {away_team_score}")

    home_team_display_name = home_team.team.display_name or "Unknown"
    home_team_score = home_team.score or "N/A"
    output.append(f"{home_team_display_name} (Home): {home_team_score}")

    status_desc = "Unknown"
    competition_status = competition.status
    if competition_status and competition_status.type:
        status_desc = competition_status.type.description or "Unknown"
    output.append(f"\nStatus: {status_desc}")

    venue_name = "Unknown"
    city = "Unknown"
    state = "Unknown"
    attendance_val = "N/A"

    game_info = data.game_info
    if game_info:
        if game_info.venue:
            venue_name = game_info.venue.full_name or "Unknown"

            if game_info.venue.address:
                city = game_info.venue.address.city or "Unknown"
                state = game_info.venue.address.state or "Unknown"

        attendance_val = game_info.attendance or "N/A"

        output.append("\n--- Venue ---")
        output.append(f"Name: {venue_name}")
        output.append(f"Location: {city}, {state}")
        output.append(f"Attendance: {attendance_val}")

    return "\n".join(output)


def format_gamelog(games, athlete_id):
    """Format game log into a nice table-like display."""
    if not games:
        return "No games available"

    # Count wins and losses
    wins = sum(
        1 for game in games if game.game_result and game.game_result.value == "W"
    )
    losses = sum(
        1 for game in games if game.game_result and game.game_result.value == "L"
    )
    ties = sum(
        1 for game in games if game.game_result and game.game_result.value == "T"
    )

    # Sort games by date (most recent first)
    sorted_games = sorted(games, key=lambda x: x.game_date, reverse=True)

    # Build header
    header = f"{'DATE':<12} {'OPPONENT':<25} {'RESULT':<8} {'SCORE':<10} {'HOME/AWAY':<10} {'WEEK':<6}"
    divider = "-" * 75

    # Build rows
    rows = []
    for game in sorted_games:
        date = game.game_date.strftime("%Y-%m-%d") if game.game_date else "N/A"
        opponent = (
            game.opponent.display_name
            if game.opponent and game.opponent.display_name
            else "Unknown"
        )
        result = game.game_result.value if game.game_result else "N/A"
        score = game.score if game.score else "N/A"
        home_away = "Home" if game.at_vs and game.at_vs.value == "vs" else "Away"
        week = f"Week {game.week}" if game.week else "N/A"

        row = f"{date:<12} {opponent:<25} {result:<8} {score:<10} {home_away:<10} {week:<6}"
        rows.append(row)

    # Build season stats
    record = f"Record: {wins}-{losses}" + (f"-{ties}" if ties > 0 else "")

    # Combine all parts
    return "\n".join([
        f"\n{'=' * 75}",
        f"GAME LOG FOR ATHLETE ID: {athlete_id}",
        f"{record}",
        f"{'=' * 75}",
        header,
        divider,
        "\n".join(rows),
    ])


@pytest.mark.api
def test_nfl_athlete_gamelog(site_web_api_client, ensure_json_output_dir):
    """Test the NFL athlete gamelog endpoint"""
    # Patrick Mahomes ID
    athlete_id = "3139477"

    # Make API request
    response = get_athlete_gamelog(athlete_id=athlete_id, client=site_web_api_client)

    # Check if request was successful
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )
    assert isinstance(response.parsed, AthleteGameLogResponse), (
        "Response should parse to AthleteGameLogResponse"
    )

    game_log = cast(AthleteGameLogResponse, response.parsed)
    assert game_log.events is not None, "Game log should have events"
    assert game_log.events.additional_properties, "Game log should have events data"

    games_count = len(game_log.events.additional_properties)
    print(f"\nFound {games_count} games for athlete ID {athlete_id}")

    # Format and display gamelog
    games = list(game_log.events.additional_properties.values())
    formatted_gamelog = format_gamelog(games, athlete_id)
    print(formatted_gamelog)

    # Save full response for analysis
    with open(
        f"{ensure_json_output_dir}/athlete_{athlete_id}_gamelog_processed.json", "w"
    ) as f:
        json.dump(game_log.to_dict(), f, indent=2)
    print(
        f"✓ Processed gamelog saved to {ensure_json_output_dir}/athlete_{athlete_id}_gamelog_processed.json"
    )


@pytest.mark.api
def test_nfl_competition_drives(sports_core_api_client, ensure_json_output_dir):
    """Test fetching NFL competition drives data"""
    event_id = "401547417"
    competition_id = "401547417"

    response = get_nfl_competition_drives(
        event_id=event_id, competition_id=competition_id, client=sports_core_api_client
    )

    assert not isinstance(response, CoreErrorResponse), (
        f"API returned an error: {response.error.message if hasattr(response, 'error') and response.error and hasattr(response.error, 'message') else str(response)}"
    )
    assert isinstance(response, DrivesListResponse), (
        "Response should be a DrivesListResponse"
    )

    print(f"\nSuccessfully retrieved drives data for competition {competition_id}")

    # Calculate some basic stats about the drives
    if response.items:
        drive_count = len(response.items)
        scoring_drives = sum(
            1 for drive in response.items if drive.is_score and drive.is_score is True
        )
        print(f"Total drives: {drive_count}")
        print(f"Scoring drives: {scoring_drives}")

        # Save the data for analysis
        with open(
            f"{ensure_json_output_dir}/competition_{competition_id}_drives_processed.json",
            "w",
        ) as f:
            json.dump(response.to_dict(), f, indent=2)
        print(
            f"✓ Processed drives data saved to {ensure_json_output_dir}/competition_{competition_id}_drives_processed.json"
        )


@pytest.mark.api
def test_nfl_competition_plays(sports_core_api_client, ensure_json_output_dir):
    """Test fetching NFL competition plays data"""
    event_id = "401547417"
    competition_id = "401547417"

    response = get_nfl_competition_plays(
        event_id=event_id, competition_id=competition_id, client=sports_core_api_client
    )

    assert not isinstance(response, CoreErrorResponse), (
        f"API returned an error: {response.error.message if hasattr(response, 'error') and response.error and hasattr(response.error, 'message') else str(response)}"
    )
    assert isinstance(response, PlaysListResponse), (
        "Response should be a PlaysListResponse"
    )

    print(f"\nSuccessfully retrieved plays data for competition {competition_id}")

    # Calculate some basic stats about the plays
    if response.items:
        play_count = len(response.items)
        print(f"Total plays: {play_count}")

        # Show a sample of plays
        sample_size = min(5, play_count)
        print(f"\nSample of {sample_size} plays:")
        for i, play in enumerate(response.items[:sample_size]):
            play_type = getattr(play, "play_type", None)
            play_type_name = (
                getattr(play_type, "name", "Unknown") if play_type else "Unknown"
            )
            play_text = getattr(play, "text", "Unknown")
            print(f"{i + 1}. [{play_type_name}] {play_text}")

        # Save the data for analysis
        with open(
            f"{ensure_json_output_dir}/competition_{competition_id}_plays_processed.json",
            "w",
        ) as f:
            json.dump(response.to_dict(), f, indent=2)
        print(
            f"✓ Processed plays data saved to {ensure_json_output_dir}/competition_{competition_id}_plays_processed.json"
        )
