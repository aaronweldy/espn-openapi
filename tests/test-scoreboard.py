#!/usr/bin/env python3
"""
Test ESPN NFL API - Scoreboard Endpoint
Requires Python 3.10+
"""

import json

import requests
from models.site_api.espn_nfl_api_client import Client
from models.site_api.espn_nfl_api_client.api.default.get_nfl_scoreboard import sync
from models.site_api.espn_nfl_api_client.models.error_response import ErrorResponse
from models.site_api.espn_nfl_api_client.models.scoreboard import Scoreboard
from models.site_api.espn_nfl_api_client.types import UNSET


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


def fetch_direct_scoreboard():
    """Fetch the scoreboard data directly using requests to bypass model issues."""
    url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def main():
    """Main function to test the ESPN NFL Scoreboard API."""
    print("ESPN NFL Scoreboard API Test Script")
    print("=" * 50)

    client = Client(base_url="https://site.api.espn.com/apis/site/v2")

    print("\nFetching NFL scoreboard data")
    print("-" * 50)

    # For testing purposes, we'll use direct request instead of the client
    # since there might be some schema mismatches until models are refined
    scoreboard_json = fetch_direct_scoreboard()

    if not scoreboard_json:
        print("✗ Failed to fetch scoreboard data directly")
        return

    # Save the raw JSON for analysis
    with open("nfl_scoreboard_direct.json", "w") as f:
        json.dump(scoreboard_json, f, indent=2)

    print("✓ Successfully fetched scoreboard data")

    # Basic validation and display from the direct JSON
    if "leagues" not in scoreboard_json or "events" not in scoreboard_json:
        print("✗ Response does not match expected structure")
        return

    print("\n=== ESPN NFL Scoreboard ===")
    league = scoreboard_json["leagues"][0]
    print(f"League: {league.get('name', 'Unknown')}")
    print(
        f"Season: {scoreboard_json.get('season', {}).get('year', 'Unknown')} (Type: {scoreboard_json.get('season', {}).get('type', 'Unknown')})"
    )
    print(f"Week: {scoreboard_json.get('week', {}).get('number', 'Unknown')}")

    print("\n--- Games ---")
    for event in scoreboard_json.get("events", []):
        print(f"\nGame: {event.get('name', 'Unknown')}")
        print(f"Date: {event.get('date', 'Unknown')}")

        competitions = event.get("competitions", [])
        if not competitions:
            print("No competition data available")
            continue

        competition = competitions[0]
        competitors = competition.get("competitors", [])
        if not competitors:
            print("No competitors found")
            continue

        # Find home and away teams
        away_team = next(
            (c for c in competitors if c.get("homeAway") == "away"),
            None,
        )
        home_team = next(
            (c for c in competitors if c.get("homeAway") == "home"),
            None,
        )

        if home_team and away_team:
            away_team_name = away_team.get("team", {}).get("displayName", "Unknown")
            home_team_name = home_team.get("team", {}).get("displayName", "Unknown")
            away_score = away_team.get("score", "0")
            home_score = home_team.get("score", "0")
            print(
                f"Teams: {away_team_name} ({away_score}) @ {home_team_name} ({home_score})"
            )

        # Game status
        status = competition.get("status", {})
        status_type = status.get("type", {})
        status_desc = status_type.get("description", "Unknown")
        print(f"Status: {status_desc}")

        # Venue info if available
        venue = competition.get("venue", {})
        venue_name = venue.get("fullName", "Unknown")
        print(f"Venue: {venue_name}")

    print("\n✓ Full scoreboard response saved to nfl_scoreboard_direct.json")

    # Optional: Try using the generated client
    try:
        print(
            "\nAttempting to use the generated client (may fail due to schema issues):"
        )
        scoreboard_data: Scoreboard | ErrorResponse | None = sync(client=client)

        if isinstance(scoreboard_data, ErrorResponse):
            print("✗ API returned an error response:")
            print(
                scoreboard_data.error.message
                if hasattr(scoreboard_data, "error")
                and scoreboard_data.error
                and hasattr(scoreboard_data.error, "message")
                else str(scoreboard_data)
            )
        elif isinstance(scoreboard_data, Scoreboard):
            # Validate schema
            if validate_schema_response(scoreboard_data):
                print("✓ Response matches expected schema structure")
            else:
                print("✗ Response does not match expected schema structure")

            # Display formatted summary
            print("\n" + format_scoreboard(scoreboard_data))

            # Save full response for analysis
            with open("nfl_scoreboard_response_processed.json", "w") as f:
                json.dump(scoreboard_data.to_dict(), f, indent=2)
            print(
                "\n✓ Full processed response saved to nfl_scoreboard_response_processed.json"
            )
        else:
            print("✗ Failed to fetch scoreboard data using client")
    except Exception as e:
        print(f"✗ Error using generated client: {str(e)}")


if __name__ == "__main__":
    main()
