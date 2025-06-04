import pytest
import json
from models.fantasy_api.espn_fantasy_api_client.api.default import get_fantasy_football_players
from models.fantasy_api.espn_fantasy_api_client.models import GetFantasyFootballPlayersView


def analyze_view_characteristics(players):
    """Analyze characteristics of a view based on player data."""
    if not players:
        return {
            'has_data': False,
            'player_count': 0
        }
    
    # Sample first few players with data
    sample_players = []
    for p in players[:10]:
        if hasattr(p, 'id') and p.id:
            sample_players.append(p)
            if len(sample_players) >= 3:
                break
    
    if not sample_players:
        return {
            'has_data': False,
            'player_count': len(players),
            'all_empty': True
        }
    
    # Analyze fields present
    fields_analysis = {
        'basic_info': False,
        'stats': False,
        'ownership': False,
        'draft_ranks': False,
        'injury_info': False,
        'position_info': False,
        'team_info': False,
        'additional_fields': set()
    }
    
    # Check common fields across sample
    for player in sample_players:
        if hasattr(player, 'full_name') and player.full_name:
            fields_analysis['basic_info'] = True
        
        if hasattr(player, 'stats') and player.stats:
            fields_analysis['stats'] = True
            
        if hasattr(player, 'ownership') and player.ownership:
            fields_analysis['ownership'] = True
            
        if hasattr(player, 'draft_ranks_by_rank_type') and player.draft_ranks_by_rank_type:
            fields_analysis['draft_ranks'] = True
            
        if hasattr(player, 'injured') or hasattr(player, 'injury_status'):
            fields_analysis['injury_info'] = True
            
        if hasattr(player, 'default_position_id') and player.default_position_id:
            fields_analysis['position_info'] = True
            
        if hasattr(player, 'pro_team_id') and player.pro_team_id:
            fields_analysis['team_info'] = True
            
        # Check for additional properties
        if hasattr(player, 'additional_properties'):
            fields_analysis['additional_fields'].update(player.additional_properties.keys())
    
    # Convert set to list for JSON serialization
    fields_analysis['additional_fields'] = list(fields_analysis['additional_fields'])
    
    return {
        'has_data': True,
        'player_count': len(players),
        'sample_size': len(sample_players),
        'fields': fields_analysis
    }


@pytest.mark.api
def test_fantasy_views_characteristics_analysis(fantasy_api_client, ensure_json_output_dir):
    """Analyze and document the characteristics of each fantasy view."""
    
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
        GetFantasyFootballPlayersView.PLAYERS_WL,
        GetFantasyFootballPlayersView.PLAYERS_WL,
        GetFantasyFootballPlayersView.ALLON
    ]
    
    view_characteristics = {}
    
    for view in all_views:
        print(f"\n{'='*60}")
        print(f"Testing view: {view.value}")
        print(f"{'='*60}")
        
        # Test with a filter to get manageable data
        response = get_fantasy_football_players.sync_detailed(
            client=fantasy_api_client,
            year=2024,
            view=view,
            x_fantasy_filter='{"players":{"limit":10,"filterActive":{"value":true}}}'
        )
        
        if response.status_code != 200:
            print(f"Failed to fetch data: {response.status_code}")
            view_characteristics[view.value] = {'error': f'HTTP {response.status_code}'}
            continue
        
        players = response.parsed
        analysis = analyze_view_characteristics(players)
        
        # Add view-specific interpretations
        if view == GetFantasyFootballPlayersView.KONA_PLAYER_INFO:
            analysis['description'] = "General player information with ownership and draft data"
            analysis['use_case'] = "Player research, draft preparation, waiver wire decisions"
            
        elif view == GetFantasyFootballPlayersView.MDRAFTDETAIL:
            analysis['description'] = "Draft-specific player details"
            analysis['use_case'] = "Draft preparation, ADP analysis"
            
        elif view == GetFantasyFootballPlayersView.MLIVESCORING:
            analysis['description'] = "Live scoring and real-time stats"
            analysis['use_case'] = "In-game tracking, live fantasy scoring"
            
        elif view == GetFantasyFootballPlayersView.MMATCHUP:
            analysis['description'] = "Matchup-specific player information"
            analysis['use_case'] = "Head-to-head matchup analysis"
            
        elif view == GetFantasyFootballPlayersView.MTEAM:
            analysis['description'] = "Team-oriented player data"
            analysis['use_case'] = "Team roster management"
            
        elif view == GetFantasyFootballPlayersView.MMATCHUPSCORE:
            analysis['description'] = "Matchup scoring details"
            analysis['use_case'] = "Scoring breakdown for matchups"
            
        elif view == GetFantasyFootballPlayersView.MSTANDINGS:
            analysis['description'] = "Standings-related player data"
            analysis['use_case'] = "League standings context"
            
        elif view == GetFantasyFootballPlayersView.MROSTER:
            analysis['description'] = "Complete roster information"
            analysis['use_case'] = "Full roster management, lineup decisions"
            
        elif view == GetFantasyFootballPlayersView.MBOXSCORE:
            analysis['description'] = "Detailed statistical boxscore"
            analysis['use_case'] = "Post-game analysis, statistical breakdown"
            
        elif view in [GetFantasyFootballPlayersView.PLAYERS_WL, GetFantasyFootballPlayersView.PLAYERS_WL]:
            analysis['description'] = "Waiver wire and free agent focused data"
            analysis['use_case'] = "Waiver wire decisions, free agent pickups"
            
        elif view == GetFantasyFootballPlayersView.ALLON:
            analysis['description'] = "All available player data combined"
            analysis['use_case'] = "Comprehensive analysis, data export"
        
        view_characteristics[view.value] = analysis
        
        # Print summary
        print(f"Has data: {analysis['has_data']}")
        print(f"Player count: {analysis['player_count']}")
        if analysis['has_data'] and 'fields' in analysis:
            fields = analysis['fields']
            print(f"\nFields present:")
            print(f"  - Basic info: {fields['basic_info']}")
            print(f"  - Stats: {fields['stats']}")
            print(f"  - Ownership: {fields['ownership']}")
            print(f"  - Draft ranks: {fields['draft_ranks']}")
            print(f"  - Injury info: {fields['injury_info']}")
            print(f"  - Position info: {fields['position_info']}")
            print(f"  - Team info: {fields['team_info']}")
            if fields['additional_fields']:
                print(f"  - Additional fields: {', '.join(fields['additional_fields'][:5])}")
    
    # Save comprehensive analysis
    with open(f"{ensure_json_output_dir}/fantasy_views_characteristics.json", "w") as f:
        json.dump(view_characteristics, f, indent=2)
    
    # Create summary table
    print(f"\n{'='*80}")
    print("FANTASY VIEWS CHARACTERISTICS SUMMARY")
    print(f"{'='*80}")
    print(f"{'View':<20} {'Has Data':<10} {'Description':<50}")
    print(f"{'-'*80}")
    
    for view_name, data in view_characteristics.items():
        if 'error' in data:
            print(f"{view_name:<20} {'ERROR':<10} {data['error']:<50}")
        else:
            has_data = '✓' if data['has_data'] else '✗'
            desc = data.get('description', 'N/A')[:48]
            print(f"{view_name:<20} {has_data:<10} {desc:<50}")
    
    # Create detailed characteristics documentation
    doc_content = "# ESPN Fantasy Football Player Views Characteristics\n\n"
    
    for view_name, data in sorted(view_characteristics.items()):
        if 'error' in data:
            continue
            
        doc_content += f"## {view_name}\n\n"
        doc_content += f"**Description**: {data.get('description', 'N/A')}\n\n"
        doc_content += f"**Use Case**: {data.get('use_case', 'N/A')}\n\n"
        
        if data['has_data'] and 'fields' in data:
            doc_content += "**Data Fields**:\n"
            fields = data['fields']
            if fields['basic_info']:
                doc_content += "- ✓ Basic player information (name, ID)\n"
            if fields['stats']:
                doc_content += "- ✓ Statistical data\n"
            if fields['ownership']:
                doc_content += "- ✓ Ownership percentages\n"
            if fields['draft_ranks']:
                doc_content += "- ✓ Draft rankings\n"
            if fields['injury_info']:
                doc_content += "- ✓ Injury status\n"
            if fields['position_info']:
                doc_content += "- ✓ Position eligibility\n"
            if fields['team_info']:
                doc_content += "- ✓ Team affiliation\n"
            if fields['additional_fields']:
                doc_content += f"- ✓ Additional fields: {', '.join(fields['additional_fields'][:5])}\n"
        else:
            doc_content += "**Note**: This view returns empty player objects without specific filters or league context.\n"
        
        doc_content += "\n---\n\n"
    
    with open(f"{ensure_json_output_dir}/fantasy_views_documentation.md", "w") as f:
        f.write(doc_content)
    
    print(f"\n✓ Detailed documentation saved to fantasy_views_documentation.md")