#!/usr/bin/env python3
"""
Test ESPN NFL API - Teams List Endpoint
Requires Python 3.10+
"""

import json
import requests

from models.site_api.espn_nfl_api_client import Client
from models.site_api.espn_nfl_api_client.api.default.get_nfl_teams_list import sync
from models.site_api.espn_nfl_api_client.models.error_response import ErrorResponse
from models.site_api.espn_nfl_api_client.models.teams_list_response import (
    TeamsListResponse,
)
from models.site_api.espn_nfl_api_client.types import UNSET


def validate_schema_response(data: TeamsListResponse) -> bool:
    """Validate if response matches expected schema structure."""
    required_attrs = ["sports"]
    for attr in required_attrs:
        if getattr(data, attr, UNSET) is UNSET:
            print(f"Missing required attribute: {attr}")
            return False

    # Check sports
    sports = data.sports
    if not sports:
        print("No sports found or sports list is empty")
        return False

    sport = sports[0]
    if (
        getattr(sport, "id", UNSET) is UNSET
        or getattr(sport, "name", UNSET) is UNSET
        or getattr(sport, "leagues", UNSET) is UNSET
    ):
        print("Invalid sport structure: missing required keys")
        return False

    # Check leagues
    leagues = sport.leagues
    if not leagues:
        print("No leagues found or leagues list is empty")
        return False

    # Check league
    league = leagues[0]
    if (
        getattr(league, "id", UNSET) is UNSET
        or getattr(league, "name", UNSET) is UNSET
        or getattr(league, "teams", UNSET) is UNSET
    ):
        print("Invalid league structure: missing required keys")
        return False

    # Check teams
    teams = league.teams
    if not teams:
        print("No teams found or teams list is empty")
        return False

    # Check first team
    team_entry = teams[0]
    if getattr(team_entry, "team", UNSET) is UNSET:
        print("Invalid team entry structure: missing team")
        return False

    team = team_entry.team
    if (
        getattr(team, "id", UNSET) is UNSET
        or getattr(team, "display_name", UNSET) is UNSET
    ):
        print("Invalid team structure: missing required keys")
        return False

    return True


def format_teams_list(data: TeamsListResponse) -> str:
    """Format teams list data for display."""
    if not data.sports:
        return "Invalid data format: missing sports"

    sport = data.sports[0]
    if not sport.leagues:
        return "Invalid data format: missing leagues"

    league = sport.leagues[0]
    if not league.teams:
        return "Invalid data format: missing teams"

    output = []
    output.append(f"=== {league.name} Teams ===")
    output.append(f"Total Teams: {len(league.teams)}")
    output.append(f"League Year: {league.year}")

    output.append("\n--- Teams ---")
    for team_entry in league.teams:
        team = team_entry.team
        output.append(f"{team.display_name} ({team.abbreviation})")
        output.append(f"  Location: {team.location}")
        output.append(f"  Colors: Primary={team.color}, Alt={team.alternate_color}")

        # Add logo URL if available
        if team.logos and len(team.logos) > 0:
            output.append(f"  Logo: {team.logos[0].href}")

        output.append("")

    return "\n".join(output)


def fetch_direct_teams_list():
    """Fetch the teams list data directly using requests to bypass model issues."""
    url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def test_mlb_teams_list():
    """Test the ESPN MLB Teams List API."""
    print("\nFetching MLB teams list data")
    print("-" * 50)

    from models.site_api.espn_nfl_api_client.api.default.get_mlb_teams_list import (
        sync as get_mlb_teams_list,
    )

    client = Client("https://site.api.espn.com/apis/site/v2")
    teams_data = get_mlb_teams_list(client=client)

    if isinstance(teams_data, ErrorResponse):
        print("✗ API returned an error response:")
        print(
            teams_data.error.message
            if hasattr(teams_data, "error")
            and teams_data.error
            and hasattr(teams_data.error, "message")
            else str(teams_data)
        )
        return False
    elif isinstance(teams_data, TeamsListResponse):
        # Validate schema
        if validate_schema_response(teams_data):
            print("✓ Response matches expected schema structure")
        else:
            print("✗ Response does not match expected schema structure")
            return False

        # Display formatted summary
        print("\n" + format_teams_list(teams_data))

        # Save full response for analysis
        with open("mlb_teams_response_processed.json", "w") as f:
            json.dump(teams_data.to_dict(), f, indent=2)
        print("\n✓ Full processed response saved to mlb_teams_response_processed.json")
        return True
    else:
        print("✗ Failed to fetch teams data using client")
        return False


def main():
    """Main function to test the ESPN NFL Teams List API."""
    print("ESPN NFL Teams List API Test Script")
    print("=" * 50)

    client = Client("https://site.api.espn.com/apis/site/v2")

    print("\nFetching NFL teams list data")
    print("-" * 50)

    # For testing purposes, we'll first try the client
    try:
        print("\nUsing the generated client to fetch teams list:")
        teams_data: TeamsListResponse | ErrorResponse | None = sync(client=client)

        if isinstance(teams_data, ErrorResponse):
            print("✗ API returned an error response:")
            print(
                teams_data.error.message
                if hasattr(teams_data, "error")
                and teams_data.error
                and hasattr(teams_data.error, "message")
                else str(teams_data)
            )
        elif isinstance(teams_data, TeamsListResponse):
            # Validate schema
            if validate_schema_response(teams_data):
                print("✓ Response matches expected schema structure")
            else:
                print("✗ Response does not match expected schema structure")

            # Display formatted summary
            print("\n" + format_teams_list(teams_data))

            # Save full response for analysis
            with open("nfl_teams_response_processed.json", "w") as f:
                json.dump(teams_data.to_dict(), f, indent=2)
            print(
                "\n✓ Full processed response saved to nfl_teams_response_processed.json"
            )
        else:
            print("✗ Failed to fetch teams data using client")
    except Exception as e:
        print(f"✗ Error using generated client: {str(e)}")

        # Fall back to direct request
        print("\nFalling back to direct request:")
        teams_json = fetch_direct_teams_list()

        if not teams_json:
            print("✗ Failed to fetch teams data directly")
            return

        # Save the raw JSON for analysis
        with open("nfl_teams_direct.json", "w") as f:
            json.dump(teams_json, f, indent=2)

        print("✓ Successfully fetched teams data")

        # Basic validation and display from the direct JSON
        if "sports" not in teams_json:
            print("✗ Response does not match expected structure")
            return

        sport = teams_json["sports"][0]
        if "leagues" not in sport or not sport["leagues"]:
            print("✗ Response does not match expected structure: missing leagues")
            return

        league = sport["leagues"][0]
        if "teams" not in league or not league["teams"]:
            print("✗ Response does not match expected structure: missing teams")
            return

        print(f"\n=== {league.get('name', 'Unknown')} Teams ===")
        print(f"Total Teams: {len(league.get('teams', []))}")

        print("\n--- Teams ---")
        for team_entry in league.get("teams", []):
            team = team_entry.get("team", {})
            print(
                f"{team.get('displayName', 'Unknown')} ({team.get('abbreviation', 'UNK')})"
            )

        print("\n✓ Full teams response saved to nfl_teams_direct.json")

    print("\nRunning MLB Teams List Test")
    mlb_result = test_mlb_teams_list()
    print(f"MLB Teams List Test: {'PASS' if mlb_result else 'FAIL'}")


if __name__ == "__main__":
    main()
