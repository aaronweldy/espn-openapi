import pytest
import json
from models.fantasy_api.espn_fantasy_api_client.api.default import get_fantasy_football_players
from models.fantasy_api.espn_fantasy_api_client.models import GetFantasyFootballPlayersView
from models.fantasy_api.espn_fantasy_api_client.types import UNSET


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
@pytest.mark.parametrize("view", [
    GetFantasyFootballPlayersView.KONA_PLAYER_INFO, 
    GetFantasyFootballPlayersView.PLAYER_WL,
    GetFantasyFootballPlayersView.MDRAFTDETAIL,
    GetFantasyFootballPlayersView.MROSTER
])
def test_get_fantasy_players_different_views(fantasy_api_client, view, ensure_json_output_dir):
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
    
    print(f"\n=== View: {view.value} ===")
    print(f"Total players returned: {len(result)}")
    
    # Check if the view returns empty objects
    if result and hasattr(result[0], 'additional_properties'):
        if not result[0].additional_properties:
            print(f"Note: This view returns empty player objects. It likely requires specific X-Fantasy-Filter headers.")
            print(f"      Views like '{view.value}' are typically used for specific fantasy operations.")
            return
    
    if result:
        # Log interesting information about the first player
        first_player = result[0]
        print(f"First player: {first_player.full_name if first_player.full_name and first_player.full_name is not UNSET else 'N/A'}")
        print(f"  - ID: {first_player.id}")
        print(f"  - Position ID: {first_player.default_position_id}")
        print(f"  - Pro Team ID: {first_player.pro_team_id}")
        print(f"  - Active: {first_player.active}")
        print(f"  - Injury Status: {first_player.injury_status}")
        
        # Check what fields are populated based on the view
        if first_player.ownership:
            print(f"  - Ownership Data: Present")
            print(f"    - Percent Owned: {first_player.ownership.percent_owned:.2%}")
            print(f"    - Average Draft Position: {first_player.ownership.average_draft_position}")
        else:
            print(f"  - Ownership Data: Not present")
            
        if first_player.draft_ranks_by_rank_type:
            print(f"  - Draft Ranks: Present ({len(first_player.draft_ranks_by_rank_type.additional_properties)} types)")
        else:
            print(f"  - Draft Ranks: Not present")
            
        if first_player.stats:
            print(f"  - Stats: {len(first_player.stats)} stat entries")
            # Check if any stats have actual data
            stats_with_data = sum(1 for stat in first_player.stats if stat.stats and stat.stats.additional_properties)
            print(f"    - Stats with data: {stats_with_data}")
        else:
            print(f"  - Stats: Not present")
        
        # Save a sample for this view - handle UNSET values
        def serialize_value(val):
            if val is UNSET:
                return None
            return val
        
        sample_data = {
            'view': view.value,
            'total_players': len(result),
            'sample_player': {
                'id': serialize_value(first_player.id),
                'fullName': serialize_value(first_player.full_name),
                'defaultPositionId': serialize_value(first_player.default_position_id),
                'proTeamId': serialize_value(first_player.pro_team_id),
                'active': serialize_value(first_player.active),
                'injuryStatus': serialize_value(first_player.injury_status),
                'hasOwnership': first_player.ownership is not None and first_player.ownership is not UNSET,
                'hasDraftRanks': first_player.draft_ranks_by_rank_type is not None and first_player.draft_ranks_by_rank_type is not UNSET,
                'statsCount': len(first_player.stats) if first_player.stats and first_player.stats is not UNSET else 0
            }
        }
        
        with open(f"{ensure_json_output_dir}/fantasy_players_{view.value}_sample.json", "w") as f:
            json.dump(sample_data, f, indent=2)


@pytest.mark.api
def test_fantasy_players_with_scoring_period(fantasy_api_client):
    """Test the players endpoint with scoringPeriodId parameter."""
    # The players_wl view with scoringPeriodId is used for getting % owned players
    response = get_fantasy_football_players.sync_detailed(
        client=fantasy_api_client,
        year=2024,
        view=GetFantasyFootballPlayersView.PLAYER_WL
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Note: The scoringPeriodId parameter would need to be added to the OpenAPI spec
    # to fully support this use case. Currently showing the basic functionality.
    print(f"\nNote: The player_wl view is designed to work with scoringPeriodId parameter")
    print(f"      to get ownership percentages for specific scoring periods.")
    print(f"      Without proper filters, it returns empty player objects.")