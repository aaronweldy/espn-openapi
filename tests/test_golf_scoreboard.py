import pytest
import json
from models.site_api.espn_nfl_api_client.api.default import get_scoreboard
from models.site_api.espn_nfl_api_client.models import SportEnum, LeagueEnum


@pytest.mark.api
def test_golf_pga_scoreboard(site_api_client, ensure_json_output_dir):
    """Test that golf/pga scoreboard works with the generic endpoint."""
    
    response = get_scoreboard.sync_detailed(
        client=site_api_client,
        sport=SportEnum.GOLF,
        league=LeagueEnum.PGA
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, "Response should parse successfully"
    
    # Check basic structure
    assert hasattr(result, 'leagues'), "Response should have leagues"
    assert hasattr(result, 'events'), "Response should have events"
    assert hasattr(result, 'season'), "Response should have season"
    
    # Check leagues
    assert result.leagues, "Leagues should not be empty"
    first_league = result.leagues[0]
    assert first_league.name, "League should have a name"
    assert first_league.abbreviation == "PGA", "League abbreviation should be PGA"
    
    # Check events (tournaments)
    if result.events:
        first_event = result.events[0]
        assert hasattr(first_event, 'name'), "Event should have a name"
        assert hasattr(first_event, 'id'), "Event should have an ID"
        
        # Golf-specific: competitions are rounds
        if hasattr(first_event, 'competitions') and first_event.competitions:
            competition = first_event.competitions[0]
            assert hasattr(competition, 'status'), "Competition should have status"
            
            # Check for competitors (golfers)
            if hasattr(competition, 'competitors') and competition.competitors:
                first_competitor = competition.competitors[0]
                assert hasattr(first_competitor, 'id'), "Competitor should have ID"
                
                # Golfers have athletes instead of team
                if hasattr(first_competitor, 'athlete'):
                    athlete = first_competitor.athlete
                    assert hasattr(athlete, 'display_name'), "Athlete should have display name"
        
        print(f"\nCurrent tournament: {first_event.name}")
        print(f"Event ID: {first_event.id}")
        if hasattr(first_event, 'competitions') and first_event.competitions:
            print(f"Number of rounds: {len(first_event.competitions)}")
    else:
        print("\nNo active tournaments at this time")
    
    # Save sample data
    sample_data = {
        'league': first_league.name if first_league.name else None,
        'abbreviation': first_league.abbreviation if first_league.abbreviation else None,
        'event_count': len(result.events) if result.events else 0,
        'has_active_tournaments': len(result.events) > 0 if result.events else False
    }
    
    if result.events and len(result.events) > 0:
        sample_data['current_tournament'] = result.events[0].name if result.events[0].name else None
    
    with open(f"{ensure_json_output_dir}/golf_pga_scoreboard_test.json", "w") as f:
        json.dump(sample_data, f, indent=2)
    
    print(f"\n✓ Golf/PGA scoreboard endpoint works with generic implementation")


@pytest.mark.api  
def test_golf_lpga_scoreboard(site_api_client):
    """Test that golf/lpga also works."""
    
    response = get_scoreboard.sync_detailed(
        client=site_api_client,
        sport=SportEnum.GOLF,
        league=LeagueEnum.LPGA
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, "Response should parse successfully"
    
    # Check leagues
    assert result.leagues, "Leagues should not be empty"
    first_league = result.leagues[0]
    assert first_league.abbreviation == "LPGA", "League abbreviation should be LPGA"
    
    print(f"\n✓ Golf/LPGA scoreboard endpoint also works")