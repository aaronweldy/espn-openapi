import pytest
import json
import logging
from models.fantasy_api.espn_fantasy_api_client.api.default import get_fantasy_player_defaults
from models.fantasy_api.espn_fantasy_api_client.models import FantasyPlayerDefaultsResponse
from models.fantasy_api.espn_fantasy_api_client.models.get_fantasy_player_defaults_view import GetFantasyPlayerDefaultsView

logging.basicConfig(level=logging.INFO)


@pytest.mark.api
def test_get_fantasy_player_defaults(fantasy_api_client, ensure_json_output_dir):
    """Test fetching fantasy player defaults with kona_player_info view."""
    
    # Fetch player defaults for 2025 season
    response = get_fantasy_player_defaults.sync_detailed(
        client=fantasy_api_client,
        year=2025,
        segment=0,
        scoring_period_id=1,  # Standard PPR scoring
        view=GetFantasyPlayerDefaultsView.KONA_PLAYER_INFO
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, FantasyPlayerDefaultsResponse), "Response should parse to FantasyPlayerDefaultsResponse"
    assert result.players, "Response should contain players"
    
    # Log some information about the response
    logging.info(f"Fetched {len(result.players)} players with defaults")
    
    # Check the structure of the first player
    if result.players:
        first_player = result.players[0]
        assert first_player.player, "Player object should exist"
        assert first_player.player.id, "Player should have ID"
        assert first_player.player.full_name, "Player should have full name"
        
        # Check fantasy-specific fields
        assert hasattr(first_player, 'draft_auction_value'), "Should have draft auction value"
        assert hasattr(first_player, 'on_team_id'), "Should have on_team_id"
        
        logging.info(f"First player: {first_player.player.full_name} (ID: {first_player.player.id})")
        logging.info(f"Draft value: ${first_player.draft_auction_value}")
        logging.info(f"On team: {first_player.on_team_id}")
    
    # Save a sample response
    sample_data = {
        "total_players": len(result.players),
        "sample_players": [
            {
                "id": p.player.id if p.player else None,
                "name": p.player.full_name if p.player else None,
                "position": p.player.default_position_id if p.player else None,
                "draft_value": p.draft_auction_value,
                "on_team": p.on_team_id
            }
            for p in result.players[:5]
        ]
    }
    
    with open(f"{ensure_json_output_dir}/fantasy_player_defaults_sample.json", "w") as f:
        json.dump(sample_data, f, indent=2)


@pytest.mark.api
def test_get_fantasy_player_defaults_with_filter(fantasy_api_client):
    """Test fetching fantasy player defaults with X-Fantasy-Filter."""
    
    # Use a filter to limit results
    headers = {
        "X-Fantasy-Filter": '{"players":{"limit":10,"sortDraftRanks":{"sortPriority":100,"sortAsc":true,"value":"STANDARD"}}}'
    }
    
    response = get_fantasy_player_defaults.sync_detailed(
        client=fantasy_api_client,
        year=2025,
        segment=0,
        scoring_period_id=1,
        view=GetFantasyPlayerDefaultsView.KONA_PLAYER_INFO,
        x_fantasy_filter=headers["X-Fantasy-Filter"]
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, FantasyPlayerDefaultsResponse), "Response should parse to FantasyPlayerDefaultsResponse"
    
    # The limit in the filter might not always be respected
    logging.info(f"Fetched {len(result.players)} players with filter (requested 10)")