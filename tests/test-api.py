#!/usr/bin/env python3
"""
Test ESPN NFL API - Game Summary Endpoint
Requires Python 3.10+
"""

import json

from models.espn_nfl_api_client import Client
from models.espn_nfl_api_client.api.default.get_nfl_game_summary import sync
from models.espn_nfl_api_client.models.error_response import ErrorResponse
from models.espn_nfl_api_client.models.game_summary import GameSummary
from models.espn_nfl_api_client.types import UNSET


def validate_schema_response(data: GameSummary) -> bool:
    """Validate if response matches expected schema structure."""
    required_attrs = ["header", "game_info", "boxscore"]
    for attr in required_attrs:
        if getattr(data, attr, UNSET) is UNSET:
            print(f"Missing required attribute: {attr}")
            return False
    header = data.header
    if header is UNSET:
        print("Invalid header structure: header is UNSET")
        return False
    if (
        getattr(header, "id", UNSET) is UNSET
        or getattr(header, "uid", UNSET) is UNSET
        or getattr(header, "season", UNSET) is UNSET
        or getattr(header, "competitions", UNSET) is UNSET
    ):
        print("Invalid header structure: missing required keys in header")
        return False

    competitions = getattr(header, "competitions", UNSET)
    if competitions is UNSET or not competitions:
        print("No competitions found or competitions list is empty")
        return False

    competition = competitions[0]
    if (
        getattr(competition, "competitors", UNSET) is UNSET
        or not competition.competitors
    ):
        print("No competitors found in competition")
        return False
    return True


def format_game_summary(data: GameSummary) -> str:
    """Format game summary data for display."""
    if data.header is UNSET:
        return "Invalid data format: header is UNSET"
    header = data.header
    if not header:
        return "Invalid data format: header is empty"

    competitions = header.competitions
    if not competitions:
        return "Invalid competition data: header.competitions is empty"
    competition = competitions[0]
    competitors_on_competition = competition.competitors
    if not competitors_on_competition:
        return "Invalid competition data: no competitors found"

    competitors_list = competitors_on_competition
    away_team = next(
        (
            c
            for c in competitors_list
            if getattr(c, "home_away", UNSET) is not UNSET and c.home_away == "away"
        ),
        None,
    )
    home_team = next(
        (
            c
            for c in competitors_list
            if getattr(c, "home_away", UNSET) is not UNSET and c.home_away == "home"
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
    game_id = getattr(header, "id", "N/A")
    output.append(f"Game ID: {game_id}")

    game_date = getattr(competition, "date", "N/A")
    output.append(f"Date: {game_date}")

    output.append("\n--- Teams ---")
    away_team_display_name = away_team.team.display_name
    away_team_score = away_team.score
    output.append(f"{away_team_display_name} (Away): {away_team_score}")

    home_team_display_name = home_team.team.display_name
    home_team_score = home_team.score
    output.append(f"{home_team_display_name} (Home): {home_team_score}")

    status_desc = "Unknown"
    competition_status = competition.status
    if competition_status is not UNSET:
        status_type_attr = getattr(competition_status, "type_", UNSET)
        if status_type_attr is not UNSET:
            status_desc_attr = getattr(status_type_attr, "description", UNSET)
            if status_desc_attr is not UNSET:
                status_desc = status_desc_attr
    output.append(f"\nStatus: {status_desc}")

    venue_name = "Unknown"
    city = "Unknown"
    state = "Unknown"
    attendance_val = "N/A"

    game_info = data.game_info
    if game_info:
        venue_name = game_info.venue.full_name

        venue_address = game_info.venue.address
        if venue_address:
            city = venue_address.city
            state = venue_address.state

        attendance_val = game_info.attendance

        output.append("\n--- Venue ---")
        output.append(f"Name: {venue_name}")
        output.append(f"Location: {city}, {state}")
        output.append(f"Attendance: {attendance_val}")

    return "\n".join(output)


def main():
    """Main function to test the ESPN NFL API."""
    print("ESPN NFL API Test Script")
    print("=" * 50)

    client = Client(base_url="https://site.api.espn.com/apis/site/v2")

    # Test with a known game ID (Super Bowl LVII)
    test_event_id = "401547417"

    print(f"\nFetching game summary for event ID: {test_event_id}")
    print("-" * 50)

    # Get game summary
    game_data: GameSummary | ErrorResponse | None = sync(
        client=client, event=test_event_id
    )

    if isinstance(game_data, ErrorResponse):
        print("✗ API returned an error response:")
        print(
            game_data.error.message
            if hasattr(game_data, "error")
            and game_data.error
            and hasattr(game_data.error, "message")
            else str(game_data)
        )
        return
    if isinstance(game_data, GameSummary):
        # Validate schema
        if validate_schema_response(game_data):
            print("✓ Response matches expected schema structure")
        else:
            print("✗ Response does not match expected schema structure")

        # Display formatted summary
        print("\n" + format_game_summary(game_data))

        # Save full response for analysis
        with open("game_summary_response.json", "w") as f:
            json.dump(game_data.to_dict(), f, indent=2)
        print("\n✓ Full response saved to game_summary_response.json")
    else:
        print("✗ Failed to fetch game data")


if __name__ == "__main__":
    main()
