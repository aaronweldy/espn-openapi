#!/usr/bin/env python3
"""
Test ESPN NFL API - Standings Endpoint
Requires Python 3.10+
"""

import json
import requests

from models.espn_nfl_api_client import Client
from models.espn_nfl_api_client.api.default.get_nfl_standings import sync
from models.espn_nfl_api_client.models.error_response import ErrorResponse
from models.espn_nfl_api_client.models.standings_response import StandingsResponse
from models.espn_nfl_api_client.models.get_nfl_standings_seasontype import GetNFLStandingsSeasontype
from models.espn_nfl_api_client.types import UNSET


def validate_schema_response(data):
    """Validate if response matches expected schema structure."""
    try:
        required_attrs = ["name", "children"]
        for attr in required_attrs:
            if getattr(data, attr, UNSET) is UNSET:
                print(f"Missing required attribute: {attr}")
                return False

        # Check children (conferences)
        children = data.children
        if not children:
            print("No conferences found or children list is empty")
            return False

        # Check first conference
        conference = children[0]
        if not hasattr(conference, "name") or not hasattr(conference, "standings"):
            print("Invalid conference structure: missing required keys")
            return False

        # Check standings
        standings = conference.standings
        if not hasattr(standings, "entries"):
            print("Invalid standings structure: missing entries")
            return False

        # Check entries
        entries = standings.entries
        if not entries:
            print("No standings entries found or entries list is empty")
            return False

        # Check team and stats
        entry = entries[0]
        if not hasattr(entry, "team") or not hasattr(entry, "stats"):
            print("Invalid entry structure: missing team or stats")
            return False

        return True
    except Exception as e:
        print(f"Error during validation: {str(e)}")
        return False


def format_standings_response(data):
    """Format standings data for display."""
    if not data.name or not data.children:
        return "Invalid data format: missing name or children"

    output = []
    output.append(f"=== {data.name} Standings ===")

    for conference in data.children:
        output.append(f"\n--- {conference.name} ---")

        if hasattr(conference, 'standings'):
            standings = conference.standings
            output.append(f"Season: {standings.season} ({standings.season_type})")

            output.append("\nTeam                  W-L    PCT   PF    PA    DIFF   STRK")
            output.append("--------------------------------------------------------------")

            if hasattr(standings, 'entries'):
                for entry in standings.entries:
                    if hasattr(entry, 'team') and hasattr(entry, 'stats'):
                        team = entry.team

                        # Extract stats for display (using snake_case attribute names)
                        wins = next((s.value for s in entry.stats if s.name == "wins"), 0)
                        losses = next((s.value for s in entry.stats if s.name == "losses"), 0)
                        ties = next((s.value for s in entry.stats if s.name == "ties"), 0)
                        win_pct = next((s.display_value for s in entry.stats if s.name == "winPercent"), "0.000")
                        points_for = next((s.value for s in entry.stats if s.name == "pointsFor"), 0)
                        points_against = next((s.value for s in entry.stats if s.name == "pointsAgainst"), 0)
                        diff = next((s.display_value for s in entry.stats if s.name == "differential"), "0")
                        streak = next((s.display_value for s in entry.stats if s.name == "streak"), "")

                        if hasattr(team, 'display_name'):
                            team_name = team.display_name
                        else:
                            team_name = "Unknown"

                        output.append(f"{team_name:<20}  {int(wins)}-{int(losses)}  {win_pct:<5} {int(points_for):<5} {int(points_against):<5} {diff:<6} {streak}")

    return "\n".join(output)


def fetch_direct_standings():
    """Fetch the standings data directly using requests to bypass model issues."""
    url = "https://site.api.espn.com/apis/v2/sports/football/nfl/standings"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def main():
    """Main function to test the ESPN NFL Standings API."""
    print("ESPN NFL Standings API Test Script")
    print("=" * 50)

    client = Client(base_url="https://site.api.espn.com/apis")

    print("\nFetching NFL standings data")
    print("-" * 50)
    
    # For testing purposes, we'll first try the direct request
    standings_json = fetch_direct_standings()
    
    if not standings_json:
        print("✗ Failed to fetch standings data directly")
        return
        
    # Save the raw JSON for analysis
    with open("json_output/nfl_standings_direct.json", "w") as f:
        json.dump(standings_json, f, indent=2)
    
    print("✓ Successfully fetched standings data")
    
    # Basic validation and display from the direct JSON
    if "name" not in standings_json or "children" not in standings_json:
        print("✗ Response does not match expected structure")
        return
    
    print(f"\n=== {standings_json.get('name', 'NFL')} Standings ===")
    
    children = standings_json.get("children", [])
    for conference in children:
        print(f"\n--- {conference.get('name', 'Unknown')} ---")
        
        standings = conference.get("standings", {})
        print(f"Season: {standings.get('season', 'Unknown')} ({standings.get('seasonType', 'Unknown')})")
        
        entries = standings.get("entries", [])
        if not entries:
            print("No standings entries found")
            continue
            
        print("\nTeam                  W-L    PCT   PF    PA    DIFF")
        print("--------------------------------------------------")
        
        for entry in entries[:5]:  # Show first 5 teams per conference
            team = entry.get("team", {})
            team_name = team.get("displayName", "Unknown")
            
            stats = entry.get("stats", [])
            wins = next((s.get("value", 0) for s in stats if s.get("name") == "wins"), 0)
            losses = next((s.get("value", 0) for s in stats if s.get("name") == "losses"), 0)
            win_pct = next((s.get("displayValue", "0.000") for s in stats if s.get("name") == "winPercent"), "0.000")
            points_for = next((s.get("value", 0) for s in stats if s.get("name") == "pointsFor"), 0)
            points_against = next((s.get("value", 0) for s in stats if s.get("name") == "pointsAgainst"), 0)
            diff = next((s.get("displayValue", "0") for s in stats if s.get("name") == "differential"), "0")
            
            print(f"{team_name:<20}  {int(wins)}-{int(losses)}  {win_pct:<5} {int(points_for):<5} {int(points_against):<5} {diff}")
    
    print("\n✓ Full standings response saved to json_output/nfl_standings_direct.json")
    
    # Now try using the generated client
    try:
        print("\nUsing the generated client to fetch standings:")
        # Use the proper enum for seasontype
        season_type = GetNFLStandingsSeasontype.VALUE_2  # Regular season

        # For debugging, directly call the API with requests
        base_url = "https://site.api.espn.com/apis"
        endpoint = "/v2/sports/football/nfl/standings"
        params = {"season": 2024, "seasontype": 2}

        print(f"Making direct request to: {base_url}{endpoint} with params: {params}")
        response = requests.get(f"{base_url}{endpoint}", params=params)

        if response.status_code == 200:
            print("✓ Direct request successful")
            print(f"Content-Type: {response.headers.get('Content-Type')}")

            # Save the raw direct response
            with open("json_output/nfl_standings_response_direct.json", "w") as f:
                json.dump(response.json(), f, indent=2)
            print("✓ Direct response saved to json_output/nfl_standings_response_direct.json")

            # Try to use the client
            try:
                standings_data = sync(client=client, season=2024, seasontype=season_type)

                if isinstance(standings_data, ErrorResponse):
                    print("✗ API returned an error response:")
                    print(
                        standings_data.error.message
                        if hasattr(standings_data, "error")
                        and standings_data.error
                        and hasattr(standings_data.error, "message")
                        else str(standings_data)
                    )
                elif isinstance(standings_data, StandingsResponse):
                    # Validate schema
                    if validate_schema_response(standings_data):
                        print("✓ Response matches expected schema structure")
                    else:
                        print("✗ Response does not match expected schema structure")

                    # Display formatted summary
                    print("\n" + format_standings_response(standings_data))

                    # Save full response for analysis
                    with open("json_output/nfl_standings_response_processed.json", "w") as f:
                        json.dump(standings_data.to_dict(), f, indent=2)
                    print("\n✓ Full processed response saved to json_output/nfl_standings_response_processed.json")
                else:
                    print("✗ Failed to fetch standings data using client")
            except Exception as e:
                print(f"✗ Error processing standings with client: {str(e)}")
                import traceback
                print(traceback.format_exc())
        else:
            print(f"✗ Direct request failed with status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"✗ Error using generated client: {str(e)}")
        import traceback
        print(traceback.format_exc())


if __name__ == "__main__":
    main()