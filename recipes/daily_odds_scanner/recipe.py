"""
Daily Odds Scanner Recipe V2

This recipe scans today's games across multiple sports to identify
value opportunities and odds discrepancies using the Site API.
"""

import argparse
import json
from datetime import datetime, date
from typing import Dict, List, Optional, Any
from models.site_api.espn_nfl_api_client import Client as SiteApiClient
from models.site_api.espn_nfl_api_client.api.default import get_scoreboard


class DailyOddsScanner:
    """Scanner for identifying value in daily betting markets."""
    
    def __init__(self):
        self.site_api_client = SiteApiClient(
            base_url="https://site.api.espn.com/apis/site/v2"
        )
        
        # Sports and leagues to scan
        self.sports_leagues = [
            ("football", "nfl", "NFL"),
            ("basketball", "nba", "NBA"),
            ("baseball", "mlb", "MLB"),
            ("hockey", "nhl", "NHL"),
            ("football", "college-football", "NCAAF"),
            ("basketball", "mens-college-basketball", "NCAAB"),
            ("basketball", "wnba", "WNBA"),
        ]
        
        # Value thresholds
        self.edge_threshold = 0.02  # 2% edge to consider valuable
        
        # Store raw games for detailed display
        self.last_raw_games = []
        
        # Options
        self.show_completed = False
        
    def calculate_implied_probability(self, american_odds: int) -> float:
        """Convert American odds to implied probability."""
        if american_odds == 0:
            return 0.0
        if american_odds > 0:
            return 100 / (american_odds + 100)
        else:
            return abs(american_odds) / (abs(american_odds) + 100)
    
    def fetch_games_for_date(self, sport: str, league: str, date_str: str) -> List[Dict[str, Any]]:
        """Fetch games for a specific sport/league/date using scoreboard endpoint."""
        games = []
        
        try:
            response = get_scoreboard.sync_detailed(
                client=self.site_api_client,
                sport=sport,
                league=league,
                dates=date_str
            )
            
            if response.status_code == 200 and response.parsed:
                data = response.parsed.to_dict()
                
                # Extract events from scoreboard
                if "events" in data:
                    for event in data["events"]:
                        game_info = self.extract_game_info(event)
                        if game_info:
                            games.append(game_info)
                
        except Exception as e:
            print(f"Error fetching games for {sport}/{league}: {e}")
            
        return games
    
    def extract_game_info(self, event: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Extract relevant game and odds information from event data."""
        try:
            game_data = {
                "id": event.get("id", ""),
                "name": event.get("name", ""),
                "date": event.get("date", ""),
                "status": event.get("status", {}).get("type", {}).get("name", ""),
                "competitions": []
            }
            
            # Extract competitions and odds
            for competition in event.get("competitions", []):
                comp_data = {
                    "id": competition.get("id", ""),
                    "competitors": [],
                    "odds": []
                }
                
                # Extract competitor info
                for competitor in competition.get("competitors", []):
                    comp_data["competitors"].append({
                        "id": competitor.get("id", ""),
                        "name": competitor.get("team", {}).get("displayName", "Unknown"),
                        "abbreviation": competitor.get("team", {}).get("abbreviation", ""),
                        "home": competitor.get("homeAway", "") == "home",
                        "score": competitor.get("score", "0")
                    })
                
                # Extract odds if available
                if "odds" in competition:
                    for odds_item in competition["odds"]:
                        provider = odds_item.get("provider", {}).get("name", "Unknown")
                        
                        odds_data = {
                            "provider": provider,
                            "details": odds_item.get("details", ""),
                            "overUnder": odds_item.get("overUnder", 0),
                            "spread": odds_item.get("spread", 0),
                            "spreadOdds": odds_item.get("spreadOdds", 0),
                            "awayTeamOdds": {
                                "moneyLine": odds_item.get("awayTeamOdds", {}).get("moneyLine", 0),
                                "spreadOdds": odds_item.get("awayTeamOdds", {}).get("spreadOdds", 0),
                                "underOdds": odds_item.get("awayTeamOdds", {}).get("underOdds", 0)
                            },
                            "homeTeamOdds": {
                                "moneyLine": odds_item.get("homeTeamOdds", {}).get("moneyLine", 0),
                                "spreadOdds": odds_item.get("homeTeamOdds", {}).get("spreadOdds", 0),
                                "overOdds": odds_item.get("homeTeamOdds", {}).get("overOdds", 0)
                            }
                        }
                        
                        comp_data["odds"].append(odds_data)
                
                game_data["competitions"].append(comp_data)
            
            return game_data
            
        except Exception as e:
            print(f"Error extracting game info: {e}")
            return None
    
    def analyze_game_odds(self, game: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze odds for a single game."""
        analysis = {
            "game_id": game["id"],
            "game_name": game["name"],
            "status": game["status"],
            "best_lines": {},
            "arbitrage": [],
            "line_movement": []
        }
        
        for competition in game.get("competitions", []):
            if not competition["odds"]:
                continue
                
            home_team = None
            away_team = None
            
            # Identify home and away teams
            for competitor in competition["competitors"]:
                if competitor["home"]:
                    home_team = competitor["name"]
                else:
                    away_team = competitor["name"]
            
            # Analyze different bet types
            spreads = []
            moneylines = []
            totals = []
            
            for odds in competition["odds"]:
                provider = odds["provider"]
                
                # Spreads
                if odds["spread"] != 0:
                    spreads.append({
                        "provider": provider,
                        "line": odds["spread"],
                        "home_odds": odds["homeTeamOdds"]["spreadOdds"],
                        "away_odds": odds["awayTeamOdds"]["spreadOdds"]
                    })
                
                # Moneylines
                home_ml = odds["homeTeamOdds"]["moneyLine"]
                away_ml = odds["awayTeamOdds"]["moneyLine"]
                if home_ml != 0 and away_ml != 0:
                    moneylines.append({
                        "provider": provider,
                        "home": home_ml,
                        "away": away_ml
                    })
                
                # Totals
                if odds["overUnder"] != 0:
                    totals.append({
                        "provider": provider,
                        "line": odds["overUnder"],
                        "over": odds["homeTeamOdds"]["overOdds"],
                        "under": odds["awayTeamOdds"]["underOdds"]
                    })
            
            # Find best lines
            if spreads:
                best_home_spread = max(spreads, key=lambda x: x["line"])
                best_away_spread = min(spreads, key=lambda x: x["line"])
                analysis["best_lines"]["spread"] = {
                    "home": {
                        "team": home_team,
                        "line": best_home_spread["line"],
                        "provider": best_home_spread["provider"]
                    },
                    "away": {
                        "team": away_team,
                        "line": best_away_spread["line"],
                        "provider": best_away_spread["provider"]
                    }
                }
            
            if moneylines:
                best_home_ml = max(moneylines, key=lambda x: x["home"])
                best_away_ml = max(moneylines, key=lambda x: x["away"])
                analysis["best_lines"]["moneyline"] = {
                    "home": {
                        "team": home_team,
                        "odds": best_home_ml["home"],
                        "provider": best_home_ml["provider"]
                    },
                    "away": {
                        "team": away_team,
                        "odds": best_away_ml["away"],
                        "provider": best_away_ml["provider"]
                    }
                }
                
                # Check for arbitrage
                home_prob = self.calculate_implied_probability(best_home_ml["home"])
                away_prob = self.calculate_implied_probability(best_away_ml["away"])
                total_prob = home_prob + away_prob
                
                if total_prob < 0.98:  # Less than 98% combined probability
                    analysis["arbitrage"].append({
                        "type": "moneyline",
                        "home": best_home_ml,
                        "away": best_away_ml,
                        "total_probability": total_prob,
                        "profit_margin": (1.0 - total_prob) * 100
                    })
            
            if totals:
                highest_total = max(totals, key=lambda x: x["line"])
                lowest_total = min(totals, key=lambda x: x["line"])
                line_diff = highest_total["line"] - lowest_total["line"]
                
                analysis["best_lines"]["total"] = {
                    "highest": {
                        "line": highest_total["line"],
                        "provider": highest_total["provider"]
                    },
                    "lowest": {
                        "line": lowest_total["line"],
                        "provider": lowest_total["provider"]
                    },
                    "difference": line_diff
                }
                
                # Flag significant line differences
                if line_diff >= 1.0:
                    analysis["line_movement"].append({
                        "type": "total",
                        "difference": line_diff,
                        "high_provider": highest_total["provider"],
                        "low_provider": lowest_total["provider"]
                    })
        
        return analysis
    
    def scan_all_games(self, scan_date: Optional[date] = None) -> Dict[str, Any]:
        """Scan all games for a specific date."""
        if scan_date is None:
            scan_date = date.today()
            
        date_str = scan_date.strftime("%Y%m%d")
        
        print(f"Scanning games for {scan_date.strftime('%Y-%m-%d')}...")
        
        all_results = {
            "scan_date": datetime.now().isoformat(),
            "games_date": scan_date.isoformat(),
            "sports": {},
            "summary": {
                "total_games": 0,
                "games_with_odds": 0,
                "total_arbitrage": 0,
                "best_values": []
            }
        }
        
        # Clear previous games
        self.last_raw_games = []
        
        for sport, league, display_name in self.sports_leagues:
            print(f"\nScanning {display_name}...")
            
            # Get games for today
            games = self.fetch_games_for_date(sport, league, date_str)
            
            if not games:
                print(f"  No games found")
                continue
                
            print(f"  Found {len(games)} games")
            
            sport_results = {
                "display_name": display_name,
                "games": []
            }
            
            for game in games:
                # Show game status for debugging
                status = game["status"]
                if not self.show_completed and status not in ["STATUS_SCHEDULED", "STATUS_IN_PROGRESS"]:
                    continue  # Skip completed games
                
                # Store raw game data
                self.last_raw_games.append(game)
                
                analysis = self.analyze_game_odds(game)
                sport_results["games"].append(analysis)
                all_results["summary"]["total_games"] += 1
                
                if analysis["best_lines"]:
                    all_results["summary"]["games_with_odds"] += 1
                    all_results["summary"]["total_arbitrage"] += len(analysis["arbitrage"])
            
            if sport_results["games"]:
                all_results["sports"][f"{sport}/{league}"] = sport_results
        
        return all_results
    
    def format_odds_table(self, game: Dict[str, Any], competitions: List[Dict[str, Any]]) -> List[str]:
        """Format odds as an ASCII table for a single game."""
        output = []
        
        if not competitions or not competitions[0]["odds"]:
            return output
        
        comp = competitions[0]
        odds_data = comp["odds"]
        
        # Get team names
        home_team = ""
        away_team = ""
        for competitor in comp["competitors"]:
            if competitor["home"]:
                home_team = competitor["abbreviation"] or competitor["name"][:10]
            else:
                away_team = competitor["abbreviation"] or competitor["name"][:10]
        
        # Group odds by provider
        providers = {}
        for odds in odds_data:
            provider = odds["provider"][:12]  # Truncate long provider names
            providers[provider] = odds
        
        if not providers:
            return output
        
        # Create spread table
        output.append("\n  SPREADS:")
        output.append("  " + "-" * 60)
        output.append(f"  {'Provider':<15} {'Line':<8} {away_team:<10} {home_team:<10}")
        output.append("  " + "-" * 60)
        
        for provider, odds in providers.items():
            if odds["spread"] != 0:
                line = f"{odds['spread']:+.1f}"
                away_odds = f"{odds['awayTeamOdds']['spreadOdds']:+d}" if odds['awayTeamOdds']['spreadOdds'] != 0 else "N/A"
                home_odds = f"{odds['homeTeamOdds']['spreadOdds']:+d}" if odds['homeTeamOdds']['spreadOdds'] != 0 else "N/A"
                output.append(f"  {provider:<15} {line:<8} {away_odds:<10} {home_odds:<10}")
        
        # Create moneyline table
        ml_available = any(odds["homeTeamOdds"]["moneyLine"] != 0 for odds in providers.values())
        if ml_available:
            output.append("\n  MONEYLINES:")
            output.append("  " + "-" * 60)
            output.append(f"  {'Provider':<15} {away_team:<15} {home_team:<15}")
            output.append("  " + "-" * 60)
            
            for provider, odds in providers.items():
                away_ml = odds["awayTeamOdds"]["moneyLine"]
                home_ml = odds["homeTeamOdds"]["moneyLine"]
                if away_ml != 0 or home_ml != 0:
                    away_str = f"{away_ml:+d}" if away_ml != 0 else "N/A"
                    home_str = f"{home_ml:+d}" if home_ml != 0 else "N/A"
                    output.append(f"  {provider:<15} {away_str:<15} {home_str:<15}")
        
        # Create totals table
        totals_available = any(odds["overUnder"] != 0 for odds in providers.values())
        if totals_available:
            output.append("\n  TOTALS:")
            output.append("  " + "-" * 60)
            output.append(f"  {'Provider':<15} {'Line':<8} {'Over':<10} {'Under':<10}")
            output.append("  " + "-" * 60)
            
            for provider, odds in providers.items():
                if odds["overUnder"] != 0:
                    line = f"{odds['overUnder']}"
                    over_odds = f"{odds['homeTeamOdds']['overOdds']:+d}" if odds['homeTeamOdds']['overOdds'] != 0 else "N/A"
                    under_odds = f"{odds['awayTeamOdds']['underOdds']:+d}" if odds['awayTeamOdds']['underOdds'] != 0 else "N/A"
                    output.append(f"  {provider:<15} {line:<8} {over_odds:<10} {under_odds:<10}")
        
        return output
    
    def format_output(self, results: Dict[str, Any]) -> str:
        """Format scan results for display."""
        output = []
        output.append("=" * 80)
        output.append("DAILY ODDS SCANNER RESULTS")
        output.append(f"Scan Date: {results['scan_date']}")
        output.append(f"Games Date: {results['games_date']}")
        output.append("=" * 80)
        output.append("")
        
        # Summary
        summary = results["summary"]
        output.append("SUMMARY")
        output.append("-" * 40)
        output.append(f"Total Scheduled Games: {summary['total_games']}")
        output.append(f"Games with Odds: {summary['games_with_odds']}")
        output.append(f"Arbitrage Opportunities: {summary['total_arbitrage']}")
        
        if summary['total_games'] == 0:
            output.append("\nNote: No scheduled games found. All games may be completed.")
            output.append("Try using a future date or check during active seasons.")
        elif summary['games_with_odds'] == 0:
            output.append("\nNote: No odds data available for scheduled games.")
            output.append("Odds are typically available closer to game time.")
        
        output.append("")
        
        # Games by sport
        for sport_key, sport_data in results["sports"].items():
            output.append(f"\n{sport_data['display_name']}")
            output.append("=" * 40)
            
            # Store the raw game data for detailed tables
            games_with_data = []
            for game in sport_data["games"]:
                # Find the raw game data to get competitions
                for raw_game in self.last_raw_games:
                    if raw_game["id"] == game["game_id"]:
                        games_with_data.append((game, raw_game))
                        break
            
            for game, raw_game in games_with_data:
                output.append(f"\n{game['game_name']}")
                output.append(f"Status: {game['status']}")
                
                # Show detailed odds table if multiple providers exist
                if raw_game.get("competitions") and len(raw_game["competitions"][0].get("odds", [])) > 1:
                    table_lines = self.format_odds_table(raw_game, raw_game["competitions"])
                    output.extend(table_lines)
                else:
                    # Fall back to simple best lines display
                    if game["best_lines"]:
                        output.append("\nBest Lines:")
                        
                        if "spread" in game["best_lines"]:
                            spread = game["best_lines"]["spread"]
                            output.append(f"  Spread:")
                            output.append(f"    {spread['home']['team']}: {spread['home']['line']:+.1f} ({spread['home']['provider']})")
                            output.append(f"    {spread['away']['team']}: {spread['away']['line']:+.1f} ({spread['away']['provider']})")
                        
                        if "moneyline" in game["best_lines"]:
                            ml = game["best_lines"]["moneyline"]
                            output.append(f"  Moneyline:")
                            output.append(f"    {ml['home']['team']}: {ml['home']['odds']:+d} ({ml['home']['provider']})")
                            output.append(f"    {ml['away']['team']}: {ml['away']['odds']:+d} ({ml['away']['provider']})")
                        
                        if "total" in game["best_lines"]:
                            total = game["best_lines"]["total"]
                            output.append(f"  Total:")
                            output.append(f"    High: {total['highest']['line']} ({total['highest']['provider']})")
                            output.append(f"    Low: {total['lowest']['line']} ({total['lowest']['provider']})")
                            if total["difference"] >= 1.0:
                                output.append(f"    ⚠️  Line difference: {total['difference']} points")
                
                # Arbitrage opportunities
                if game["arbitrage"]:
                    output.append("\n⚡ ARBITRAGE OPPORTUNITY:")
                    for arb in game["arbitrage"]:
                        output.append(f"    Profit Margin: {arb['profit_margin']:.2f}%")
                        output.append(f"    Combined Probability: {arb['total_probability']:.2%}")
        
        return "\n".join(output)


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Scan today's games for betting value across multiple sportsbooks"
    )
    
    parser.add_argument(
        "--date",
        help="Date to scan (YYYY-MM-DD format, default: today)",
        default=None
    )
    
    parser.add_argument(
        "--output",
        help="Output file for results (JSON format)",
        default=None
    )
    
    parser.add_argument(
        "--sport",
        help="Specific sport to scan (e.g., nfl, nba)",
        default=None
    )
    
    parser.add_argument(
        "--show-completed",
        action="store_true",
        help="Show completed games (for demonstration purposes)"
    )
    
    args = parser.parse_args()
    
    # Parse date if provided
    scan_date = None
    if args.date:
        try:
            scan_date = datetime.strptime(args.date, "%Y-%m-%d").date()
        except ValueError:
            print(f"Invalid date format: {args.date}. Use YYYY-MM-DD.")
            return
    
    # Create scanner
    scanner = DailyOddsScanner()
    
    # Set options
    scanner.show_completed = args.show_completed
    
    # Filter sports if specified
    if args.sport:
        original_sports = scanner.sports_leagues
        scanner.sports_leagues = [
            (s, l, d) for s, l, d in original_sports 
            if l.lower() == args.sport.lower()
        ]
        if not scanner.sports_leagues:
            print(f"Sport '{args.sport}' not found.")
            return
    
    # Run scan
    results = scanner.scan_all_games(scan_date)
    
    # Output results
    formatted_output = scanner.format_output(results)
    print(formatted_output)
    
    # Save to file if requested
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\nResults saved to: {args.output}")


if __name__ == "__main__":
    main()