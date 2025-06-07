#!/usr/bin/env python3
"""
Fantasy Draft Value Finder - Identify undervalued players for fantasy football drafts.

This recipe fetches fantasy football player data including projections, ownership percentages,
and ADP (Average Draft Position) to calculate value scores and identify potential sleepers
and busts for your fantasy draft.
"""

import argparse
import json
import sys
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from collections import defaultdict

# Import API clients and models
from models.fantasy_api.espn_fantasy_api_client import Client as FantasyApiClient
from models.fantasy_api.espn_fantasy_api_client.api.default import get_fantasy_football_players


def create_fantasy_client() -> FantasyApiClient:
    """Create and return a Fantasy API client."""
    return FantasyApiClient(
        base_url="https://lm-api-reads.fantasy.espn.com"
    )


def fetch_players_data(client: FantasyApiClient, year: int, view: str = "kona_player_info",
                      scoring_period: int = 1) -> Optional[List[Dict]]:
    """Fetch fantasy player data with projections and ownership info."""
    try:
        # Import the view enum
        from models.fantasy_api.espn_fantasy_api_client.models.get_fantasy_football_players_view import GetFantasyFootballPlayersView
        
        # Create fantasy filter to get more players with better filtering
        fantasy_filter = json.dumps({
            "players": {
                "limit": 1000,
                "sortPercOwned": {
                    "sortPriority": 4,
                    "sortAsc": False
                }
            }
        })
        
        # Use the enum for view
        view_enum = GetFantasyFootballPlayersView(view)
        
        response = get_fantasy_football_players.sync_detailed(
            client=client,
            year=year,
            view=view_enum,
            scoring_period_id=scoring_period,
            x_fantasy_filter=fantasy_filter
        )
        
        if response.status_code == 200:
            # Get raw content and parse as JSON
            try:
                data = json.loads(response.content)
                # Check if data has a 'players' key
                if isinstance(data, dict) and 'players' in data:
                    return data['players']
                # Otherwise return as is (for views that return direct arrays)
                return data
            except:
                print("Failed to parse response as JSON")
                return None
        else:
            print(f"Error fetching players: HTTP {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Error fetching player data: {e}")
        return None


def calculate_value_score(player: Dict, scoring_system: str = "ppr") -> float:
    """Calculate a value score based on projections vs ADP/ownership."""
    # Find projected stats for current season
    projected_points = 0
    stats = player.get('stats', [])
    for stat in stats:
        if stat.get('statSourceId') == 1:  # Projected stats
            if scoring_system == "ppr":
                projected_points = stat.get('appliedTotal', 0)
            else:
                # Adjust for standard scoring (rough approximation)
                projected_points = stat.get('appliedTotal', 0) * 0.85
    
    # Get ownership metrics
    ownership = player.get('ownership', {})
    percent_owned = ownership.get('percentOwned', 0)
    average_draft_position = ownership.get('averageDraftPosition', 300)
    
    # Prevent division by zero
    if average_draft_position == 0:
        average_draft_position = 300
    
    # If no projections available, use ownership-based value score
    if projected_points == 0:
        # For players with high ownership but late ADP, they might be undervalued
        if percent_owned > 20 and average_draft_position > 100:
            # Calculate based on ownership vs ADP mismatch
            ownership_value = percent_owned / 100
            adp_discount = (300 - average_draft_position) / 300
            value_score = ownership_value * adp_discount * 100
        else:
            value_score = 0
    else:
        # Calculate value score with projections (higher is better)
        # Formula: (Projected Points / ADP) * (100 - % Owned) / 100
        adp_value = projected_points / average_draft_position
        ownership_multiplier = (100 - percent_owned) / 100
        
        # Boost value for later round picks
        round_boost = 1.0
        if average_draft_position > 100:
            round_boost = 1.2
        elif average_draft_position > 150:
            round_boost = 1.5
        
        value_score = adp_value * ownership_multiplier * round_boost * 100
    
    return value_score


def process_players(players_data: List[Dict], position_filter: Optional[str] = None,
                   scoring_system: str = "ppr", min_adp: int = 1, 
                   max_adp: int = 300) -> List[Dict]:
    """Process player data and calculate value scores."""
    processed_players = []
    
    if not players_data:
        return processed_players
    
    for player in players_data:
        # Get basic info
        player_id = player.get('id')
        full_name = player.get('fullName', 'Unknown')
        position = player.get('defaultPositionId', 0)
        
        # Map position IDs to abbreviations
        position_map = {1: "QB", 2: "RB", 3: "WR", 4: "TE", 5: "K", 
                       16: "DST"}
        position_abbr = position_map.get(position, "Unknown")
        
        # Apply position filter
        if position_filter and position_abbr.lower() != position_filter.lower():
            continue
        
        # Get ownership data
        ownership = player.get('ownership', {})
        adp = ownership.get('averageDraftPosition', 300)
        percent_owned = ownership.get('percentOwned', 0)
        percent_started = ownership.get('percentStarted', 0)
        
        # Apply ADP filter
        if adp < min_adp or adp > max_adp:
            continue
        
        # Calculate value score
        value_score = calculate_value_score(player, scoring_system)
        
        # Get projected points
        projected_points = 0
        stats = player.get('stats', [])
        for stat in stats:
            if stat.get('statSourceId') == 1:  # Projected stats
                if scoring_system == "ppr":
                    projected_points = stat.get('appliedTotal', 0)
                else:
                    projected_points = stat.get('appliedTotal', 0) * 0.85
        
        processed_players.append({
            "id": player_id,
            "name": full_name,
            "position": position_abbr,
            "adp": round(adp, 1),
            "projected_points": round(projected_points, 1),
            "percent_owned": round(percent_owned, 1),
            "percent_started": round(percent_started, 1),
            "value_score": round(value_score, 2),
            "round": int((adp - 1) / 12) + 1  # Assuming 12-team league
        })
    
    # Sort by value score (descending)
    processed_players.sort(key=lambda x: x["value_score"], reverse=True)
    
    return processed_players


def display_console_output(players: List[Dict], limit: int = 25):
    """Display formatted console output."""
    print("\n" + "=" * 80)
    print("FANTASY DRAFT VALUE FINDER")
    print("=" * 80)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Showing top {min(limit, len(players))} value picks")
    print()
    
    # Header
    print(f"{'Rank':<5} {'Player':<25} {'Pos':<4} {'ADP':<6} {'Proj':<6} "
          f"{'Own%':<6} {'Value':<8} {'Round':<6}")
    print("-" * 80)
    
    # Display players
    for i, player in enumerate(players[:limit], 1):
        print(f"{i:<5} {player['name'][:24]:<25} {player['position']:<4} "
              f"{player['adp']:<6.1f} {player['projected_points']:<6.1f} "
              f"{player['percent_owned']:<6.1f} {player['value_score']:<8.2f} "
              f"{player['round']:<6}")
    
    print()
    
    # Show some insights
    print("TOP VALUE PICKS BY POSITION:")
    print("-" * 40)
    
    # Group by position
    by_position = defaultdict(list)
    for player in players:
        by_position[player['position']].append(player)
    
    for pos in ["QB", "RB", "WR", "TE", "DST", "K"]:
        if pos in by_position and by_position[pos]:
            top_player = by_position[pos][0]
            print(f"{pos}: {top_player['name']} (ADP: {top_player['adp']}, "
                  f"Value: {top_player['value_score']:.1f})")
    
    print()
    
    # Show late round sleepers
    print("LATE ROUND SLEEPERS (ADP > 150):")
    print("-" * 40)
    
    late_sleepers = [p for p in players if p['adp'] > 150][:5]
    for player in late_sleepers:
        print(f"{player['name']} ({player['position']}) - "
              f"ADP: {player['adp']}, Projected: {player['projected_points']}")


def save_json_output(players: List[Dict], filename: str):
    """Save results as JSON."""
    output = {
        "generated": datetime.now().isoformat(),
        "total_players": len(players),
        "players": players
    }
    
    with open(filename, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"Results saved to {filename}")


def save_csv_output(players: List[Dict], filename: str):
    """Save results as CSV."""
    import csv
    
    with open(filename, 'w', newline='') as f:
        if players:
            writer = csv.DictWriter(f, fieldnames=players[0].keys())
            writer.writeheader()
            writer.writerows(players)
    
    print(f"Results saved to {filename}")


def main():
    """Main function to run the recipe."""
    parser = argparse.ArgumentParser(
        description="Find undervalued fantasy football players based on projections vs ADP"
    )
    
    # Add arguments
    parser.add_argument("--year", type=int, default=2025,
                       help="Season year (default: 2025)")
    parser.add_argument("--position", choices=["qb", "rb", "wr", "te", "dst", "k"],
                       help="Filter by position")
    parser.add_argument("--scoring", choices=["ppr", "standard"], default="ppr",
                       help="Scoring system (default: ppr)")
    parser.add_argument("--min-adp", type=int, default=1,
                       help="Minimum ADP to consider (default: 1)")
    parser.add_argument("--max-adp", type=int, default=300,
                       help="Maximum ADP to consider (default: 300)")
    parser.add_argument("--limit", type=int, default=25,
                       help="Number of results to show (default: 25)")
    parser.add_argument("--output", choices=["console", "json", "csv"], default="console",
                       help="Output format (default: console)")
    parser.add_argument("--save", help="Save output to file")
    
    args = parser.parse_args()
    
    # Create client
    print("Fetching fantasy player data...")
    client = create_fantasy_client()
    
    # Fetch player data
    players_data = fetch_players_data(client, args.year)
    
    if not players_data:
        print("Error: Could not fetch player data")
        sys.exit(1)
    
    # Process players
    print("Calculating value scores...")
    processed = process_players(
        players_data,
        position_filter=args.position,
        scoring_system=args.scoring,
        min_adp=args.min_adp,
        max_adp=args.max_adp
    )
    
    if not processed:
        print("No players found matching criteria")
        sys.exit(0)
    
    # Output results
    if args.output == "json":
        if args.save:
            save_json_output(processed, args.save)
        else:
            print(json.dumps(processed[:args.limit], indent=2))
    elif args.output == "csv":
        if args.save:
            save_csv_output(processed[:args.limit], args.save)
        else:
            print("Error: CSV output requires --save parameter")
    else:
        display_console_output(processed, args.limit)


if __name__ == "__main__":
    main()