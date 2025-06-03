import pytest
import json
import logging
from models.fantasy_api.espn_fantasy_api_client.api.default import get_fantasy_football_players
from models.fantasy_api.espn_fantasy_api_client.models import GetFantasyFootballPlayersView
from models.fantasy_api.espn_fantasy_api_client.types import UNSET

# Set up logger
logger = logging.getLogger(__name__)


def analyze_player_structure(player, view_name):
    """Analyze the structure and data available in a player object."""
    analysis = {
        'view': view_name,
        'has_basic_info': False,
        'has_stats': False,
        'has_ownership': False,
        'has_draft_ranks': False,
        'has_injury_info': False,
        'fields_present': [],
        'stats_info': None,
        'ownership_info': None,
        'draft_info': None
    }
    
    # Check basic info
    if hasattr(player, 'id') and player.id and player.id is not UNSET:
        analysis['has_basic_info'] = True
        analysis['fields_present'].append('id')
    
    if hasattr(player, 'full_name') and player.full_name and player.full_name is not UNSET:
        analysis['fields_present'].append('full_name')
    
    if hasattr(player, 'first_name') and player.first_name and player.first_name is not UNSET:
        analysis['fields_present'].append('first_name')
        
    if hasattr(player, 'last_name') and player.last_name and player.last_name is not UNSET:
        analysis['fields_present'].append('last_name')
    
    if hasattr(player, 'default_position_id') and player.default_position_id is not UNSET:
        analysis['fields_present'].append('default_position_id')
    
    if hasattr(player, 'pro_team_id') and player.pro_team_id is not UNSET:
        analysis['fields_present'].append('pro_team_id')
    
    if hasattr(player, 'jersey') and player.jersey and player.jersey is not UNSET:
        analysis['fields_present'].append('jersey')
    
    if hasattr(player, 'active') and player.active is not UNSET:
        analysis['fields_present'].append('active')
    
    if hasattr(player, 'eligible_slots') and player.eligible_slots and player.eligible_slots is not UNSET:
        analysis['fields_present'].append('eligible_slots')
    
    # Check injury info
    if hasattr(player, 'injured') and player.injured is not UNSET:
        analysis['has_injury_info'] = True
        analysis['fields_present'].append('injured')
    
    if hasattr(player, 'injury_status') and player.injury_status and player.injury_status is not UNSET:
        analysis['fields_present'].append('injury_status')
    
    # Check stats
    if hasattr(player, 'stats') and player.stats and player.stats is not UNSET:
        analysis['has_stats'] = True
        analysis['fields_present'].append('stats')
        
        # Analyze stats structure
        stats_summary = {
            'total_stat_entries': len(player.stats),
            'stat_types': set(),
            'seasons_covered': set(),
            'has_projections': False,
            'has_actual_stats': False
        }
        
        for stat in player.stats[:5]:  # Look at first 5 stat entries
            if hasattr(stat, 'stat_source_id') and stat.stat_source_id is not UNSET:
                if stat.stat_source_id == 1:
                    stats_summary['has_projections'] = True
                elif stat.stat_source_id == 0:
                    stats_summary['has_actual_stats'] = True
            
            if hasattr(stat, 'season_id') and stat.season_id is not UNSET:
                stats_summary['seasons_covered'].add(stat.season_id)
            
            if hasattr(stat, 'stat_split_type_id') and stat.stat_split_type_id is not UNSET:
                stats_summary['stat_types'].add(stat.stat_split_type_id)
        
        stats_summary['seasons_covered'] = list(stats_summary['seasons_covered'])
        stats_summary['stat_types'] = list(stats_summary['stat_types'])
        analysis['stats_info'] = stats_summary
    
    # Check ownership
    if hasattr(player, 'ownership') and player.ownership and player.ownership is not UNSET:
        analysis['has_ownership'] = True
        analysis['fields_present'].append('ownership')
        
        ownership_info = {}
        if hasattr(player.ownership, 'percent_owned') and player.ownership.percent_owned is not UNSET:
            ownership_info['percent_owned'] = player.ownership.percent_owned
        
        if hasattr(player.ownership, 'percent_started') and player.ownership.percent_started is not UNSET:
            ownership_info['percent_started'] = player.ownership.percent_started
        
        if hasattr(player.ownership, 'average_draft_position') and player.ownership.average_draft_position is not UNSET:
            ownership_info['average_draft_position'] = player.ownership.average_draft_position
        
        if hasattr(player.ownership, 'percent_change') and player.ownership.percent_change is not UNSET:
            ownership_info['percent_change'] = player.ownership.percent_change
        
        analysis['ownership_info'] = ownership_info
    
    # Check draft ranks
    if hasattr(player, 'draft_ranks_by_rank_type') and player.draft_ranks_by_rank_type and player.draft_ranks_by_rank_type is not UNSET:
        analysis['has_draft_ranks'] = True
        analysis['fields_present'].append('draft_ranks_by_rank_type')
        
        draft_info = {
            'rank_types': list(player.draft_ranks_by_rank_type.additional_properties.keys()),
            'ranks': {}
        }
        
        for rank_type, rank_data in player.draft_ranks_by_rank_type.additional_properties.items():
            if hasattr(rank_data, 'rank') and rank_data.rank is not UNSET:
                draft_info['ranks'][rank_type] = {
                    'rank': rank_data.rank,
                    'auction_value': rank_data.auction_value if hasattr(rank_data, 'auction_value') and rank_data.auction_value is not UNSET else None
                }
        
        analysis['draft_info'] = draft_info
    
    # Check for additional properties that might be view-specific
    if hasattr(player, 'additional_properties'):
        for key in player.additional_properties:
            analysis['fields_present'].append(f'additional:{key}')
    
    return analysis


@pytest.mark.api
def test_fantasy_views_detailed_analysis(fantasy_api_client, ensure_json_output_dir):
    """Perform detailed analysis of each fantasy view to understand their purpose."""
    
    views_to_test = [
        (GetFantasyFootballPlayersView.KONA_PLAYER_INFO, '{"players":{"limit":5,"sortPercOwned":{"sortPriority":1,"sortAsc":false}}}'),
        (GetFantasyFootballPlayersView.MROSTER, '{"players":{"limit":5}}'),
        (GetFantasyFootballPlayersView.MLIVESCORING, '{"players":{"limit":5}}'),
        (GetFantasyFootballPlayersView.MMATCHUP, '{"players":{"limit":5}}'),
        (GetFantasyFootballPlayersView.MBOXSCORE, '{"players":{"limit":5}}'),
        (GetFantasyFootballPlayersView.ALLON, '{"players":{"limit":5}}'),
        # Views that typically need more context
        (GetFantasyFootballPlayersView.MDRAFTDETAIL, '{"players":{"limit":5,"filterSlotIds":{"value":[0,2,4,6]}}}'),
        (GetFantasyFootballPlayersView.MTEAM, '{"players":{"limit":5,"filterActive":{"value":true}}}'),
        (GetFantasyFootballPlayersView.MMATCHUPSCORE, '{"players":{"limit":5,"filterActive":{"value":true}}}'),
        (GetFantasyFootballPlayersView.MSTANDINGS, '{"players":{"limit":5,"filterActive":{"value":true}}}'),
        (GetFantasyFootballPlayersView.PLAYER_WL, '{"players":{"limit":5,"filterIds":{"value":[3139477,2576980]}}}')
    ]
    
    detailed_results = {}
    
    for view, filter_json in views_to_test:
        logger.info("=" * 60)
        logger.info(f"Analyzing view: {view.value}")
        logger.info("=" * 60)
        
        # Fetch data with filter
        response = get_fantasy_football_players.sync_detailed(
            client=fantasy_api_client,
            year=2024,
            view=view,
            x_fantasy_filter=filter_json
        )
        
        assert response.status_code == 200
        result = response.parsed
        
        view_analysis = {
            'view_name': view.value,
            'total_players': len(result) if result and isinstance(result, list) else 0,
            'players_with_data': 0,
            'empty_objects': 0,
            'common_fields': set(),
            'unique_features': [],
            'sample_analyses': []
        }
        
        if result and isinstance(result, list) and len(result) > 0:
            # Analyze up to 3 players
            for i, player in enumerate(result[:3]):
                # Check if it's an empty object
                if hasattr(player, 'additional_properties') and not player.additional_properties and not (hasattr(player, 'id') and player.id and player.id is not UNSET):
                    view_analysis['empty_objects'] += 1
                    continue
                
                view_analysis['players_with_data'] += 1
                player_analysis = analyze_player_structure(player, view.value)
                view_analysis['sample_analyses'].append(player_analysis)
                
                # Track common fields
                if i == 0:
                    view_analysis['common_fields'] = set(player_analysis['fields_present'])
                else:
                    view_analysis['common_fields'] &= set(player_analysis['fields_present'])
                
                # Print player summary
                logger.info(f"Player {i+1}:")
                if player.full_name and player.full_name is not UNSET:
                    logger.info(f"  Name: {player.full_name}")
                if player.id and player.id is not UNSET:
                    logger.info(f"  ID: {player.id}")
                logger.info(f"  Fields present: {', '.join(player_analysis['fields_present'][:10])}")
                if len(player_analysis['fields_present']) > 10:
                    logger.info(f"    ... and {len(player_analysis['fields_present']) - 10} more fields")
                
                if player_analysis['has_stats']:
                    logger.info(f"  Stats: {player_analysis['stats_info']['total_stat_entries']} entries")
                    logger.info(f"    - Has projections: {player_analysis['stats_info']['has_projections']}")
                    logger.info(f"    - Has actual stats: {player_analysis['stats_info']['has_actual_stats']}")
                
                if player_analysis['has_ownership']:
                    logger.info(f"  Ownership: {player_analysis['ownership_info']}")
                
                if player_analysis['has_draft_ranks']:
                    logger.info(f"  Draft ranks: {player_analysis['draft_info']['rank_types']}")
        
        # Convert sets to lists for JSON serialization
        view_analysis['common_fields'] = list(view_analysis['common_fields'])
        
        # Determine unique features of this view
        if view_analysis['players_with_data'] > 0:
            first_analysis = view_analysis['sample_analyses'][0]
            
            # Identify what makes this view unique
            if view.value == 'kona_player_info':
                view_analysis['unique_features'] = ['General player information with ownership and draft data']
            elif view.value == 'mRoster':
                view_analysis['unique_features'] = ['Full roster information with all player details']
            elif view.value == 'mLiveScoring':
                view_analysis['unique_features'] = ['Live scoring focus, may include real-time stats']
            elif view.value == 'mMatchup':
                view_analysis['unique_features'] = ['Matchup-specific information']
            elif view.value == 'mBoxscore':
                view_analysis['unique_features'] = ['Detailed boxscore statistics']
            elif view.value == 'allon':
                view_analysis['unique_features'] = ['Comprehensive view with all available data']
        
        detailed_results[view.value] = view_analysis
        
        # Print summary
        logger.info(f"Summary for {view.value}:")
        logger.info(f"  Players with data: {view_analysis['players_with_data']}")
        logger.info(f"  Empty objects: {view_analysis['empty_objects']}")
        logger.info(f"  Common fields: {', '.join(view_analysis['common_fields'][:5])}")
        if len(view_analysis['common_fields']) > 5:
            logger.info(f"    ... and {len(view_analysis['common_fields']) - 5} more")
        logger.info(f"  Unique features: {', '.join(view_analysis['unique_features'])}")
    
    # Save detailed analysis
    with open(f"{ensure_json_output_dir}/fantasy_views_detailed_analysis.json", "w") as f:
        # Convert to JSON-serializable format
        json_safe_results = {}
        for view_name, analysis in detailed_results.items():
            json_safe_results[view_name] = {
                'view_name': analysis['view_name'],
                'total_players': analysis['total_players'],
                'players_with_data': analysis['players_with_data'],
                'empty_objects': analysis['empty_objects'],
                'common_fields': analysis['common_fields'],
                'unique_features': analysis['unique_features'],
                'sample_count': len(analysis['sample_analyses'])
            }
        json.dump(json_safe_results, f, indent=2)
    
    # Print final comparison
    logger.info("=" * 60)
    logger.info("FINAL VIEW COMPARISON")
    logger.info("=" * 60)
    
    for view_name, analysis in detailed_results.items():
        if analysis['players_with_data'] > 0:
            logger.info(f"{view_name}:")
            logger.info(f"  Purpose: {', '.join(analysis['unique_features']) if analysis['unique_features'] else 'Unknown'}")
            logger.info(f"  Data availability: {analysis['players_with_data']}/{analysis['total_players']} players have data")
            
            # Check what key data is available
            if analysis['sample_analyses']:
                first = analysis['sample_analyses'][0]
                data_types = []
                if first['has_stats']:
                    data_types.append('statistics')
                if first['has_ownership']:
                    data_types.append('ownership')
                if first['has_draft_ranks']:
                    data_types.append('draft rankings')
                if first['has_injury_info']:
                    data_types.append('injury status')
                logger.info(f"  Key data: {', '.join(data_types)}")


@pytest.mark.api
def test_fantasy_draft_rankings_view(fantasy_api_client, ensure_json_output_dir):
    """Test specific draft rankings view with detailed analysis."""
    
    # Test mDraftDetail view with specific filter for QB/RB/WR/TE positions
    response = get_fantasy_football_players.sync_detailed(
        client=fantasy_api_client,
        year=2024,
        view=GetFantasyFootballPlayersView.MDRAFTDETAIL,
        x_fantasy_filter='{"players":{"limit":50,"sortDraftRanks":{"sortPriority":1,"sortAsc":true},"filterSlotIds":{"value":[0,2,4,6]}}}'
    )
    
    assert response.status_code == 200
    result = response.parsed
    assert result and isinstance(result, list) and len(result) > 0
    
    # Analyze draft rankings data
    draft_analysis = {
        'total_players': len(result),
        'players_with_ranks': 0,
        'rank_types_found': set(),
        'position_distribution': {},
        'top_10_players': []
    }
    
    for i, player in enumerate(result[:10]):
        if not player.id or player.id is UNSET:
            continue
            
        # Debug: Print what fields are available
        if i == 0:
            logger.info("Debug - First player fields:")
            for attr in dir(player):
                if not attr.startswith('_') and hasattr(player, attr):
                    value = getattr(player, attr)
                    if value and value is not UNSET and not callable(value):
                        logger.info(f"  {attr}: {type(value).__name__}")
                        if attr == 'draft_ranks_by_rank_type':
                            logger.info(f"    Value: {value}")
            
        player_info = {
            'name': player.full_name if player.full_name else 'Unknown',
            'id': player.id,
            'position': None,
            'team': None,
            'ranks': {}
        }
        
        # Get position
        if player.default_position_id and player.default_position_id is not UNSET:
            position_map = {1: 'QB', 2: 'RB', 3: 'WR', 4: 'TE', 5: 'K', 16: 'D/ST'}
            player_info['position'] = position_map.get(player.default_position_id, f'POS_{player.default_position_id}')
            
            # Track position distribution
            if player_info['position'] not in draft_analysis['position_distribution']:
                draft_analysis['position_distribution'][player_info['position']] = 0
            draft_analysis['position_distribution'][player_info['position']] += 1
        
        # Get team
        if player.pro_team_id and player.pro_team_id is not UNSET:
            player_info['team'] = player.pro_team_id
        
        # Get draft ranks
        if player.draft_ranks_by_rank_type:
            draft_analysis['players_with_ranks'] += 1
            
            for rank_type, rank_data in player.draft_ranks_by_rank_type.additional_properties.items():
                draft_analysis['rank_types_found'].add(rank_type)
                
                if rank_data.rank and rank_data.rank is not UNSET:
                    player_info['ranks'][rank_type] = {
                        'rank': rank_data.rank,
                        'auction_value': rank_data.auction_value if rank_data.auction_value else None
                    }
        
        draft_analysis['top_10_players'].append(player_info)
    
    # Convert set to list for JSON
    draft_analysis['rank_types_found'] = list(draft_analysis['rank_types_found'])
    
    # Save draft rankings analysis
    with open(f"{ensure_json_output_dir}/fantasy_draft_rankings_sample.json", "w") as f:
        json.dump(draft_analysis, f, indent=2)
    
    # Print analysis
    logger.info(f"Draft Rankings Analysis (mDraftDetail view):")
    logger.info(f"Total players: {draft_analysis['total_players']}")
    logger.info(f"Players with rankings: {draft_analysis['players_with_ranks']}")
    logger.info(f"Rank types found: {', '.join(draft_analysis['rank_types_found'])}")
    logger.info(f"Position distribution: {draft_analysis['position_distribution']}")
    
    logger.info("Top 10 Players by Draft Rank:")
    for i, player in enumerate(draft_analysis['top_10_players'], 1):
        logger.info(f"{i}. {player['name']} ({player['position']}) - Team {player['team']}")
        for rank_type, rank_info in player['ranks'].items():
            logger.info(f"   {rank_type}: Rank {rank_info['rank']}, Value ${rank_info['auction_value']}")
    
    # Verify we got players even if no draft rankings
    assert draft_analysis['total_players'] > 0, "Should have received players"
    
    # Note if we didn't get draft rankings
    if draft_analysis['players_with_ranks'] == 0:
        logger.info("Note: No draft rankings found in response. This view may require specific conditions or league context.")
    else:
        assert len(draft_analysis['rank_types_found']) > 0, "Should have found rank types"
        
    # Check position distribution if we have any
    if draft_analysis['position_distribution']:
        logger.info(f"Positions found: {list(draft_analysis['position_distribution'].keys())}")
    else:
        logger.info("No position data found in players")