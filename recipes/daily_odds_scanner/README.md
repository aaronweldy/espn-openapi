# Daily Odds Scanner

Scans current and future games across multiple sports to identify betting value opportunities by comparing odds across different sportsbooks.

## Features

- **Multi-Sport Coverage**: Scans NFL, NBA, MLB, NHL, NCAAF, NCAAB, WNBA games
- **Comprehensive Odds Analysis**: Analyzes spreads, moneylines, and totals
- **Best Line Identification**: Finds the best available odds for each bet type
- **Arbitrage Detection**: Identifies potential arbitrage opportunities
- **Real-Time Data**: Fetches current odds from multiple sportsbooks
- **Flexible Date Selection**: Scan games for any date

## Usage

```bash
# Scan today's games
python -m recipes.daily_odds_scanner.recipe

# Scan games for a specific date
python -m recipes.daily_odds_scanner.recipe --date 2024-12-25

# Scan only NFL games
python -m recipes.daily_odds_scanner.recipe --sport nfl

# Save results to JSON
python -m recipes.daily_odds_scanner.recipe --output odds_scan.json
```

## Options

- `--date`: Date to scan in YYYY-MM-DD format (default: today)
- `--sport`: Specific sport/league to scan (e.g., nfl, nba, mlb, nhl)
- `--output`: Save results to JSON file

## Output Format

The scanner provides:

1. **Game Information**: Name, time, number of odds providers
2. **Best Lines**:
   - Spread: Best lines for home and away teams
   - Moneyline: Best odds for each team
   - Total: Highest/lowest totals and best over/under odds
3. **Arbitrage Alerts**: Opportunities where combined probabilities < 100%

## Example Output

```
================================================================================
DAILY ODDS SCANNER RESULTS
Scan Date: 2025-06-06T23:00:00.000000
Games Date: 2025-06-06
================================================================================

SUMMARY
----------------------------------------
Total Games Found: 15
Arbitrage Opportunities: 2

NFL
----------------------------------------

Kansas City Chiefs @ Buffalo Bills
Game Time: 2025-06-06T20:15:00Z
Providers: 8

Best Lines:
  Spread:
    Home: +3.5 (DraftKings)
    Away: -3.0 (FanDuel)
  Moneyline:
    Home: +155 (BetMGM)
    Away: -145 (Caesars)
  Total:
    Highest: 48.5 (DraftKings)
    Lowest: 47.0 (BetRivers)
    Best Over: -105 (FanDuel)
    Best Under: -105 (DraftKings)
```

## How It Works

1. **Event Discovery**: Fetches all games scheduled for the selected date
2. **Odds Collection**: Retrieves odds from all available providers for each game
3. **Analysis**: Compares odds to find:
   - Best available lines for each bet type
   - Significant line discrepancies
   - Potential arbitrage opportunities
4. **Reporting**: Presents findings in an easy-to-read format

## Notes

- Odds are subject to rapid change; always verify before placing bets
- Arbitrage opportunities are rare and may indicate stale lines
- Provider availability varies by sport and location
- Some games may not have odds from all providers
- Historical odds data is not available for completed games
- For future games, odds availability depends on how far out the game is scheduled
- ESPN BET typically has odds available furthest in advance