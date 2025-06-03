import pytest
import json
from models.fantasy_api.espn_fantasy_api_client.api.default import get_fantasy_football_players
from models.fantasy_api.espn_fantasy_api_client.models import GetFantasyFootballPlayersView
from models.fantasy_api.espn_fantasy_api_client.types import UNSET


@pytest.mark.api
@pytest.mark.parametrize("view,filter_json,description", [
    (
        GetFantasyFootballPlayersView.KONA_PLAYER_INFO,
        '{"players":{"limit":10,"sortPercOwned":{"sortPriority":1,"sortAsc":false}}}',
        "Top 10 most owned players"
    ),
    (
        GetFantasyFootballPlayersView.PLAYER_WL,
        '{"players":{"filterIds":{"value":[3139477,2576980]}},"filterActive":{"value":true}}',
        "Specific players by ID with active filter"
    ),
    (
        GetFantasyFootballPlayersView.MDRAFTDETAIL,
        '{"players":{"filterSlotIds":{"value":[0,2,4,6]}},"filterRanksForSlotIds":{"value":[0,2,4,6]}}',
        "Draft details for specific positions"
    ),
    (
        GetFantasyFootballPlayersView.MROSTER,
        '{"players":{"filterProTeamIds":{"value":[12,22]},"limit":20}}',
        "Players from specific teams"
    ),
    (
        GetFantasyFootballPlayersView.MLIVESCORING,
        '{"players":{"limit":50}}',
        "Live scoring view"
    ),
    (
        GetFantasyFootballPlayersView.MMATCHUP,
        '{"players":{"limit":50}}',
        "Matchup view"
    ),
    (
        GetFantasyFootballPlayersView.MTEAM,
        '{"players":{"limit":50}}',
        "Team view"
    ),
    (
        GetFantasyFootballPlayersView.MMATCHUPSCORE,
        '{"players":{"limit":50}}',
        "Matchup score view"
    ),
    (
        GetFantasyFootballPlayersView.MSTANDINGS,
        '{"players":{"limit":50}}',
        "Standings view"
    ),
    (
        GetFantasyFootballPlayersView.MBOXSCORE,
        '{"players":{"limit":50}}',
        "Boxscore view"
    ),
    (
        GetFantasyFootballPlayersView.ALLON,
        '{"players":{"limit":50}}',
        "All-on view"
    )
])
def test_fantasy_players_with_various_filters(fantasy_api_client, view, filter_json, description, ensure_json_output_dir):
    """Test fetching fantasy players with different views and filters."""
    print(f"\n=== Testing: {description} ===")
    print(f"View: {view.value}")
    print(f"Filter: {filter_json}")
    
    # Make the API call
    response = get_fantasy_football_players.sync_detailed(
        client=fantasy_api_client,
        year=2024,
        view=view,
        x_fantasy_filter=filter_json
    )
    
    # Check response status
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Parse the response
    result = response.parsed
    assert isinstance(result, list), "Response should be a list of players"
    
    print(f"Players returned: {len(result)}")
    
    # Log some interesting information
    if result:
        # Count how many players have actual data
        players_with_data = 0
        players_with_ownership = 0
        players_with_stats = 0
        
        for player in result[:10]:  # Check first 10 players
            # Check if player has basic data
            if player.id and player.id is not UNSET:
                players_with_data += 1
                
            if player.ownership and player.ownership is not UNSET:
                players_with_ownership += 1
                
            if player.stats and player.stats is not UNSET and len(player.stats) > 0:
                players_with_stats += 1
        
        print(f"Players with data (first 10): {players_with_data}")
        print(f"Players with ownership info: {players_with_ownership}")
        print(f"Players with stats: {players_with_stats}")
        
        # Show details of first player with data
        for i, player in enumerate(result[:5]):
            if player.id and player.id is not UNSET:
                print(f"\nPlayer {i+1}:")
                print(f"  Name: {player.full_name if player.full_name and player.full_name is not UNSET else 'N/A'}")
                print(f"  ID: {player.id}")
                
                if player.ownership and player.ownership is not UNSET:
                    print(f"  % Owned: {player.ownership.percent_owned:.2%}")
                    print(f"  Avg Draft Pos: {player.ownership.average_draft_position}")
                
                if player.pro_team_id and player.pro_team_id is not UNSET:
                    print(f"  Team ID: {player.pro_team_id}")
                    
                break  # Just show first player with data
    else:
        print("No players returned")


@pytest.mark.api
def test_player_wl_with_scoring_period(fantasy_api_client):
    """Test player_wl view with scoringPeriodId in filter."""
    filter_json = '{"players":{"limit":50,"sortPercOwned":{"sortPriority":1,"sortAsc":false}}}'
    
    print(f"\n=== Testing player_wl with ownership sorting ===")
    
    response = get_fantasy_football_players.sync_detailed(
        client=fantasy_api_client,
        year=2024,
        view=GetFantasyFootballPlayersView.PLAYER_WL,
        x_fantasy_filter=filter_json
    )
    
    assert response.status_code == 200
    result = response.parsed
    
    print(f"Total players: {len(result)}")
    
    # Check if we get empty objects or actual data
    if result:
        first_player = result[0]
        if hasattr(first_player, 'additional_properties') and not first_player.additional_properties:
            print("Note: player_wl view returns empty objects even with filters.")
            print("This view may require specific league context or additional parameters.")
        elif first_player.id and first_player.id is not UNSET:
            print(f"First player: {first_player.full_name if first_player.full_name else 'Unknown'}")


@pytest.mark.api
def test_advanced_draft_filter(fantasy_api_client, ensure_json_output_dir):
    """Test with advanced draft filtering."""
    # Complex filter for draft analysis
    filter_json = json.dumps({
        "players": {
            "limit": 100,
            "sortDraftRanks": {
                "sortPriority": 100,
                "sortAsc": True,
                "value": "STANDARD"
            },
            "filterRanksForScoringPeriodIds": {
                "value": [1]
            },
            "filterRanksForRankTypes": {
                "value": ["STANDARD"]
            },
            "filterRanksForSlotIds": {
                "value": [0, 2, 4, 6]  # QB, RB, WR, TE
            }
        }
    })
    
    print(f"\n=== Testing advanced draft filtering ===")
    
    response = get_fantasy_football_players.sync_detailed(
        client=fantasy_api_client,
        year=2024,
        view=GetFantasyFootballPlayersView.KONA_PLAYER_INFO,
        x_fantasy_filter=filter_json
    )
    
    assert response.status_code == 200
    result = response.parsed
    
    print(f"Players returned: {len(result)}")
    
    if result:
        # Collect draft rank information
        draft_data = []
        for player in result[:20]:  # Top 20 by draft rank
            if player.draft_ranks_by_rank_type and player.draft_ranks_by_rank_type is not UNSET:
                standard_rank = None
                for rank_type, rank_info in player.draft_ranks_by_rank_type.additional_properties.items():
                    if rank_type == "STANDARD":
                        standard_rank = rank_info.rank
                        break
                
                if standard_rank and player.full_name and player.full_name is not UNSET:
                    draft_data.append({
                        'name': player.full_name,
                        'position': player.default_position_id,
                        'rank': standard_rank,
                        'team': player.pro_team_id
                    })
        
        # Save draft rankings
        with open(f"{ensure_json_output_dir}/fantasy_draft_rankings_sample.json", "w") as f:
            json.dump(draft_data[:10], f, indent=2)
        
        print(f"Saved top 10 draft rankings to file")
        for i, player_info in enumerate(draft_data[:5]):
            print(f"{i+1}. {player_info['name']} (Pos: {player_info['position']}, Rank: {player_info['rank']})")


@pytest.mark.api
def test_all_fantasy_views(fantasy_api_client, ensure_json_output_dir):
    """Test all available fantasy views and document their behavior."""
    all_views = [
        GetFantasyFootballPlayersView.KONA_PLAYER_INFO,
        GetFantasyFootballPlayersView.MDRAFTDETAIL,
        GetFantasyFootballPlayersView.MLIVESCORING,
        GetFantasyFootballPlayersView.MMATCHUP,
        GetFantasyFootballPlayersView.MTEAM,
        GetFantasyFootballPlayersView.MMATCHUPSCORE,
        GetFantasyFootballPlayersView.MSTANDINGS,
        GetFantasyFootballPlayersView.MROSTER,
        GetFantasyFootballPlayersView.MBOXSCORE,
        GetFantasyFootballPlayersView.PLAYER_WL,
        GetFantasyFootballPlayersView.ALLON
    ]
    
    view_results = {}
    
    for view in all_views:
        print(f"\n=== Testing view: {view.value} ===")
        
        # Test without filter first
        response = get_fantasy_football_players.sync_detailed(
            client=fantasy_api_client,
            year=2024,
            view=view
        )
        
        assert response.status_code == 200, f"Failed for view {view.value}: {response.status_code}"
        result = response.parsed
        
        # Test with basic filter
        filter_response = get_fantasy_football_players.sync_detailed(
            client=fantasy_api_client,
            year=2024,
            view=view,
            x_fantasy_filter='{"players":{"limit":100}}'
        )
        
        assert filter_response.status_code == 200
        filter_result = filter_response.parsed
        
        # Analyze results
        has_data = False
        sample_player = None
        
        if result and len(result) > 0:
            first = result[0]
            if hasattr(first, 'id') and first.id and first.id is not UNSET:
                has_data = True
                sample_player = {
                    'id': first.id if first.id is not UNSET else None,
                    'name': first.full_name if first.full_name and first.full_name is not UNSET else None,
                    'position': first.default_position_id if hasattr(first, 'default_position_id') and first.default_position_id is not UNSET else None
                }
        
        view_info = {
            'view': view.value,
            'has_data_without_filter': has_data,
            'count_without_filter': len(result) if result else 0,
            'count_with_filter': len(filter_result) if filter_result else 0,
            'sample_player': sample_player
        }
        
        view_results[view.value] = view_info
        
        print(f"  Without filter: {view_info['count_without_filter']} players, has_data={has_data}")
        print(f"  With filter: {view_info['count_with_filter']} players")
        if sample_player:
            print(f"  Sample: {sample_player['name']} (ID: {sample_player['id']})")
    
    # Save summary
    with open(f"{ensure_json_output_dir}/fantasy_views_summary.json", "w") as f:
        json.dump(view_results, f, indent=2)
    
    print("\n=== Summary ===")
    print("Views with data:")
    for view_name, info in view_results.items():
        if info['has_data_without_filter']:
            print(f"  - {view_name}: {info['count_without_filter']} players")
    
    print("\nViews requiring filters/context:")
    for view_name, info in view_results.items():
        if not info['has_data_without_filter']:
            print(f"  - {view_name}")