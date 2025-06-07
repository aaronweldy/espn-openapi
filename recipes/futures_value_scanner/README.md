# Futures Value Scanner Recipe

Scans futures betting markets across multiple sports to identify value opportunities based on odds discrepancies between providers.

## Overview

This recipe analyzes futures betting markets (championship winners, MVP awards, etc.) to find:
- **Arbitrage opportunities**: Significant odds differences between providers
- **Value bets**: Selections where odds appear mispriced compared to market consensus

## Features

- Scans multiple sports: NFL, NBA, MLB, NHL, NCAAF, NCAAB
- Identifies arbitrage opportunities across different betting providers
- Finds value bets based on implied probability analysis
- Calculates edge percentages for each opportunity
- Sorts results by value to highlight best opportunities

## Usage

### Basic Scan
```bash
python -m recipes.futures_value_scanner.recipe
```

### Scan Specific Year
```bash
python -m recipes.futures_value_scanner.recipe --year 2024
```

### Save Results to File
```bash
python -m recipes.futures_value_scanner.recipe --output futures_scan_results.json
```

### Custom Edge Threshold
```bash
python -m recipes.futures_value_scanner.recipe --edge-threshold 0.10  # 10% minimum edge
```

## Example Output

```
================================================================================
FUTURES VALUE SCANNER RESULTS
Scan Date: 2025-01-06T10:30:00
Year: 2025
================================================================================

SUMMARY
----------------------------------------
Markets Scanned: 6
Arbitrage Opportunities: 3
Value Bets Found: 15
Best Value: 12.50%

TOP ARBITRAGE OPPORTUNITIES
----------------------------------------

1. FOOTBALL/NFL
   Market: Super Bowl Winner
   Selection: Kansas City Chiefs
   Best Odds: +450 (DraftKings)
   Worst Odds: +380 (FanDuel)
   Edge: 8.25%

TOP VALUE BETS
----------------------------------------

1. BASKETBALL/NBA
   Market: NBA Championship
   Selection: Denver Nuggets
   Best Odds: +700 (BetMGM)
   Implied Prob: 12.50%
   Market Avg Prob: 15.25%
   Value: 2.75%
```

## How It Works

1. **Data Collection**: Fetches futures odds from ESPN's API for configured sports/leagues
2. **Implied Probability**: Converts American odds to implied probabilities
3. **Arbitrage Detection**: Identifies selections with significant odds differences
4. **Value Calculation**: Compares individual odds against market consensus
5. **Ranking**: Sorts opportunities by edge/value percentage

## Configuration

The scanner uses these default settings:
- **Edge Threshold**: 5% (adjustable via command line)
- **Sports**: NFL, NBA, MLB, NHL, NCAAF, NCAAB
- **Minimum Providers**: 3 (for value bet analysis)

## Output Fields

### Arbitrage Opportunities
- `market`: The futures market (e.g., "Super Bowl Winner")
- `selection`: The team/player selection
- `best_odds`: Highest odds available and provider
- `worst_odds`: Lowest odds available and provider
- `edge_percentage`: The arbitrage edge as a percentage

### Value Bets
- `market`: The futures market
- `selection`: The team/player selection
- `best_odds`: Best available odds
- `provider`: Provider offering best odds
- `implied_prob`: Implied probability of best odds
- `avg_implied_prob`: Market average implied probability
- `value_percentage`: The value edge as a percentage

## Notes

- Futures availability varies by season and sport
- Some markets may not have odds from multiple providers
- Edge calculations assume efficient market hypothesis
- Always verify odds directly with providers before betting