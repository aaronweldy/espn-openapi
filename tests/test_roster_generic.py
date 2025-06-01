import pytest
import json
from models.site_api.espn_nfl_api_client.api.default import get_team_roster
from models.site_api.espn_nfl_api_client.models.team_roster_response import TeamRosterResponse
from models.site_api.espn_nfl_api_client.models.sport_enum import SportEnum
from models.site_api.espn_nfl_api_client.models.league_enum import LeagueEnum


@pytest.mark.api
@pytest.mark.parametrize("sport,league,team_id", [
    (SportEnum.FOOTBALL, LeagueEnum.NFL, "KC"),
    (SportEnum.BASKETBALL, LeagueEnum.NBA, "LAL"),
    (SportEnum.BASEBALL, LeagueEnum.MLB, "NYY"),
    (SportEnum.HOCKEY, LeagueEnum.NHL, "TOR"),
    (SportEnum.FOOTBALL, LeagueEnum.COLLEGE_FOOTBALL, "MICH"),
    (SportEnum.BASKETBALL, LeagueEnum.MENS_COLLEGE_BASKETBALL, "DUKE"),
    (SportEnum.BASKETBALL, LeagueEnum.WOMENS_COLLEGE_BASKETBALL, "2"),
])
def test_get_team_roster_cross_sport(site_api_client, ensure_json_output_dir, sport, league, team_id):
    """Test retrieving team roster for various sports and leagues."""
    response = get_team_roster.sync_detailed(
        client=site_api_client,
        sport=sport,
        league=league,
        team_id_or_abbrev=team_id
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code} for {sport}/{league}/{team_id}"
    
    result = response.parsed
    assert isinstance(result, TeamRosterResponse), f"Response should parse to TeamRosterResponse for {sport}/{league}"
    
    # Validate required fields
    assert result.status, f"Response should have status field for {sport}/{league}"
    assert result.timestamp, f"Response should have timestamp field for {sport}/{league}"
    assert result.season, f"Response should have season field for {sport}/{league}"
    assert result.team, f"Response should have team field for {sport}/{league}"
    assert result.athletes, f"Response should have athletes field for {sport}/{league}"
    
    # Validate team info
    assert result.team.id, f"Team should have ID for {sport}/{league}"
    assert result.team.display_name, f"Team should have display name for {sport}/{league}"
    
    # Validate athletes structure (can be position groups or direct athletes)
    assert len(result.athletes) > 0, f"Should have at least one athlete/position group for {sport}/{league}"
    
    # Check if it's position groups (NFL/MLB style) or direct athletes (NBA style)
    first_item = result.athletes[0]
    
    # Import the model classes
    from models.site_api.espn_nfl_api_client.models.position_group import PositionGroup
    from models.site_api.espn_nfl_api_client.models.roster_athlete import RosterAthlete
    
    if isinstance(first_item, PositionGroup):
        # Position group structure (NFL/MLB/College Football)
        has_athletes = False
        for group in result.athletes:
            assert group.position, f"Position group should have position field for {sport}/{league}"
            assert hasattr(group, 'items'), f"Position group should have items field for {sport}/{league}"
            
            # Some groups might be empty (e.g., injured reserve)
            if group.items and len(group.items) > 0:
                has_athletes = True
                # Validate first athlete in group
                athlete = group.items[0]
                assert athlete.id, f"Athlete should have ID for {sport}/{league}"
                assert athlete.display_name, f"Athlete should have display name for {sport}/{league}"
        
        assert has_athletes, f"Should have at least one athlete across all position groups for {sport}/{league}"
    elif isinstance(first_item, RosterAthlete):
        # Direct athlete structure (NBA/College Basketball)
        for athlete in result.athletes:
            assert athlete.id, f"Athlete should have ID for {sport}/{league}"
            assert athlete.display_name, f"Athlete should have display name for {sport}/{league}"
    else:
        pytest.fail(f"Unexpected athlete structure type: {type(first_item)} for {sport}/{league}")
    
    # Validate coaches if present
    if result.coach:
        assert len(result.coach) > 0, f"If coach field exists, should have at least one coach for {sport}/{league}"
        coach = result.coach[0]
        assert coach.id, f"Coach should have ID for {sport}/{league}"
        assert coach.first_name, f"Coach should have first name for {sport}/{league}"
        assert coach.last_name, f"Coach should have last name for {sport}/{league}"
    
    # Save one example response for reference
    if sport == SportEnum.FOOTBALL and league == LeagueEnum.COLLEGE_FOOTBALL:
        with open(f"{ensure_json_output_dir}/roster_{league.value}_{team_id}_generic.json", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
    
    print(f"✓ {sport.value}/{league.value} roster for {team_id}: {result.team.display_name} - {len(result.athletes)} position groups")


@pytest.mark.api
def test_get_team_roster_invalid_team(site_api_client):
    """Test retrieving roster with invalid team ID."""
    response = get_team_roster.sync_detailed(
        client=site_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        team_id_or_abbrev="INVALID"
    )
    
    # ESPN API typically returns 400 for invalid team IDs
    assert response.status_code == 400, f"Expected status code 400 for invalid team, got {response.status_code}"