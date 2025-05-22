#!/usr/bin/env python3
"""
Test ESPN NFL API - Teams List Endpoint
Requires Python 3.10+
"""

import json
import logging
import pytest

from models.site_api.espn_nfl_api_client.api.default.get_nfl_teams_list import sync
from models.site_api.espn_nfl_api_client.api.default.get_mlb_teams_list import (
    sync as get_mlb_teams_list,
)
from models.site_api.espn_nfl_api_client.models.error_response import ErrorResponse
from models.site_api.espn_nfl_api_client.models.teams_list_response import (
    TeamsListResponse,
)
from models.site_api.espn_nfl_api_client.types import UNSET

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def validate_schema_response(data: TeamsListResponse):
    """Validate if response matches expected schema structure."""
    # Use assertions instead of returning True/False
    assert data.sports, "No sports found or sports list is empty"

    sport = data.sports[0]
    assert sport.id is not UNSET, "Sport is missing ID"
    assert sport.name is not UNSET, "Sport is missing name"
    assert sport.leagues is not UNSET, "Sport is missing leagues"
    assert sport.leagues, "No leagues found or leagues list is empty"

    # Check league
    league = sport.leagues[0]
    assert league.id is not UNSET, "League is missing ID"
    assert league.name is not UNSET, "League is missing name"
    assert league.teams is not UNSET, "League is missing teams"
    assert league.teams, "No teams found or teams list is empty"

    # Check first team
    team_entry = league.teams[0]
    assert team_entry.team is not UNSET, "Invalid team entry structure: missing team"

    team = team_entry.team
    assert team.id is not UNSET, "Team is missing ID"
    assert team.display_name is not UNSET, "Team is missing display name"


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


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,get_teams_func,filename",
    [
        ("NFL", sync, "nfl_teams_response_processed.json"),
        ("MLB", get_mlb_teams_list, "mlb_teams_response_processed.json"),
    ],
)
def test_teams_list(
    site_api_client, ensure_json_output_dir, sport, get_teams_func, filename
):
    """Test the ESPN Teams List API for different sports."""

    logger.info(f"Fetching {sport} teams list data")

    try:
        teams_data = get_teams_func(client=site_api_client)

        assert not isinstance(teams_data, ErrorResponse), (
            f"API returned an error: {teams_data.error.message if teams_data.error else 'Unknown error'}"
        )
        assert isinstance(teams_data, TeamsListResponse), (
            "Response should be a TeamsListResponse"
        )

        # Validate schema structure
        validate_schema_response(teams_data)

        output = format_teams_list(teams_data)
        logger.info(output)

        # Save full response for analysis
        output_path = f"{ensure_json_output_dir}/{filename}"
        with open(output_path, "w") as f:
            json.dump(teams_data.to_dict(), f, indent=2)
        logger.info(f"Full processed response saved to {output_path}")
    except Exception as e:
        logger.error(f"Error using generated client: {str(e)}")
        pytest.fail(f"Exception during test: {str(e)}")
