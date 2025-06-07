#!/usr/bin/env python3
"""
Working Correlation Analysis Recipe

This recipe fetches real NFL data and calculates correlations between 
player statistics and fantasy points.
"""

import argparse
import json
import statistics
from typing import Dict, List, Tuple

# Import API clients
from models.site_web_api.espn_site_web_api_client import Client as SiteWebApiClient
from models.site_web_api.espn_site_web_api_client.api.default import get_league_leaders
from models.site_web_api.espn_site_web_api_client.models.get_league_leaders_sport import GetLeagueLeadersSport


class CorrelationAnalyzer:
    """Analyze correlations between NFL player statistics."""
    
    def __init__(self):
        self.web_client = SiteWebApiClient(base_url="https://site.web.api.espn.com")
        
        # Stat name mappings for better display
        self.stat_display_names = {
            'passingyards': 'Passing Yards',
            'passingtouchdowns': 'Passing TDs',
            'interceptions': 'Interceptions',
            'rushingcarries': 'Rushing Attempts',
            'rushingyards': 'Rushing Yards',
            'rushingtouchdowns': 'Rushing TDs',
            'receptions': 'Receptions',
            'receivingyards': 'Receiving Yards',
            'receivingtouchdowns': 'Receiving TDs',
            'points': 'Points Scored',
            'fieldgoalsmade': 'Field Goals Made',
            'fieldgoalsmissed': 'Field Goals Missed',
            'extrapointsmade': 'Extra Points Made'
        }
        
    def fetch_players_by_position(self, year: int, position: str) -> List[Dict]:
        """Fetch player data for a specific position."""
        try:
            response = get_league_leaders.sync_detailed(
                client=self.web_client,
                sport=GetLeagueLeadersSport.FOOTBALL,
                league="nfl",
                season=year
            )
            
            if response.status_code != 200:
                print(f"Error fetching data: {response.status_code}")
                return []
                
            players = {}  # Use dict to aggregate stats by player
            
            if hasattr(response.parsed, 'leaders') and response.parsed.leaders:
                # Process categories
                if hasattr(response.parsed.leaders, 'categories'):
                    for category in response.parsed.leaders.categories:
                        if hasattr(category, 'leaders') and category.leaders:
                            # Get category name
                            category_name = category.name.lower().replace(' ', '').replace('/', '_') if hasattr(category, 'name') else 'unknown'
                            
                            for leader in category.leaders:
                                if hasattr(leader, 'athlete') and leader.athlete:
                                    # Check position filter
                                    athlete_pos = leader.athlete.position.abbreviation if hasattr(leader.athlete, 'position') and hasattr(leader.athlete.position, 'abbreviation') else ''
                                    
                                    if position and athlete_pos != position:
                                        continue
                                        
                                    # Get player name
                                    player_name = leader.athlete.display_name if hasattr(leader.athlete, 'display_name') else 'Unknown'
                                    
                                    # Initialize player if not exists
                                    if player_name not in players:
                                        players[player_name] = {
                                            'name': player_name,
                                            'position': athlete_pos,
                                            'stats': {}
                                        }
                                    
                                    # Add stat value
                                    if hasattr(leader, 'value'):
                                        try:
                                            value_str = str(leader.value).replace(',', '')
                                            players[player_name]['stats'][category_name] = float(value_str)
                                        except ValueError:
                                            pass
                                            
            # Convert to list and calculate fantasy points
            player_list = list(players.values())
            for player in player_list:
                self.calculate_fantasy_points(player)
                
            return player_list
            
        except Exception as e:
            print(f"Error fetching player data: {e}")
            return []
            
    def calculate_fantasy_points(self, player: Dict):
        """Calculate estimated fantasy points for a player."""
        stats = player['stats']
        position = player['position']
        fantasy_points = 0
        
        # QB scoring
        if position == 'QB':
            fantasy_points += stats.get('passingyards', 0) / 25
            fantasy_points += stats.get('passingtouchdowns', 0) * 4
            fantasy_points -= stats.get('interceptions', 0) * 2
            fantasy_points += stats.get('rushingyards', 0) / 10
            fantasy_points += stats.get('rushingtouchdowns', 0) * 6
            
        # RB scoring
        elif position == 'RB':
            fantasy_points += stats.get('rushingyards', 0) / 10
            fantasy_points += stats.get('rushingtouchdowns', 0) * 6
            fantasy_points += stats.get('receptions', 0) * 1  # PPR
            fantasy_points += stats.get('receivingyards', 0) / 10
            fantasy_points += stats.get('receivingtouchdowns', 0) * 6
            
        # WR/TE scoring
        elif position in ['WR', 'TE']:
            fantasy_points += stats.get('receptions', 0) * 1  # PPR
            fantasy_points += stats.get('receivingyards', 0) / 10
            fantasy_points += stats.get('receivingtouchdowns', 0) * 6
            fantasy_points += stats.get('rushingyards', 0) / 10
            fantasy_points += stats.get('rushingtouchdowns', 0) * 6
            
        # K scoring
        elif position == 'K':
            fantasy_points += stats.get('fieldgoalsmade', 0) * 3
            fantasy_points += stats.get('extrapointsmade', 0) * 1
            
        stats['fantasy_points'] = fantasy_points
        
    def calculate_correlation(self, x: List[float], y: List[float]) -> Tuple[float, float]:
        """Calculate Pearson correlation coefficient and p-value."""
        if len(x) != len(y) or len(x) < 3:
            return 0.0, 1.0
            
        try:
            # Use statistics module
            r = statistics.correlation(x, y)
            
            # Calculate p-value approximation
            n = len(x)
            if abs(r) >= 1:
                p_value = 0.0
            else:
                import math
                t = r * math.sqrt(n - 2) / math.sqrt(1 - r**2)
                # Approximate p-value
                if abs(t) > 3.5:
                    p_value = 0.001
                elif abs(t) > 2.8:
                    p_value = 0.01
                elif abs(t) > 2.3:
                    p_value = 0.05
                elif abs(t) > 1.8:
                    p_value = 0.1
                else:
                    p_value = 0.5
                    
            return r, p_value
            
        except (statistics.StatisticsError, ZeroDivisionError):
            return 0.0, 1.0
            
    def analyze_position(self, players: List[Dict]) -> Dict[str, Dict]:
        """Analyze correlations for a specific position."""
        if len(players) < 5:
            return {}
            
        # Filter players with valid fantasy points
        valid_players = [p for p in players if 'fantasy_points' in p['stats'] and p['stats']['fantasy_points'] > 0]
        
        if len(valid_players) < 5:
            return {}
            
        # First pass: collect all stat names
        all_stat_names = set()
        for player in valid_players:
            for stat_name in player['stats']:
                if stat_name != 'fantasy_points' and isinstance(player['stats'][stat_name], (int, float)):
                    all_stat_names.add(stat_name)
                    
        # Second pass: build aligned arrays
        fantasy_points = []
        stats_arrays = {stat_name: [] for stat_name in all_stat_names}
        
        for player in valid_players:
            fantasy_points.append(player['stats']['fantasy_points'])
            for stat_name in all_stat_names:
                # Use 0 as default for missing stats
                value = player['stats'].get(stat_name, 0)
                stats_arrays[stat_name].append(value)
                        
        # Calculate correlations
        correlations = {}
        for stat_name, values in stats_arrays.items():
            if len(values) >= 5:  # Need at least 5 data points
                corr, p_value = self.calculate_correlation(values, fantasy_points)
                correlations[stat_name] = {
                    'correlation': corr,
                    'p_value': p_value,
                    'sample_size': len(values)
                }
                
        return correlations
        
    def display_results(self, position: str, players: List[Dict], correlations: Dict[str, Dict]):
        """Display analysis results."""
        print(f"\n{'='*60}")
        print(f"{position} FANTASY CORRELATION ANALYSIS")
        print(f"{'='*60}")
        print(f"Players analyzed: {len(players)}")
        
        if not correlations:
            print("Not enough data for correlation analysis")
            return
            
        print(f"\nSTAT CORRELATIONS WITH FANTASY POINTS")
        print(f"{'-'*60}")
        print(f"{'Statistic':<25} {'Correlation':>12} {'P-Value':>12} {'Sample':>8}")
        print(f"{'-'*60}")
        
        # Sort by absolute correlation
        sorted_stats = sorted(correlations.items(), 
                            key=lambda x: abs(x[1]['correlation']), 
                            reverse=True)
        
        for stat_name, data in sorted_stats:
            display_name = self.stat_display_names.get(stat_name, stat_name.title())
            corr = data['correlation']
            p_val = data['p_value']
            sample = data['sample_size']
            
            # Significance markers
            if p_val <= 0.001:
                sig = "***"
            elif p_val <= 0.01:
                sig = "**"
            elif p_val <= 0.05:
                sig = "*"
            else:
                sig = ""
                
            print(f"{display_name:<25} {corr:>12.3f}{sig:<3} {p_val:>9.3f} {sample:>8}")
            
        print("\nSignificance: * p<0.05, ** p<0.01, *** p<0.001")
        
        # Show top fantasy performers
        print(f"\nTOP 5 {position}s BY FANTASY POINTS")
        print(f"{'-'*60}")
        sorted_players = sorted(players, key=lambda x: x['stats'].get('fantasy_points', 0), reverse=True)
        for i, player in enumerate(sorted_players[:5], 1):
            fp = player['stats'].get('fantasy_points', 0)
            print(f"{i}. {player['name']:<30} {fp:>8.1f} pts")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Analyze fantasy correlations for NFL players"
    )
    
    parser.add_argument(
        "--year",
        type=int,
        default=2023,
        help="Season year (default: 2023)"
    )
    
    parser.add_argument(
        "--position",
        choices=["QB", "RB", "WR", "TE", "K"],
        default="QB",
        help="Position to analyze (default: QB)"
    )
    
    parser.add_argument(
        "--save",
        help="Save results to JSON file"
    )
    
    args = parser.parse_args()
    
    analyzer = CorrelationAnalyzer()
    
    print(f"Fetching {args.position} data for {args.year}...")
    players = analyzer.fetch_players_by_position(args.year, args.position)
    
    if not players:
        print(f"No {args.position} data found")
        return
        
    print(f"Analyzing {len(players)} {args.position}s...")
    correlations = analyzer.analyze_position(players)
    
    analyzer.display_results(args.position, players, correlations)
    
    if args.save:
        results = {
            'year': args.year,
            'position': args.position,
            'players': players,
            'correlations': correlations
        }
        with open(args.save, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\nResults saved to {args.save}")


if __name__ == "__main__":
    main()