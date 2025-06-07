# Team Performance Trends

Analyze team performance metrics and trends over time across NFL, NBA, MLB, and NHL.

## Features

- **Comprehensive Performance Analysis**: Track wins/losses, scoring trends, and performance metrics
- **Multiple Time Windows**: Analyze full season, recent games, or custom date ranges
- **Home/Away Splits**: Compare performance at home vs on the road
- **Trend Visualization**: See offensive and defensive trends with indicators
- **Streak Tracking**: Current streaks and longest win/loss streaks
- **Team Comparison**: Compare multiple teams side-by-side
- **Flexible Output**: Console display, JSON export, or CSV format

## Usage

```bash
python recipe.py <team1> [team2 ...] --league <league> [options]
```

## Options

- `teams`: One or more team abbreviations or IDs to analyze (required)
- `--league`: League to analyze (required). Options: nfl, nba, mlb, nhl
- `--season`: Season year (default: current season)
- `--last-n`: Number of recent games for trend analysis (default: 10)
- `--output`: Output format (default: console). Options: console, json, csv
- `--save`: Save output to specified file
- `--compare`: Compare multiple teams side by side (console output only)

## Examples

### Analyze a single NFL team
```bash
python recipe.py KC --league nfl
```

### Compare multiple NBA teams
```bash
python recipe.py LAL BOS MIA --league nba --compare
```

### Analyze MLB team with custom window
```bash
python recipe.py NYY --league mlb --last-n 20
```

### Export NHL team trends to JSON
```bash
python recipe.py TOR --league nhl --output json --save maple_leafs_trends.json
```

### Analyze previous season
```bash
python recipe.py SF --league nfl --season 2023
```

### Export comparison to CSV
```bash
python recipe.py DAL PHI NYG WAS --league nfl --output csv --save nfc_east_trends.csv
```

## Output Format

### Console Output (Single Team)
```
NFL Team Performance Trends
================================================================================

Kansas City Chiefs (KC)
------------------------------------------------------------

Overall Record: 11-6 (0.647)
Division: 4-2
Conference: 8-4

Home: 6-2 (0.750)
Away: 5-4 (0.556)

Last 10 Games: 6-4 (0.600)
Form (Last 5): W L W W L
Current Streak: 1L

Scoring Averages:
  Points For: 23.5 (Last 10: 25.2)
  Points Against: 19.8 (Last 10: 18.4)
  Average Margin: +3.7
  Offensive Trend: 📈
  Defensive Trend: 📈
```

### Console Output (Comparison Mode)
```
NBA Team Comparison
================================================================================

Metric              LAL         BOS         MIA
------------------------------------------------------------
Overall Record      35-30       54-14       42-29
Win %               0.538       0.794       0.592
Last 10 Games       6-4         8-2         5-5
PPG                 117.6       120.6       110.1
Opp PPG             116.0       110.4       109.6
Current Streak      2W          3W          1L
```

### JSON Output Structure
```json
{
  "league": "nba",
  "season": 2025,
  "analysis_date": "2025-01-06T12:00:00",
  "teams": {
    "LAL": {
      "info": {
        "id": "13",
        "abbreviation": "LAL",
        "display_name": "Los Angeles Lakers",
        "location": "Los Angeles"
      },
      "trends": {
        "overall": {
          "wins": 35,
          "losses": 30,
          "win_pct": 0.538
        },
        "last_n": {
          "wins": 6,
          "losses": 4,
          "win_pct": 0.600,
          "n": 10
        },
        "scoring": {
          "avg_points_for": 117.6,
          "avg_points_against": 116.0,
          "avg_margin": 1.6,
          "last_n_avg_for": 119.8,
          "last_n_avg_against": 114.2
        },
        "streaks": {
          "current": {
            "type": "W",
            "length": 2
          },
          "longest_win": 7,
          "longest_loss": 4
        },
        "form": ["W", "W", "L", "W", "L"]
      },
      "record": {
        "division": {
          "wins": 8,
          "losses": 4
        },
        "conference": {
          "wins": 22,
          "losses": 18
        }
      }
    }
  }
}
```

### CSV Output
The CSV format includes columns for:
- League
- Team Name and Abbreviation
- Overall and split records (Home/Away)
- Last N games performance
- Current streak
- Scoring averages (overall and recent)
- Point differential

## Performance Metrics Explained

### Win Percentage
- Overall, home, away, and recent game winning percentages
- Division and conference records (when available)

### Scoring Trends
- **PPG (Points Per Game)**: Average points scored
- **Opp PPG**: Average points allowed
- **Average Margin**: Point differential per game
- **Trend Indicators**: 
  - 📈 Improving (recent average better than season average)
  - 📉 Declining (recent average worse than season average)

### Streaks
- **Current Streak**: Active winning (W) or losing (L) streak
- **Form**: Results of last 5 games (most recent first)
- **Longest Streaks**: Best and worst runs during the season

## Notes

- Games are processed in chronological order for accurate trend analysis
- Only completed games are included in statistics
- The `--last-n` parameter affects trend calculations and comparisons
- Division/conference records may not be available for all leagues
- Some historical data may be limited based on the ESPN API

## Rate Limiting

The recipe uses synchronous API calls with built-in error handling:
- Gracefully handles missing data or API errors
- No parallel processing to avoid rate limits
- Each team is processed sequentially