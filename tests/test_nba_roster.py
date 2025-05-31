import pytest
import json
from models.site_api.espn_nfl_api_client.api.default import get_nba_team_roster
from models.site_api.espn_nfl_api_client.models import NBATeamRosterResponse, NBATeamAbbreviation


@pytest.mark.api
def test_get_nba_team_roster_by_abbreviation(site_api_client, ensure_json_output_dir):
    """Test NBA team roster endpoint with team abbreviation."""
    response = get_nba_team_roster.sync_detailed(
        client=site_api_client,
        team_id_or_abbrev="LAL"
    )
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, NBATeamRosterResponse), "Response should be a NBATeamRosterResponse"
    
    # Verify required fields
    assert result.status, "Response should have status"
    assert result.timestamp, "Response should have timestamp"
    assert result.season, "Response should have season"
    assert result.athletes, "Response should have athletes"
    assert result.team, "Response should have team"
    
    # Verify team info
    if result.team:
        assert result.team.id, "Team should have id"
        assert result.team.display_name, "Team should have display name"
        assert result.team.abbreviation == "LAL", "Team abbreviation should match requested"
    
    # Verify athletes list
    assert len(result.athletes) > 0, "Roster should have at least one athlete"
    
    # Check first athlete has expected fields
    first_athlete = result.athletes[0]
    assert first_athlete.id, "Athlete should have id"
    assert first_athlete.display_name, "Athlete should have display name"
    if first_athlete.position:
        # NBA positions are objects with display_name
        assert hasattr(first_athlete.position, 'display_name'), "Position should have display_name"
        assert first_athlete.position.display_name, "Position should have display name value"
    
    # Save test output
    with open(f"{ensure_json_output_dir}/nba_roster_LAL.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    print(f"✓ NBA roster for LAL: {len(result.athletes)} athletes")


@pytest.mark.api
def test_get_nba_team_roster_by_id(site_api_client, ensure_json_output_dir):
    """Test NBA team roster endpoint with numeric team ID."""
    response = get_nba_team_roster.sync_detailed(
        client=site_api_client,
        team_id_or_abbrev="13"  # Lakers numeric ID
    )
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, NBATeamRosterResponse), "Response should be a NBATeamRosterResponse"
    assert result.team.id == "13", "Team ID should match requested ID"
    
    # Save test output
    with open(f"{ensure_json_output_dir}/nba_roster_id_13.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)


@pytest.mark.api
def test_get_nba_team_roster_invalid_team(site_api_client):
    """Test NBA roster endpoint with invalid team."""
    response = get_nba_team_roster.sync_detailed(
        client=site_api_client,
        team_id_or_abbrev="INVALID"
    )
    
    # ESPN API typically returns 400 for invalid team IDs
    assert response.status_code in [400, 404], f"Expected 400 or 404 for invalid team, got {response.status_code}"