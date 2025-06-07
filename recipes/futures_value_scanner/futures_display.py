#!/usr/bin/env python3
"""
Display all available futures markets and odds.
"""

import argparse
import json
from datetime import datetime
from typing import Dict, List, Optional, Any
from models.sports_core_api.espn_sports_core_api_client import Client as SportsCoreClient
from models.sports_core_api.espn_sports_core_api_client.api.default import get_season_futures


def extract_id_from_ref(ref_url: str) -> str:
    """Extract ID from ESPN API $ref URL."""
    import re
    match = re.search(r'/(teams|athletes)/(\d+)', ref_url)
    if match:
        return match.group(2)
    return "Unknown"


def display_futures(sport: str, league: str, year: int):
    """Display all futures for a sport/league/year."""
    client = SportsCoreClient(base_url="https://sports.core.api.espn.com/v2")
    
    # Common team mappings
    team_names = {
        # NFL
        "1": "ATL", "2": "BUF", "3": "CHI", "4": "CIN", "5": "CLE",
        "6": "DAL", "7": "DEN", "8": "DET", "9": "GB", "10": "TEN",
        "11": "IND", "12": "KC", "13": "LV", "14": "LAR", "15": "MIA",
        "16": "MIN", "17": "NE", "18": "NO", "19": "NYG", "20": "NYJ",
        "21": "PHI", "22": "ARI", "23": "PIT", "24": "LAC", "25": "SF",
        "26": "SEA", "27": "TB", "28": "WSH", "29": "CAR", "30": "JAX",
        "33": "BAL", "34": "HOU"
    }
    
    try:
        response = get_season_futures.sync_detailed(
            client=client,
            sport=sport,
            league=league,
            year=year
        )
        
        if response.status_code != 200:
            print(f"Error: API returned status {response.status_code}")
            if response.status_code == 404:
                print(f"No futures found for {sport}/{league} {year}")
            return
            
        data = response.parsed.to_dict()
        items = data.get("items", [])
        
        if not items:
            print(f"No futures markets found for {sport}/{league} in {year}")
            return
        
        print(f"\n{'='*80}")
        print(f"FUTURES MARKETS - {league.upper()} {year}")
        print(f"{'='*80}\n")
        
        # Display each futures market
        for market in items:
            market_name = market.get("displayName", market.get("name", "Unknown"))
            futures = market.get("futures", [])
            
            if not futures:
                continue
                
            print(f"\n{market_name}")
            print("-" * len(market_name))
            
            for future in futures:
                provider = future.get("provider", {}).get("name", "Unknown")
                books = future.get("books", [])
                
                if books:
                    print(f"\nProvider: {provider}")
                    print(f"{'Selection':<25} {'Odds':>10}")
                    print("-" * 40)
                    
                    # Sort books by odds value
                    sorted_books = []
                    for book in books:
                        odds_str = book.get("value", "0")
                        try:
                            odds_val = int(odds_str.replace("+", ""))
                        except:
                            odds_val = 999999
                            
                        if "team" in book and isinstance(book["team"], dict):
                            if "$ref" in book["team"]:
                                team_id = extract_id_from_ref(book["team"]["$ref"])
                                selection = team_names.get(team_id, f"Team {team_id}")
                            else:
                                selection = book["team"].get("displayName", "Unknown")
                        elif "athlete" in book and isinstance(book["athlete"], dict):
                            if "$ref" in book["athlete"]:
                                selection = f"Athlete {extract_id_from_ref(book['athlete']['$ref'])}"
                            else:
                                selection = book["athlete"].get("displayName", "Unknown")
                        else:
                            selection = "Unknown"
                            
                        sorted_books.append((selection, odds_str, odds_val))
                    
                    # Sort by odds value
                    sorted_books.sort(key=lambda x: x[2])
                    
                    # Display top 10 selections
                    for selection, odds, _ in sorted_books[:10]:
                        print(f"{selection:<25} {odds:>10}")
                    
                    if len(sorted_books) > 10:
                        print(f"... and {len(sorted_books) - 10} more")
        
        print(f"\nTotal markets found: {len(items)}")
        
    except Exception as e:
        print(f"Error fetching futures: {e}")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Display all available futures markets and odds"
    )
    
    parser.add_argument(
        "--sport",
        default="football",
        help="Sport (default: football)"
    )
    
    parser.add_argument(
        "--league", 
        default="nfl",
        help="League (default: nfl)"
    )
    
    parser.add_argument(
        "--year",
        type=int,
        default=datetime.now().year,
        help="Year (default: current year)"
    )
    
    args = parser.parse_args()
    
    display_futures(args.sport, args.league, args.year)


if __name__ == "__main__":
    main()