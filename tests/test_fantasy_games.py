import pytest
import json
import logging
from models.site_web_api.espn_site_web_api_client.api.fantasy_football import get_fantasy_football_games

logging.basicConfig(level=logging.INFO)


@pytest.mark.api
def test_get_fantasy_football_games(site_web_api_client, ensure_json_output_dir):
    """Test getting fantasy football games without date filter."""
    response = get_fantasy_football_games.sync_detailed(
        client=site_web_api_client
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, "Response should parse successfully"
    
    # Validate structure
    assert hasattr(result, 'events'), "Response should have events"
    assert hasattr(result, 'statistics'), "Response should have statistics"
    
    # Check events
    assert isinstance(result.events, list), "Events should be a list"
    if len(result.events) > 0:
        event = result.events[0]
        assert hasattr(event, 'id'), "Event should have id"
        assert hasattr(event, 'date'), "Event should have date"
        assert hasattr(event, 'competitors'), "Event should have competitors"
    
    # Check statistics
    assert isinstance(result.statistics, list), "Statistics should be a list"
    
    # Save response
    with open(f"{ensure_json_output_dir}/fantasy_ffl_games_test.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    logging.info(f"Retrieved {len(result.events)} fantasy football games")
    logging.info(f"Found {len(result.statistics)} statistics types")


@pytest.mark.api
def test_get_fantasy_football_games_with_date(site_web_api_client, ensure_json_output_dir):
    """Test getting fantasy football games with date filter."""
    # Use a date during NFL season
    test_date = "20241201"
    
    response = get_fantasy_football_games.sync_detailed(
        client=site_web_api_client,
        dates=test_date
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, "Response should parse successfully"
    
    # Validate we got events for that date
    assert len(result.events) > 0, f"Should have events for {test_date}"
    
    # Check first event
    event = result.events[0]
    if hasattr(event, 'competitors') and event.competitors:
        assert len(event.competitors) == 2, "Each event should have 2 competitors"
        
        # Check competitor structure
        for competitor in event.competitors:
            assert hasattr(competitor, 'home_away'), "Competitor should have home_away"
            assert hasattr(competitor, 'display_name'), "Competitor should have display_name"
            
            # Check for fantasy-relevant data
            if hasattr(competitor, 'leaders') and competitor.leaders:
                leader = competitor.leaders[0]
                assert hasattr(leader, 'name'), "Leader should have name"
                assert hasattr(leader, 'display_value'), "Leader should have display_value"
    
    # Save response
    with open(f"{ensure_json_output_dir}/fantasy_ffl_games_{test_date}_test.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    logging.info(f"Retrieved {len(result.events)} games for {test_date}")


@pytest.mark.api
@pytest.mark.parametrize("date_range", [
    "20241124-20241130",  # Week 13 of 2024 NFL season
    "20241201-20241207",  # Week 14 of 2024 NFL season
])
def test_get_fantasy_football_games_date_range(site_web_api_client, date_range):
    """Test getting fantasy football games with date range."""
    response = get_fantasy_football_games.sync_detailed(
        client=site_web_api_client,
        dates=date_range
    )
    
    assert response.status_code == 200, f"Expected status code 200 for {date_range}, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, f"Response should parse successfully for {date_range}"
    
    # Check we got multiple games
    assert len(result.events) > 0, f"Should have events for date range {date_range}"
    
    logging.info(f"Date range {date_range}: {len(result.events)} games")