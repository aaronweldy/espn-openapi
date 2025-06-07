# Fantasy Correlation Analysis

Analyzes correlations between player statistics and fantasy points to identify which stats are most predictive of fantasy success. Also identifies high-value player stacks (e.g., QB-WR combinations from the same team).

## Features

- **Statistical Correlation Analysis**: Calculate correlations between various stats and fantasy points
- **Position-Specific Analysis**: Analyze correlations separately for QB, RB, WR, and TE positions
- **Player Stack Analysis**: Identify QB-receiver combinations with high combined fantasy output
- **Statistical Significance**: Shows p-values to indicate statistical reliability
- **Multiple Output Formats**: Console display, JSON export, or CSV for further analysis

## Usage

```bash
# Basic usage - analyze last completed season
python -m recipes.correlation_analysis.recipe

# Analyze specific positions for 2023
python -m recipes.correlation_analysis.recipe --year 2023 --positions QB WR

# Save detailed results to JSON
python -m recipes.correlation_analysis.recipe --year 2024 --output json --save correlations_2024.json

# Analyze top 300 players
python -m recipes.correlation_analysis.recipe --limit 300
```

## Options

- `--year`: Season year to analyze (default: last completed season)
- `--positions`: Specific positions to analyze (choices: QB, RB, WR, TE)
- `--output`: Output format - console, json, or csv (default: console)
- `--save`: Save output to specified file
- `--limit`: Number of players to analyze (default: 200)
- `--min-correlation`: Minimum correlation threshold to display (default: 0.3)

## Understanding the Output

### Correlation Values

The correlation coefficient ranges from -1 to 1:
- **1.0**: Perfect positive correlation (as one stat increases, fantasy points always increase)
- **0.7 to 1.0**: Strong positive correlation
- **0.3 to 0.7**: Moderate positive correlation
- **-0.3 to 0.3**: Weak or no correlation
- **-1.0 to -0.3**: Negative correlation (as one stat increases, fantasy points decrease)

### Statistical Significance

- `***` : p < 0.001 (extremely significant)
- `**` : p < 0.01 (very significant)
- `*` : p < 0.05 (significant)
- No symbol: Not statistically significant

## Example Output

### Console Output
```
ALL POSITIONS STAT CORRELATIONS WITH FANTASY POINTS
============================================================
Statistic            Correlation      P-Value   Sample
------------------------------------------------------------
passing_tds              0.892***       0.000      150
receiving_yds            0.845***       0.000      180
rushing_tds              0.823***       0.000      165
passing_yds              0.798***       0.000      150
receptions               0.756***       0.000      180
rushing_yds              0.721***       0.000      165
targets                  0.689***       0.000      180
completions              0.654***       0.000      150
rushing_att              0.523***       0.000      165
interceptions           -0.234*         0.045      150

Significance: * p<0.05, ** p<0.01, *** p<0.001

QB STAT CORRELATIONS WITH FANTASY POINTS
============================================================
Statistic            Correlation      P-Value   Sample
------------------------------------------------------------
passing_tds              0.945***       0.000       32
passing_yds              0.921***       0.000       32
completions              0.887***       0.000       32
passing_att              0.756***       0.000       32
rushing_tds              0.523**        0.002       32
rushing_yds              0.412*         0.019       32
interceptions           -0.389*         0.028       32

TOP QB-RECEIVER STACKS
================================================================================
Team  QB                   Receiver             Pos  Combined    TD%   Yds%
--------------------------------------------------------------------------------
MIA   Tua Tagovailoa      Tyreek Hill          WR      678.3   34.5   45.2
BUF   Josh Allen          Stefon Diggs         WR      654.2   28.9   38.7
CIN   Joe Burrow          Ja'Marr Chase        WR      642.1   31.2   41.3
MIN   Kirk Cousins        Justin Jefferson     WR      635.8   29.4   43.8
PHI   Jalen Hurts         A.J. Brown           WR      628.4   25.7   35.6
```

### JSON Output Structure
```json
{
  "year": 2023,
  "summary": {
    "total_players_analyzed": 200,
    "positions_analyzed": ["QB", "RB", "WR", "TE"],
    "top_stacks_count": 50
  },
  "overall_correlations": {
    "passing_tds": {
      "correlation": 0.892,
      "p_value": 0.000001,
      "sample_size": 150
    },
    ...
  },
  "position_correlations": {
    "QB": {...},
    "RB": {...},
    "WR": {...},
    "TE": {...}
  },
  "player_stacks": [
    {
      "team": "MIA",
      "qb": "Tua Tagovailoa",
      "receiver": "Tyreek Hill",
      "receiver_pos": "WR",
      "qb_fantasy_pts": 342.5,
      "receiver_fantasy_pts": 335.8,
      "combined_pts": 678.3,
      "td_share": 34.5,
      "yds_share": 45.2
    },
    ...
  ]
}
```

## Insights and Applications

### For Fantasy Drafting
- **High Correlation Stats**: Focus on players who excel in highly correlated stats
- **Position-Specific**: Different stats matter for different positions
- **Stack Building**: Target QB-WR combinations with high correlation

### Common Findings
1. **QBs**: Passing TDs and yards have the highest correlation with fantasy points
2. **RBs**: Rushing TDs are more predictive than rushing yards
3. **WRs/TEs**: Targets and receptions are strong indicators of fantasy success
4. **Negative Correlations**: Turnovers (INTs, fumbles) negatively impact fantasy points

### Stack Strategy
- High TD% share indicates a receiver who gets a large portion of their QB's TDs
- High Yds% share shows consistent involvement in the passing game
- Combined points show the ceiling of stacking these players together

## Notes

- Uses built-in Python statistics for correlation calculations
- Fantasy scoring is based on standard ESPN scoring settings
- Correlations are based on season totals (game-by-game analysis would require additional data)
- Player must have sufficient games played to be included in analysis
- Stack analysis focuses on QB-receiver combinations but could be extended to other combos
- P-values are approximated for demonstration purposes

## Future Enhancements

- Game-by-game correlation analysis for more accurate stack correlations
- Week-to-week consistency metrics
- Opponent-adjusted correlations
- Multi-year trend analysis
- Custom scoring system support
- RB-defense correlations for game script analysis