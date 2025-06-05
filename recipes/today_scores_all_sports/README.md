# Get Today's Scores Across All Major Sports

## Description

This recipe fetches live scores and game information for NFL, NBA, MLB, and NHL games happening today. Perfect for sports fans who want a quick overview of all ongoing games or for building sports dashboards and notifications.

## Prerequisites

- Python 3.8+
- ESPN API client models installed (`pip install -e .` from project root)
- No authentication required (uses public ESPN API endpoints)

## Usage

Basic usage:
```bash
python recipe.py
```

Filter by sport:
```bash
python recipe.py --sport nfl
```

Output to JSON file:
```bash
python recipe.py --output scores.json
```

Example output:
```
=== NFL SCORES (2025-01-06) ===
Kansas City Chiefs (15-1) vs Buffalo Bills (13-3)
  Status: Final
  Score: Chiefs 31, Bills 28
  
=== NBA SCORES (2025-01-06) ===
LA Lakers @ Boston Celtics
  Status: 3rd Quarter - 5:23
  Score: Lakers 78, Celtics 82
  
...
```

## Key Concepts

### API Endpoints Used
- `/apis/site/v2/sports/football/nfl/scoreboard`
- `/apis/site/v2/sports/basketball/nba/scoreboard`
- `/apis/site/v2/sports/baseball/mlb/scoreboard`
- `/apis/site/v2/sports/hockey/nhl/scoreboard`

### Important Model Classes
- `ScoreboardResponse` - Main response object containing events
- `Event` - Individual game information
- `Competition` - Game details including score and status
- `Competitor` - Team information including score

### Data Transformations
- Extracts team names, scores, and game status from nested API response
- Formats game time/status into human-readable format
- Groups games by sport for organized display

## Customization

### Different Sports/Leagues
Modify the `SPORTS_LEAGUES` dictionary to include other leagues:
```python
SPORTS_LEAGUES = {
    "football": ["nfl", "college-football"],
    "basketball": ["nba", "wnba", "mens-college-basketball"],
    # Add more as needed
}
```

### Date Range
Change from today's games to a specific date:
```python
date_str = "20250115"  # January 15, 2025
```

### Output Format
The recipe includes functions for:
- Console output (default)
- JSON export
- CSV export (scores only)
- Can be imported and used in other scripts

### Common Variations
1. **Live games only**: Filter by `status.type.state == "in"`
2. **Completed games**: Filter by `status.type.completed == True`
3. **Specific teams**: Filter events by team ID or name
4. **Add betting lines**: Include odds data from the competition object