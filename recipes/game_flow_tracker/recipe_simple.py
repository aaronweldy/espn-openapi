#!/usr/bin/env python3
"""
Track game flow, score changes, and momentum shifts for a specific game.

This recipe analyzes game data to show scoring by period and key game stats.
"""

import argparse
import json
import sys
import time
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

# Import generated models
from models.site_api.espn_nfl_api_client import Client as SiteApiClient
from models.site_api.espn_nfl_api_client.types import UNSET
from models.site_api.espn_nfl_api_client.api.default import get_game_summary
from models.site_api.espn_nfl_api_client.models.sport_enum import SportEnum
from models.site_api.espn_nfl_api_client.models.league_enum import LeagueEnum

# Sport configurations
SPORT_CONFIG = {
    "football": {
        "periods": 4,
        "period_name": "Quarter",
        "sport_enum": SportEnum.FOOTBALL,
        "league_enum": LeagueEnum.NFL
    },
    "basketball": {
        "periods": 4,
        "period_name": "Quarter", 
        "sport_enum": SportEnum.BASKETBALL,
        "league_enum": LeagueEnum.NBA
    },
    "hockey": {
        "periods": 3,
        "period_name": "Period",
        "sport_enum": SportEnum.HOCKEY,
        "league_enum": LeagueEnum.NHL
    },
    "baseball": {
        "periods": 9,
        "period_name": "Inning",
        "sport_enum": SportEnum.BASEBALL,
        "league_enum": LeagueEnum.MLB
    }
}


class GameFlowTracker:
    def __init__(self, sport: str = "football", league: str = "nfl"):
        self.sport = sport
        self.league = league
        self.sport_config = SPORT_CONFIG.get(sport, SPORT_CONFIG["football"])
        self.site_client = SiteApiClient(base_url="https://site.api.espn.com/apis/site/v2")
        
    def get_game_summary(self, event_id: str) -> Optional[Any]:
        """Fetch game summary data."""
        try:
            response = get_game_summary.sync_detailed(
                client=self.site_client,
                sport=self.sport_config["sport_enum"],
                league=self.sport_config["league_enum"],
                event=event_id
            )
            
            if response.status_code == 200:
                return response.parsed
            else:
                print(f"Error fetching game summary: HTTP {response.status_code}")
                return None
                
        except Exception as e:
            print(f"Error fetching game summary: {e}")
            return None
    
    def analyze_game_flow(self, event_id: str) -> Dict:
        """Analyze game flow from summary data."""
        # Get game summary
        summary = self.get_game_summary(event_id)
        if not summary:
            return {"error": "Could not fetch game summary"}
        
        # Extract and analyze game info
        game_info = self._extract_game_info(summary)
        flow_analysis = self._analyze_flow(summary, game_info)
        
        return {**game_info, **flow_analysis}
    
    def _extract_game_info(self, summary: Any) -> Dict:
        """Extract basic game information from summary."""
        info = {
            "event_id": None,
            "status": "Unknown",
            "home_team": None,
            "away_team": None,
            "home_score": 0,
            "away_score": 0,
            "period": 0,
            "clock": "",
            "venue": None,
            "attendance": None
        }
        
        if hasattr(summary, 'header') and summary.header:
            header = summary.header
            
            if hasattr(header, 'id'):
                info["event_id"] = header.id
                
            if hasattr(header, 'competitions') and header.competitions:
                comp = header.competitions[0]
                
                # Get status
                if hasattr(comp, 'status') and comp.status:
                    status = comp.status
                    if hasattr(status, 'type') and status.type:
                        info["status"] = status.type.description or "Unknown"
                    if hasattr(status, 'period') and status.period is not UNSET:
                        info["period"] = status.period
                    if hasattr(status, 'display_clock'):
                        info["clock"] = status.display_clock
                
                # Get teams and scores
                if hasattr(comp, 'competitors') and comp.competitors:
                    for competitor in comp.competitors:
                        if hasattr(competitor, 'home_away'):
                            team_info = {
                                "name": competitor.team.display_name if competitor.team else "Unknown",
                                "abbreviation": competitor.team.abbreviation if competitor.team else "UNK",
                                "score": int(competitor.score) if competitor.score and competitor.score is not UNSET else 0,
                                "record": competitor.records[0].summary if competitor.records and competitor.records is not UNSET else None
                            }
                            
                            if competitor.home_away == "home":
                                info["home_team"] = team_info
                                info["home_score"] = team_info["score"]
                            else:
                                info["away_team"] = team_info
                                info["away_score"] = team_info["score"]
                
                # Get venue info
                if hasattr(comp, 'venue') and comp.venue:
                    info["venue"] = comp.venue.full_name if hasattr(comp.venue, 'full_name') else None
                
                # Get attendance
                if hasattr(comp, 'attendance') and comp.attendance is not UNSET:
                    info["attendance"] = comp.attendance
        
        return info
    
    def _analyze_flow(self, summary, game_info: Dict) -> Dict:
        """Analyze game flow from summary data."""
        analysis = {
            "scoring_by_period": {},
            "lead_changes": 0,
            "largest_lead": {"team": None, "points": 0},
            "total_points": game_info["home_score"] + game_info["away_score"],
            "point_differential": abs(game_info["home_score"] - game_info["away_score"]),
            "is_overtime": False,
            "is_close_game": abs(game_info["home_score"] - game_info["away_score"]) <= 7
        }
        
        # Check for scoring plays if available
        if hasattr(summary, 'scoring_plays') and summary.scoring_plays:
            period_scores = {}
            home_score = 0
            away_score = 0
            last_leader = None
            
            for play in summary.scoring_plays:
                period = play.period.number if hasattr(play, 'period') and play.period else 1
                
                if period not in period_scores:
                    period_scores[period] = {"home": 0, "away": 0}
                
                # Determine which team scored
                if hasattr(play, 'team') and play.team:
                    if play.team.id == game_info["home_team"].get("id"):
                        period_scores[period]["home"] += play.score_value
                        home_score += play.score_value
                    else:
                        period_scores[period]["away"] += play.score_value
                        away_score += play.score_value
                
                # Track lead changes
                current_leader = "home" if home_score > away_score else ("away" if away_score > home_score else "tied")
                if current_leader != last_leader and last_leader is not None:
                    analysis["lead_changes"] += 1
                last_leader = current_leader
                
                # Track largest lead
                lead_size = abs(home_score - away_score)
                if lead_size > analysis["largest_lead"]["points"]:
                    analysis["largest_lead"] = {
                        "team": game_info["home_team"]["name"] if home_score > away_score else game_info["away_team"]["name"],
                        "points": lead_size
                    }
            
            analysis["scoring_by_period"] = period_scores
        
        # Check for overtime
        if isinstance(game_info["period"], int) and game_info["period"] > self.sport_config["periods"]:
            analysis["is_overtime"] = True
        
        # Extract additional stats if available
        if hasattr(summary, 'leaders') and summary.leaders:
            analysis["game_leaders"] = self._extract_leaders(summary.leaders)
        
        return analysis
    
    def _extract_leaders(self, leaders) -> Dict:
        """Extract game leaders information."""
        leader_info = {}
        
        for category in leaders:
            if hasattr(category, 'name') and hasattr(category, 'leaders'):
                cat_name = category.name.lower().replace(' ', '_')
                leader_info[cat_name] = []
                
                for leader in category.leaders[:2]:  # Top 2 in each category
                    if hasattr(leader, 'athlete') and leader.athlete:
                        leader_info[cat_name].append({
                            "name": leader.athlete.display_name,
                            "team": leader.team.abbreviation if leader.team else "UNK",
                            "value": leader.value,
                            "display": leader.display_value
                        })
        
        return leader_info
    
    def display_game_flow(self, flow_data: Dict):
        """Display game flow analysis."""
        if "error" in flow_data:
            print(f"Error: {flow_data['error']}")
            return
            
        # Header
        home = flow_data["home_team"]["name"] if flow_data["home_team"] else "Home"
        away = flow_data["away_team"]["name"] if flow_data["away_team"] else "Away"
        print(f"\n=== GAME FLOW: {away} vs {home} ===")
        print(f"Event ID: {flow_data['event_id']}")
        print(f"Status: {flow_data['status']} - {away} {flow_data['away_score']}, {home} {flow_data['home_score']}")
        
        if flow_data["venue"]:
            print(f"Venue: {flow_data['venue']}")
        if flow_data["attendance"]:
            print(f"Attendance: {flow_data['attendance']:,}")
        print()
        
        # Game characteristics
        print("GAME CHARACTERISTICS:")
        print(f"Total Points: {flow_data['total_points']}")
        print(f"Point Differential: {flow_data['point_differential']}")
        if flow_data["is_overtime"]:
            print("Game went to OVERTIME")
        if flow_data["is_close_game"]:
            print("CLOSE GAME (within 7 points)")
        print()
        
        # Period scoring if available
        if flow_data["scoring_by_period"]:
            print("SCORING BY PERIOD:")
            home_abbrev = flow_data["home_team"]["abbreviation"]
            away_abbrev = flow_data["away_team"]["abbreviation"]
            
            # Header
            periods = sorted(flow_data["scoring_by_period"].keys())
            period_name = self.sport_config["period_name"][:1]
            header = f"Team  | " + " | ".join([f"{period_name}{p}" for p in periods]) + " | Total"
            print(header)
            print("-" * len(header))
            
            # Away team
            away_line = f"{away_abbrev:5} | "
            away_total = 0
            for p in periods:
                score = flow_data["scoring_by_period"][p]["away"]
                away_total += score
                away_line += f"{score:2} | "
            away_line += f"{away_total:3}"
            print(away_line)
            
            # Home team
            home_line = f"{home_abbrev:5} | "
            home_total = 0
            for p in periods:
                score = flow_data["scoring_by_period"][p]["home"]
                home_total += score
                home_line += f"{score:2} | "
            home_line += f"{home_total:3}"
            print(home_line)
            print()
        
        # Key stats
        if flow_data["lead_changes"] > 0:
            print(f"Lead Changes: {flow_data['lead_changes']}")
        if flow_data["largest_lead"]["team"]:
            print(f"Largest Lead: {flow_data['largest_lead']['team']} by {flow_data['largest_lead']['points']}")
        
        # Game leaders
        if flow_data.get("game_leaders"):
            print("\nGAME LEADERS:")
            for category, leaders in flow_data["game_leaders"].items():
                cat_display = category.replace('_', ' ').title()
                print(f"\n{cat_display}:")
                for leader in leaders:
                    print(f"  {leader['name']} ({leader['team']}): {leader['display']}")
    
    def track_live(self, event_id: str, interval: int = 30):
        """Track game with live updates."""
        print(f"Tracking game {event_id} with updates every {interval} seconds")
        print("Press Ctrl+C to stop\n")
        
        last_home_score = 0
        last_away_score = 0
        
        try:
            while True:
                flow_data = self.analyze_game_flow(event_id)
                
                # Check for score changes
                if flow_data.get("home_score", 0) != last_home_score or flow_data.get("away_score", 0) != last_away_score:
                    # Score changed - show notification
                    print(f"\n🚨 SCORE UPDATE: {flow_data['away_team']['name']} {flow_data['away_score']}, "
                          f"{flow_data['home_team']['name']} {flow_data['home_score']}")
                    last_home_score = flow_data.get("home_score", 0)
                    last_away_score = flow_data.get("away_score", 0)
                
                # Clear screen and display update
                print("\033[2J\033[H")
                self.display_game_flow(flow_data)
                
                # Check if game is final
                if "final" in flow_data.get("status", "").lower():
                    print("\n✅ Game has ended.")
                    break
                
                # Wait for next update
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print("\n\nStopped live tracking.")


def main():
    """Main function to run the recipe."""
    parser = argparse.ArgumentParser(description="Track game flow and momentum shifts")
    parser.add_argument("--event-id", required=True, help="ESPN event/game ID")
    parser.add_argument("--sport", default="football", 
                        choices=["football", "basketball", "hockey", "baseball"],
                        help="Sport type")
    parser.add_argument("--league", default="nfl", help="League (nfl, nba, nhl, mlb)")
    parser.add_argument("--live", action="store_true", help="Track live with updates")
    parser.add_argument("--interval", type=int, default=30, 
                        help="Update interval in seconds for live tracking")
    parser.add_argument("--export", help="Export data to JSON file")
    
    args = parser.parse_args()
    
    # Create tracker
    tracker = GameFlowTracker(sport=args.sport, league=args.league)
    
    # Track game
    if args.live:
        tracker.track_live(args.event_id, args.interval)
    else:
        # Single analysis
        flow_data = tracker.analyze_game_flow(args.event_id)
        tracker.display_game_flow(flow_data)
        
        # Export if requested
        if args.export:
            with open(args.export, "w") as f:
                json.dump(flow_data, f, indent=2, default=str)
            print(f"\nExported data to {args.export}")


if __name__ == "__main__":
    main()