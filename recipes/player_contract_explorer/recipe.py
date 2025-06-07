#!/usr/bin/env python3
"""
Player Contract Explorer - Search and analyze player contracts across ESPN's supported sports.

This recipe allows users to explore player contract information including salary details,
contract length, and key terms for athletes across NFL, NBA, MLB, and NHL.
"""

import argparse
import json
import sys
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import asyncio
import httpx
from collections import defaultdict

# Import API clients and models
from models.sports_core_api.espn_sports_core_api_client import Client as SportsCoreApiClient
from models.sports_core_api.espn_sports_core_api_client.api.default import get_athlete_contracts
from models.sports_core_api.espn_sports_core_api_client.types import UNSET
from models.site_web_api.espn_site_web_api_client import Client as SiteWebApiClient
from models.site_web_api.espn_site_web_api_client.api.default import get_general_search_v2

# Supported leagues with their sport mappings
SUPPORTED_LEAGUES = {
    "nfl": ("football", "nfl", "NFL"),
    "nba": ("basketball", "nba", "NBA"),
    "mlb": ("baseball", "mlb", "MLB"),
    "nhl": ("hockey", "nhl", "NHL")
}

def create_core_client() -> SportsCoreApiClient:
    """Create and return Sports Core API client."""
    return SportsCoreApiClient(base_url="https://sports.core.api.espn.com/v2")

def create_web_client() -> SiteWebApiClient:
    """Create and return Site Web API client."""
    return SiteWebApiClient(base_url="https://site.web.api.espn.com")

def format_currency(amount: float) -> str:
    """Format currency values with proper formatting."""
    if amount >= 1_000_000:
        return f"${amount/1_000_000:.1f}M"
    elif amount >= 1_000:
        return f"${amount/1_000:.0f}K"
    else:
        return f"${amount:.0f}"

def search_athletes(web_client: SiteWebApiClient, sport: str, league: str, query: str, limit: int = 50) -> List[Dict]:
    """Search for athletes by name using the search API."""
    try:
        # Use search v2 API
        response = get_general_search_v2.sync_detailed(
            client=web_client,
            query=query,
            limit=limit
        )
        
        if response.status_code != 200:
            print(f"Search API returned status code: {response.status_code}")
            return []
        
        if not response.parsed:
            print("No search results found")
            return []
        
        athletes = []
        
        # Look for player results
        if hasattr(response.parsed, 'results') and response.parsed.results:
            for result_type in response.parsed.results:
                if hasattr(result_type, 'type') and result_type.type == 'player':
                    if hasattr(result_type, 'contents') and result_type.contents:
                        for player in result_type.contents:
                            # Filter by sport/league
                            if hasattr(player, 'sport') and hasattr(player, 'default_league_slug'):
                                # Check if this player is from the requested league
                                if player.sport == sport and player.default_league_slug == league:
                                    # Extract athlete ID from UID
                                    athlete_id = None
                                    if hasattr(player, 'uid') and player.uid:
                                        # UID format: "s:20~l:28~a:2330"
                                        parts = player.uid.split('~')
                                        for part in parts:
                                            if part.startswith('a:'):
                                                athlete_id = part[2:]
                                                break
                                    
                                    if athlete_id:
                                        athlete_dict = {
                                            'id': athlete_id,
                                            'name': player.display_name if hasattr(player, 'display_name') else '',
                                            'position': None,
                                            'team': None
                                        }
                                        
                                        # Extract team from subtitle
                                        if hasattr(player, 'subtitle') and player.subtitle:
                                            athlete_dict['team'] = player.subtitle
                                        
                                        athletes.append(athlete_dict)
        
        return athletes[:limit]
        
    except Exception as e:
        print(f"Error searching athletes: {e}")
        return []

def fetch_contract_data(client: SportsCoreApiClient, sport: str, league: str, athlete_id: str) -> Optional[Dict]:
    """Fetch contract data for a specific athlete."""
    try:
        response = get_athlete_contracts.sync_detailed(
            client=client,
            sport=sport,
            league=league,
            athlete_id=athlete_id
        )
        
        if response.status_code == 200 and response.parsed:
            return process_contract_response(response.parsed)
        
        return None
        
    except Exception:
        return None

def process_contract_response(contract_data) -> Dict:
    """Process contract response data into a standardized format."""
    result = {
        'contracts': [],
        'total_value': 0,
        'average_annual': 0,
        'years_remaining': 0
    }
    
    if hasattr(contract_data, 'items') and contract_data.items:
        for contract in contract_data.items:
            contract_info = {}
            
            # Extract year
            if hasattr(contract, 'year') and contract.year is not UNSET:
                contract_info['year'] = contract.year
            
            # Extract salary info
            if hasattr(contract, 'salary') and contract.salary is not UNSET:
                contract_info['salary'] = contract.salary
                result['total_value'] += contract.salary
            
            # Extract bonus info
            if hasattr(contract, 'bonus') and contract.bonus is not UNSET:
                contract_info['bonus'] = contract.bonus
                result['total_value'] += contract.bonus
            
            # Calculate total for year
            year_total = contract_info.get('salary', 0) + contract_info.get('bonus', 0)
            contract_info['total'] = year_total
            
            result['contracts'].append(contract_info)
    
    # Calculate averages and years
    if result['contracts']:
        result['years_remaining'] = len(result['contracts'])
        result['average_annual'] = result['total_value'] / result['years_remaining'] if result['years_remaining'] > 0 else 0
    
    return result

async def fetch_contract_async(session: httpx.AsyncClient, base_url: str, sport: str, league: str, athlete_id: str) -> Tuple[str, Optional[Dict]]:
    """Fetch contract data asynchronously."""
    url = f"{base_url}/sports/{sport}/leagues/{league}/athletes/{athlete_id}/contracts"
    
    try:
        response = await session.get(url, timeout=30.0)
        if response.status_code == 200:
            data = response.json()
            result = process_raw_contract_data(data)
            
            # For NBA, fetch detailed year data if we only have references
            if league == 'nba' and result.get('has_data') and result.get('contracts'):
                # Check if we need to fetch individual years
                if all(c.get('total', 0) == 0 for c in result['contracts']):
                    # Fetch ALL available years
                    years_to_fetch = [c['year'] for c in result['contracts']]
                    total_value = 0
                    years_with_data = 0
                    
                    # Fetch in batches to avoid overwhelming the API
                    batch_size = 5
                    for i in range(0, len(years_to_fetch), batch_size):
                        batch = years_to_fetch[i:i+batch_size]
                        
                        # Fetch years in parallel within the batch
                        year_tasks = []
                        for year in batch:
                            year_url = f"{url}/{year}"
                            year_tasks.append(session.get(year_url, timeout=10.0))
                        
                        # Gather results
                        import asyncio as aio
                        year_responses = await aio.gather(*year_tasks, return_exceptions=True)
                        
                        # Process responses
                        for idx, year_response in enumerate(year_responses):
                            if not isinstance(year_response, Exception) and year_response.status_code == 200:
                                year = batch[idx]
                                year_data = year_response.json()
                                
                                # Update the contract for this year
                                for c in result['contracts']:
                                    if c['year'] == year:
                                        salary = year_data.get('salary', 0)
                                        bonus = year_data.get('bonus', 0)
                                        c['salary'] = salary
                                        c['bonus'] = bonus
                                        c['total'] = salary + bonus
                                        
                                        # Additional contract details if available
                                        if 'optionType' in year_data:
                                            c['option_type'] = year_data['optionType']
                                        if 'team' in year_data and '$ref' in year_data['team']:
                                            # Extract team ID from ref and map to abbreviation
                                            import re
                                            team_match = re.search(r'/teams/(\d+)', year_data['team']['$ref'])
                                            if team_match:
                                                team_id = team_match.group(1)
                                                # Common NBA team ID mappings
                                                team_map = {
                                                    '13': 'LAL', '5': 'CLE', '14': 'MIA',
                                                    '17': 'MIL', '21': 'PHI', '1': 'ATL',
                                                    '2': 'BOS', '3': 'NO', '4': 'CHI',
                                                    '6': 'DAL', '7': 'DEN', '8': 'DET',
                                                    '9': 'GSW', '10': 'HOU', '11': 'IND',
                                                    '12': 'LAC', '15': 'MEM', '16': 'MIL',
                                                    '18': 'MIN', '19': 'BKN', '20': 'NYK',
                                                    '22': 'PHX', '23': 'POR', '24': 'SAS',
                                                    '25': 'OKC', '26': 'UTA', '27': 'TOR',
                                                    '28': 'WAS', '29': 'CHA', '30': 'SAC'
                                                }
                                                c['team'] = team_map.get(team_id, team_id)
                                        
                                        total_value += c['total']
                                        years_with_data += 1
                                        break
                    
                    # Update totals
                    result['total_value'] = total_value
                    result['years_with_data'] = years_with_data
                    if years_with_data > 0:
                        result['average_annual'] = total_value / years_with_data
            
            return (athlete_id, result)
        return (athlete_id, None)
    except Exception:
        return (athlete_id, None)

def process_raw_contract_data(data: Dict) -> Dict:
    """Process raw contract JSON data."""
    result = {
        'contracts': [],
        'total_value': 0,
        'average_annual': 0,
        'years_remaining': 0,
        'has_data': False
    }
    
    # Check if we have contract items
    if 'items' in data and data['items']:
        result['has_data'] = True
        
        # For contract lists, we need to fetch individual year data
        # For now, we'll just count the years
        for item in data['items']:
            if '$ref' in item:
                # Extract year from the reference URL if possible
                import re
                year_match = re.search(r'/(\d{4})(?:\?|$)', item['$ref'])
                if year_match:
                    year = int(year_match.group(1))
                    contract_info = {
                        'year': year,
                        'salary': 0,  # Would need to fetch individual year data
                        'bonus': 0,
                        'total': 0,
                        'ref': item['$ref']
                    }
                    result['contracts'].append(contract_info)
        
        # Sort by year
        result['contracts'].sort(key=lambda x: x['year'])
        result['years_remaining'] = len(result['contracts'])
    
    elif 'salary' in data:
        # Single year contract data
        result['has_data'] = True
        salary = data.get('salary', 0)
        year = None
        
        # Try to extract year from season ref
        if 'season' in data and '$ref' in data['season']:
            import re
            year_match = re.search(r'/(\d{4})(?:\?|$)', data['season']['$ref'])
            if year_match:
                year = int(year_match.group(1))
        
        contract_info = {
            'year': year or datetime.now().year,
            'salary': salary,
            'bonus': 0,
            'total': salary
        }
        
        result['contracts'].append(contract_info)
        result['total_value'] = salary
        result['average_annual'] = salary
        result['years_remaining'] = data.get('yearsRemaining', 1)
    
    return result

async def fetch_multiple_contracts_async(athletes: List[Dict], sport: str, league: str, fetch_all_years: bool = True) -> Dict[str, Dict]:
    """Fetch contracts for multiple athletes asynchronously."""
    base_url = "https://sports.core.api.espn.com/v2"
    results = {}
    
    async with httpx.AsyncClient(timeout=30.0) as session:
        tasks = []
        for athlete in athletes:
            if athlete.get('id'):
                tasks.append(fetch_contract_async_with_option(session, base_url, sport, league, str(athlete['id']), fetch_all_years))
        
        # Process in batches
        batch_size = 10
        for i in range(0, len(tasks), batch_size):
            batch = tasks[i:i+batch_size]
            batch_results = await asyncio.gather(*batch)
            
            for athlete_id, contract_data in batch_results:
                if contract_data:
                    results[athlete_id] = contract_data
    
    return results

async def fetch_contract_async_with_option(session: httpx.AsyncClient, base_url: str, sport: str, league: str, athlete_id: str, fetch_all_years: bool) -> Tuple[str, Optional[Dict]]:
    """Wrapper to pass fetch_all_years option."""
    if fetch_all_years and league == 'nba':
        return await fetch_contract_async(session, base_url, sport, league, athlete_id)
    else:
        # Just fetch the contract list without individual years
        url = f"{base_url}/sports/{sport}/leagues/{league}/athletes/{athlete_id}/contracts"
        try:
            response = await session.get(url, timeout=30.0)
            if response.status_code == 200:
                data = response.json()
                return (athlete_id, process_raw_contract_data(data))
        except:
            pass
        return (athlete_id, None)

def display_console_output(athletes: List[Dict], contracts: Dict[str, Dict], league_name: str) -> None:
    """Display formatted console output."""
    print(f"\n{league_name} Player Contracts")
    print("=" * 80)
    
    if not athletes:
        print("No athletes found matching your search criteria.")
        return
    
    # Check if this league typically has contract data
    league_has_contracts = any(c.get('has_data', False) for c in contracts.values())
    
    # Sort by total contract value
    sorted_athletes = sorted(athletes, 
                           key=lambda a: contracts.get(str(a['id']), {}).get('total_value', 0), 
                           reverse=True)
    
    # Count athletes with contracts
    athletes_with_contracts = sum(1 for a in sorted_athletes if contracts.get(str(a['id']), {}).get('has_data', False))
    
    if not league_has_contracts and league_name in ['NFL', 'MLB', 'NHL']:
        print(f"\nNote: Contract data is typically not available for {league_name} through the ESPN API.")
        print("NBA contract data is the most comprehensive.\n")
    
    for athlete in sorted_athletes:
        athlete_id = str(athlete['id'])
        contract = contracts.get(athlete_id, {})
        
        # Build header line
        header_parts = [athlete['name']]
        if athlete.get('position'):
            header_parts.append(f"({athlete['position']})")
        if athlete.get('team'):
            header_parts.append(f"- {athlete['team']}")
        
        print(f"\n{' '.join(header_parts)}")
        print("-" * 60)
        
        if contract.get('has_data') and contract.get('contracts'):
            # For contract lists without salary data
            if all(c.get('total', 0) == 0 for c in contract['contracts']):
                print(f"Contract Years Available: {contract['years_remaining']}")
                print("Years:", ', '.join(str(c['year']) for c in contract['contracts']))
                print("(Detailed salary information not yet fetched)")
            else:
                # Full contract data
                if contract.get('total_value', 0) > 0:
                    print(f"Total Value: {format_currency(contract['total_value'])}")
                    print(f"Average Annual: {format_currency(contract['average_annual'])}")
                
                years_with_data = contract.get('years_with_data', 0)
                total_years = contract['years_remaining']
                
                if years_with_data < total_years:
                    print(f"Years: {total_years} ({years_with_data} with salary data)")
                else:
                    print(f"Years: {total_years}")
                
                print("\nYear-by-Year Breakdown:")
                for year_contract in sorted(contract['contracts'], key=lambda x: x['year']):
                    year_str = f"  {year_contract['year']}:"
                    parts = []
                    
                    if year_contract.get('total', 0) > 0:
                        if year_contract.get('salary'):
                            parts.append(f"Salary: {format_currency(year_contract['salary'])}")
                        if year_contract.get('bonus'):
                            parts.append(f"Bonus: {format_currency(year_contract['bonus'])}")
                        parts.append(f"Total: {format_currency(year_contract['total'])}")
                        
                        # Add team info if changed
                        if year_contract.get('team'):
                            parts.append(f"[{year_contract['team']}]")
                    else:
                        parts.append("No salary data available")
                    
                    print(f"{year_str} {', '.join(parts)}")
        else:
            print("  No contract information available")

def save_json_output(data: Dict, filename: str) -> None:
    """Save data as JSON."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Data saved to {filename}")

def save_csv_output(athletes: List[Dict], contracts: Dict[str, Dict], filename: str, league: str) -> None:
    """Save data as CSV."""
    import csv
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['League', 'Name', 'Position', 'Team', 'Total Value', 'Average Annual', 'Years', 'Current Year Salary'])
        
        for athlete in athletes:
            athlete_id = str(athlete['id'])
            contract = contracts.get(athlete_id, {})
            
            current_salary = 0
            if contract.get('contracts'):
                # Find current year contract
                current_year = datetime.now().year
                for c in contract['contracts']:
                    if c.get('year') == current_year:
                        current_salary = c.get('total', 0)
                        break
                
                # If not found, use first contract
                if current_salary == 0 and contract['contracts']:
                    current_salary = contract['contracts'][0].get('total', 0)
            
            writer.writerow([
                league.upper(),
                athlete['name'],
                athlete.get('position', ''),
                athlete.get('team', ''),
                contract.get('total_value', 0),
                contract.get('average_annual', 0),
                contract.get('years_remaining', 0),
                current_salary
            ])
    
    print(f"Data saved to {filename}")

def main():
    parser = argparse.ArgumentParser(
        description='Search and analyze player contracts across ESPN\'s supported sports.'
    )
    
    # Required arguments
    parser.add_argument('query', help='Player name to search for')
    
    # Optional arguments
    parser.add_argument('--leagues', nargs='+', choices=list(SUPPORTED_LEAGUES.keys()),
                       default=['nfl', 'nba'], help='Leagues to search (default: nfl nba)')
    parser.add_argument('--output', choices=['console', 'json', 'csv'],
                       default='console', help='Output format (default: console)')
    parser.add_argument('--save', help='Save output to file')
    parser.add_argument('--limit', type=int, default=10,
                       help='Maximum number of players to show per league (default: 10)')
    parser.add_argument('--top-contracts', action='store_true',
                       help='Show only players with contract data, sorted by value')
    parser.add_argument('--all-years', action='store_true',
                       help='Fetch complete contract history for all years (NBA only)')
    
    args = parser.parse_args()
    
    # Create clients
    core_client = create_core_client()
    web_client = create_web_client()
    
    # Store all results
    all_results = {}
    
    # Search each league
    for league_key in args.leagues:
        sport, league, display_name = SUPPORTED_LEAGUES[league_key]
        
        print(f"\nSearching {display_name} for '{args.query}'...")
        
        # Search for athletes
        athletes = search_athletes(web_client, sport, league, args.query, limit=args.limit * 3)  # Get extra in case some don't have contracts
        
        if athletes:
            # Fetch contracts asynchronously
            print(f"Found {len(athletes)} athletes, fetching contract details...")
            if league == 'nba' and args.all_years:
                print("(This may take a moment as we fetch data for all contract years...)")
            contracts = asyncio.run(fetch_multiple_contracts_async(athletes[:args.limit], sport, league, args.all_years))
            
            # Filter to only those with contracts if requested
            if args.top_contracts:
                athletes = [a for a in athletes if contracts.get(str(a['id']))]
            
            # Store results
            all_results[league_key] = {
                'athletes': athletes[:args.limit],
                'contracts': contracts,
                'league_name': display_name
            }
    
    # Output results
    if args.output == 'console':
        for league_key, data in all_results.items():
            display_console_output(data['athletes'], data['contracts'], data['league_name'])
    
    elif args.output == 'json':
        # Prepare JSON output
        json_output = {}
        for league_key, data in all_results.items():
            json_output[league_key] = []
            for athlete in data['athletes']:
                athlete_data = athlete.copy()
                athlete_data['contract'] = data['contracts'].get(str(athlete['id']), {})
                json_output[league_key].append(athlete_data)
        
        if args.save:
            save_json_output(json_output, args.save)
        else:
            print(json.dumps(json_output, indent=2))
    
    elif args.output == 'csv':
        if not args.save:
            print("CSV output requires --save parameter")
            sys.exit(1)
        
        # Combine all results for CSV
        all_athletes = []
        all_contracts = {}
        
        for league_key, data in all_results.items():
            # Add league info to each athlete
            for athlete in data['athletes']:
                athlete['league'] = league_key
                all_athletes.append(athlete)
            all_contracts.update(data['contracts'])
        
        save_csv_output(all_athletes, all_contracts, args.save, 'multi')

if __name__ == '__main__':
    main()