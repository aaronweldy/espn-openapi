# Track Fantasy Football Player Ownership Trends

## Description

This recipe tracks ownership percentages for fantasy football players, helping identify rising stars and dropping players. It's particularly useful during the season for finding waiver wire targets and monitoring player sentiment changes. The recipe can track specific players over time or scan for the biggest movers by automatically fetching historical data from previous weeks.

## Prerequisites

- Python 3.8+
- ESPN API client models installed (`pip install -e .` from project root)
- No authentication required for ownership data

## Usage

Track top owned players:
```bash
python recipe.py --top 20
```

Track specific players:
```bash
python recipe.py --players "Patrick Mahomes" "Justin Jefferson"
```

Find biggest ownership changes (automatically fetches historical data):
```bash
python recipe.py --movers --days 7
```

Export data for tracking:
```bash
python recipe.py --top 50 --export ownership_data.json
```

Example output:
```
=== TOP 20 OWNED FANTASY PLAYERS (2025-01-06) ===

1. Christian McCaffrey (RB, SF)
   Ownership: 98.5%
   Projected Points: 18.3
   
2. Tyreek Hill (WR, MIA) 
   Ownership: 97.2%
   Projected Points: 16.8
   
3. Justin Jefferson (WR, MIN)
   Ownership: 96.8%
   Projected Points: 17.1
   
...

=== BIGGEST MOVERS (LAST 7 DAYS) ===

RISING:
↑ Puka Nacua (WR, LAR): 45.2% → 72.3% (+27.1%) (1 week ago)
↑ Kyren Williams (RB, LAR): 38.5% → 58.9% (+20.4%) (1 week ago)

FALLING:
↓ Kenneth Walker (RB, SEA): 89.2% → 71.5% (-17.7%) (1 week ago)
↓ Mike Evans (WR, TB): 94.1% → 82.3% (-11.8%) (1 week ago)
```

## Key Concepts

### API Endpoints Used
- `/apis/v3/games/ffl/seasons/{year}/players?scoringPeriodId={period}&view=players_wl` - Player list with ownership for specific scoring periods
- The `scoringPeriodId` parameter corresponds to NFL weeks (0=current, 1-17 for regular season weeks)

### Important Model Classes
- `FantasyPlayer` - Player information including ownership percentage
- `PlayerPoolEntry` - Container for player data
- `PlayerStats` - Statistical projections and ownership data

### Data Transformations
- Extracts ownership percentage from nested player pool data
- Calculates ownership changes when historical data available
- Filters and sorts players by various criteria
- Maps player IDs to names and team information

## Customization

### Scoring Format
Change from standard to PPR scoring:
```python
PPR_SCORING_ID = 3  # PPR scoring
STANDARD_SCORING_ID = 1  # Standard scoring
```

### Position Filtering
Filter by specific positions:
```python
POSITIONS = ["QB", "RB", "WR", "TE"]  # Modify as needed
```

### Ownership Thresholds
Set minimum ownership for "rostered" players:
```python
MIN_OWNERSHIP = 5.0  # Only show players owned in 5%+ of leagues
```

### Time Periods
Track different time ranges:
```python
# Weekly tracking
track_days = 7

# Season-long tracking  
track_days = 0  # From start of season
```

### Common Variations

1. **Waiver Wire Targets**: Players with <50% ownership and rising
2. **Drop Candidates**: Players with high ownership but falling
3. **League-Specific**: Compare to your specific league's ownership
4. **Injury Impact**: Track ownership changes after injury news
5. **Breakout Candidates**: Low-owned players with high projections

### Data Storage

The recipe supports saving historical data for trend analysis:
```python
# Save current snapshot
save_ownership_snapshot("ownership_2025_01_06.json")

# Load and compare
changes = compare_ownership_snapshots("ownership_2025_01_01.json", 
                                    "ownership_2025_01_06.json")
```

### Automatic Historical Data Fetching

New feature: The recipe now automatically fetches historical data when using the `--movers` flag:
- Automatically determines the current NFL week based on the date
- Fetches data from multiple past weeks based on the `--days` parameter
- Calculates ownership changes with time period indicators
- No need to manually save snapshots for basic trend tracking
- Shows how many weeks ago the comparison data is from

Example:
```bash
# Fetch changes from the last 14 days (2 weeks)
python recipe.py --movers --days 14
```

This will fetch data from 2 weeks ago and compare it to current ownership percentages.