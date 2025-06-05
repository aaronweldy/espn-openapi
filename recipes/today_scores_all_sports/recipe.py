#!/usr/bin/env python3
"""
Get today's scores across all major sports using ESPN API.

This recipe demonstrates how to fetch and display live scores from NFL, NBA, MLB, and NHL.
"""

import argparse
import json
import sys
from datetime import datetime
from typing import Dict, List, Optional

# Import generated models
from models.site_api.espn_nfl_api_client import Client as SiteApiClient
from models.site_api.espn_nfl_api_client.api.default import get_scoreboard
from models.site_api.espn_nfl_api_client.models import GenericScoreboardResponse
from models.site_api.espn_nfl_api_client.models.get_scoreboard_sport import GetScoreboardSport
from models.site_api.espn_nfl_api_client.types import UNSET


# Sports and leagues to check
SPORTS_LEAGUES = {
    "football": ["nfl"],
    "basketball": ["nba"],
    "baseball": ["mlb"],
    "hockey": ["nhl"]
}


def create_client() -> SiteApiClient:
    """Create and return an ESPN Site API client."""
    return SiteApiClient(base_url="https://site.api.espn.com/apis/site/v2")


def get_scoreboard_for_league(client: SiteApiClient, sport: str, league: str, date: Optional[str] = None) -> Optional[GenericScoreboardResponse]:
    """
    Fetch scoreboard data for a specific sport and league.
    
    Args:
        client: ESPN API client
        sport: Sport name (e.g., "football", "basketball")
        league: League name (e.g., "nfl", "nba")
        date: Date in YYYYMMDD format (defaults to today)
        
    Returns:
        ScoreboardResponse object or None if error
    """
    try:
        # Default to today if no date provided
        if not date:
            date = datetime.now().strftime("%Y%m%d")
        
        # Convert sport string to enum
        sport_enum = GetScoreboardSport(sport)
            
        response = get_scoreboard.sync_detailed(
            client=client,
            sport=sport_enum,
            league=league,
            dates=date
        )
        
        if response.status_code == 200 and hasattr(response, 'parsed'):
            # Ensure we have a GenericScoreboardResponse, not an ErrorResponse
            if isinstance(response.parsed, GenericScoreboardResponse):
                return response.parsed
            else:
                print(f"Error fetching {sport}/{league} scoreboard: Invalid response format")
                return None
        else:
            print(f"Error fetching {sport}/{league} scoreboard: HTTP {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Error fetching {sport}/{league} scoreboard: {e}")
        return None


def format_game_status(event) -> str:
    """Format game status into human-readable string."""
    if not event.status:
        return "Unknown"
    
    # Get status type correctly
    if hasattr(event.status, 'type'):
        status_type = event.status.type
    else:
        return "Unknown"
    
    # Check if game is completed
    if hasattr(status_type, 'completed') and status_type.completed:
        return "Final"
    
    # Check game state
    if hasattr(status_type, 'state'):
        state = status_type.state
        if state == "pre":
            # Show start time for games that haven't started
            if event.date:
                try:
                    game_time = datetime.fromisoformat(event.date.replace('Z', '+00:00'))
                    return f"Starts at {game_time.strftime('%-I:%M %p')}"
                except:
                    pass
            return "Scheduled"
        elif state == "in":
            # Show period and clock for live games
            if event.status.display_clock and event.status.period:
                detail = getattr(status_type, 'detail', '')
                return f"{detail} - {event.status.display_clock}" if detail else f"Period {event.status.period} - {event.status.display_clock}"
            return "In Progress"
        elif state == "post":
            return "Final"
    
    # Fall back to description if available
    return getattr(status_type, 'description', '') or "Unknown"


def format_team_record(competitor) -> str:
    """Format team record if available."""
    if competitor.records and len(competitor.records) > 0:
        record = competitor.records[0]
        if record.summary:
            return f" ({record.summary})"
    return ""


def display_scoreboard(scoreboard_data: Dict[str, GenericScoreboardResponse], output_format: str = "console"):
    """
    Display scoreboard data in the specified format.
    
    Args:
        scoreboard_data: Dictionary mapping "sport/league" to ScoreboardResponse
        output_format: One of "console", "json", or "csv"
    """
    if output_format == "json":
        # Convert to JSON-serializable format
        output = {}
        for key, scoreboard in scoreboard_data.items():
            if scoreboard and scoreboard.events:
                output[key] = []
                for event in scoreboard.events:
                    if event.competitions and len(event.competitions) > 0:
                        competition = event.competitions[0]
                        game_data = {
                            "id": event.id,
                            "name": event.name,
                            "short_name": event.short_name,
                            "date": event.date,
                            "status": format_game_status(event),
                            "competitors": []
                        }
                        
                        if competition.competitors:
                            for competitor in competition.competitors:
                                team_data = {
                                    "id": competitor.id,
                                    "name": competitor.team.display_name if competitor.team else "Unknown",
                                    "abbreviation": competitor.team.abbreviation if competitor.team else "",
                                    "score": competitor.score or "0",
                                    "home_away": competitor.home_away,
                                    "winner": competitor.winner if competitor.winner is not UNSET else False
                                }
                                game_data["competitors"].append(team_data)
                        
                        output[key].append(game_data)
        
        return json.dumps(output, indent=2, default=str)
    
    elif output_format == "console":
        # Console display
        date_str = datetime.now().strftime("%Y-%m-%d")
        
        for key, scoreboard in scoreboard_data.items():
            _, league = key.split("/")
            print(f"\n=== {league.upper()} SCORES ({date_str}) ===")
            
            if not scoreboard or not scoreboard.events:
                print("No games scheduled")
                continue
            
            for event in scoreboard.events:
                if not event.competitions or len(event.competitions) == 0:
                    continue
                    
                competition = event.competitions[0]
                if not competition.competitors or len(competition.competitors) < 2:
                    continue
                
                # Get teams (usually index 0 is away, 1 is home)
                away_team = None
                home_team = None
                
                for competitor in competition.competitors:
                    if competitor.home_away == "away":
                        away_team = competitor
                    elif competitor.home_away == "home":
                        home_team = competitor
                
                if away_team and home_team:
                    # Build team display with records
                    away_display = f"{away_team.team.display_name if away_team.team else 'Unknown'}{format_team_record(away_team)}"
                    home_display = f"{home_team.team.display_name if home_team.team else 'Unknown'}{format_team_record(home_team)}"
                    
                    print(f"\n{away_display} @ {home_display}")
                    print(f"  Status: {format_game_status(event)}")
                    
                    # Only show score if game has started
                    if event.status and hasattr(event.status, 'type'):
                        status_type = event.status.type
                        if hasattr(status_type, 'state') and status_type.state in ["in", "post"]:
                            away_score = away_team.score or "0"
                            home_score = home_team.score or "0"
                            print(f"  Score: {away_team.team.abbreviation if away_team.team else 'AWAY'} {away_score}, "
                                  f"{home_team.team.abbreviation if home_team.team else 'HOME'} {home_score}")


def main():
    """Main function to run the recipe."""
    parser = argparse.ArgumentParser(description="Get today's scores across major sports")
    parser.add_argument("--sport", help="Filter by specific sport (nfl, nba, mlb, nhl)")
    parser.add_argument("--date", help="Date in YYYYMMDD format (default: today)")
    parser.add_argument("--output", choices=["console", "json"], default="console",
                        help="Output format")
    parser.add_argument("--save", help="Save output to file")
    
    args = parser.parse_args()
    
    # Create API client
    client = create_client()
    
    # Determine which sports/leagues to fetch
    if args.sport:
        # Map single sport to sport/league pair
        sport_map = {
            "nfl": ("football", "nfl"),
            "nba": ("basketball", "nba"),
            "mlb": ("baseball", "mlb"),
            "nhl": ("hockey", "nhl")
        }
        
        if args.sport.lower() in sport_map:
            sport, league = sport_map[args.sport.lower()]
            leagues_to_fetch = {sport: [league]}
        else:
            print(f"Unknown sport: {args.sport}")
            sys.exit(1)
    else:
        leagues_to_fetch = SPORTS_LEAGUES
    
    # Fetch scoreboard data
    scoreboard_data = {}
    
    for sport, leagues in leagues_to_fetch.items():
        for league in leagues:
            print(f"Fetching {sport}/{league} scores...", end="", flush=True)
            scoreboard = get_scoreboard_for_league(client, sport, league, args.date)
            if scoreboard:
                scoreboard_data[f"{sport}/{league}"] = scoreboard
                print(" ✓")
            else:
                print(" ✗")
    
    # Display or save results
    output = display_scoreboard(scoreboard_data, args.output)
    
    if args.save and args.output == "json" and output:
        with open(args.save, "w") as f:
            f.write(output)
        print(f"\nSaved to {args.save}")
    elif args.output == "json":
        print(output)


if __name__ == "__main__":
    main()