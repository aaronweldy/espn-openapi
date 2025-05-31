"""Test the generic team details endpoint."""

import pytest
import json
from models.site_api.espn_nfl_api_client.api.default import get_team_details
from models.site_api.espn_nfl_api_client.models.team_details_response import (
    TeamDetailsResponse,
)
from models.site_api.espn_nfl_api_client.models.sport_enum import SportEnum
from models.site_api.espn_nfl_api_client.models.league_enum import LeagueEnum


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league,team_id,team_name_contains",
    [
        (SportEnum.BASKETBALL, LeagueEnum.NBA, "LAL", "Lakers"),
        (SportEnum.BASKETBALL, LeagueEnum.NBA, "13", "Lakers"),  # Numeric ID
        (SportEnum.BASKETBALL, LeagueEnum.NBA, "BOS", "Celtics"),
        (SportEnum.BASKETBALL, LeagueEnum.WNBA, "LA", "Sparks"),
        (SportEnum.FOOTBALL, LeagueEnum.NFL, "KC", "Chiefs"),
        (SportEnum.BASEBALL, LeagueEnum.MLB, "NYY", "Yankees"),
        (SportEnum.HOCKEY, LeagueEnum.NHL, "TOR", "Maple Leafs"),
    ],
)
def test_get_team_details_cross_sport(
    site_api_client, sport, league, team_id, team_name_contains, ensure_json_output_dir
):
    """Test getting team details for various sports and leagues."""
    response = get_team_details.sync_detailed(
        client=site_api_client, sport=sport, league=league, team_id_or_abbrev=team_id
    )

    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, TeamDetailsResponse), (
        "Response should parse to TeamDetailsResponse"
    )

    # Verify team data
    assert result.team, "Response should have team data"
    assert result.team.display_name, "Team should have display name"
    assert team_name_contains in result.team.display_name, (
        f"Expected team name to contain '{team_name_contains}'"
    )

    # Save response for analysis
    filename = f"{sport.value}_{league.value}_team_{team_id.replace('/', '_')}.json"
    with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
        json.dump(result.to_dict(), f, indent=2)


@pytest.mark.api
def test_team_details_invalid_id(site_api_client):
    """Test team details with invalid team ID."""
    response = get_team_details.sync_detailed(
        client=site_api_client,
        sport=SportEnum.BASKETBALL,
        league=LeagueEnum.NBA,
        team_id_or_abbrev="INVALID",
    )

    assert response.status_code == 400, (
        f"Expected status code 400 for invalid team, got {response.status_code}"
    )


@pytest.mark.api
def test_team_details_response_structure(site_api_client):
    """Test the structure of the team details response."""
    response = get_team_details.sync_detailed(
        client=site_api_client,
        sport=SportEnum.BASKETBALL,
        league=LeagueEnum.NBA,
        team_id_or_abbrev="LAL",
    )

    assert response.status_code == 200
    result = response.parsed
    assert isinstance(result, TeamDetailsResponse), (
        "Response should parse to TeamDetailsResponse"
    )

    # Check team structure
    assert result.team.id, "Team should have ID"
    assert result.team.uid, "Team should have UID"
    assert result.team.slug, "Team should have slug"
    assert result.team.abbreviation, "Team should have abbreviation"

    # Check optional fields
    if result.team.color:
        assert isinstance(result.team.color, str), "Color should be string"

    if result.team.logos:
        assert len(result.team.logos) > 0, "Should have at least one logo"
        assert result.team.logos[0].href, "Logo should have href"

    if result.team.record:
        assert hasattr(result.team.record, "items"), "Record should have items"
