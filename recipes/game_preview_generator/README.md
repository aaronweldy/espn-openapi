# Game Preview Generator

Auto-generates comprehensive game previews by combining data from multiple ESPN API endpoints including team stats, injury reports, recent performance, and head-to-head history.

## Features

- **Multi-Sport Support**: Generate previews for NFL, NBA, MLB, NHL, NCAAF, and NCAAB games
- **Comprehensive Data**: Combines injury reports, recent form, team records, and key storylines
- **Relevant News**: Automatically filters and includes recent news articles about the teams
- **Multiple Output Formats**: Console display, JSON export, or Markdown formatting
- **Date Selection**: Preview games for any date (default: today)
- **Batch Processing**: Generate multiple previews across different leagues simultaneously

## Usage

```bash
# Basic usage - NFL games for today
python -m recipes.game_preview_generator.recipe

# Multiple leagues for a specific date
python -m recipes.game_preview_generator.recipe --leagues nfl nba --date 20250608

# Generate markdown previews and save to file
python -m recipes.game_preview_generator.recipe --leagues nfl --output markdown --save previews.md

# Limit to first 3 games per league
python -m recipes.game_preview_generator.recipe --leagues nfl nba --limit 3
```

## Options

- `--leagues`: Leagues to generate previews for (choices: nfl, nba, mlb, nhl, ncaaf, ncaab)
- `--date`: Date for games in YYYYMMDD format (default: today)
- `--output`: Output format - console, json, or markdown (default: console)
- `--save`: Save output to specified file
- `--limit`: Limit number of games per league

## Examples

### Console Output Example
```
================================================================================
NFL GAME PREVIEW
================================================================================

Buffalo Bills at Kansas City Chiefs
Date: January 21, 2024 at 6:30 PM

MATCHUP
----------------------------------------
AWAY: Buffalo Bills (11-6)
HOME: Kansas City Chiefs (11-6)

INJURY REPORT
----------------------------------------

Kansas City Chiefs:
  - Travis Kelce (TE): QUESTIONABLE - Knee
  - Chris Jones (DT): OUT - Calf

Buffalo Bills:
  - Stefon Diggs (WR): QUESTIONABLE - Ankle

RECENT FORM
----------------------------------------

Kansas City Chiefs (Last 5 games):
  01/14: W vs Miami Dolphins 26
  01/07: L vs Las Vegas Raiders 14
  12/31: W vs Cincinnati Bengals 25
  12/25: L vs Las Vegas Raiders 14
  12/17: W vs New England Patriots 27

Buffalo Bills (Last 5 games):
  01/15: W vs Pittsburgh Steelers 31
  01/07: W vs Miami Dolphins 21
  12/31: W vs New England Patriots 27
  12/24: L vs Los Angeles Chargers 22
  12/17: W vs Dallas Cowboys 31

KEY STORYLINES
----------------------------------------
• Kansas City Chiefs dealing with 2 key injuries
• Buffalo Bills riding a 3-game winning streak

RECENT NEWS
----------------------------------------

Bills' Von Miller: Return timeline still unclear
  Buffalo Bills linebacker Von Miller's return from suspension remains uncertain as the team prepares for their divisional matchup...
  - January 18, 2024

Patrick Mahomes: "We're ready for this moment"
  Kansas City Chiefs quarterback Patrick Mahomes spoke confidently about his team's preparation heading into the playoff showdown...
  - January 19, 2024
```

### JSON Output Structure
```json
{
  "game_info": {
    "id": "401547602",
    "name": "Buffalo Bills at Kansas City Chiefs",
    "short_name": "BUF @ KC",
    "date": "2024-01-21T23:30:00Z",
    "status": "scheduled",
    "competitors": [...]
  },
  "teams": {
    "home": {
      "id": "12",
      "name": "Kansas City Chiefs",
      "abbreviation": "KC",
      "home_away": "home"
    },
    "away": {
      "id": "2",
      "name": "Buffalo Bills",
      "abbreviation": "BUF",
      "home_away": "away"
    }
  },
  "injuries": {
    "home": [...],
    "away": [...]
  },
  "recent_form": {
    "home": [...],
    "away": [...]
  },
  "head_to_head": {...},
  "relevant_news": [
    {
      "headline": "Bills' Von Miller: Return timeline still unclear",
      "description": "Buffalo Bills linebacker Von Miller's return from suspension...",
      "published": "2024-01-18T14:30:00Z",
      "type": "article",
      "premium": false
    }
  ],
  "key_storylines": [...]
}
```

### Markdown Output Example
```markdown
# NFL Game Preview: Buffalo Bills at Kansas City Chiefs

**Date:** January 21, 2024 at 6:30 PM

## Matchup

| Team | Record |
|------|--------|
| **AWAY:** Buffalo Bills | 11-6 |
| **HOME:** Kansas City Chiefs | 11-6 |

## Injury Report

### Kansas City Chiefs

| Player | Position | Status | Injury |
|--------|----------|--------|--------|
| Travis Kelce | TE | QUESTIONABLE | Knee |
| Chris Jones | DT | OUT | Calf |

### Buffalo Bills

| Player | Position | Status | Injury |
|--------|----------|--------|--------|
| Stefon Diggs | WR | QUESTIONABLE | Ankle |

## Recent Form

### Kansas City Chiefs (Last 5 games)

| Date | Result | Opponent | Score |
|------|--------|----------|-------|
| 01/14 | W | Miami Dolphins | 26 |
| 01/07 | L | Las Vegas Raiders | 14 |
...
```

## Data Sources

The recipe combines data from multiple ESPN API endpoints:

1. **Scoreboard API**: Gets upcoming games and basic matchup information
2. **Team Details API**: Fetches team information and records
3. **Injuries API**: Retrieves current injury reports for each team
4. **Schedule API**: Gets recent game results for form analysis
5. **News API**: Filters recent news articles for team-specific stories
6. **Odds API**: (Future enhancement) Could add betting lines and predictions

## Notes

- Injury data may not be available for all sports/teams
- Recent form shows last 5 completed games with full scores (winner score - loser score)
- News articles are filtered to only show stories mentioning the teams playing
- Head-to-head history is currently a placeholder for future enhancement
- Key storylines are auto-generated based on injuries and recent performance

## Future Enhancements

- Add betting odds and expert predictions
- Include weather information for outdoor games
- Add player stats and key matchups
- Historical head-to-head results
- Team statistics comparison (offense/defense rankings)
- Social media sentiment analysis