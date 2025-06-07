# Fantasy Draft Value Finder

Identify undervalued players for your fantasy football draft by analyzing projections, ownership percentages, and average draft position (ADP) to calculate value scores.

## Features

- **Value Score Calculation**: Combines projected points, ADP, and ownership data to identify undervalued players
- **Position Filtering**: Focus on specific positions (QB, RB, WR, TE, DST, K)
- **Scoring System Support**: Adjust calculations for PPR or standard scoring
- **ADP Range Filtering**: Find sleepers in specific draft rounds
- **Multiple Output Formats**: Console table, JSON, or CSV export
- **Late Round Sleeper Detection**: Automatically highlights high-value late-round picks
- **Position-based Analysis**: Shows top value picks for each position

## How It Works

The recipe calculates a value score for each player based on ownership and ADP data:

**When projections are unavailable** (current state):
- For players with >20% ownership and ADP >100:
  - `Value Score = (% Owned / 100) × ((300 - ADP) / 300) × 100`
- This identifies players who are highly owned but available in later rounds

**When projections are available** (future enhancement):
- `Value Score = (Projected Points / ADP) × (100 - % Owned) / 100 × Round Boost`
- Where Round Boost = 1.2x for ADP > 100, 1.5x for ADP > 150

The current implementation focuses on the ownership vs. ADP mismatch, which can indicate:
- Players recovering from injury who are being drafted later
- Handcuffs with standalone value
- Veterans being undervalued vs. rookies

## Usage

```bash
python recipes/fantasy_draft_value_finder/recipe.py [options]
```

## Options

- `--year YEAR`: Season year (default: 2025)
- `--position {qb,rb,wr,te,dst,k}`: Filter by specific position
- `--scoring {ppr,standard}`: Scoring system (default: ppr)
- `--min-adp N`: Minimum ADP to consider (default: 1)
- `--max-adp N`: Maximum ADP to consider (default: 300)
- `--limit N`: Number of results to show (default: 25)
- `--output {console,json,csv}`: Output format (default: console)
- `--save FILENAME`: Save output to file

## Examples

### Find Top 25 Overall Value Picks
```bash
python recipe.py
```

### Find Undervalued Running Backs
```bash
python recipe.py --position rb --limit 15
```

### Find Late Round Sleepers (Rounds 10+)
```bash
python recipe.py --min-adp 120 --max-adp 300
```

### Export Top 50 Values to CSV
```bash
python recipe.py --limit 50 --output csv --save draft_values.csv
```

### Standard Scoring League Values
```bash
python recipe.py --scoring standard
```

### Mid-Round Value Targets (Rounds 5-10)
```bash
python recipe.py --min-adp 50 --max-adp 120
```

### Save Full Analysis as JSON
```bash
python recipe.py --limit 200 --output json --save fantasy_values_2025.json
```

## Output Format

### Console Output
```
================================================================================
FANTASY DRAFT VALUE FINDER
================================================================================
Generated: 2025-01-05 14:30
Showing top 25 value picks

Rank  Player                    Pos  ADP    Proj   Own%   Value    Round
--------------------------------------------------------------------------------
1     Rachaad White             RB   87.3   198.5  45.2   124.89   8
2     Tony Pollard              RB   95.1   185.3  38.7   119.45   8
3     Jaylen Warren             RB   125.4  165.2  22.1   102.87   11
...

TOP VALUE PICKS BY POSITION:
----------------------------------------
QB: Jalen Hurts (ADP: 45.2, Value: 89.3)
RB: Rachaad White (ADP: 87.3, Value: 124.9)
WR: Chris Olave (ADP: 65.8, Value: 98.2)
TE: Kyle Pitts (ADP: 78.9, Value: 87.6)
DST: Dallas Cowboys (ADP: 145.2, Value: 45.3)
K: Justin Tucker (ADP: 162.3, Value: 38.9)

LATE ROUND SLEEPERS (ADP > 150):
----------------------------------------
Khalil Herbert (RB) - ADP: 165.3, Projected: 125.4
Marvin Mims Jr. (WR) - ADP: 178.9, Projected: 112.3
...
```

### JSON Output Structure
```json
{
  "generated": "2025-01-05T14:30:00.000Z",
  "total_players": 200,
  "players": [
    {
      "id": 4047365,
      "name": "Rachaad White",
      "position": "RB",
      "adp": 87.3,
      "projected_points": 198.5,
      "percent_owned": 45.2,
      "percent_started": 28.3,
      "value_score": 124.89,
      "round": 8
    },
    ...
  ]
}
```

## Draft Strategy Tips

### Using Value Scores

1. **High Value Score (>100)**: Strong candidates for reaching slightly early
2. **Medium Value Score (50-100)**: Good targets at or slightly before ADP
3. **Low Value Score (<50)**: Consider waiting or passing

### Position-Specific Strategies

- **QB**: Look for values in rounds 5-8 if you miss the elite tier
- **RB**: Target high-value handcuffs in later rounds
- **WR**: Find upside plays with low ownership in rounds 10+
- **TE**: Either go early or wait for late-round values

### Red Flags to Watch

- High ownership % but falling ADP might indicate injury/situation concerns
- Very low ownership % might mean news you haven't heard yet
- Check recent news for any high-value players before drafting

## Notes

- Value scores are relative and should be used as one factor in your draft strategy
- **Current Limitation**: Projections are not currently available from the ESPN Fantasy API endpoints used. The recipe uses ownership percentage and ADP data to calculate value scores instead
- When projections become available, the recipe will automatically use them for more accurate value calculations
- Consider your league's specific scoring settings when interpreting results
- The round boost multiplier favors late-round picks to help identify sleepers
- High value scores indicate players who are widely owned but available later in drafts, suggesting potential value

## Requirements

- Python 3.7+
- ESPN API client models (generated from OpenAPI spec)
- Network connection to access ESPN Fantasy API