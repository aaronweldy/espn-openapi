"""
Futures Value Scanner Recipe

This recipe scans futures betting markets across multiple sports to identify
value opportunities based on current odds and historical data.
"""

import argparse
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any
from models.sports_core_api.espn_sports_core_api_client import Client as SportsCoreClient
from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_season_futures
)


class FuturesValueScanner:
    """Scanner for identifying value in futures betting markets."""
    
    def __init__(self):
        self.sports_core_client = SportsCoreClient(
            base_url="https://sports.core.api.espn.com"
        )
        
        # Sports and leagues to scan
        self.sports_leagues = [
            ("football", "nfl"),
            ("basketball", "nba"),
            ("baseball", "mlb"),
            ("hockey", "nhl"),
            ("football", "college-football"),
            ("basketball", "mens-college-basketball"),
        ]
        
        # Value thresholds
        self.edge_threshold = 0.02  # 2% edge to consider valuable
        
        # Common team ID mappings (partial list for demonstration)
        # Note: IDs can overlap between sports, so context matters
        self.team_names = {
            # NFL
            "1": "ATL", "2": "BUF", "3": "CHI", "4": "CIN", "5": "CLE",
            "6": "DAL", "7": "DEN", "8": "DET", "9": "GB", "10": "TEN",
            "11": "IND", "12": "KC", "13": "LV", "14": "LAR", "15": "MIA",
            "16": "MIN", "17": "NE", "18": "NO", "19": "NYG", "20": "NYJ",
            "21": "PHI", "22": "ARI", "23": "PIT", "24": "LAC", "25": "SF",
            "26": "SEA", "27": "TB", "28": "WSH", "29": "CAR", "30": "JAX",
            "33": "BAL", "34": "HOU"
        }
        
    def extract_id_from_ref(self, ref_url: str) -> str:
        """Extract ID from ESPN API $ref URL."""
        import re
        # Match patterns like /teams/12 or /athletes/12483
        match = re.search(r'/(teams|athletes)/(\d+)', ref_url)
        if match:
            return match.group(2)
        return "Unknown"
        
    def fetch_futures(self, sport: str, league: str, year: int) -> Optional[Dict[str, Any]]:
        """Fetch futures data for a specific sport/league/year."""
        try:
            response = get_season_futures.sync_detailed(
                client=self.sports_core_client,
                sport=sport,
                league=league,
                year=year
            )
            
            if response.status_code == 200 and response.parsed:
                data = response.parsed.to_dict()
                if 'items' in data and data['items']:
                    print(f"  Found {len(data['items'])} futures markets")
                    # Debug: check provider count for first market
                    if data['items'] and 'futures' in data['items'][0]:
                        providers = len(data['items'][0]['futures'])
                        print(f"  First market has {providers} provider(s)")
                elif 'futures' in data and data['futures']:
                    print(f"  Found {len(data['futures'])} futures markets")
                else:
                    print(f"  No futures data found in response")
                return data
            else:
                print(f"  API returned status {response.status_code}")
                return None
                
        except Exception as e:
            print(f"Error fetching futures for {sport}/{league}/{year}: {e}")
            return None
    
    def calculate_implied_probability(self, american_odds: int) -> float:
        """Convert American odds to implied probability."""
        if american_odds > 0:
            return 100 / (american_odds + 100)
        else:
            return abs(american_odds) / (abs(american_odds) + 100)
    
    def identify_arbitrage_opportunities(self, market_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify arbitrage opportunities across different providers."""
        opportunities = []
        
        # Extract markets from the response
        items = market_data.get("items", market_data.get("futures", []))
        if not items:
            return opportunities
            
        for market in items:
            market_name = market.get("displayName", market.get("name", "Unknown Market"))
            
            # Get futures data (different structure based on API response)
            futures_data = market.get("futures", [])
            if not futures_data or len(futures_data) < 2:
                continue  # Need at least 2 providers for arbitrage
                
            # Group all selections across providers
            all_provider_odds = {}
            
            for future in futures_data:
                provider_name = future.get("provider", {}).get("name", "Unknown Provider")
                books = future.get("books", [])
                
                for book in books:
                    # Handle different structures for selection name
                    if "athlete" in book and isinstance(book["athlete"], dict):
                        if "$ref" in book["athlete"]:
                            athlete_id = self.extract_id_from_ref(book["athlete"]["$ref"])
                            selection = f"Athlete {athlete_id}"
                        else:
                            selection = book["athlete"].get("displayName", book["athlete"].get("name", "Unknown"))
                    elif "team" in book and isinstance(book["team"], dict):
                        if "$ref" in book["team"]:
                            team_id = self.extract_id_from_ref(book["team"]["$ref"])
                            team_name = self.team_names.get(team_id, f"Team {team_id}")
                            selection = team_name
                        else:
                            selection = book["team"].get("displayName", book["team"].get("name", "Unknown"))
                    else:
                        continue
                    
                    odds_value = book.get("value", 0)
                    # Convert string odds to int (e.g., "+550" to 550, "-110" to -110)
                    if isinstance(odds_value, str):
                        try:
                            odds_value = int(odds_value)
                        except ValueError:
                            continue
                    
                    if odds_value == 0 or odds_value > 100000:  # Filter out unrealistic odds
                        continue
                    
                    if selection not in all_provider_odds:
                        all_provider_odds[selection] = []
                        
                    all_provider_odds[selection].append({
                        "provider": provider_name,
                        "odds": odds_value,
                        "implied_prob": self.calculate_implied_probability(odds_value)
                    })
            
            # Check for arbitrage across providers for same selection
            for selection, odds_list in all_provider_odds.items():
                if len(odds_list) < 2:
                    continue
                    
                # Find best odds
                best_odds = max(odds_list, key=lambda x: x["odds"])
                worst_odds = min(odds_list, key=lambda x: x["odds"])
                
                # Calculate edge
                edge = best_odds["implied_prob"] - worst_odds["implied_prob"]
                
                if edge > self.edge_threshold:
                    opportunities.append({
                        "market": market.get("name", "Unknown Market"),
                        "selection": selection,
                        "best_odds": best_odds,
                        "worst_odds": worst_odds,
                        "edge": edge,
                        "edge_percentage": edge * 100
                    })
        
        return opportunities
    
    def find_value_bets(self, market_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Find value bets based on odds discrepancies."""
        value_bets = []
        
        # Extract markets from the response
        items = market_data.get("items", market_data.get("futures", []))
        if not items:
            return value_bets
            
        for market in items:
            market_name = market.get("displayName", market.get("name", "Unknown Market"))
            
            # Get futures data
            futures_data = market.get("futures", [])
            if not futures_data:
                continue
                
            # Aggregate all odds across providers
            all_selections = {}
            
            for future in futures_data:
                provider_name = future.get("provider", {}).get("name", "Unknown Provider")
                books = future.get("books", [])
                
                for book in books:
                    # Handle different structures for selection name
                    if "athlete" in book and isinstance(book["athlete"], dict):
                        if "$ref" in book["athlete"]:
                            athlete_id = self.extract_id_from_ref(book["athlete"]["$ref"])
                            selection = f"Athlete {athlete_id}"
                        else:
                            selection = book["athlete"].get("displayName", book["athlete"].get("name", "Unknown"))
                    elif "team" in book and isinstance(book["team"], dict):
                        if "$ref" in book["team"]:
                            team_id = self.extract_id_from_ref(book["team"]["$ref"])
                            team_name = self.team_names.get(team_id, f"Team {team_id}")
                            selection = team_name
                        else:
                            selection = book["team"].get("displayName", book["team"].get("name", "Unknown"))
                    else:
                        continue
                    
                    odds_value = book.get("value", 0)
                    # Convert string odds to int (e.g., "+550" to 550, "-110" to -110)
                    if isinstance(odds_value, str):
                        try:
                            odds_value = int(odds_value)
                        except ValueError:
                            continue
                    
                    if odds_value == 0 or odds_value > 100000:  # Filter out unrealistic odds
                        continue
                    
                    if selection not in all_selections:
                        all_selections[selection] = []
                        
                    all_selections[selection].append({
                        "provider": provider_name,
                        "odds": odds_value,
                        "implied_prob": self.calculate_implied_probability(odds_value)
                    })
            
            # Find value in selections with multiple providers
            for selection, odds_list in all_selections.items():
                if len(odds_list) < 2:  # Need at least 2 providers for comparison
                    continue
                    
                # Calculate average implied probability
                avg_prob = sum(p["implied_prob"] for p in odds_list) / len(odds_list)
                
                # Find best odds
                best_odds_data = max(odds_list, key=lambda x: x["odds"])
                
                # Calculate value - positive value means the odds are better than average
                # Lower implied probability = better odds for the bettor
                value = best_odds_data["implied_prob"] - avg_prob
                
                # Only show if the best odds offer better value than average
                if value < -self.edge_threshold:  # Negative means better for bettor
                    # Flag likely errors (extreme deviations)
                    likely_error = -value > 0.20  # More than 20% difference
                    
                    value_bets.append({
                        "market": market_name,
                        "selection": selection,
                        "best_odds": best_odds_data["odds"],
                        "provider": best_odds_data["provider"],
                        "implied_prob": best_odds_data["implied_prob"],
                        "avg_implied_prob": avg_prob,
                        "value": -value,  # Make positive for display
                        "value_percentage": -value * 100,  # Make positive for display
                        "likely_error": likely_error
                    })
        
        return sorted(value_bets, key=lambda x: x["value"], reverse=True)
    
    def scan_all_markets(self, year: Optional[int] = None) -> Dict[str, Any]:
        """Scan all configured sports/leagues for value opportunities."""
        if year is None:
            year = datetime.now().year
            
        results = {
            "scan_date": datetime.now().isoformat(),
            "year": year,
            "arbitrage_opportunities": [],
            "value_bets": [],
            "summary": {
                "total_markets_scanned": 0,
                "total_arbitrage_opportunities": 0,
                "total_value_bets": 0,
                "best_value_percentage": 0
            }
        }
        
        for sport, league in self.sports_leagues:
            print(f"\nScanning {sport}/{league} futures for {year}...")
            
            futures_data = self.fetch_futures(sport, league, year)
            if not futures_data:
                continue
                
            results["summary"]["total_markets_scanned"] += 1
            
            # Find arbitrage opportunities
            arbitrage_opps = self.identify_arbitrage_opportunities(futures_data)
            for opp in arbitrage_opps:
                opp["sport"] = sport
                opp["league"] = league
                results["arbitrage_opportunities"].append(opp)
            
            # Find value bets
            value_bets = self.find_value_bets(futures_data)
            for bet in value_bets:
                bet["sport"] = sport
                bet["league"] = league
                results["value_bets"].append(bet)
                
                # Update best value
                if bet["value_percentage"] > results["summary"]["best_value_percentage"]:
                    results["summary"]["best_value_percentage"] = bet["value_percentage"]
        
        # Update summary
        results["summary"]["total_arbitrage_opportunities"] = len(results["arbitrage_opportunities"])
        results["summary"]["total_value_bets"] = len(results["value_bets"])
        
        # Sort results by value
        results["arbitrage_opportunities"].sort(key=lambda x: x["edge_percentage"], reverse=True)
        results["value_bets"].sort(key=lambda x: x["value_percentage"], reverse=True)
        
        return results
    
    def format_results(self, results: Dict[str, Any]) -> str:
        """Format scan results for display."""
        output = []
        output.append("=" * 80)
        output.append("FUTURES VALUE SCANNER RESULTS")
        output.append(f"Scan Date: {results['scan_date']}")
        output.append(f"Year: {results['year']}")
        output.append("=" * 80)
        output.append("")
        
        # Summary
        summary = results["summary"]
        output.append("SUMMARY")
        output.append("-" * 40)
        output.append(f"Markets Scanned: {summary['total_markets_scanned']}")
        output.append(f"Arbitrage Opportunities: {summary['total_arbitrage_opportunities']}")
        output.append(f"Value Bets Found: {summary['total_value_bets']}")
        output.append(f"Best Value: {summary['best_value_percentage']:.2f}%")
        output.append("")
        
        # Top Arbitrage Opportunities
        if results["arbitrage_opportunities"]:
            output.append("TOP ARBITRAGE OPPORTUNITIES")
            output.append("-" * 40)
            for i, opp in enumerate(results["arbitrage_opportunities"][:5]):
                output.append(f"\n{i+1}. {opp['sport'].upper()}/{opp['league'].upper()}")
                output.append(f"   Market: {opp['market']}")
                output.append(f"   Selection: {opp['selection']}")
                output.append(f"   Best Odds: {opp['best_odds']['odds']:+d} ({opp['best_odds']['provider']})")
                output.append(f"   Worst Odds: {opp['worst_odds']['odds']:+d} ({opp['worst_odds']['provider']})")
                output.append(f"   Edge: {opp['edge_percentage']:.2f}%")
        
        output.append("")
        
        # Top Value Bets
        if results["value_bets"]:
            output.append("TOP VALUE BETS")
            output.append("-" * 40)
            for i, bet in enumerate(results["value_bets"][:10]):
                output.append(f"\n{i+1}. {bet['sport'].upper()}/{bet['league'].upper()}")
                output.append(f"   Market: {bet['market']}")
                output.append(f"   Selection: {bet['selection']}")
                output.append(f"   Best Odds: {bet['best_odds']:+d} ({bet['provider']})")
                output.append(f"   Implied Prob: {bet['implied_prob']:.2%}")
                output.append(f"   Market Avg Prob: {bet['avg_implied_prob']:.2%}")
                output.append(f"   Value: {bet['value_percentage']:.2f}%")
                if bet.get('likely_error', False):
                    output.append("   ⚠️  WARNING: Likely stale line or data error")
        
        return "\n".join(output)


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Scan futures betting markets for value opportunities"
    )
    parser.add_argument(
        "--year",
        type=int,
        help="Year to scan futures for (default: current year)"
    )
    parser.add_argument(
        "--output",
        help="Output file for results (JSON format)"
    )
    parser.add_argument(
        "--edge-threshold",
        type=float,
        default=0.05,
        help="Minimum edge percentage to consider valuable (default: 0.05)"
    )
    
    args = parser.parse_args()
    
    # Create scanner
    scanner = FuturesValueScanner()
    
    # Set custom edge threshold if provided
    if args.edge_threshold:
        scanner.edge_threshold = args.edge_threshold
    
    # Run scan
    print(f"Starting futures value scan for year {args.year or datetime.now().year}...")
    results = scanner.scan_all_markets(year=args.year)
    
    # Display results
    formatted_results = scanner.format_results(results)
    print(formatted_results)
    
    # Save to file if requested
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\nResults saved to: {args.output}")


if __name__ == "__main__":
    main()