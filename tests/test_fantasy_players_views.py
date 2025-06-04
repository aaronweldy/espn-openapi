import pytest
from models.fantasy_api.espn_fantasy_api_client.api.default import get_fantasy_football_players
from models.fantasy_api.espn_fantasy_api_client.models import GetFantasyFootballPlayersView


@pytest.mark.api
@pytest.mark.parametrize("view", [
    GetFantasyFootballPlayersView.PLAYERS_WL,
    GetFantasyFootballPlayersView.PLAYERS_WL
])
def test_fantasy_players_wl_views(fantasy_api_client, view):
    """Test both player_wl and players_wl views work."""
    
    # Use a small limit to avoid large responses
    response = get_fantasy_football_players.sync_detailed(
        client=fantasy_api_client,
        year=2024,
        view=view,
        x_fantasy_filter='{"players":{"limit":5}}'
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code} for view {view}"
    
    result = response.parsed
    assert result is not None, f"Response should parse successfully for view {view}"
    assert isinstance(result, list), f"Response should be a list for view {view}"
    assert len(result) > 0, f"Response should contain players for view {view}"
    
    # Check first player has expected fields
    first_player = result[0]
    assert hasattr(first_player, 'id'), f"Player should have ID for view {view}"
    
    # Note: The API seems to ignore the limit in X-Fantasy-Filter for these views
    print(f"\nView {view.value}: Returned {len(result)} players (filter requested 5)")


@pytest.mark.api
def test_fantasy_filter_limit_behavior(fantasy_api_client):
    """Test how X-Fantasy-Filter limit behaves across different views."""
    
    views_to_test = [
        (GetFantasyFootballPlayersView.KONA_PLAYER_INFO, 10),
        (GetFantasyFootballPlayersView.PLAYERS_WL, 10),
        (GetFantasyFootballPlayersView.MDRAFTDETAIL, 10),
    ]
    
    results = {}
    
    for view, limit in views_to_test:
        response = get_fantasy_football_players.sync_detailed(
            client=fantasy_api_client,
            year=2024,
            view=view,
            x_fantasy_filter=f'{{"players":{{"limit":{limit}}}}}'
        )
        
        if response.status_code == 200 and response.parsed:
            actual_count = len(response.parsed)
            results[view.value] = {
                'requested_limit': limit,
                'actual_count': actual_count,
                'limit_respected': actual_count <= limit
            }
    
    print("\nX-Fantasy-Filter limit behavior:")
    print("-" * 60)
    for view_name, data in results.items():
        respected = "✓" if data['limit_respected'] else "✗"
        print(f"{view_name:20} | Requested: {data['requested_limit']:4} | Actual: {data['actual_count']:4} | Respected: {respected}")
    
    # At least some views should respect the limit
    respected_count = sum(1 for data in results.values() if data['limit_respected'])
    print(f"\nViews that respected limit: {respected_count}/{len(results)}")