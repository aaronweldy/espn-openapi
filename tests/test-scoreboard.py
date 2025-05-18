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


def test_mlb_scoreboard():
    """Test the MLB scoreboard endpoint and print the full formatted scoreboard for today's games, including active games."""
    from models.site_api.espn_nfl_api_client import Client
    from models.site_api.espn_nfl_api_client.api.default.get_mlb_scoreboard import (
        sync as get_mlb_scoreboard,
    )
    from models.site_api.espn_nfl_api_client.models.mlb_scoreboard_response import (
        MlbScoreboardResponse,
    )
    from models.site_api.espn_nfl_api_client.types import UNSET
    import os
    from datetime import datetime

    today = datetime.now().strftime("%Y%m%d")
    print(f"\n--- Testing MLB Scoreboard for {today} ---")
    client = Client(base_url="https://site.api.espn.com/apis/site/v2")
    response = get_mlb_scoreboard(client=client, dates=today)
    if not isinstance(response, MlbScoreboardResponse):
        print(f"✗ Response is not MlbScoreboardResponse: {type(response)}")
        return False
    # Defensive: check for missing or empty fields
    if not getattr(response, "leagues", None) or not getattr(response, "events", None):
        print("No MLB games scheduled for today.")
        return True
    league = response.leagues[0]
    print(f"League: {getattr(league, 'name', '[no name]')}")
    print("\n--- MLB Games Today ---")
    for event in response.events:
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
    # Save processed response
    os.makedirs("json_output", exist_ok=True)
    with open("json_output/mlb_scoreboard_processed.json", "w") as f:
        import json

        json.dump(response.to_dict(), f, indent=2)
    print(
        "✓ Processed MLB scoreboard saved to json_output/mlb_scoreboard_processed.json"
    )
    return True


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

    print("\n--- Running MLB Scoreboard Test ---")
    mlb_result = test_mlb_scoreboard()
    print(f"MLB Scoreboard Test: {'PASS' if mlb_result else 'FAIL'}")


def test_monday_night_football():
    from models.site_api.espn_nfl_api_client.api.default.get_monday_night_football import (
        sync as mnf_sync,
    )
    from models.site_api.espn_nfl_api_client.models.monday_night_football_response import (
        MondayNightFootballResponse,
    )

    client = Client(base_url="https://site.api.espn.com/apis/site/v2")
    response = mnf_sync(client=client)
    assert isinstance(response, MondayNightFootballResponse)
    assert response.leagues and response.season and response.events
    print(
        "\nMonday Night Football: ",
        response.leagues[0].name,
        "- Events:",
        len(response.events),
    )
    if response.events:
        print("First MNF Event:", response.events[0].name)


def test_thursday_night_football():
    from models.site_api.espn_nfl_api_client.api.default.get_thursday_night_football import (
        sync as tnf_sync,
    )
    from models.site_api.espn_nfl_api_client.models.thursday_night_football_response import (
        ThursdayNightFootballResponse,
    )

    client = Client(base_url="https://site.api.espn.com/apis/site/v2")
    response = tnf_sync(client=client)
    assert isinstance(response, ThursdayNightFootballResponse)
    assert response.leagues and response.season and response.events
    print(
        "\nThursday Night Football: ",
        response.leagues[0].name,
        "- Events:",
        len(response.events),
    )
    if response.events:
        print("First TNF Event:", response.events[0].name)


def test_sunday_night_football():
    from models.site_api.espn_nfl_api_client.api.default.get_sunday_night_football import (
        sync as snf_sync,
    )
    from models.site_api.espn_nfl_api_client.models.sunday_night_football_response import (
        SundayNightFootballResponse,
    )

    client = Client(base_url="https://site.api.espn.com/apis/site/v2")
    response = snf_sync(client=client)
    assert isinstance(response, SundayNightFootballResponse)
    assert response.leagues and response.season and response.events
    print(
        "\nSunday Night Football: ",
        response.leagues[0].name,
        "- Events:",
        len(response.events),
    )
    if response.events:
        print("First SNF Event:", response.events[0].name)


if __name__ == "__main__":
    main()
    print("\n--- Running Night Football Endpoint Tests ---")
    test_monday_night_football()
    test_thursday_night_football()
    test_sunday_night_football()
