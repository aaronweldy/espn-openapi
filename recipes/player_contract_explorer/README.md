# Player Contract Explorer

Search and analyze player contracts across NFL, NBA, MLB, and NHL using ESPN's API.

## Features

- **Multi-league search**: Search for players across multiple sports leagues simultaneously
- **Contract details**: View complete contract breakdowns including salary, bonuses, and year-by-year details
- **Flexible output**: Display results in console, JSON, or CSV format
- **Async processing**: Fast performance when searching multiple players
- **Top contracts**: Filter to show only players with available contract data

## Usage

```bash
python recipe.py <player_name> [options]
```

## Options

- `query`: Player name to search for (required)
- `--leagues`: Leagues to search (default: nfl nba). Options: nfl, nba, mlb, nhl
- `--output`: Output format (default: console). Options: console, json, csv
- `--save`: Save output to specified file
- `--limit`: Maximum number of players to show per league (default: 10)
- `--top-contracts`: Show only players with contract data, sorted by value
- `--all-years`: Fetch complete contract history for all years (NBA only)

## Examples

### Search for a player across default leagues (NFL, NBA)
```bash
python recipe.py "mahomes"
```

### Search across all leagues with JSON output
```bash
python recipe.py "smith" --leagues nfl nba mlb nhl --output json --save contracts.json
```

### Find top contracts for players named "Jones" in the NFL
```bash
python recipe.py "jones" --leagues nfl --top-contracts --limit 5
```

### Export contract data to CSV
```bash
python recipe.py "williams" --leagues nba nfl --output csv --save williams_contracts.csv
```

### Search for a specific player in MLB
```bash
python recipe.py "ohtani" --leagues mlb
```

### Get complete contract history for an NBA player
```bash
python recipe.py "lebron james" --leagues nba --all-years
```

### Quick NBA contract overview (without fetching all years)
```bash
python recipe.py "curry" --leagues nba --limit 5
```

## Output Format

### Console Output
```
NFL Player Contracts
================================================================================

Patrick Mahomes (QB) - KC
------------------------------------------------------------
Total Value: $450.0M
Average Annual: $45.0M
Years: 10

Year-by-Year Breakdown:
  2024: Salary: $35.8M, Bonus: $10.0M, Total: $45.8M
  2025: Salary: $41.9M, Bonus: $10.0M, Total: $51.9M
  ...
```

### JSON Output
```json
{
  "nfl": [
    {
      "id": "3139477",
      "name": "Patrick Mahomes",
      "position": "QB",
      "team": "KC",
      "contract": {
        "contracts": [
          {
            "year": 2024,
            "salary": 35800000,
            "bonus": 10000000,
            "total": 45800000
          }
        ],
        "total_value": 450000000,
        "average_annual": 45000000,
        "years_remaining": 10
      }
    }
  ]
}
```

### CSV Output
The CSV format includes columns for:
- League
- Name
- Position
- Team
- Total Value
- Average Annual
- Years
- Current Year Salary

## Notes

- **Contract data availability varies significantly by sport:**
  - **NBA**: Most comprehensive contract data available, including year-by-year salary details
  - **NFL, MLB, NHL**: Contract data is typically not available through the ESPN API
- Use `--all-years` flag to fetch complete NBA contract history (may take longer)
- Without `--all-years`, the recipe shows available contract years but not salary details
- Some players may not have publicly available contract information
- The search is case-insensitive and matches partial names
- Results are sorted by total contract value when using `--top-contracts`
- Async processing ensures fast performance even when searching multiple leagues

## Rate Limiting

The recipe implements batch processing to avoid overwhelming the API:
- Processes players in batches of 10
- Includes timeout handling for network requests
- Gracefully handles missing or unavailable contract data