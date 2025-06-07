#!/usr/bin/env python3
"""
Simple Correlation Analysis using Site API

Analyzes correlations between NFL player statistics using the site API.
"""

import argparse
import json
import math
from datetime import datetime
from typing import Dict, List, Optional, Tuple

# Import API clients
from models.site_api.espn_nfl_api_client import Client as SiteApiClient
from models.site_web_api.espn_site_web_api_client import Client as SiteWebApiClient

# Import specific endpoints
from models.site_web_api.espn_site_web_api_client.api.default import (
    get_athlete_stats,
    get_team_leaders,
    get_league_leaders
)
# Site API imports removed - using web API only


class SimpleCorrelationAnalyzer:
    """Analyze correlations using available NFL data."""
    
    def __init__(self):
        self.site_client = SiteApiClient(base_url="https://site.api.espn.com/apis/site/v2")
        self.web_client = SiteWebApiClient(base_url="https://site.web.api.espn.com")
        
    def fetch_qb_data(self, year: int = 2023) -> List[Dict]:
        """Fetch QB data from league leaders."""
        try:
            # Get league leaders which includes QB stats
            response = get_league_leaders.sync_detailed(
                client=self.web_client,
                sport="football",
                league="nfl",
                season=year
            )
            
            if response.status_code != 200:
                print(f"Error fetching leaders data: {response.status_code}")
                return []
                
            qb_data = []
            if hasattr(response.parsed, 'leaders') and response.parsed.leaders:
                # Leaders is a container object, need to check its attributes
                leaders_attrs = [attr for attr in dir(response.parsed.leaders) if not attr.startswith('_')]
                print(f"Leaders attributes: {leaders_attrs}")
                
                # Try to iterate directly
                if hasattr(response.parsed.leaders, 'categories'):
                    categories = response.parsed.leaders.categories
                else:
                    # Maybe it's directly iterable
                    categories = []
                    for attr in leaders_attrs:
                        val = getattr(response.parsed.leaders, attr)
                        if hasattr(val, 'leaders'):
                            categories.append(val)
                
                for category in categories:
                    if hasattr(category, 'name') and 'passing' in category.name.lower():
                        if hasattr(category, 'leaders') and category.leaders:
                            for leader in category.leaders[:30]:  # Top 30 QBs
                                if hasattr(leader, 'athlete') and leader.athlete:
                                    athlete_name = leader.athlete.display_name if hasattr(leader.athlete, 'display_name') else 'Unknown'
                                    
                                    # Find or create player entry
                                    player_entry = None
                                    for p in qb_data:
                                        if p['name'] == athlete_name:
                                            player_entry = p
                                            break
                                            
                                    if not player_entry:
                                        player_entry = {
                                            'name': athlete_name,
                                            'position': 'QB',
                                            'team': leader.athlete.team.abbreviation if hasattr(leader.athlete, 'team') and hasattr(leader.athlete.team, 'abbreviation') else '',
                                            'stats': {}
                                        }
                                        qb_data.append(player_entry)
                                        
                                    # Add stat
                                    stat_name = category.name.lower().replace(' ', '_').replace('/', '_')
                                    if hasattr(leader, 'value'):
                                        try:
                                            # Handle comma-separated numbers
                                            value_str = str(leader.value).replace(',', '')
                                            player_entry['stats'][stat_name] = float(value_str)
                                        except ValueError:
                                            pass
                        
            return qb_data
            
        except Exception as e:
            print(f"Error fetching QB data: {e}")
            return []
            
    def fetch_all_leaders_data(self, sport: str = "football", league: str = "nfl", 
                               year: int = 2023) -> List[Dict]:
        """Fetch all season leaders data."""
        try:
            response = get_league_leaders.sync_detailed(
                client=self.web_client,
                sport=sport,
                league=league,
                season=year
            )
            
            if response.status_code != 200:
                print(f"Error fetching all leaders: {response.status_code}")
                return []
                
            players = []
            if hasattr(response.parsed, 'leaders') and response.parsed.leaders:
                for category in response.parsed.leaders:
                    if hasattr(category, 'leaders') and category.leaders:
                        category_name = category.name if hasattr(category, 'name') else 'Unknown'
                        
                        for leader in category.leaders[:20]:  # Top 20 in each category
                            if hasattr(leader, 'athlete') and leader.athlete:
                                # Find or create player entry
                                player_name = leader.athlete.display_name if hasattr(leader.athlete, 'display_name') else 'Unknown'
                                player_entry = None
                                
                                for p in players:
                                    if p['name'] == player_name:
                                        player_entry = p
                                        break
                                        
                                if not player_entry:
                                    player_entry = {
                                        'name': player_name,
                                        'position': leader.athlete.position.abbreviation if hasattr(leader.athlete, 'position') and hasattr(leader.athlete.position, 'abbreviation') else '',
                                        'team': leader.athlete.team.abbreviation if hasattr(leader.athlete, 'team') and hasattr(leader.athlete.team, 'abbreviation') else '',
                                        'stats': {}
                                    }
                                    players.append(player_entry)
                                    
                                # Add stat value
                                if hasattr(leader, 'value'):
                                    stat_key = category_name.lower().replace(' ', '_')
                                    try:
                                        player_entry['stats'][stat_key] = float(leader.value)
                                    except ValueError:
                                        pass
                                        
            return players
            
        except Exception as e:
            print(f"Error fetching leaders: {e}")
            return []
            
    def calculate_correlation(self, x: List[float], y: List[float]) -> Tuple[float, float]:
        """Calculate Pearson correlation coefficient and p-value."""
        if len(x) != len(y) or len(x) < 3:
            return 0.0, 1.0
            
        n = len(x)
        
        # Calculate means
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        
        # Calculate standard deviations
        std_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x) / (n - 1))
        std_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y) / (n - 1))
        
        if std_x == 0 or std_y == 0:
            return 0.0, 1.0
        
        # Calculate correlation
        cov = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / (n - 1)
        r = cov / (std_x * std_y)
        
        # Calculate t-statistic for p-value
        if abs(r) >= 1:
            p_value = 0.0
        else:
            t = r * math.sqrt(n - 2) / math.sqrt(1 - r**2)
            # Approximate p-value
            df = n - 2
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
        
    def analyze_qb_correlations(self, qb_data: List[Dict]) -> Dict[str, Dict]:
        """Analyze correlations for QB data."""
        if not qb_data:
            return {}
            
        # Look for a proxy for fantasy points (e.g., total yards, TDs)
        # Create a simple fantasy points estimate
        for qb in qb_data:
            stats = qb['stats']
            # Simple fantasy scoring: 1 pt per 25 pass yds, 4 pts per pass TD
            fantasy_pts = 0
            if 'passingyards' in stats:
                fantasy_pts += stats['passingyards'] / 25
            elif 'passing_yards' in stats:
                fantasy_pts += stats['passing_yards'] / 25
                
            if 'passingtouchdowns' in stats:
                fantasy_pts += stats['passingtouchdowns'] * 4
            elif 'passing_touchdowns' in stats:
                fantasy_pts += stats['passing_touchdowns'] * 4
                
            if 'rushing_yards' in stats:
                fantasy_pts += stats['rushing_yards'] / 10
            if 'rushing_touchdowns' in stats:
                fantasy_pts += stats['rushing_touchdowns'] * 6
                
            # Add interception penalty
            if 'interceptions' in stats:
                fantasy_pts -= stats['interceptions'] * 2
                
            stats['estimated_fantasy_points'] = fantasy_pts
            
        # Calculate correlations
        correlations = {}
        target = 'estimated_fantasy_points'
        
        # Gather all stats
        all_stats = {}
        target_values = []
        
        for qb in qb_data:
            if target in qb['stats']:
                target_values.append(qb['stats'][target])
                for stat_name, value in qb['stats'].items():
                    if stat_name != target and isinstance(value, (int, float)):
                        if stat_name not in all_stats:
                            all_stats[stat_name] = []
                        all_stats[stat_name].append(value)
                        
        # Calculate correlations
        for stat_name, values in all_stats.items():
            if len(values) == len(target_values) and len(values) >= 5:
                corr, p_value = self.calculate_correlation(values, target_values)
                correlations[stat_name] = {
                    'correlation': corr,
                    'p_value': p_value,
                    'sample_size': len(values)
                }
                
        return correlations
        
    def display_results(self, correlations: Dict[str, Dict], position: str = "QB"):
        """Display correlation results."""
        print(f"\n{position} CORRELATIONS WITH ESTIMATED FANTASY POINTS")
        print("="*60)
        print(f"{'Statistic':<25} {'Correlation':>12} {'P-Value':>12} {'Sample':>8}")
        print("-"*60)
        
        # Sort by absolute correlation
        sorted_stats = sorted(correlations.items(), 
                            key=lambda x: abs(x[1]['correlation']), 
                            reverse=True)
        
        for stat, data in sorted_stats:
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
                
            print(f"{stat:<25} {corr:>12.3f}{sig:<3} {p_val:>9.3f} {sample:>8}")
            
        print("\nSignificance: * p<0.05, ** p<0.01, *** p<0.001")
        
    def run(self, year: int = 2023):
        """Run the analysis."""
        print(f"\nFetching QB data for {year}...")
        qb_data = self.fetch_qb_data(year)
        
        if qb_data:
            print(f"Analyzing {len(qb_data)} QBs...")
            correlations = self.analyze_qb_correlations(qb_data)
            
            if correlations:
                self.display_results(correlations, "QB")
            else:
                print("Not enough data for correlation analysis")
                
            # Save raw data
            with open(f"qb_correlations_{year}.json", "w") as f:
                json.dump({
                    'year': year,
                    'qb_data': qb_data,
                    'correlations': correlations
                }, f, indent=2)
                print(f"\nData saved to qb_correlations_{year}.json")
        else:
            print("No QB data found")
            
        # Also try to get general leaders
        print(f"\nFetching season leaders...")
        leaders = self.fetch_all_leaders_data(year=year)
        
        if leaders:
            print(f"Found {len(leaders)} players in leader categories")
            # Group by position
            by_position = {}
            for player in leaders:
                pos = player['position']
                if pos not in by_position:
                    by_position[pos] = []
                by_position[pos].append(player)
                
            print(f"Positions found: {list(by_position.keys())}")
            
            # Save leaders data
            with open(f"leaders_{year}.json", "w") as f:
                json.dump(leaders, f, indent=2)


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Simple correlation analysis using available NFL data"
    )
    
    parser.add_argument(
        "--year",
        type=int,
        default=2023,
        help="Season year (default: 2023)"
    )
    
    args = parser.parse_args()
    
    analyzer = SimpleCorrelationAnalyzer()
    analyzer.run(args.year)


if __name__ == "__main__":
    main()