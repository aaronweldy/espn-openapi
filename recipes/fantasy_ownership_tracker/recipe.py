#!/usr/bin/env python3
"""
Track fantasy football player ownership trends using ESPN Fantasy API.

This recipe helps identify rising and falling players based on ownership percentages.
"""

import argparse
import json
import os
from datetime import datetime, timedelta
import time
from typing import Dict, List, Optional, Tuple

# Import generated models
from models.fantasy_api.espn_fantasy_api_client import Client as FantasyApiClient
from models.fantasy_api.espn_fantasy_api_client.api.default import (
    get_fantasy_player_defaults,
    get_fantasy_football_players,
)
from models.fantasy_api.espn_fantasy_api_client.types import UNSET


# Constants
CURRENT_YEAR = datetime.now().year
DEFAULT_SCORING_ID = 1  # Standard scoring
PPR_SCORING_ID = 3  # PPR scoring

# Positions to track
FANTASY_POSITIONS = ["QB", "RB", "WR", "TE", "K", "D/ST"]


def create_client() -> FantasyApiClient:
    """Create and return an ESPN Fantasy API client."""
    return FantasyApiClient(base_url="https://lm-api-reads.fantasy.espn.com")


def get_player_ownership_data(client: FantasyApiClient, year: int = CURRENT_YEAR, 
                            scoring_id: int = DEFAULT_SCORING_ID, scoring_period: int = 0) -> Optional[List]:
    """
    Fetch player ownership data from ESPN Fantasy API.
    
    Args:
        client: ESPN Fantasy API client
        year: Season year
        scoring_id: Scoring system ID (1=standard, 3=PPR)
        scoring_period: Week/period to fetch (0=current, 1-17 for NFL weeks)
        
    Returns:
        List of player data or None if error
    """
    try:
        # Get player data with ownership info
        from models.fantasy_api.espn_fantasy_api_client.models.get_fantasy_football_players_view import GetFantasyFootballPlayersView
        
        response = get_fantasy_football_players.sync_detailed(
            client=client,
            year=year,
            view=GetFantasyFootballPlayersView.PLAYERS_WL,
            scoring_period_id=scoring_period,
            x_fantasy_filter=json.dumps({
                "players": {
                    "limit": 2000,
                    "sortPercOwned": {
                        "sortPriority": 1,
                        "sortAsc": False
                    }
                }
            })
        )
        
        if response.status_code == 200 and isinstance(response.parsed, list):
            return response.parsed
        else:
            print(f"Error fetching player data for period {scoring_period}: HTTP {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Error fetching player data: {e}")
        return None


def extract_player_info(player_data: List) -> List[Dict]:
    """Extract relevant player information from API response."""
    players = []
    
    # player_data is already a list of FantasyPlayer objects
    if player_data:
        for player in player_data:
            # Extract player details
            player_info = {
                "id": player.id if hasattr(player, 'id') else None,
                "name": player.full_name if hasattr(player, 'full_name') else "Unknown",
                "position": None,
                "team": None,
                "ownership_pct": 0.0,
                "projected_points": 0.0,
                "average_points": 0.0
            }
            
            # Get position
            if hasattr(player, 'default_position_id'):
                position_map = {1: "QB", 2: "RB", 3: "WR", 4: "TE", 5: "K", 16: "D/ST"}
                player_info["position"] = position_map.get(player.default_position_id, "Unknown")
            
            # Get team
            if hasattr(player, 'pro_team_id'):
                # Map team IDs to abbreviations (simplified - full mapping needed)
                team_map = {
                    1: "ATL", 2: "BUF", 3: "CHI", 4: "CIN", 5: "CLE",
                    6: "DAL", 7: "DEN", 8: "DET", 9: "GB", 10: "TEN",
                    11: "IND", 12: "KC", 13: "LV", 14: "LAR", 15: "MIA",
                    16: "MIN", 17: "NE", 18: "NO", 19: "NYG", 20: "NYJ",
                    21: "PHI", 22: "ARI", 23: "PIT", 24: "LAC", 25: "SF",
                    26: "SEA", 27: "TB", 28: "WSH", 29: "CAR", 30: "JAX",
                    33: "BAL", 34: "HOU"
                }
                player_info["team"] = team_map.get(player.pro_team_id, "FA")
            
            # Get ownership and stats
            if hasattr(player, 'ownership'):
                if hasattr(player.ownership, 'percent_owned'):
                    player_info["ownership_pct"] = player.ownership.percent_owned
            
            # Get player stats/projections
            if hasattr(player, 'stats'):
                for stat in player.stats:
                    if hasattr(stat, 'scoring_period_id') and stat.scoring_period_id == 0:
                        if hasattr(stat, 'applied_total'):
                            player_info["projected_points"] = stat.applied_total
            
            # Add to list if it's a relevant position
            if player_info["position"] in FANTASY_POSITIONS:
                players.append(player_info)
    
    return players


def load_historical_data(filename: str) -> Optional[Dict]:
    """Load previously saved ownership data."""
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading historical data: {e}")
    return None


def save_ownership_snapshot(players: List[Dict], filename: str):
    """Save current ownership data for future comparison."""
    data = {
        "date": datetime.now().isoformat(),
        "players": players
    }
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Saved ownership data to {filename}")


def get_current_scoring_period(year: int = None) -> int:
    """
    Calculate the current NFL scoring period (week) based on the date.
    NFL season typically starts in early September.
    """
    now = datetime.now()
    if year is None:
        year = now.year
    
    # Approximate NFL season start (first Thursday after Labor Day)
    # For simplicity, using September 7 as approximate start
    season_start = datetime(year, 9, 7)
    
    # If we're in a different year than requested, assume end of season
    if now.year != year:
        return 17 if now.year > year else 0
    
    # If we're before the season, return 0
    if now < season_start:
        return 0
    
    # Calculate weeks since season start
    days_since_start = (now - season_start).days
    current_week = min((days_since_start // 7) + 1, 17)  # Cap at week 17
    
    return current_week


def get_historical_ownership_data(client: FantasyApiClient, days_back: int, year: int = CURRENT_YEAR) -> Optional[Dict[int, List]]:
    """
    Fetch ownership data from multiple scoring periods to track changes.
    
    Args:
        client: ESPN Fantasy API client
        days_back: Number of days to look back
        year: Season year
        
    Returns:
        Dictionary mapping scoring_period to player data
    """
    current_period = get_current_scoring_period(year)
    weeks_back = max(1, days_back // 7)  # Convert days to weeks
    
    historical_data = {}
    
    # If we're in the off-season (period 0), use last year's data
    if current_period == 0:
        print("Off-season detected. Using previous year's data...")
        year = year - 1
        current_period = 17  # Use end of previous season
    
    # Calculate which periods to fetch
    periods_to_fetch = []
    for i in range(weeks_back + 1):
        period = current_period - i
        if period >= 1:  # Don't go before week 1
            periods_to_fetch.append(period)
    
    print(f"Fetching data for weeks: {sorted(periods_to_fetch)}")
    
    for period in sorted(periods_to_fetch):
        print(f"Fetching week {period} data...", end="", flush=True)
        data = get_player_ownership_data(client, year, scoring_period=period)
        if data:
            historical_data[period] = data
            print(" ✓")
        else:
            print(" ✗")
        
        # Small delay to avoid rate limiting
        if period != periods_to_fetch[-1]:
            time.sleep(0.5)
    
    return historical_data if historical_data else None


def calculate_ownership_changes_from_historical(current_data: List, historical_data: Dict[int, List]) -> List[Tuple[Dict, float, int]]:
    """
    Calculate ownership changes between current and historical data.
    
    Args:
        current_data: Current player data
        historical_data: Dictionary of historical data by scoring period
        
    Returns:
        List of tuples: (player_info, change_percentage, weeks_back)
    """
    changes = []
    
    # Extract current player info
    current_players = extract_player_info(current_data)
    current_lookup = {p['id']: p for p in current_players if p['id']}
    
    # Find the oldest period we have data for
    if not historical_data:
        return changes
        
    periods = sorted(historical_data.keys())
    oldest_period = periods[0] if periods else None
    
    if oldest_period and oldest_period in historical_data:
        # Extract historical player info
        hist_players = extract_player_info(historical_data[oldest_period])
        hist_lookup = {p['id']: p['ownership_pct'] for p in hist_players if p['id']}
        
        # Calculate changes
        for player_id, current_player in current_lookup.items():
            if player_id in hist_lookup:
                old_ownership = hist_lookup[player_id]
                change = current_player['ownership_pct'] - old_ownership
                
                if abs(change) > 0.5:  # Only significant changes
                    # For off-season, just show generic "previous season" indicator
                    current_period = get_current_scoring_period()
                    if current_period == 0:
                        weeks_diff = -1  # Special indicator for previous season
                    else:
                        weeks_diff = current_period - oldest_period
                    changes.append((current_player, change, weeks_diff))
    
    return sorted(changes, key=lambda x: abs(x[1]), reverse=True)


def display_top_owned(players: List[Dict], limit: int = 20):
    """Display top owned players."""
    print(f"\n=== TOP {limit} OWNED FANTASY PLAYERS ({datetime.now().strftime('%Y-%m-%d')}) ===\n")
    
    # Sort by ownership
    sorted_players = sorted(players, key=lambda x: x["ownership_pct"], reverse=True)
    
    for i, player in enumerate(sorted_players[:limit], 1):
        print(f"{i}. {player['name']} ({player['position']}, {player['team']})")
        print(f"   Ownership: {player['ownership_pct']:.1f}%")
        if player['projected_points'] > 0:
            print(f"   Projected Points: {player['projected_points']:.1f}")
        print()


def display_ownership_changes(changes: List[Tuple[Dict, float]], limit: int = 10):
    """Display biggest ownership changes."""
    print(f"\n=== BIGGEST OWNERSHIP CHANGES ===\n")
    
    # Separate rising and falling
    rising = [(p, c) for p, c in changes if c > 0][:limit]
    falling = [(p, c) for p, c in changes if c < 0][:limit]
    
    if rising:
        print("RISING:")
        for player, change in rising:
            old_pct = player["ownership_pct"] - change
            print(f"↑ {player['name']} ({player['position']}, {player['team']}): "
                  f"{old_pct:.1f}% → {player['ownership_pct']:.1f}% (+{change:.1f}%)")
        print()
    
    if falling:
        print("FALLING:")
        for player, change in falling:
            old_pct = player["ownership_pct"] - change
            print(f"↓ {player['name']} ({player['position']}, {player['team']}): "
                  f"{old_pct:.1f}% → {player['ownership_pct']:.1f}% ({change:.1f}%)")


def display_ownership_changes_auto(changes: List[Tuple[Dict, float, int]], limit: int = 10):
    """Display ownership changes with time period information."""
    print(f"\n=== BIGGEST OWNERSHIP CHANGES ===\n")
    
    if not changes:
        print("No significant ownership changes found.")
        return
    
    # Separate rising and falling
    rising = [(p, c, w) for p, c, w in changes if c > 0][:limit]
    falling = [(p, c, w) for p, c, w in changes if c < 0][:limit]
    
    if rising:
        print("RISING:")
        for player, change, weeks in rising:
            old_pct = player["ownership_pct"] - change
            if weeks == -1:
                period_str = "(previous season)"
            else:
                period_str = f"({weeks} week{'s' if weeks != 1 else ''} ago)"
            print(f"↑ {player['name']} ({player['position']}, {player['team']}): "
                  f"{old_pct:.1f}% → {player['ownership_pct']:.1f}% (+{change:.1f}%) {period_str}")
        print()
    
    if falling:
        print("FALLING:")
        for player, change, weeks in falling:
            old_pct = player["ownership_pct"] - change
            if weeks == -1:
                period_str = "(previous season)"
            else:
                period_str = f"({weeks} week{'s' if weeks != 1 else ''} ago)"
            print(f"↓ {player['name']} ({player['position']}, {player['team']}): "
                  f"{old_pct:.1f}% → {player['ownership_pct']:.1f}% ({change:.1f}%) {period_str}")


def search_players(players: List[Dict], names: List[str]):
    """Search for specific players by name."""
    print(f"\n=== PLAYER SEARCH RESULTS ===\n")
    
    for search_name in names:
        search_lower = search_name.lower()
        found = False
        
        for player in players:
            if search_lower in player['name'].lower():
                print(f"{player['name']} ({player['position']}, {player['team']})")
                print(f"   Ownership: {player['ownership_pct']:.1f}%")
                if player['projected_points'] > 0:
                    print(f"   Projected Points: {player['projected_points']:.1f}")
                print()
                found = True
                break
        
        if not found:
            print(f"Player '{search_name}' not found\n")


def main():
    """Main function to run the recipe."""
    parser = argparse.ArgumentParser(description="Track fantasy football player ownership")
    parser.add_argument("--top", type=int, default=20, help="Show top N owned players")
    parser.add_argument("--players", nargs="+", help="Search for specific players")
    parser.add_argument("--movers", action="store_true", help="Show biggest ownership changes")
    parser.add_argument("--days", type=int, default=7, help="Days to look back for changes")
    parser.add_argument("--export", help="Export data to JSON file")
    parser.add_argument("--historical", help="Historical data file for comparison")
    parser.add_argument("--ppr", action="store_true", help="Use PPR scoring")
    
    args = parser.parse_args()
    
    # Create API client
    client = create_client()
    
    # Determine scoring system
    scoring_id = PPR_SCORING_ID if args.ppr else DEFAULT_SCORING_ID
    
    # Fetch current ownership data
    print("Fetching player ownership data...")
    player_data = get_player_ownership_data(client, CURRENT_YEAR, scoring_id)
    
    if not player_data:
        print("Failed to fetch player data")
        return
    
    # Extract player information
    players = extract_player_info(player_data)
    
    if not players:
        print("No player data found")
        return
    
    print(f"Found {len(players)} fantasy-relevant players")
    
    # Handle different modes
    if args.players:
        # Search for specific players
        search_players(players, args.players)
    
    elif args.movers:
        # Show ownership changes by automatically fetching historical data
        print(f"\nFetching historical data for the last {args.days} days...")
        historical_data = get_historical_ownership_data(client, args.days, CURRENT_YEAR)
        
        if historical_data and player_data:
            # Calculate changes from historical data
            changes = calculate_ownership_changes_from_historical(player_data, historical_data)
            display_ownership_changes_auto(changes)
        else:
            print("Unable to fetch historical data for comparison.")
    
    else:
        # Show top owned players
        display_top_owned(players, args.top)
    
    # Export data if requested
    if args.export:
        save_ownership_snapshot(players, args.export)


if __name__ == "__main__":
    main()