#!/usr/bin/env python3
"""
Team Performance Trends - Analyze team performance metrics and trends over time.

This recipe tracks team performance including wins/losses, scoring trends, and
various performance metrics across different time periods for ESPN's supported sports.
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import asyncio
import httpx
from collections import defaultdict
import statistics

# Import API clients and models
from models.site_api.espn_nfl_api_client import Client as SiteApiClient
from models.sports_core_api.espn_sports_core_api_client import Client as SportsCoreApiClient
from models.site_api.espn_nfl_api_client.api.default import get_teams_list, get_team_schedule
from models.sports_core_api.espn_sports_core_api_client.api.default import get_team_record

# Supported leagues with their sport mappings
SUPPORTED_LEAGUES = {
    "nfl": ("football", "nfl", "NFL"),
    "nba": ("basketball", "nba", "NBA"),
    "mlb": ("baseball", "mlb", "MLB"),
    "nhl": ("hockey", "nhl", "NHL")
}

def create_site_client() -> SiteApiClient:
    """Create and return Site API client."""
    return SiteApiClient(base_url="https://site.api.espn.com/apis/site/v2")

def create_core_client() -> SportsCoreApiClient:
    """Create and return Sports Core API client."""
    return SportsCoreApiClient(base_url="https://sports.core.api.espn.com/v2")

def get_team_list(client: SiteApiClient, sport: str, league: str) -> List[Dict]:
    """Get list of teams for a league."""
    try:
        response = get_teams_list.sync_detailed(
            client=client,
            sport=sport,
            league=league
        )
        
        if response.status_code != 200 or not response.parsed:
            return []
        
        teams = []
        if hasattr(response.parsed, 'sports') and response.parsed.sports:
            for sport_obj in response.parsed.sports:
                if hasattr(sport_obj, 'leagues') and sport_obj.leagues:
                    for league_obj in sport_obj.leagues:
                        if hasattr(league_obj, 'teams') and league_obj.teams:
                            for team in league_obj.teams:
                                if hasattr(team, 'team') and team.team:
                                    t = team.team
                                    teams.append({
                                        'id': t.id if hasattr(t, 'id') else None,
                                        'abbreviation': t.abbreviation if hasattr(t, 'abbreviation') else None,
                                        'display_name': t.display_name if hasattr(t, 'display_name') else None,
                                        'location': t.location if hasattr(t, 'location') else None
                                    })
        
        return teams
        
    except Exception:
        return []

def fetch_team_schedule(client: SiteApiClient, sport: str, league: str, team_id: str, season: Optional[int] = None) -> List[Dict]:
    """Fetch team schedule and results."""
    try:
        params = {'sport': sport, 'league': league, 'team_id_or_abbrev': team_id}
        if season:
            params['season'] = season
            
        response = get_team_schedule.sync_detailed(
            client=client,
            **params
        )
        
        if response.status_code != 200 or not response.parsed:
            return []
        
        games = []
        if hasattr(response.parsed, 'events') and response.parsed.events:
            for event in response.parsed.events:
                game_info = {
                    'id': event.id if hasattr(event, 'id') else None,
                    'date': event.date if hasattr(event, 'date') else None,
                    'name': event.name if hasattr(event, 'name') else None,
                    'completed': False,
                    'home_game': False,
                    'result': None,
                    'score': None,
                    'opponent_score': None,
                    'opponent': None
                }
                
                # Check if game is completed
                if hasattr(event, 'competitions') and event.competitions:
                    comp = event.competitions[0]
                    if hasattr(comp, 'status') and comp.status:
                        if hasattr(comp.status, 'type') and comp.status.type:
                            if hasattr(comp.status.type, 'completed'):
                                game_info['completed'] = comp.status.type.completed
                    
                    # Get team and opponent info
                    if hasattr(comp, 'competitors') and comp.competitors:
                        for competitor in comp.competitors:
                            if hasattr(competitor, 'id') and str(competitor.id) == str(team_id):
                                # This is our team
                                if hasattr(competitor, 'home_away'):
                                    game_info['home_game'] = competitor.home_away == 'home'
                                if hasattr(competitor, 'winner'):
                                    game_info['result'] = 'W' if competitor.winner else 'L'
                                if hasattr(competitor, 'score'):
                                    # Handle different score formats
                                    if isinstance(competitor.score, dict):
                                        game_info['score'] = int(competitor.score.get('value', 0)) if 'value' in competitor.score else 0
                                    else:
                                        game_info['score'] = int(competitor.score) if competitor.score else 0
                            else:
                                # This is the opponent
                                if hasattr(competitor, 'team') and competitor.team:
                                    if hasattr(competitor.team, 'abbreviation'):
                                        game_info['opponent'] = competitor.team.abbreviation
                                if hasattr(competitor, 'score'):
                                    # Handle different score formats
                                    if isinstance(competitor.score, dict):
                                        game_info['opponent_score'] = int(competitor.score.get('value', 0)) if 'value' in competitor.score else 0
                                    else:
                                        game_info['opponent_score'] = int(competitor.score) if competitor.score else 0
                
                games.append(game_info)
        
        return games
        
    except Exception as e:
        print(f"Error fetching schedule: {e}")
        return []

def fetch_team_record(client: SportsCoreApiClient, sport: str, league: str, team_id: str, 
                     year: int, season_type: int = 2) -> Optional[Dict]:
    """Fetch team record data."""
    try:
        response = get_team_record.sync_detailed(
            client=client,
            sport=sport,
            league=league,
            year=year,
            seasontype=season_type,
            team_id=team_id
        )
        
        if response.status_code != 200:
            return None
            
        # Parse the response JSON directly
        data = response.json()
        
        record_info = {
            'overall': {'wins': 0, 'losses': 0, 'ties': 0},
            'home': {'wins': 0, 'losses': 0, 'ties': 0},
            'away': {'wins': 0, 'losses': 0, 'ties': 0},
            'division': {'wins': 0, 'losses': 0, 'ties': 0},
            'conference': {'wins': 0, 'losses': 0, 'ties': 0}
        }
        
        # Extract record items
        if 'items' in data:
            for item in data['items']:
                record_type = item.get('type', '')
                stats = item.get('stats', [])
                
                # Map record types
                type_map = {
                    'total': 'overall',
                    'home': 'home', 
                    'road': 'away',
                    'vsdiv': 'division',
                    'vsconf': 'conference'
                }
                
                if record_type in type_map:
                    key = type_map[record_type]
                    for stat in stats:
                        if stat.get('name') == 'wins':
                            record_info[key]['wins'] = int(stat.get('value', 0))
                        elif stat.get('name') == 'losses':
                            record_info[key]['losses'] = int(stat.get('value', 0))
                        elif stat.get('name') == 'ties':
                            record_info[key]['ties'] = int(stat.get('value', 0))
        
        return record_info
        
    except Exception:
        return None

def calculate_trends(games: List[Dict], window_size: int = 10) -> Dict:
    """Calculate performance trends from game data."""
    trends = {
        'overall': {'wins': 0, 'losses': 0, 'win_pct': 0.0},
        'last_n': {'wins': 0, 'losses': 0, 'win_pct': 0.0, 'n': window_size},
        'home': {'wins': 0, 'losses': 0, 'win_pct': 0.0},
        'away': {'wins': 0, 'losses': 0, 'win_pct': 0.0},
        'scoring': {
            'avg_points_for': 0.0,
            'avg_points_against': 0.0,
            'avg_margin': 0.0,
            'last_n_avg_for': 0.0,
            'last_n_avg_against': 0.0
        },
        'streaks': {
            'current': {'type': None, 'length': 0},
            'longest_win': 0,
            'longest_loss': 0
        },
        'form': []  # Last 5 games W/L
    }
    
    # Filter completed games
    completed_games = [g for g in games if g['completed'] and g['result']]
    
    if not completed_games:
        return trends
    
    # Overall record
    for game in completed_games:
        if game['result'] == 'W':
            trends['overall']['wins'] += 1
        else:
            trends['overall']['losses'] += 1
            
        # Home/Away splits
        if game['home_game']:
            if game['result'] == 'W':
                trends['home']['wins'] += 1
            else:
                trends['home']['losses'] += 1
        else:
            if game['result'] == 'W':
                trends['away']['wins'] += 1
            else:
                trends['away']['losses'] += 1
    
    # Calculate win percentages
    total_games = trends['overall']['wins'] + trends['overall']['losses']
    if total_games > 0:
        trends['overall']['win_pct'] = trends['overall']['wins'] / total_games
    
    home_games = trends['home']['wins'] + trends['home']['losses']
    if home_games > 0:
        trends['home']['win_pct'] = trends['home']['wins'] / home_games
        
    away_games = trends['away']['wins'] + trends['away']['losses']
    if away_games > 0:
        trends['away']['win_pct'] = trends['away']['wins'] / away_games
    
    # Last N games
    recent_games = completed_games[-window_size:] if len(completed_games) >= window_size else completed_games
    for game in recent_games:
        if game['result'] == 'W':
            trends['last_n']['wins'] += 1
        else:
            trends['last_n']['losses'] += 1
    
    recent_total = trends['last_n']['wins'] + trends['last_n']['losses']
    if recent_total > 0:
        trends['last_n']['win_pct'] = trends['last_n']['wins'] / recent_total
        trends['last_n']['n'] = recent_total
    
    # Scoring trends
    points_for = []
    points_against = []
    for game in completed_games:
        if game['score'] is not None and game['opponent_score'] is not None:
            points_for.append(game['score'])
            points_against.append(game['opponent_score'])
    
    if points_for:
        trends['scoring']['avg_points_for'] = statistics.mean(points_for)
        trends['scoring']['avg_points_against'] = statistics.mean(points_against)
        trends['scoring']['avg_margin'] = trends['scoring']['avg_points_for'] - trends['scoring']['avg_points_against']
        
        # Last N games scoring
        recent_for = points_for[-window_size:] if len(points_for) >= window_size else points_for
        recent_against = points_against[-window_size:] if len(points_against) >= window_size else points_against
        trends['scoring']['last_n_avg_for'] = statistics.mean(recent_for)
        trends['scoring']['last_n_avg_against'] = statistics.mean(recent_against)
    
    # Form (last 5 games)
    form_games = completed_games[-5:] if len(completed_games) >= 5 else completed_games
    trends['form'] = [g['result'] for g in reversed(form_games)]  # Most recent first
    
    # Streaks
    if completed_games:
        current_streak_type = completed_games[-1]['result']
        current_streak_length = 1
        
        for i in range(len(completed_games) - 2, -1, -1):
            if completed_games[i]['result'] == current_streak_type:
                current_streak_length += 1
            else:
                break
        
        trends['streaks']['current'] = {
            'type': current_streak_type,
            'length': current_streak_length
        }
        
        # Longest streaks
        win_streak = 0
        loss_streak = 0
        current_win = 0
        current_loss = 0
        
        for game in completed_games:
            if game['result'] == 'W':
                current_win += 1
                current_loss = 0
                win_streak = max(win_streak, current_win)
            else:
                current_loss += 1
                current_win = 0
                loss_streak = max(loss_streak, current_loss)
        
        trends['streaks']['longest_win'] = win_streak
        trends['streaks']['longest_loss'] = loss_streak
    
    return trends

def display_console_output(team_data: Dict[str, Dict], league_name: str) -> None:
    """Display formatted console output."""
    print(f"\n{league_name} Team Performance Trends")
    print("=" * 80)
    
    for team_id, data in team_data.items():
        team_info = data['team_info']
        trends = data['trends']
        record = data['record']
        
        print(f"\n{team_info['display_name']} ({team_info['abbreviation']})")
        print("-" * 60)
        
        # Overall Record
        overall = trends['overall']
        print(f"\nOverall Record: {overall['wins']}-{overall['losses']} ({overall['win_pct']:.3f})")
        
        if record and (record['division']['wins'] > 0 or record['division']['losses'] > 0):
            print(f"Division: {record['division']['wins']}-{record['division']['losses']}")
        if record and (record['conference']['wins'] > 0 or record['conference']['losses'] > 0):
            print(f"Conference: {record['conference']['wins']}-{record['conference']['losses']}")
        
        # Home/Away Splits
        print(f"\nHome: {trends['home']['wins']}-{trends['home']['losses']} ({trends['home']['win_pct']:.3f})")
        print(f"Away: {trends['away']['wins']}-{trends['away']['losses']} ({trends['away']['win_pct']:.3f})")
        
        # Recent Form
        last_n = trends['last_n']
        print(f"\nLast {last_n['n']} Games: {last_n['wins']}-{last_n['losses']} ({last_n['win_pct']:.3f})")
        print(f"Form (Last 5): {' '.join(trends['form'])}")
        
        # Current Streak
        streak = trends['streaks']['current']
        if streak['type']:
            streak_text = f"{streak['length']}{streak['type']}"
            print(f"Current Streak: {streak_text}")
        
        # Scoring Trends
        scoring = trends['scoring']
        if scoring['avg_points_for'] > 0:
            print(f"\nScoring Averages:")
            print(f"  Points For: {scoring['avg_points_for']:.1f} (Last {last_n['n']}: {scoring['last_n_avg_for']:.1f})")
            print(f"  Points Against: {scoring['avg_points_against']:.1f} (Last {last_n['n']}: {scoring['last_n_avg_against']:.1f})")
            print(f"  Average Margin: {scoring['avg_margin']:+.1f}")
            
            # Trend indicators
            scoring_trend = "📈" if scoring['last_n_avg_for'] > scoring['avg_points_for'] else "📉"
            defense_trend = "📈" if scoring['last_n_avg_against'] < scoring['avg_points_against'] else "📉"
            print(f"  Offensive Trend: {scoring_trend}")
            print(f"  Defensive Trend: {defense_trend}")

def generate_trend_chart(values: List[float], width: int = 20, height: int = 5) -> List[str]:
    """Generate a simple ASCII trend chart."""
    if not values or len(values) < 2:
        return []
    
    # Normalize values to fit in the height
    min_val = min(values)
    max_val = max(values)
    range_val = max_val - min_val if max_val != min_val else 1
    
    # Create chart
    chart = []
    for h in range(height, 0, -1):
        line = ""
        for i, val in enumerate(values[-width:] if len(values) > width else values):
            normalized = (val - min_val) / range_val
            if normalized * height >= h - 0.5:
                line += "█"
            else:
                line += " "
        chart.append(line)
    
    return chart

def save_json_output(data: Dict, filename: str) -> None:
    """Save data as JSON."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, default=str)
    print(f"\nData saved to {filename}")

def save_csv_output(team_data: Dict[str, Dict], filename: str, league: str) -> None:
    """Save data as CSV."""
    import csv
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        headers = [
            'League', 'Team', 'Abbreviation', 
            'Overall W', 'Overall L', 'Win %',
            'Home W', 'Home L', 'Away W', 'Away L',
            'Last 10 W', 'Last 10 L', 'Current Streak',
            'Avg PF', 'Avg PA', 'Avg Margin',
            'Last 10 PF', 'Last 10 PA'
        ]
        writer.writerow(headers)
        
        for team_id, data in team_data.items():
            team_info = data['team_info']
            trends = data['trends']
            
            streak = trends['streaks']['current']
            streak_text = f"{streak['length']}{streak['type']}" if streak['type'] else "0"
            
            writer.writerow([
                league.upper(),
                team_info['display_name'],
                team_info['abbreviation'],
                trends['overall']['wins'],
                trends['overall']['losses'],
                f"{trends['overall']['win_pct']:.3f}",
                trends['home']['wins'],
                trends['home']['losses'],
                trends['away']['wins'],
                trends['away']['losses'],
                trends['last_n']['wins'],
                trends['last_n']['losses'],
                streak_text,
                f"{trends['scoring']['avg_points_for']:.1f}",
                f"{trends['scoring']['avg_points_against']:.1f}",
                f"{trends['scoring']['avg_margin']:+.1f}",
                f"{trends['scoring']['last_n_avg_for']:.1f}",
                f"{trends['scoring']['last_n_avg_against']:.1f}"
            ])
    
    print(f"\nData saved to {filename}")

async def process_teams_async(teams: List[str], sport: str, league: str, 
                            site_client: SiteApiClient, core_client: SportsCoreApiClient,
                            season: Optional[int] = None, last_n: int = 10) -> Dict[str, Dict]:
    """Process multiple teams asynchronously."""
    results = {}
    
    # Get team list to validate and get IDs
    all_teams = get_team_list(site_client, sport, league)
    team_map = {}
    for team in all_teams:
        if team['abbreviation']:
            team_map[team['abbreviation'].upper()] = team
            team_map[str(team['id'])] = team
    
    # Process each requested team
    for team_input in teams:
        team_upper = team_input.upper()
        if team_upper in team_map or team_input in team_map:
            team_info = team_map.get(team_upper, team_map.get(team_input))
            team_id = team_info['id']
            
            print(f"Processing {team_info['display_name']}...")
            
            # Fetch schedule
            schedule = fetch_team_schedule(site_client, sport, league, team_id, season)
            
            # Fetch record
            current_year = season or datetime.now().year
            record = fetch_team_record(core_client, sport, league, team_id, current_year)
            
            # Calculate trends
            trends = calculate_trends(schedule, last_n)
            
            results[team_id] = {
                'team_info': team_info,
                'schedule': schedule,
                'record': record,
                'trends': trends
            }
        else:
            print(f"Warning: Team '{team_input}' not found in {league.upper()}")
    
    return results

def main():
    parser = argparse.ArgumentParser(
        description='Analyze team performance trends over time across ESPN\'s supported sports.'
    )
    
    # Required arguments
    parser.add_argument('teams', nargs='+', help='Team abbreviations or IDs to analyze')
    
    # Optional arguments
    parser.add_argument('--league', choices=list(SUPPORTED_LEAGUES.keys()),
                       required=True, help='League to analyze')
    parser.add_argument('--season', type=int, help='Season year (default: current season)')
    parser.add_argument('--last-n', type=int, default=10,
                       help='Number of recent games for trend analysis (default: 10)')
    parser.add_argument('--output', choices=['console', 'json', 'csv'],
                       default='console', help='Output format (default: console)')
    parser.add_argument('--save', help='Save output to file')
    parser.add_argument('--compare', action='store_true',
                       help='Compare multiple teams side by side')
    
    args = parser.parse_args()
    
    # Create clients
    site_client = create_site_client()
    core_client = create_core_client()
    
    # Get league info
    sport, league, display_name = SUPPORTED_LEAGUES[args.league]
    
    print(f"Analyzing {display_name} team performance trends...")
    
    # Process teams
    team_data = asyncio.run(
        process_teams_async(
            args.teams, sport, league, site_client, core_client,
            args.season, args.last_n
        )
    )
    
    if not team_data:
        print("No valid teams found to analyze.")
        sys.exit(1)
    
    # Output results
    if args.output == 'console':
        if args.compare and len(team_data) > 1:
            # Side-by-side comparison
            print(f"\n{display_name} Team Comparison")
            print("=" * 80)
            
            # Create comparison table
            print(f"\n{'Metric':<20}", end='')
            for data in team_data.values():
                print(f"{data['team_info']['abbreviation']:>12}", end='')
            print()
            print("-" * (20 + 12 * len(team_data)))
            
            # Overall record
            print(f"{'Overall Record':<20}", end='')
            for data in team_data.values():
                trends = data['trends']
                record_str = f"{trends['overall']['wins']}-{trends['overall']['losses']}"
                print(f"{record_str:>12}", end='')
            print()
            
            # Win percentage
            print(f"{'Win %':<20}", end='')
            for data in team_data.values():
                win_pct = f"{data['trends']['overall']['win_pct']:.3f}"
                print(f"{win_pct:>12}", end='')
            print()
            
            # Last N games
            print(f"{f'Last {args.last_n} Games':<20}", end='')
            for data in team_data.values():
                last_n = data['trends']['last_n']
                record_str = f"{last_n['wins']}-{last_n['losses']}"
                print(f"{record_str:>12}", end='')
            print()
            
            # Points per game
            print(f"{'PPG':<20}", end='')
            for data in team_data.values():
                ppg = f"{data['trends']['scoring']['avg_points_for']:.1f}"
                print(f"{ppg:>12}", end='')
            print()
            
            # Points against
            print(f"{'Opp PPG':<20}", end='')
            for data in team_data.values():
                papg = f"{data['trends']['scoring']['avg_points_against']:.1f}"
                print(f"{papg:>12}", end='')
            print()
            
            # Current streak
            print(f"{'Current Streak':<20}", end='')
            for data in team_data.values():
                streak = data['trends']['streaks']['current']
                streak_str = f"{streak['length']}{streak['type']}" if streak['type'] else "0"
                print(f"{streak_str:>12}", end='')
            print()
            
        else:
            display_console_output(team_data, display_name)
    
    elif args.output == 'json':
        # Prepare JSON output
        json_output = {
            'league': args.league,
            'season': args.season or datetime.now().year,
            'analysis_date': datetime.now().isoformat(),
            'teams': {}
        }
        
        for team_id, data in team_data.items():
            json_output['teams'][data['team_info']['abbreviation']] = {
                'info': data['team_info'],
                'trends': data['trends'],
                'record': data['record']
            }
        
        if args.save:
            save_json_output(json_output, args.save)
        else:
            print(json.dumps(json_output, indent=2, default=str))
    
    elif args.output == 'csv':
        if not args.save:
            print("CSV output requires --save parameter")
            sys.exit(1)
        
        save_csv_output(team_data, args.save, args.league)

if __name__ == '__main__':
    main()