#!/usr/bin/env python3
"""
Test ESPN NFL API - Team Details Endpoint
Requires Python 3.10+
"""

import json
import pytest
import requests

from models.site_api.espn_nfl_api_client.api.default.get_nfl_team_details import sync
from models.site_api.espn_nfl_api_client.api.default.get_mlb_team_details import (
    sync as get_mlb_team_details,
)
from models.site_api.espn_nfl_api_client.models.error_response import ErrorResponse
from models.site_api.espn_nfl_api_client.models.team_details_response import (
    TeamDetailsResponse,
)
from models.site_api.espn_nfl_api_client.models.get_mlb_team_details_team_id_or_abbrev import (
    GetMLBTeamDetailsTeamIdOrAbbrev,
)
from models.site_api.espn_nfl_api_client.types import UNSET


def validate_schema_response(data: TeamDetailsResponse) -> bool:
    """Validate if response matches expected schema structure."""
    if not data.team:
        print("Missing required attribute: team")
        return False

    team = data.team
    required_attrs = ["id", "display_name", "abbreviation"]
    for attr in required_attrs:
        if getattr(team, attr, UNSET) is UNSET:
            print(f"Missing required attribute: {attr}")
            return False

    # We'll validate other fields when we have the actual API response
    # to see the exact field names

    return True


def format_team_details(data: TeamDetailsResponse) -> str:
    """Format team details data for display."""
    if not data.team:
        return "Invalid data format: missing team"

    team = data.team
    output = []
    output.append(f"=== {team.display_name} ({team.abbreviation}) ===")
    output.append(f"Team ID: {team.id}")

    if team.location and team.name:
        output.append(f"Location: {team.location}")
        output.append(f"Name: {team.name}")

    if team.color:
        output.append(
            f"Colors: Primary={team.color}, Alt={team.alternate_color or 'None'}"
        )

    # Add logo URL if available
    if team.logos and len(team.logos) > 0:
        output.append(f"Logo: {team.logos[0].href}")

    # Add record if available
    if team.record and hasattr(team.record, "items") and team.record.items:
        output.append("\n--- Records ---")
        for record in team.record.items:
            desc = record.description or record.type or ""
            output.append(f"{desc}: {record.summary}")

    # Add standing summary if available
    if team.standing_summary:
        output.append(f"\nStanding: {team.standing_summary}")

    # Add venue info if available in franchise
    if team.franchise and team.franchise.venue:
        venue = team.franchise.venue
        output.append("\n--- Venue ---")
        output.append(f"Name: {venue.full_name}")
        if venue.address:
            city = venue.address.city or ""
            state = venue.address.state or ""
            output.append(f"Location: {city}, {state}")
        output.append(f"Indoor: {'Yes' if venue.indoor else 'No'}")
        output.append(f"Grass: {'Yes' if venue.grass else 'No'}")

    return "\n".join(output)


def fetch_direct_team_details(team_id: str):
    """Fetch the team details data directly using requests to bypass model issues."""
    url = f"https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/{team_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


@pytest.mark.api
def test_mlb_team_details(site_api_client, ensure_json_output_dir):
    """Test the ESPN MLB Team Details API."""
    print("\nFetching MLB team details for team ID: BOS (Boston Red Sox)")
    print("-" * 50)

    # Use the enum value instead of an integer
    team_data = get_mlb_team_details(
        client=site_api_client, team_id_or_abbrev=GetMLBTeamDetailsTeamIdOrAbbrev.BOS
    )

    assert not isinstance(team_data, ErrorResponse), (
        f"API returned an error response: "
        f"{team_data.error.message if team_data.error and team_data.error.message else str(team_data)}"
    )

    assert isinstance(team_data, TeamDetailsResponse), (
        "Response should be a TeamDetailsResponse"
    )

    # Validate schema
    assert validate_schema_response(team_data), (
        "Response does not match expected schema structure"
    )

    # Display formatted summary
    print("\n" + format_team_details(team_data))

    # Save full response for analysis
    with open(
        f"{ensure_json_output_dir}/mlb_team_details_response_processed.json", "w"
    ) as f:
        json.dump(team_data.to_dict(), f, indent=2)

    print(
        f"\n✓ Full processed response saved to {ensure_json_output_dir}/mlb_team_details_response_processed.json"
    )


@pytest.mark.api
def test_nfl_team_details(site_api_client, ensure_json_output_dir):
    """Test the ESPN NFL Team Details API."""
    print("ESPN NFL Team Details API Test")
    print("=" * 50)

    # Team ID to test with - Kansas City Chiefs
    team_id = "12"

    print(f"\nFetching NFL team details for team ID: {team_id}")
    print("-" * 50)

    try:
        print("\nUsing the generated client to fetch team details:")
        team_data = sync(client=site_api_client, team_id=team_id)

        assert not isinstance(team_data, ErrorResponse), (
            f"API returned an error response: "
            f"{team_data.error.message if team_data.error and team_data.error.message else str(team_data)}"
        )

        assert isinstance(team_data, TeamDetailsResponse), (
            "Response should be a TeamDetailsResponse"
        )

        # Validate schema
        assert validate_schema_response(team_data), (
            "Response does not match expected schema structure"
        )

        # Display formatted summary
        print("\n" + format_team_details(team_data))

        # Save full response for analysis
        with open(
            f"{ensure_json_output_dir}/nfl_team_details_response_processed.json", "w"
        ) as f:
            json.dump(team_data.to_dict(), f, indent=2)

        print(
            f"\n✓ Full processed response saved to {ensure_json_output_dir}/nfl_team_details_response_processed.json"
        )

    except Exception as e:
        print(f"✗ Error using generated client: {str(e)}")

        # Fall back to direct request
        print("\nFalling back to direct request:")
        team_json = fetch_direct_team_details(team_id)

        assert team_json is not None, (
            f"Failed to fetch team details for team ID {team_id} directly"
        )

        # Save the raw JSON for analysis
        with open(f"{ensure_json_output_dir}/nfl_team_details_direct.json", "w") as f:
            json.dump(team_json, f, indent=2)

        print("✓ Successfully fetched team details")

        # Basic validation and display from the direct JSON
        assert "team" in team_json, "Response does not match expected structure"

        team = team_json["team"]
        print(
            f"\n=== {team.get('displayName', 'Unknown')} ({team.get('abbreviation', 'UNK')}) ==="
        )
        print(f"Team ID: {team.get('id', 'Unknown')}")
        print(f"Location: {team.get('location', 'Unknown')}")
        print(
            f"Colors: Primary={team.get('color', 'Unknown')}, Alt={team.get('alternateColor', 'None')}"
        )

        print(
            f"\n✓ Full team details response saved to {ensure_json_output_dir}/nfl_team_details_direct.json"
        )

        # If we get here after falling back to direct request, fail the test
        pytest.fail(f"API client failed, had to use direct request: {str(e)}")
