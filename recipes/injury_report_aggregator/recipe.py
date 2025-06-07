#!/usr/bin/env python3
"""
Injury Report Aggregator - Compile injury reports across teams and leagues.

This recipe demonstrates how to fetch and aggregate injury reports from multiple
teams across different sports leagues using the ESPN API.
"""

import argparse
import json
import sys
import asyncio
from datetime import datetime
from typing import Dict, List, Optional, Set
from collections import defaultdict
import httpx

# Import generated models
from models.site_api.espn_nfl_api_client import Client as SiteApiClient
from models.site_api.espn_nfl_api_client.api.default import get_teams_list
from models.sports_core_api.espn_sports_core_api_client import Client as SportsCoreApiClient
from models.sports_core_api.espn_sports_core_api_client.api.default import get_team_injuries, get_athlete_details
from models.sports_core_api.espn_sports_core_api_client.models.paginated_reference_list_response import PaginatedReferenceListResponse
from models.sports_core_api.espn_sports_core_api_client.types import UNSET


# Supported sports and leagues
SUPPORTED_LEAGUES = {
    "nfl": ("football", "nfl", "NFL"),
    "nba": ("basketball", "nba", "NBA"),
    "mlb": ("baseball", "mlb", "MLB"),
    "nhl": ("hockey", "nhl", "NHL")
}


def create_site_client() -> SiteApiClient:
    """Create and return an ESPN Site API client."""
    return SiteApiClient(base_url="https://site.api.espn.com/apis/site/v2")


def create_core_client() -> SportsCoreApiClient:
    """Create and return an ESPN Sports Core API client."""
    return SportsCoreApiClient(base_url="https://sports.core.api.espn.com")


def get_league_teams(client: SiteApiClient, sport: str, league: str) -> List[Dict]:
    """
    Get all teams for a specific sport and league.
    
    Returns list of team dictionaries with id, name, and abbreviation.
    """
    try:
        response = get_teams_list.sync_detailed(
            client=client,
            sport=sport,
            league=league
        )
        
        if response.status_code == 200 and response.parsed:
            teams = []
            if hasattr(response.parsed, 'sports') and response.parsed.sports:
                for sport_obj in response.parsed.sports:
                    if hasattr(sport_obj, 'leagues') and sport_obj.leagues:
                        for league_obj in sport_obj.leagues:
                            if hasattr(league_obj, 'teams') and league_obj.teams:
                                for team in league_obj.teams:
                                    if hasattr(team, 'team') and team.team:
                                        teams.append({
                                            'id': team.team.id,
                                            'name': team.team.display_name,
                                            'abbreviation': team.team.abbreviation,
                                            'location': getattr(team.team, 'location', ''),
                                            'nickname': getattr(team.team, 'name', '')
                                        })
            return teams
        else:
            print(f"Error fetching {sport}/{league} teams: HTTP {response.status_code}")
            return []
            
    except Exception as e:
        print(f"Error fetching {sport}/{league} teams: {e}")
        return []


async def fetch_injury_details_async(session: httpx.AsyncClient, injury_url: str, core_client: SportsCoreApiClient, sport: str, league: str) -> Optional[Dict]:
    """
    Fetch individual injury details from the API reference URL asynchronously.
    
    Returns injury dictionary or None if error.
    """
    try:
        response = await session.get(injury_url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Extract relevant injury information
            injury_info = {
                'athlete_id': '',
                'athlete_name': 'Unknown',
                'position': 'Unknown',
                'jersey': '',
                'status': 'Unknown',
                'date': '',
                'type': '',
                'details': '',
                'side': '',
                'body_part': ''
            }
            
            # Parse athlete information
            if 'athlete' in data and data['athlete']:
                athlete = data['athlete']
                # Check if athlete is a reference
                if '$ref' in athlete and len(athlete) == 1:
                    # Extract athlete ID from the URL
                    # URL format: .../athletes/{athlete_id}/injuries/...
                    try:
                        import re
                        match = re.search(r'/athletes/(\d+)', athlete['$ref'])
                        if match:
                            athlete_id = match.group(1)
                            injury_info['athlete_id'] = athlete_id
                            
                            # Use the proper API to fetch athlete details
                            athlete_response = await asyncio.to_thread(
                                get_athlete_details.sync_detailed,
                                client=core_client,
                                sport=sport,
                                league=league,
                                athlete_id=athlete_id
                            )
                            
                            if athlete_response.status_code == 200 and athlete_response.parsed:
                                athlete_data = athlete_response.parsed
                                if athlete_data.display_name:
                                    injury_info['athlete_name'] = athlete_data.display_name
                                if athlete_data.jersey:
                                    injury_info['jersey'] = str(athlete_data.jersey)
                                if athlete_data.position and athlete_data.position.abbreviation:
                                    injury_info['position'] = athlete_data.position.abbreviation
                    except Exception as e:
                        # Fall back to basic info
                        pass
                else:
                    # Direct athlete data
                    injury_info['athlete_id'] = str(athlete.get('id', ''))
                    injury_info['athlete_name'] = athlete.get('displayName', 'Unknown')
                    injury_info['jersey'] = str(athlete.get('jersey', ''))
                    
                    if 'position' in athlete and athlete['position']:
                        injury_info['position'] = athlete['position'].get('abbreviation', 'Unknown')
            
            # Parse injury details
            injury_info['status'] = format_injury_status(data.get('status', 'unknown'))
            injury_info['date'] = data.get('date', '')
            
            if 'type' in data and data['type']:
                injury_info['type'] = data['type'].get('text', data['type'].get('description', ''))
            
            # Get injury description from comments
            if 'longComment' in data:
                injury_info['details'] = data['longComment']
            elif 'shortComment' in data:
                injury_info['details'] = data['shortComment']
            
            if 'details' in data and data['details']:
                details = data['details']
                if not injury_info['details']:
                    injury_info['details'] = details.get('detail', '')
                injury_info['side'] = details.get('side', '')
                injury_info['body_part'] = details.get('location', '')
            
            return injury_info
        else:
            return None
            
    except Exception as e:
        return None


async def get_team_injuries_async(core_client: SportsCoreApiClient, sport: str, league: str, team: Dict) -> List[Dict]:
    """
    Get injury report for a specific team asynchronously.
    
    Returns list of injury dictionaries.
    """
    try:
        response = get_team_injuries.sync_detailed(
            client=core_client,
            sport=sport,
            league=league,
            team_id=str(team['id']),
            limit=100
        )
        
        if response.status_code == 200 and response.parsed:
            injuries = []
            if hasattr(response.parsed, 'items') and response.parsed.items:
                # Collect all injury URLs
                injury_urls = []
                for injury_ref in response.parsed.items:
                    if hasattr(injury_ref, 'ref') and injury_ref.ref:
                        injury_urls.append(injury_ref.ref)
                
                # Fetch all injury details in parallel
                if injury_urls:
                    async with httpx.AsyncClient(timeout=30.0) as session:
                        tasks = [fetch_injury_details_async(session, url, core_client, sport, league) for url in injury_urls]
                        injury_results = await asyncio.gather(*tasks)
                        
                        for injury_data in injury_results:
                            if injury_data:
                                injury_data['team_name'] = team['name']
                                injury_data['team_id'] = team['id']
                                injuries.append(injury_data)
            
            return injuries
        elif response.status_code == 404:
            # No injuries for this team
            return []
        else:
            # Don't print error for 404s
            return []
            
    except Exception as e:
        # Silently handle errors - teams often don't have injury data
        return []


def format_injury_status(status: str) -> str:
    """Format injury status for display."""
    status_map = {
        "out": "OUT",
        "doubtful": "DOUBTFUL",
        "questionable": "QUESTIONABLE",
        "probable": "PROBABLE",
        "day-to-day": "DAY-TO-DAY",
        "injured-reserve": "IR",
        "physically-unable": "PUP",
        "suspended": "SUSPENDED"
    }
    
    return status_map.get(status.lower(), status.upper())


async def aggregate_injuries_async(site_client: SiteApiClient, core_client: SportsCoreApiClient, leagues: List[str]) -> Dict[str, List[Dict]]:
    """
    Aggregate injury reports across specified leagues using parallel processing.
    
    Returns dictionary mapping league to list of injuries.
    """
    all_injuries = {}
    
    for league in leagues:
        if league not in SUPPORTED_LEAGUES:
            continue
            
        sport, league_key, display_name = SUPPORTED_LEAGUES[league]
        print(f"\nFetching {display_name} injuries...")
        
        # Get all teams for the league
        teams = get_league_teams(site_client, sport, league_key)
        print(f"Found {len(teams)} teams")
        
        if not teams:
            continue
        
        league_injuries = []
        
        # Process teams in batches to avoid overwhelming the API
        batch_size = 10
        for i in range(0, len(teams), batch_size):
            batch = teams[i:i+batch_size]
            print(f"Processing teams {i+1}-{min(i+batch_size, len(teams))}...")
            
            # Get injuries for each team in the batch
            tasks = []
            for team in batch:
                task = get_team_injuries_async(core_client, sport, league_key, team)
                tasks.append(task)
            
            # Wait for all tasks in this batch to complete
            batch_results = await asyncio.gather(*tasks)
            
            # Combine results
            for injuries in batch_results:
                league_injuries.extend(injuries)
        
        all_injuries[league] = league_injuries
        
        # Summary
        teams_with_injuries = len([1 for team in teams if any(
            injury['team_id'] == team['id'] for injury in league_injuries
        )])
        print(f"{teams_with_injuries} teams with injuries, {len(league_injuries)} total injuries in {display_name}")
    
    return all_injuries


def aggregate_injuries(site_client: SiteApiClient, core_client: SportsCoreApiClient, leagues: List[str]) -> Dict[str, List[Dict]]:
    """
    Wrapper to run async aggregation synchronously.
    """
    return asyncio.run(aggregate_injuries_async(site_client, core_client, leagues))


def filter_by_severity(injuries: Dict[str, List[Dict]], severities: List[str]) -> Dict[str, List[Dict]]:
    """
    Filter injuries by severity/status.
    
    Returns filtered dictionary of injuries.
    """
    if not severities:
        return injuries
        
    filtered = {}
    for league, league_injuries in injuries.items():
        filtered[league] = [
            injury for injury in league_injuries
            if injury.get('status', '').upper() in severities
        ]
    
    return filtered


def display_console_output(injuries: Dict[str, List[Dict]]) -> None:
    """Display injuries in a formatted console output."""
    total_injuries = sum(len(league_injuries) for league_injuries in injuries.values())
    
    if total_injuries == 0:
        print("\nNo injuries found across any leagues.")
        print("This may be due to:")
        print("- Off-season periods when injury data is limited")
        print("- API data availability")
        return
    
    print(f"\n{'='*80}")
    print(f"INJURY REPORT SUMMARY - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*80}")
    
    for league, league_injuries in injuries.items():
        if not league_injuries:
            continue
            
        sport, league_key, display_name = SUPPORTED_LEAGUES[league]
        print(f"\n{display_name} INJURIES ({len(league_injuries)} total)")
        print("-" * 40)
        
        # Group by team
        teams = defaultdict(list)
        for injury in league_injuries:
            teams[injury.get('team_name', 'Unknown')].append(injury)
        
        # Display by team
        for team_name in sorted(teams.keys()):
            team_injuries = teams[team_name]
            print(f"\n{team_name} ({len(team_injuries)} injuries):")
            
            for injury in sorted(team_injuries, key=lambda x: x.get('status', '')):
                status = injury.get('status', 'UNKNOWN')
                name = injury.get('athlete_name', 'Unknown')
                position = injury.get('position', 'Unknown')
                jersey = injury.get('jersey', '')
                injury_type = injury.get('type', '')
                body_part = injury.get('body_part', '')
                side = injury.get('side', '')
                details = injury.get('details', '')
                
                # Format injury description
                injury_desc = []
                if body_part:
                    if side:
                        injury_desc.append(f"{side} {body_part}")
                    else:
                        injury_desc.append(body_part)
                if injury_type:
                    injury_desc.append(f"({injury_type})")
                if details:
                    injury_desc.append(f"- {details}")
                
                injury_str = " ".join(injury_desc) if injury_desc else "No details"
                
                # Display formatted injury
                jersey_str = f"#{jersey}" if jersey else ""
                print(f"  [{status:12}] {name:20} {jersey_str:4} {position:3} - {injury_str}")


def save_json_output(injuries: Dict[str, List[Dict]], filename: str) -> None:
    """Save injuries to JSON file."""
    output = {
        'generated_at': datetime.now().isoformat(),
        'total_injuries': sum(len(league_injuries) for league_injuries in injuries.values()),
        'injuries_by_league': injuries
    }
    
    with open(filename, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\nSaved JSON output to: {filename}")


def save_csv_output(injuries: Dict[str, List[Dict]], filename: str) -> None:
    """Save injuries to CSV file."""
    import csv
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow([
            'League', 'Team', 'Player', 'Jersey', 'Position', 
            'Status', 'Injury Type', 'Body Part', 'Side', 'Details', 'Date'
        ])
        
        # Data rows
        for league, league_injuries in injuries.items():
            sport, league_key, display_name = SUPPORTED_LEAGUES[league]
            
            for injury in league_injuries:
                writer.writerow([
                    display_name,
                    injury.get('team_name', ''),
                    injury.get('athlete_name', ''),
                    injury.get('jersey', ''),
                    injury.get('position', ''),
                    injury.get('status', ''),
                    injury.get('type', ''),
                    injury.get('body_part', ''),
                    injury.get('side', ''),
                    injury.get('details', ''),
                    injury.get('date', '')
                ])
    
    print(f"\nSaved CSV output to: {filename}")


def main():
    parser = argparse.ArgumentParser(
        description='Aggregate injury reports across NFL, NBA, MLB, and NHL teams'
    )
    
    parser.add_argument(
        '--leagues',
        nargs='+',
        choices=list(SUPPORTED_LEAGUES.keys()),
        default=list(SUPPORTED_LEAGUES.keys()),
        help='Leagues to include (default: all)'
    )
    
    parser.add_argument(
        '--severity',
        nargs='+',
        choices=['OUT', 'DOUBTFUL', 'QUESTIONABLE', 'PROBABLE', 'DAY-TO-DAY', 'IR', 'PUP'],
        help='Filter by injury severity/status'
    )
    
    parser.add_argument(
        '--output',
        choices=['console', 'json', 'csv'],
        default='console',
        help='Output format (default: console)'
    )
    
    parser.add_argument(
        '--save',
        help='Save output to file'
    )
    
    args = parser.parse_args()
    
    # Create API clients
    site_client = create_site_client()
    core_client = create_core_client()
    
    # Aggregate injuries
    print("Aggregating injury reports...")
    all_injuries = aggregate_injuries(site_client, core_client, args.leagues)
    
    # Filter by severity if requested
    if args.severity:
        all_injuries = filter_by_severity(all_injuries, args.severity)
    
    # Output results
    if args.output == 'console':
        display_console_output(all_injuries)
    elif args.output == 'json':
        if args.save:
            save_json_output(all_injuries, args.save)
        else:
            print(json.dumps(all_injuries, indent=2))
    elif args.output == 'csv':
        if args.save:
            save_csv_output(all_injuries, args.save)
        else:
            print("CSV output requires --save filename")
            sys.exit(1)


if __name__ == '__main__':
    main()