# Game Flow Tracker

## Description

This recipe tracks score changes and momentum shifts for a specific game, providing insights into how the game unfolded. It fetches play-by-play data and analyzes scoring runs, lead changes, and key momentum moments. Perfect for post-game analysis, understanding game dynamics, or tracking live games with detailed updates.

## Prerequisites

- Python 3.8+
- ESPN API client models installed (`pip install -e .` from project root)
- A valid ESPN event/game ID

## Usage

Track a specific game:
```bash
python recipe.py --event-id 401547417
```

Track with live updates (refreshes every 30 seconds):
```bash
python recipe.py --event-id 401547417 --live
```

Export game flow data:
```bash
python recipe.py --event-id 401547417 --export gameflow.json
```

Analyze specific quarter/period:
```bash
python recipe.py --event-id 401547417 --period 4
```

Example output:
```
=== GAME FLOW: Kansas City Chiefs vs Buffalo Bills ===
Event ID: 401547417
Status: Final - Chiefs 31, Bills 28

SCORING SUMMARY:
Q1: Chiefs 7, Bills 3 (Chiefs +4)
Q2: Chiefs 14, Bills 10 (Chiefs +4)
Q3: Chiefs 21, Bills 21 (Tied)
Q4: Chiefs 31, Bills 28 (Chiefs +3)

MOMENTUM SHIFTS:
- Q1 5:23: Chiefs score TD, take 7-0 lead (Momentum: Chiefs)
- Q2 12:15: Bills FG, cut lead to 7-3
- Q3 8:47: Bills score TD, tie game 21-21 (Momentum: Bills)
- Q4 2:03: Chiefs FG, win 31-28 (Momentum: Chiefs)

LEAD CHANGES: 3
LARGEST LEAD: Chiefs by 11 (Q2)
COMEBACK: Bills erased 11-point deficit
CLUTCH MOMENTS: 2 scores in final 5 minutes
```

## Key Concepts

### API Endpoints Used
- `/apis/site/v2/sports/{sport}/{league}/summary?event={event_id}` - Game summary and current score
- `/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{event_id}/plays` - Play-by-play data (sports.core.api)
- `/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{event_id}/drives` - Drive data (NFL)

### Important Model Classes
- `GameSummary` - Overall game information and status
- `Play` - Individual play data
- `Drive` - Drive summaries (NFL specific)
- `ScoringPlay` - Scoring play details

### Data Analysis
- Tracks cumulative score throughout the game
- Identifies momentum shifts (3+ unanswered scores)
- Calculates lead changes and largest leads
- Highlights clutch moments (scores in final 5 minutes)
- Analyzes scoring runs and droughts

## Customization

### Different Sports
The recipe supports multiple sports with sport-specific analysis:
```python
SPORT_CONFIG = {
    "football": {"periods": 4, "period_name": "Quarter"},
    "basketball": {"periods": 4, "period_name": "Quarter"},
    "hockey": {"periods": 3, "period_name": "Period"},
    "baseball": {"periods": 9, "period_name": "Inning"}
}
```

### Analysis Options
Modify analysis parameters:
```python
# Momentum threshold (consecutive scores)
MOMENTUM_THRESHOLD = 3

# Clutch time (minutes remaining)
CLUTCH_TIME = 5

# Score differential for "close game"
CLOSE_GAME_THRESHOLD = 7
```

### Live Tracking
For live games, configure update intervals:
```python
# Update interval in seconds
LIVE_UPDATE_INTERVAL = 30

# Show notifications for scoring plays
SHOW_NOTIFICATIONS = True
```

### Common Variations

1. **Scoring Runs**: Track consecutive scores by one team
2. **Quarter Analysis**: Deep dive into specific periods
3. **Clutch Performance**: Focus on final minutes
4. **Comeback Tracker**: Monitor deficit recoveries
5. **Live Alerts**: Real-time notifications for score changes

### Visual Output

The recipe can generate visual representations:
- ASCII chart of score differential over time
- Momentum meter showing current game flow
- Quarter-by-quarter breakdown