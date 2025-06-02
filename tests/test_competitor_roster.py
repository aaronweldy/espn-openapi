import pytest
import json
from models.sports_core_api.espn_sports_core_api_client.api.default import get_competitor_roster
from models.sports_core_api.espn_sports_core_api_client.models.competitor_roster_response import CompetitorRosterResponse


@pytest.mark.api
def test_get_competitor_roster_nfl(sports_core_api_client, ensure_json_output_dir):
    """Test getting competitor roster for NFL event - basic functionality."""
    # Using a known NFL game with valid roster data
    event_id = "401547417"
    competition_id = "401547417"
    competitor_id = "1"  # Team 1 in this game
    
    response = get_competitor_roster.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        event_id=event_id,
        competition_id=competition_id,
        competitor_id=competitor_id
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.parsed is not None, "Response should have parsed content"
    
    result = response.parsed
    assert isinstance(result, CompetitorRosterResponse), "Response should parse to CompetitorRosterResponse"
    
    # Validate structure
    assert result.ref, "Response should have $ref field"
    assert result.entries, "Response should have entries (roster players)"
    assert len(result.entries) > 0, "Should have at least one roster entry"
    
    # Check first entry structure
    first_entry = result.entries[0]
    assert first_entry.player_id, "Entry should have player_id"
    assert first_entry.jersey, "Entry should have jersey number"
    assert first_entry.display_name, "Entry should have display_name"
    assert first_entry.athlete, "Entry should have athlete reference"
    assert hasattr(first_entry, 'starter'), "Entry should have starter field"
    assert hasattr(first_entry, 'valid'), "Entry should have valid field"
    assert hasattr(first_entry, 'did_not_play'), "Entry should have did_not_play field"
    
    # Save response
    with open(f"{ensure_json_output_dir}/competitor_roster_nfl_{event_id}_competitor{competitor_id}_test.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    print(f"Successfully retrieved roster for NFL game {event_id}, competitor {competitor_id}")
    print(f"Roster contains {len(result.entries)} players")
    if len(result.entries) > 0:
        print(f"First player: {first_entry.display_name} (#{first_entry.jersey})")


@pytest.mark.api
def test_get_competitor_roster_multiple_competitors(sports_core_api_client, ensure_json_output_dir):
    """Test getting roster for both competitors in an NFL game."""
    event_id = "401547417"
    competition_id = "401547417"
    
    # Test both competitors in the game
    for competitor_id in ["1", "9"]:  # Team 1 and Team 9
        response = get_competitor_roster.sync_detailed(
            client=sports_core_api_client,
            sport="football",
            league="nfl",
            event_id=event_id,
            competition_id=competition_id,
            competitor_id=competitor_id
        )
        
        assert response.status_code == 200, f"Expected status code 200 for competitor {competitor_id}, got {response.status_code}"
        result = response.parsed
        assert isinstance(result, CompetitorRosterResponse), f"Response should parse to CompetitorRosterResponse for competitor {competitor_id}"
        assert result.entries, f"Should have roster entries for competitor {competitor_id}"
        
        # Save each competitor's roster
        with open(f"{ensure_json_output_dir}/competitor_roster_nfl_{event_id}_competitor{competitor_id}_multi_test.json", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
        
        print(f"Competitor {competitor_id}: {len(result.entries)} players")


@pytest.mark.api
def test_get_competitor_roster_cross_sport(sports_core_api_client, ensure_json_output_dir):
    """Test competitor roster across different sports where supported."""
    test_cases = [
        # NFL - Known to work
        {
            "sport": "football",
            "league": "nfl", 
            "event_id": "401547417",
            "competition_id": "401547417",
            "competitor_id": "1",
            "should_work": True
        },
        # Basketball - May or may not work
        {
            "sport": "basketball",
            "league": "nba",
            "event_id": "401584793", 
            "competition_id": "401584793",
            "competitor_id": "2",
            "should_work": False  # Expect this might not work
        },
        # Baseball - May or may not work
        {
            "sport": "baseball",
            "league": "mlb",
            "event_id": "401472463",
            "competition_id": "401472463", 
            "competitor_id": "3",
            "should_work": False  # Expect this might not work
        }
    ]
    
    for test_case in test_cases:
        sport = test_case["sport"]
        league = test_case["league"]
        event_id = test_case["event_id"]
        competition_id = test_case["competition_id"]
        competitor_id = test_case["competitor_id"]
        should_work = test_case["should_work"]
        
        response = get_competitor_roster.sync_detailed(
            client=sports_core_api_client,
            sport=sport,
            league=league,
            event_id=event_id,
            competition_id=competition_id,
            competitor_id=competitor_id
        )
        
        if should_work:
            assert response.status_code == 200, f"Expected {sport}/{league} to work, got {response.status_code}"
            result = response.parsed
            assert isinstance(result, CompetitorRosterResponse), f"Response should parse for {sport}/{league}"
            assert result.entries, f"Should have roster entries for {sport}/{league}"
            
            with open(f"{ensure_json_output_dir}/competitor_roster_{sport}_{league}_{event_id}_test.json", "w") as f:
                json.dump(result.to_dict(), f, indent=2)
                
            print(f"✓ {sport.upper()}/{league.upper()}: {len(result.entries)} players")
        else:
            # These might return 404 or other errors - that's expected
            if response.status_code == 200:
                result = response.parsed
                if isinstance(result, CompetitorRosterResponse) and result.entries:
                    with open(f"{ensure_json_output_dir}/competitor_roster_{sport}_{league}_{event_id}_test.json", "w") as f:
                        json.dump(result.to_dict(), f, indent=2)
                    print(f"✓ {sport.upper()}/{league.upper()}: {len(result.entries)} players (unexpected success)")
                else:
                    print(f"? {sport.upper()}/{league.upper()}: Got 200 but no valid roster data")
            else:
                print(f"✗ {sport.upper()}/{league.upper()}: {response.status_code} (expected)")


@pytest.mark.api
def test_get_competitor_roster_invalid_params(sports_core_api_client):
    """Test competitor roster with invalid parameters."""
    # Test with invalid event ID
    response = get_competitor_roster.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        event_id="999999999",
        competition_id="999999999",
        competitor_id="1"
    )
    
    # Should return 404 for invalid event
    assert response.status_code in [400, 404], f"Expected 400 or 404 for invalid event, got {response.status_code}"
    
    # Test with invalid competitor ID in valid event
    response = get_competitor_roster.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        event_id="401547417",
        competition_id="401547417",
        competitor_id="999"  # Invalid competitor ID
    )
    
    # Should return 404 for invalid competitor
    assert response.status_code in [400, 404], f"Expected 400 or 404 for invalid competitor, got {response.status_code}"


@pytest.mark.api 
def test_competitor_roster_data_validation(sports_core_api_client):
    """Test that competitor roster data contains expected fields and types."""
    response = get_competitor_roster.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl", 
        event_id="401547417",
        competition_id="401547417",
        competitor_id="1"
    )
    
    assert response.status_code == 200
    result = response.parsed
    assert isinstance(result, CompetitorRosterResponse)
    
    # Validate response structure
    assert result.ref.startswith("http"), "$ref should be a valid URL"
    assert "roster" in result.ref, "$ref should contain 'roster'"
    
    # Check entries
    assert len(result.entries) > 0, "Should have roster entries"
    
    for entry in result.entries[:5]:  # Check first 5 entries
        # Required fields
        assert isinstance(entry.player_id, int), "player_id should be integer"
        assert isinstance(entry.jersey, str), "jersey should be string"
        assert isinstance(entry.display_name, str), "display_name should be string"
        assert isinstance(entry.starter, bool), "starter should be boolean"
        assert isinstance(entry.valid, bool), "valid should be boolean"
        assert isinstance(entry.did_not_play, bool), "did_not_play should be boolean"
        
        # References should be valid
        assert entry.athlete, "athlete reference should exist"
        assert entry.athlete.ref, "athlete should have $ref"
        
        if entry.position:
            assert entry.position.ref, "position should have $ref if present"
            
        if entry.statistics:
            assert entry.statistics.ref, "statistics should have $ref if present"
        
        print(f"Player: {entry.display_name} (#{entry.jersey}) - Starter: {entry.starter}")