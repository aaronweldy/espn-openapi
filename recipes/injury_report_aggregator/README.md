# Injury Report Aggregator

Compile and analyze injury reports across all NFL teams.

**Note**: Currently, the ESPN API only provides injury data for NFL teams. Support for other leagues (NBA, MLB, NHL) may be added in the future if the API adds those endpoints.

## Features

- Fetches current injury reports for all 32 NFL teams
- Aggregates injuries with detailed player information
- Filters by injury severity (OUT, DOUBTFUL, QUESTIONABLE, etc.)
- Multiple output formats (console, JSON, CSV)
- Summary statistics and team-by-team breakdowns

## Usage

### Basic Usage

```bash
python recipe.py
```

This will fetch injury reports for all NFL teams.

### Demo Mode

If the API is not returning injury data (common during off-season), you can use demo mode:

```bash
python recipe.py --demo
```

This will show sample injury data to demonstrate the functionality.

### Filter by Severity

```bash
# Only show players who are OUT or DOUBTFUL
python recipe.py --severity OUT DOUBTFUL

# Show all questionable players across all leagues
python recipe.py --severity QUESTIONABLE
```

### Output Formats

```bash
# JSON output
python recipe.py --output json

# CSV output (great for spreadsheets)
python recipe.py --output csv --save injuries_report.csv

# Pretty console output (default)
python recipe.py --output console
```

### Combined Examples

```bash
# Get all OUT players in NFL, save as JSON
python recipe.py --severity OUT --output json --save out_players.json

# Export all injuries to CSV for analysis
python recipe.py --output csv --save all_injuries.csv

# Console report of serious injuries (OUT/DOUBTFUL)
python recipe.py --severity OUT DOUBTFUL

# Save questionable players to a file
python recipe.py --severity QUESTIONABLE --output json --save questionable_players.json
```

## Output Examples

### Console Output
```
================================================================================
                             NFL INJURY REPORT                                  
================================================================================
Generated: 2025-01-06 02:45 PM

Total injuries: 127

Injuries by status:
  QUESTIONABLE: 45
  OUT: 32
  DAY-TO-DAY: 21
  IR: 15
  DOUBTFUL: 10
  PROBABLE: 4

============================================================
DETAILED INJURY REPORT
============================================================

OUT (12 players)
----------------------------------------
  Joe Burrow (QB)
    Injury: Right wrist
    Date: 2025-01-03

  Nick Chubb (RB)
    Injury: Left knee
    Details: MCL sprain
    Date: 2025-01-01

...
```

### JSON Output Structure
```json
{
  "nfl": [
    {
      "team_id": "6",
      "athlete_id": "3915511",
      "athlete_name": "Joe Burrow",
      "position": "QB",
      "jersey": "9",
      "status": "OUT",
      "date": "2025-01-03",
      "type": "Injury",
      "details": "Expected to miss 2-3 weeks",
      "side": "Right",
      "body_part": "Wrist"
    },
    ...
  ],
  "nba": [...],
  "mlb": [...],
  "nhl": [...]
}
```

### CSV Output Columns
- league
- team_id
- athlete_name
- position
- jersey
- status
- type
- body_part
- side
- details
- date

## Use Cases

1. **Fantasy Sports**: Quickly check injury status before setting lineups
2. **Betting**: Monitor key player availability across games
3. **Team Analysis**: Track injury trends for specific teams
4. **Cross-Sport Monitoring**: See injury patterns across different leagues
5. **Data Analysis**: Export to CSV for deeper statistical analysis

## Notes

- Injury data is fetched in real-time from ESPN's API
- Currently only supports NFL teams (API limitation)
- Some teams may not have injury data available
- The script fetches injury details for each player individually, so it may take a minute to complete
- Status definitions:
  - **OUT**: Player will not play
  - **DOUBTFUL**: Player unlikely to play (25% chance)
  - **QUESTIONABLE**: Uncertain status (50% chance)
  - **PROBABLE**: Player likely to play (75% chance)
  - **DAY-TO-DAY**: Minor injury, status updated daily
  - **IR**: Injured Reserve (long-term injury)
  - **PUP**: Physically Unable to Perform

## Troubleshooting

If you encounter errors:
1. Ensure you're in the project virtual environment
2. Check that all dependencies are installed: `pip install -r requirements.txt`
3. The NFL may have limited injury data during the off-season
4. API rate limits may apply for rapid repeated requests
5. If httpx is not installed, run: `pip install httpx`