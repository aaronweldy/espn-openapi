import pytest
import json
from models.sports_core_api.espn_sports_core_api_client.api.default import get_odds_predictors
from models.sports_core_api.espn_sports_core_api_client.models.odds_predictors_response import OddsPredictorsResponse


@pytest.mark.api
def test_get_odds_predictors_nfl(sports_core_api_client, ensure_json_output_dir):
    """Test getting odds predictors for NFL event."""
    # Using a known NFL game with available odds predictors
    event_id = "401326315"
    competition_id = "401326315"
    provider_id = "1003"  # Known working provider
    
    response = get_odds_predictors.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        event_id=event_id,
        competition_id=competition_id,
        provider_id=provider_id
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.parsed is not None, "Response should have parsed content"
    
    result = response.parsed
    assert isinstance(result, OddsPredictorsResponse), "Response should parse to OddsPredictorsResponse"
    
    # Validate structure
    assert result.count > 0, "Should have predictor count"
    assert result.items, "Response should have predictor items"
    assert len(result.items) > 0, "Should have at least one predictor"
    
    # Check first predictor structure
    first_predictor = result.items[0]
    assert first_predictor.rank, "Predictor should have rank"
    assert first_predictor.value, "Predictor should have value"
    assert first_predictor.display_value, "Predictor should have display_value"
    
    # Save response
    with open(f"{ensure_json_output_dir}/odds_predictors_nfl_{event_id}_provider{provider_id}_test.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    print(f"Successfully retrieved {len(result.items)} predictors for NFL game {event_id}")
    print(f"First predictor: Rank {first_predictor.rank}, Value {first_predictor.display_value}")


@pytest.mark.api
def test_get_odds_predictors_multiple_events(sports_core_api_client, ensure_json_output_dir):
    """Test odds predictors with different NFL events."""
    # Test multiple NFL events that have predictors (from 2020-2021 seasons)
    test_events = [
        {"event_id": "401326315", "season": "2021-early"},
        {"event_id": "401326317", "season": "2021-recent"},
        {"event_id": "401249063", "season": "2020"}
    ]
    
    for event_data in test_events:
        event_id = event_data["event_id"]
        season = event_data["season"]
        
        response = get_odds_predictors.sync_detailed(
            client=sports_core_api_client,
            sport="football",
            league="nfl",
            event_id=event_id,
            competition_id=event_id,
            provider_id="1003"
        )
        
        assert response.status_code == 200, f"Expected 200 for event {event_id}, got {response.status_code}"
        result = response.parsed
        assert isinstance(result, OddsPredictorsResponse), f"Should parse for event {event_id}"
        assert result.items, f"Should have predictors for event {event_id}"
        
        # Save response
        with open(f"{ensure_json_output_dir}/odds_predictors_nfl_{event_id}_provider1003_multi_events_test.json", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
            
        print(f"✓ NFL Event {event_id} ({season}): {len(result.items)} predictors")


@pytest.mark.api 
def test_get_odds_predictors_multiple_providers(sports_core_api_client, ensure_json_output_dir):
    """Test odds predictors with different providers."""
    event_id = "401326315"
    competition_id = "401326315"
    
    # Test multiple providers
    provider_ids = ["1003", "1002", "58"]  # Different betting providers
    
    for provider_id in provider_ids:
        response = get_odds_predictors.sync_detailed(
            client=sports_core_api_client,
            sport="football",
            league="nfl",
            event_id=event_id,
            competition_id=competition_id,
            provider_id=provider_id
        )
        
        if response.status_code == 200:
            result = response.parsed
            assert isinstance(result, OddsPredictorsResponse), f"Should parse for provider {provider_id}"
            
            # Save response
            with open(f"{ensure_json_output_dir}/odds_predictors_nfl_{event_id}_provider{provider_id}_multi_test.json", "w") as f:
                json.dump(result.to_dict(), f, indent=2)
                
            print(f"✓ Provider {provider_id}: {len(result.items)} predictors")
        else:
            print(f"✗ Provider {provider_id}: {response.status_code} (no predictors)")


@pytest.mark.api
def test_get_odds_predictors_cross_sport(sports_core_api_client, ensure_json_output_dir):
    """Test odds predictors across different sports."""
    test_cases = [
        # NFL - Known to work
        {
            "sport": "football",
            "league": "nfl", 
            "event_id": "401326315",
            "competition_id": "401326315",
            "provider_id": "1003",
            "should_work": True
        },
        # Basketball - May or may not work
        {
            "sport": "basketball",
            "league": "nba",
            "event_id": "401584793", 
            "competition_id": "401584793",
            "provider_id": "1003",
            "should_work": False
        },
        # Baseball - May or may not work
        {
            "sport": "baseball",
            "league": "mlb",
            "event_id": "401472463",
            "competition_id": "401472463", 
            "provider_id": "1003",
            "should_work": False
        }
    ]
    
    for test_case in test_cases:
        sport = test_case["sport"]
        league = test_case["league"]
        event_id = test_case["event_id"]
        competition_id = test_case["competition_id"]
        provider_id = test_case["provider_id"]
        should_work = test_case["should_work"]
        
        response = get_odds_predictors.sync_detailed(
            client=sports_core_api_client,
            sport=sport,
            league=league,
            event_id=event_id,
            competition_id=competition_id,
            provider_id=provider_id
        )
        
        if should_work:
            assert response.status_code == 200, f"Expected {sport}/{league} to work, got {response.status_code}"
            result = response.parsed
            assert isinstance(result, OddsPredictorsResponse), f"Response should parse for {sport}/{league}"
            
            with open(f"{ensure_json_output_dir}/odds_predictors_{sport}_{league}_{event_id}_test.json", "w") as f:
                json.dump(result.to_dict(), f, indent=2)
                
            print(f"✓ {sport.upper()}/{league.upper()}: {len(result.items)} predictors")
        else:
            # These might return 404 or other errors - that's expected
            if response.status_code == 200:
                result = response.parsed
                if isinstance(result, OddsPredictorsResponse) and result.items:
                    with open(f"{ensure_json_output_dir}/odds_predictors_{sport}_{league}_{event_id}_test.json", "w") as f:
                        json.dump(result.to_dict(), f, indent=2)
                    print(f"✓ {sport.upper()}/{league.upper()}: {len(result.items)} predictors (unexpected success)")
                else:
                    print(f"? {sport.upper()}/{league.upper()}: Got 200 but no valid predictor data")
            else:
                print(f"✗ {sport.upper()}/{league.upper()}: {response.status_code} (expected)")


@pytest.mark.api
def test_get_odds_predictors_invalid_params(sports_core_api_client):
    """Test odds predictors with invalid parameters."""
    # Test with invalid event ID
    response = get_odds_predictors.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        event_id="999999999",
        competition_id="999999999",
        provider_id="1003"
    )
    
    # Should return 404 for invalid event
    assert response.status_code in [400, 404], f"Expected 400 or 404 for invalid event, got {response.status_code}"
    
    # Test with invalid provider ID
    response = get_odds_predictors.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        event_id="401326315",
        competition_id="401326315",
        provider_id="99999"  # Invalid provider ID
    )
    
    # Should return 404 for invalid provider
    assert response.status_code in [400, 404], f"Expected 400 or 404 for invalid provider, got {response.status_code}"


@pytest.mark.api 
def test_odds_predictors_data_validation(sports_core_api_client):
    """Test that odds predictors data contains expected fields and types."""
    response = get_odds_predictors.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl", 
        event_id="401326315",
        competition_id="401326315",
        provider_id="1003"
    )
    
    assert response.status_code == 200
    result = response.parsed
    assert isinstance(result, OddsPredictorsResponse)
    
    # Validate response structure
    assert result.count > 0, "Should have predictor count"
    assert result.page_index >= 1, "Should have valid page index"
    assert result.page_size > 0, "Should have valid page size"
    assert result.page_count >= 1, "Should have valid page count"
    assert len(result.items) <= result.page_size, "Items should not exceed page size"
    
    # Check predictor items
    assert len(result.items) > 0, "Should have predictor items"
    
    for predictor in result.items[:3]:  # Check first 3 predictors
        # Required fields
        assert isinstance(predictor.rank, int), "rank should be integer"
        assert isinstance(predictor.value, (int, float)), "value should be numeric"
        assert isinstance(predictor.display_value, str), "display_value should be string"
        
        # Optional fields that might be present
        if predictor.total:
            assert predictor.total in ["OVER", "UNDER"], "total should be OVER or UNDER if present"
            
        # References should be valid if present
        if predictor.predictor_competition:
            assert predictor.predictor_competition.ref, "predictor_competition should have $ref"
            
        if predictor.projected_winner:
            assert predictor.projected_winner.ref, "projected_winner should have $ref"
        
        print(f"Predictor {predictor.rank}: {predictor.display_value} ({predictor.total if predictor.total else 'N/A'})")