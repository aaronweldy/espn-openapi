import pytest
import json
import logging
from models.site_api.espn_nfl_api_client.api.fantasy_football import get_fantasy_player_news

logging.basicConfig(level=logging.INFO)


@pytest.mark.api
def test_get_fantasy_player_news_no_filter(site_api_fantasy_client, ensure_json_output_dir):
    """Test getting fantasy player news without player filter."""
    response = get_fantasy_player_news.sync_detailed(
        client=site_api_fantasy_client,
        limit=5
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, "Response should parse successfully"
    
    # Validate structure
    assert hasattr(result, 'feed'), "Response should have feed"
    assert hasattr(result, 'results_count'), "Response should have results_count"
    assert hasattr(result, 'results_limit'), "Response should have results_limit"
    assert hasattr(result, 'results_offset'), "Response should have results_offset"
    assert hasattr(result, 'status'), "Response should have status"
    assert hasattr(result, 'timestamp'), "Response should have timestamp"
    
    # Check feed
    assert isinstance(result.feed, list), "Feed should be a list"
    
    # Save response
    with open(f"{ensure_json_output_dir}/fantasy_player_news_test.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    logging.info(f"Retrieved {len(result.feed)} news items")
    logging.info(f"Total results available: {result.results_count}")


@pytest.mark.api
def test_get_fantasy_player_news_with_player_id(site_api_fantasy_client, ensure_json_output_dir):
    """Test getting fantasy player news for specific player."""
    # Use Patrick Mahomes as test player
    player_id = 3139477
    
    response = get_fantasy_player_news.sync_detailed(
        client=site_api_fantasy_client,
        player_id=player_id,
        limit=10
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, "Response should parse successfully"
    
    # Check we got player-specific news
    if len(result.feed) > 0:
        # Check first news item
        news_item = result.feed[0]
        assert hasattr(news_item, 'headline'), "News item should have headline"
        assert hasattr(news_item, 'description'), "News item should have description"
        
        # If player_id is present in response, verify it matches
        if hasattr(news_item, 'player_id') and news_item.player_id:
            assert news_item.player_id == player_id, f"Expected player_id {player_id}, got {news_item.player_id}"
        
        # Log some details
        logging.info(f"First headline: {news_item.headline}")
        if hasattr(news_item, 'published') and news_item.published:
            logging.info(f"Published: {news_item.published}")
    
    # Save response
    with open(f"{ensure_json_output_dir}/fantasy_player_news_{player_id}_test.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    logging.info(f"Retrieved {len(result.feed)} news items for player {player_id}")


@pytest.mark.api
@pytest.mark.parametrize("player_id,player_name", [
    (3139477, "Patrick Mahomes"),
    (3915511, "Saquon Barkley"),
    (4241479, "Amon-Ra St. Brown"),
    (4360310, "Kenneth Walker III"),
])
def test_get_fantasy_player_news_multiple_players(site_api_fantasy_client, player_id, player_name):
    """Test getting news for multiple players."""
    response = get_fantasy_player_news.sync_detailed(
        client=site_api_fantasy_client,
        player_id=player_id,
        limit=3
    )
    
    assert response.status_code == 200, f"Expected status code 200 for {player_name}, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, f"Response should parse successfully for {player_name}"
    
    # Log results
    logging.info(f"{player_name} ({player_id}): {len(result.feed)} news items")