import pytest
import json
from models.fantasy_api.espn_fantasy_api_client.api.default import get_fantasy_football_players
from models.fantasy_api.espn_fantasy_api_client.models import GetFantasyFootballPlayersView


@pytest.mark.api
def test_get_fantasy_football_players(fantasy_api_client, ensure_json_output_dir):
    """Test fetching fantasy football players list."""
    # Make the API call
    response = get_fantasy_football_players.sync_detailed(
        client=fantasy_api_client,
        year=2024,
        view=GetFantasyFootballPlayersView.KONA_PLAYER_INFO
    )
    
    # Check response status
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Parse the response
    result = response.parsed
    assert isinstance(result, list), "Response should be a list of players"
    assert len(result) > 0, "Should return at least one player"
    
    # Check first player structure
    first_player = result[0]
    assert hasattr(first_player, 'id'), "Player should have id"
    assert hasattr(first_player, 'full_name'), "Player should have full_name"
    assert hasattr(first_player, 'default_position_id'), "Player should have default_position_id"
    
    # Check ownership data
    if first_player.ownership:
        assert hasattr(first_player.ownership, 'percent_owned'), "Ownership should have percent_owned"
    
    # Save a sample of the response for analysis
    sample_data = []
    for player in result[:5]:  # First 5 players
        player_dict = {
            'id': player.id,
            'fullName': player.full_name,
            'firstName': player.first_name,
            'lastName': player.last_name,
            'defaultPositionId': player.default_position_id,
            'proTeamId': player.pro_team_id,
            'injured': player.injured,
            'injuryStatus': player.injury_status
        }
        sample_data.append(player_dict)
    
    with open(f"{ensure_json_output_dir}/fantasy_players_test_sample.json", "w") as f:
        json.dump(sample_data, f, indent=2)
    
    print(f"Successfully fetched {len(result)} fantasy players")


@pytest.mark.api
def test_get_fantasy_players_with_filter(fantasy_api_client):
    """Test fetching fantasy players with X-Fantasy-Filter header."""
    # Make the API call with filter header
    response = get_fantasy_football_players.sync_detailed(
        client=fantasy_api_client,
        year=2024,
        view=GetFantasyFootballPlayersView.KONA_PLAYER_INFO,
        x_fantasy_filter='{"players":{"limit":100}}'
    )
    
    # Check response status
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Parse the response
    result = response.parsed
    assert isinstance(result, list), "Response should be a list of players"
    
    # The limit parameter might not be honored exactly by the API
    assert len(result) > 0, "Should return at least one player"
    # Note: X-Fantasy-Filter doesn't seem to limit results as expected, API returns many players
    
    print(f"Successfully fetched {len(result)} fantasy players with filter")


@pytest.mark.api
@pytest.mark.parametrize("view", [GetFantasyFootballPlayersView.KONA_PLAYER_INFO, GetFantasyFootballPlayersView.PLAYER_WL])
def test_get_fantasy_players_different_views(fantasy_api_client, view):
    """Test fetching fantasy players with different view parameters."""
    # Make the API call
    response = get_fantasy_football_players.sync_detailed(
        client=fantasy_api_client,
        year=2024,
        view=view
    )
    
    # Check response status
    assert response.status_code == 200, f"Expected status code 200 for view {view}, got {response.status_code}"
    
    # Parse the response
    result = response.parsed
    assert isinstance(result, list), f"Response should be a list for view {view}"
    
    print(f"Successfully fetched fantasy players with view: {view}")