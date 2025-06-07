#!/usr/bin/env python3
"""
Fantasy Correlation Analysis Recipe

This recipe analyzes correlations between player statistics and fantasy points,
helping identify which stats are most predictive of fantasy success and which
player combinations have high correlation (e.g., QB-WR stacks).
"""

import argparse
import json
import math
from datetime import datetime
from typing import Dict, List, Optional, Tuple

# Try to import scipy for better statistical calculations
try:
    from scipy import stats as scipy_stats
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False
    # Fallback to basic statistics module
    import statistics

# Import API clients
from models.fantasy_api.espn_fantasy_api_client import Client as FantasyApiClient
from models.site_web_api.espn_site_web_api_client import Client as SiteWebApiClient

# Import specific endpoints  
from models.fantasy_api.espn_fantasy_api_client.api.default import (
    get_fantasy_football_players
)
from models.fantasy_api.espn_fantasy_api_client.models.get_fantasy_football_players_view import (
    GetFantasyFootballPlayersView
)


class CorrelationAnalyzer:
    """Analyze correlations between fantasy player statistics."""
    
    def __init__(self):
        self.fantasy_client = FantasyApiClient(base_url="https://lm-api-reads.fantasy.espn.com")
        self.web_client = SiteWebApiClient(base_url="https://site.web.api.espn.com")
        
        # Position mappings
        self.positions = {
            1: "QB",
            2: "RB", 
            3: "WR",
            4: "TE",
            5: "K",
            16: "D/ST"
        }
        
        # Comprehensive stat ID mappings (from ESPN fantasy)
        self.stat_names = {
            # Passing stats
            0: "passing_yds",
            1: "passing_tds",  
            2: "interceptions",
            3: "passing_2pt_conv",
            4: "passing_att",  # Sometimes used for attempts
            19: "passing_int_tds",  # Pick-6s against
            20: "passing_att",
            21: "completions",
            22: "incompletions",
            23: "passing_comp_pct",
            24: "passing_yds_per_att",
            25: "passing_tds_pct",
            26: "passing_int_pct",
            27: "passing_yds_per_game",
            28: "passing_tds_per_game",
            29: "passing_300_yd_games",
            30: "passing_400_yd_games",
            
            # Rushing stats (actual IDs based on ESPN)
            33: "rushing_att",
            34: "rushing_yds",
            35: "rushing_tds",
            36: "rushing_2pt_conv",
            37: "rushing_fumbles",
            38: "rushing_fumbles_lost",
            39: "rushing_yds_per_att",
            40: "rushing_yds_per_game",
            
            # Receiving stats (actual IDs)
            41: "receptions",
            42: "receiving_yds",  
            43: "receiving_tds",
            44: "receiving_2pt_conv",
            45: "receiving_fumbles",
            46: "receiving_fumbles_lost",
            47: "receiving_yds_per_rec",
            48: "receiving_yds_per_game",
            49: "receiving_tds_per_game",
            50: "receiving_100_yd_games",
            51: "receiving_200_yd_games",
            52: "receiving_targets_per_game",
            53: "receptions_per_game",
            57: "receiving_fumble_tds",
            58: "targets_per_game",
            59: "target_share_pct",
            60: "catch_pct",
            61: "receiving_yds_per_target",
            
            # Misc offensive stats
            15: "fumbles",
            16: "fumbles_lost",
            17: "fumble_tds",
            18: "total_tds",
            
            # Kicking stats
            80: "fg_made_0_19",
            81: "fg_made_20_29",
            82: "fg_made_30_39",
            83: "fg_made_40_49",
            84: "fg_made_50_plus",
            85: "fg_missed",
            86: "xp_made",
            87: "xp_missed",
            
            # Defensive/IDP stats
            95: "tackles_solo",
            96: "tackles_assist",
            97: "tackles_total",
            98: "sacks",
            99: "interceptions_def",
            100: "forced_fumbles",
            101: "fumbles_recovered",
            102: "int_tds",
            103: "fumble_rec_tds",
            104: "blocked_kicks",
            105: "safeties",
            106: "passes_defended",
            
            # Fantasy scoring
            210: "fantasy_pts_per_game",
            211: "fantasy_pts_last_1",
            212: "fantasy_pts_last_5",
            213: "fantasy_pts_total",
            214: "fantasy_pts_avg",
            
            # Additional stats
            300: "games_played",
            301: "games_started"
        }
        
    def fetch_player_data(self, year: int, position: Optional[str] = None, 
                         limit: int = 200) -> List[Dict]:
        """Fetch player data with statistics."""
        try:
            # Get players with statistics
            filter_json = json.dumps({
                "players": {
                    "limit": limit,
                    "offset": 0,
                    "sortPercOwned": {
                        "sortPriority": 1,
                        "sortAsc": False
                    },
                    "filterActive": {"value": True}
                }
            })
            
            response = get_fantasy_football_players.sync_detailed(
                client=self.fantasy_client,
                year=year,
                view=GetFantasyFootballPlayersView.KONA_PLAYER_INFO,
                scoring_period_id=0,
                x_fantasy_filter=filter_json
            )
            
            if response.status_code != 200:
                print(f"Error fetching players: {response.status_code}")
                if response.status_code == 302:
                    print("Redirect detected - API endpoint may have moved")
                    print(f"Headers: {response.headers}")
                return []
                
            players = []
            print(f"Response status: {response.status_code}")
            if response.parsed:
                print(f"Response type: {type(response.parsed)}")
                
                # Check if it's a list directly or has players attribute
                player_list = []
                if isinstance(response.parsed, list):
                    print(f"Got list of {len(response.parsed)} items")
                    player_list = response.parsed
                elif hasattr(response.parsed, '__class__') and response.parsed.__class__.__name__ != 'ErrorResponse':
                    # Try to access players attribute if not an error
                    if hasattr(response.parsed, 'players'):
                        print(f"Response has players attr")
                        player_list = response.parsed.players
                else:
                    print("Response doesn't match expected format or is an error")
                    return []
                    
                for i, player in enumerate(player_list[:limit]):  # Process up to limit
                    if i == 0:
                        print(f"First player type: {type(player)}")
                        print(f"Player attributes: {[attr for attr in dir(player) if not attr.startswith('_')]}")
                        # Check the player dict representation
                        player_dict = player.to_dict()
                        print(f"Player dict keys: {list(player_dict.keys())[:10]}")  # First 10 keys
                        if 'stats' in player_dict and player_dict['stats']:
                            print(f"Stats in dict: {player_dict['stats'][0] if isinstance(player_dict['stats'], list) else player_dict['stats']}")
                    
                    # Extract player info
                    player_data = {
                        'id': player.id if hasattr(player, 'id') else None,
                        'name': player.full_name if hasattr(player, 'full_name') else 'Unknown',
                        'position': None,
                        'team': None,
                        'stats': {}
                    }
                    
                    # Get position
                    if hasattr(player, 'default_position_id') and player.default_position_id:
                        player_data['position'] = self.positions.get(int(player.default_position_id), 'Unknown')
                        
                    # Get team
                    if hasattr(player, 'pro_team_id'):
                        player_data['team'] = player.pro_team_id
                        
                    # Extract stats
                    if hasattr(player, 'stats') and player.stats:
                        if i == 0:
                            print(f"Stats type: {type(player.stats)}")
                            print(f"Stats length: {len(player.stats) if hasattr(player.stats, '__len__') else 'N/A'}")
                            if len(player.stats) > 0:
                                print(f"First stat type: {type(player.stats[0])}")
                                print(f"First stat attrs: {[attr for attr in dir(player.stats[0]) if not attr.startswith('_')]}")
                        
                        for stat in player.stats:
                            # Check different stat formats
                            if hasattr(stat, 'scoring_period_id') and hasattr(stat, 'stats'):
                                # This might be the format
                                if stat.scoring_period_id == 0:  # Season total
                                    if i == 0:
                                        print(f"Stats object type: {type(stat.stats)}")
                                        print(f"Stats object attrs: {[attr for attr in dir(stat.stats) if not attr.startswith('_')]}")
                                        # Let's see what's in the stat object itself
                                        print(f"Stat dict: {stat.to_dict()}")
                                    
                                    # Try to access stats from additional_properties
                                    if stat.stats and hasattr(stat.stats, 'additional_properties'):
                                        if i == 0:
                                            print(f"Additional properties: {stat.stats.additional_properties}")
                                        
                                        for stat_id_str, value in stat.stats.additional_properties.items():
                                            try:
                                                stat_id = int(stat_id_str)
                                                if isinstance(value, (int, float)):
                                                    stat_name = self.stat_names.get(stat_id, f"stat_{stat_id}")
                                                    player_data['stats'][stat_name] = value
                                            except (ValueError, AttributeError):
                                                # Skip non-numeric stat IDs
                                                pass
                                            
                    # Filter by position if specified
                    if position and player_data['position'] != position:
                        continue
                        
                    # Only include players with stats
                    if player_data['stats']:
                        players.append(player_data)
                        
            return players
            
        except Exception as e:
            print(f"Error fetching player data: {e}")
            return []
            
    def calculate_correlation(self, x: List[float], y: List[float]) -> Tuple[float, float]:
        """Calculate Pearson correlation coefficient and p-value."""
        if len(x) != len(y) or len(x) < 3:
            return 0.0, 1.0
            
        if HAS_SCIPY:
            # Use scipy for accurate calculations
            try:
                r, p_value = scipy_stats.pearsonr(x, y)
                return r, p_value
            except Exception:
                # Fall back to manual calculation if scipy fails
                pass
                
        # Manual calculation if scipy is not available
        n = len(x)
        
        # Use statistics module if available
        try:
            mean_x = statistics.mean(x)
            mean_y = statistics.mean(y)
            
            # Calculate correlation using covariance and standard deviations
            cov = statistics.covariance(x, y)
            std_x = statistics.stdev(x)
            std_y = statistics.stdev(y)
            
            if std_x == 0 or std_y == 0:
                return 0.0, 1.0
                
            r = cov / (std_x * std_y)
            
            # Calculate t-statistic for p-value
            if abs(r) >= 1:
                p_value = 0.0
            else:
                t = r * math.sqrt(n - 2) / math.sqrt(1 - r**2)
                # Use t-distribution approximation
                df = n - 2
                # Better approximation of p-value
                if abs(t) > 4.0:
                    p_value = 0.001
                elif abs(t) > 3.355:  # ~99% confidence for df=10
                    p_value = 0.01
                elif abs(t) > 2.228:  # ~95% confidence for df=10
                    p_value = 0.05
                elif abs(t) > 1.812:  # ~90% confidence for df=10
                    p_value = 0.1
                else:
                    # Rough linear approximation for smaller t values
                    p_value = 1.0 - (abs(t) / 2.0)
                    
            return r, p_value
            
        except (AttributeError, statistics.StatisticsError):
            # Fallback to basic calculation
            mean_x = sum(x) / n
            mean_y = sum(y) / n
            
            # Calculate correlation
            num = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
            den_x = sum((x[i] - mean_x) ** 2 for i in range(n))
            den_y = sum((y[i] - mean_y) ** 2 for i in range(n))
            
            if den_x == 0 or den_y == 0:
                return 0.0, 1.0
                
            r = num / math.sqrt(den_x * den_y)
            
            # Simple p-value approximation
            if abs(r) >= 1:
                p_value = 0.0
            else:
                t = r * math.sqrt(n - 2) / math.sqrt(1 - r**2)
                if abs(t) > 3:
                    p_value = 0.01
                elif abs(t) > 2:
                    p_value = 0.05
                else:
                    p_value = 0.5
                    
            return r, p_value
            
    def calculate_correlations(self, players: List[Dict]) -> Dict[str, Dict]:
        """Calculate correlations between different statistics."""
        # Organize stats by type
        stats_by_type = {}
        fantasy_points = []
        
        for player in players:
            if 'fantasy_points' in player['stats']:
                fantasy_points.append(player['stats']['fantasy_points'])
                for stat_name, value in player['stats'].items():
                    if stat_name not in ['fantasy_points'] and isinstance(value, (int, float)):
                        if stat_name not in stats_by_type:
                            stats_by_type[stat_name] = []
                        stats_by_type[stat_name].append(value)
                        
        if not fantasy_points or len(fantasy_points) < 10:
            return {}
            
        # Calculate correlations
        correlations = {}
        for stat_name, values in stats_by_type.items():
            if len(values) == len(fantasy_points) and len(values) >= 10:
                corr, p_value = self.calculate_correlation(values, fantasy_points)
                correlations[stat_name] = {
                    'correlation': corr,
                    'p_value': p_value,
                    'sample_size': len(values)
                }
                
        return correlations
        
    def analyze_player_stacks(self, players: List[Dict]) -> List[Dict]:
        """Analyze correlations between player pairs (e.g., QB-WR stacks)."""
        stacks = []
        
        # Group players by team and position
        team_players = {}
        for player in players:
            if player['team'] and player['position']:
                if player['team'] not in team_players:
                    team_players[player['team']] = {'QB': [], 'WR': [], 'TE': [], 'RB': []}
                if player['position'] in team_players[player['team']]:
                    team_players[player['team']][player['position']].append(player)
                    
        # Analyze QB-WR/TE stacks
        for team, positions in team_players.items():
            if positions['QB'] and (positions['WR'] or positions['TE']):
                for qb in positions['QB']:
                    # Combine WR and TE for pass catchers
                    pass_catchers = positions['WR'] + positions['TE']
                    for receiver in pass_catchers:
                        # Calculate correlation between QB passing stats and receiver stats
                        if ('passing_yds' in qb['stats'] and 'receiving_yds' in receiver['stats'] and
                            'fantasy_points' in qb['stats'] and 'fantasy_points' in receiver['stats']):
                            
                            stack_data = {
                                'team': team,
                                'qb': qb['name'],
                                'receiver': receiver['name'],
                                'receiver_pos': receiver['position'],
                                'qb_fantasy_pts': qb['stats']['fantasy_points'],
                                'receiver_fantasy_pts': receiver['stats']['fantasy_points'],
                                'combined_pts': qb['stats']['fantasy_points'] + receiver['stats']['fantasy_points']
                            }
                            
                            # Add correlation info if we had game-by-game data
                            # For now, we'll use season totals as a proxy
                            if qb['stats'].get('passing_tds', 0) > 0:
                                stack_data['td_share'] = (receiver['stats'].get('receiving_tds', 0) / 
                                                         qb['stats']['passing_tds']) * 100
                            else:
                                stack_data['td_share'] = 0
                                
                            if qb['stats'].get('passing_yds', 0) > 0:
                                stack_data['yds_share'] = (receiver['stats'].get('receiving_yds', 0) / 
                                                          qb['stats']['passing_yds']) * 100
                            else:
                                stack_data['yds_share'] = 0
                                
                            stacks.append(stack_data)
                            
        return sorted(stacks, key=lambda x: x['combined_pts'], reverse=True)
        
    def analyze_position_correlations(self, players: List[Dict]) -> Dict[str, Dict]:
        """Analyze correlations by position."""
        position_correlations = {}
        
        # Group by position
        for position in ['QB', 'RB', 'WR', 'TE']:
            position_players = [p for p in players if p['position'] == position]
            if len(position_players) >= 10:
                corr_dict = self.calculate_correlations(position_players)
                if corr_dict:
                    position_correlations[position] = corr_dict
                    
        return position_correlations
        
    def format_correlation_output(self, correlations: Dict[str, Dict], position: str = "All") -> List[str]:
        """Format correlation analysis for console output."""
        lines = []
        
        if not correlations:
            lines.append(f"No correlation data available for {position}")
            return lines
            
        lines.append(f"\n{position} STAT CORRELATIONS WITH FANTASY POINTS")
        lines.append("=" * 60)
        lines.append(f"{'Statistic':<20} {'Correlation':>12} {'P-Value':>12} {'Sample':>8}")
        lines.append("-" * 60)
        
        # Sort by absolute correlation value
        sorted_stats = sorted(correlations.items(), 
                            key=lambda x: abs(x[1]['correlation']), 
                            reverse=True)
        
        for stat, data in sorted_stats:
            corr_value = data['correlation']
            p_value = data['p_value']
            sample_size = int(data['sample_size'])
            
            # Format correlation with significance indicators
            if p_value < 0.001:
                sig = "***"
            elif p_value < 0.01:
                sig = "**"
            elif p_value < 0.05:
                sig = "*"
            else:
                sig = ""
                
            lines.append(f"{stat:<20} {corr_value:>12.3f}{sig:<3} {p_value:>9.3f} {sample_size:>8}")
            
        lines.append("\nSignificance: * p<0.05, ** p<0.01, *** p<0.001")
        
        return lines
        
    def format_stacks_output(self, stacks: List[Dict], limit: int = 20) -> List[str]:
        """Format player stack analysis for console output."""
        lines = []
        
        lines.append("\nTOP QB-RECEIVER STACKS")
        lines.append("=" * 80)
        lines.append(f"{'Team':<5} {'QB':<20} {'Receiver':<20} {'Pos':<4} {'Combined':>10} {'TD%':>6} {'Yds%':>6}")
        lines.append("-" * 80)
        
        for stack in stacks[:limit]:
            lines.append(f"{stack['team']:<5} {stack['qb']:<20} {stack['receiver']:<20} "
                        f"{stack['receiver_pos']:<4} {stack['combined_pts']:>10.1f} "
                        f"{stack['td_share']:>6.1f} {stack['yds_share']:>6.1f}")
            
        return lines
        
    def run(self, year: int, positions: Optional[List[str]] = None,
            output_format: str = 'console', limit: int = 200) -> Dict:
        """Run the correlation analysis."""
        results = {
            'year': year,
            'overall_correlations': None,
            'position_correlations': {},
            'player_stacks': [],
            'summary': {}
        }
        
        print(f"Fetching fantasy player data for {year}...")
        
        # Fetch player data
        all_players = self.fetch_player_data(year, limit=limit)
        
        if not all_players:
            print("No player data found")
            return results
            
        print(f"Analyzing {len(all_players)} players...")
        
        # Overall correlations
        overall_corr = self.calculate_correlations(all_players)
        results['overall_correlations'] = overall_corr
        
        # Position-specific correlations
        if positions:
            for pos in positions:
                pos_players = [p for p in all_players if p['position'] == pos]
                if pos_players:
                    pos_corr = self.calculate_correlations(pos_players)
                    results['position_correlations'][pos] = pos_corr
        else:
            # Analyze all positions
            results['position_correlations'] = self.analyze_position_correlations(all_players)
            
        # Player stacks
        print("Analyzing player stacks...")
        results['player_stacks'] = self.analyze_player_stacks(all_players)
        
        # Generate summary
        results['summary'] = {
            'total_players_analyzed': len(all_players),
            'positions_analyzed': list(results['position_correlations'].keys()),
            'top_stacks_count': len(results['player_stacks'])
        }
        
        # Format output
        if output_format == 'console':
            # Overall correlations
            for line in self.format_correlation_output(overall_corr, "ALL POSITIONS"):
                print(line)
                
            # Position-specific
            for position, corr_df in results['position_correlations'].items():
                for line in self.format_correlation_output(corr_df, position):
                    print(line)
                    
            # Stacks
            if results['player_stacks']:
                for line in self.format_stacks_output(results['player_stacks']):
                    print(line)
                    
        return results


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Analyze fantasy correlations between player statistics"
    )
    
    parser.add_argument(
        "--year",
        type=int,
        default=datetime.now().year - 1,
        help="Season year to analyze (default: last completed season)"
    )
    
    parser.add_argument(
        "--positions",
        nargs="+",
        choices=["QB", "RB", "WR", "TE"],
        help="Specific positions to analyze"
    )
    
    parser.add_argument(
        "--output",
        choices=["console", "json", "csv"],
        default="console",
        help="Output format"
    )
    
    parser.add_argument(
        "--save",
        help="Save output to file"
    )
    
    parser.add_argument(
        "--limit",
        type=int,
        default=200,
        help="Number of players to analyze (default: 200)"
    )
    
    parser.add_argument(
        "--min-correlation",
        type=float,
        default=0.3,
        help="Minimum correlation threshold to display (default: 0.3)"
    )
    
    args = parser.parse_args()
    
    # Create analyzer
    analyzer = CorrelationAnalyzer()
    
    # Run analysis
    results = analyzer.run(
        year=args.year,
        positions=args.positions,
        output_format=args.output,
        limit=args.limit
    )
    
    # Save if requested
    if args.save:
        if args.output == 'json':
            with open(args.save, 'w') as f:
                json.dump(results, f, indent=2, default=str)
            print(f"\nResults saved to: {args.save}")
            
        elif args.output == 'csv':
            # Save correlations to CSV format
            if results['overall_correlations']:
                with open(args.save, 'w') as f:
                    f.write("Statistic,Correlation,P-Value,Sample Size\n")
                    for stat, data in results['overall_correlations'].items():
                        f.write(f"{stat},{data['correlation']:.4f},{data['p_value']:.4f},{data['sample_size']}\n")
                print(f"\nCorrelations saved to: {args.save}")


if __name__ == "__main__":
    main()