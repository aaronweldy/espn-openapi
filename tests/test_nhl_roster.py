import pytest
import json
from models.site_api.espn_nfl_api_client.api.default import get_nhl_team_roster
from models.site_api.espn_nfl_api_client.models.nhl_team_roster_response import NhlTeamRosterResponse


@pytest.mark.api
def test_get_nhl_team_roster(site_api_client, ensure_json_output_dir):
    """Test getting NHL team roster."""
    response = get_nhl_team_roster.sync_detailed(
        client=site_api_client,
        team_id_or_abbrev="TOR"
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, "Response should not be None"
    assert isinstance(result, NhlTeamRosterResponse), "Response should parse to NhlTeamRosterResponse"
    
    # Validate team information
    assert result.team, "Response should have team information"
    assert result.team.display_name, "Team should have display name"
    
    # Validate athletes (position groups)
    assert result.athletes, "Response should have athlete position groups"
    assert len(result.athletes) > 0, "Team should have at least one position group"
    
    # Check first position group
    first_group = result.athletes[0]
    assert first_group.position, "Position group should have a position name"
    assert first_group.items, "Position group should have athletes"
    assert len(first_group.items) > 0, "Position group should have at least one athlete"
    
    # Check first athlete in first group has required fields
    first_athlete = first_group.items[0]
    assert first_athlete.id, "Athlete should have an ID"
    assert first_athlete.full_name, "Athlete should have a full name"
    
    # Save response for reference
    with open(f"{ensure_json_output_dir}/nhl_team_roster_test.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    print(f"NHL Team Roster for {result.team.display_name}:")
    
    # Count total athletes
    total_athletes = sum(len(group.items) for group in result.athletes)
    print(f"  Total Athletes: {total_athletes}")
    
    if result.coach:
        print(f"  Total Coaches: {len(result.coach)}")
        for coach in result.coach:
            print(f"    Head Coach: {coach.first_name} {coach.last_name}")
    
    # Show athletes by position
    for group in result.athletes:
        print(f"\n  {group.position} ({len(group.items)}):")
        for i, athlete in enumerate(group.items[:3]):  # Show first 3 of each position
            position_info = ""
            if athlete.position and athlete.position.display_name:
                position_info = athlete.position.display_name
            jersey = athlete.jersey if athlete.jersey else "N/A"
            print(f"    {i+1}. {athlete.full_name} - {position_info} (#{jersey})")


@pytest.mark.api
@pytest.mark.parametrize("team_id", [
    "TOR",  # Toronto Maple Leafs
    "BOS",  # Boston Bruins
    "1",    # New Jersey Devils (by ID)
])
def test_get_nhl_team_roster_multiple_teams(site_api_client, team_id):
    """Test getting NHL team roster for multiple teams."""
    response = get_nhl_team_roster.sync_detailed(
        client=site_api_client,
        team_id_or_abbrev=team_id
    )
    
    assert response.status_code == 200, f"Expected status code 200 for team {team_id}, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, f"Response should not be None for team {team_id}"
    assert isinstance(result, NhlTeamRosterResponse), f"Response should parse to NhlTeamRosterResponse for team {team_id}"
    assert result.athletes, f"Team {team_id} should have athletes"


@pytest.mark.api  
def test_get_nhl_team_roster_invalid_team(site_api_client):
    """Test getting NHL team roster with invalid team ID."""
    response = get_nhl_team_roster.sync_detailed(
        client=site_api_client,
        team_id_or_abbrev="INVALID"
    )
    
    # ESPN API typically returns 400 for invalid team IDs
    assert response.status_code == 400, f"Expected status code 400 for invalid team, got {response.status_code}"