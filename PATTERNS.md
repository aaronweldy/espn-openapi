# ESPN API Patterns Reference Guide

This document contains discovered patterns and common structures in the ESPN API to speed up implementation.

## Table of Contents
- [Response Structures](#response-structures)
- [Error Handling](#error-handling)
- [Common Fields](#common-fields)
- [URL Patterns](#url-patterns)
- [Query Parameters](#query-parameters)
- [Schema Reuse](#schema-reuse)
- [Sport-Specific Notes](#sport-specific-notes)

## Response Structures

### List Endpoints
List endpoints (teams, news, standings) typically wrap responses in a nested structure:

```json
{
  "sports": [
    {
      "id": "90",
      "leagues": [
        {
          "id": "28",
          "teams": [...]  // or "news": [...], "standings": [...]
        }
      ]
    }
  ]
}
```

**Path to data**: `response.sports[0].leagues[0].{resource}`

### Detail Endpoints
Detail endpoints (team/{id}, athlete/{id}) return the resource at root level:

```json
{
  "team": {
    "id": "12",
    "displayName": "Kansas City Chiefs",
    // ... team details
  }
}
```

**Path to data**: `response.{resource}`

### Scoreboard Endpoints
Scoreboard responses have a complex structure with events:

```json
{
  "leagues": [...],
  "events": [
    {
      "id": "401547417",
      "competitions": [...]
    }
  ]
}
```

## Error Handling

### Common Error Responses
- **400 Bad Request**: Invalid resource ID or malformed request
  - Example: `/teams/INVALID` returns 400, not 404
- **404 Not Found**: Endpoint doesn't exist
- **500 Internal Server Error**: Server-side issues

### Error Response Format
```json
{
  "error": {
    "code": 400,
    "message": "Invalid team identifier"
  }
}
```

## Common Fields

### Resource Identifiers
Almost all resources have these fields:
- `id`: Numeric or string identifier
- `uid`: Unique identifier (format: `s:{sport}~l:{league}~t:{id}`)
- `displayName`: Human-readable name
- `abbreviation`: Short code (teams, leagues)
- `slug`: URL-friendly name

### Links Pattern
Resources often include a `links` array:
```json
"links": [
  {
    "rel": ["clubhouse", "desktop", "team"],
    "href": "https://www.espn.com/nfl/team/_/name/kc/kansas-city-chiefs"
  },
  {
    "rel": ["api", "teams"],  
    "href": "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/teams/12"
  }
]
```

### Logos Pattern
Teams and leagues include logo arrays:
```json
"logos": [
  {
    "href": "https://a.espncdn.com/i/teamlogos/nfl/500/kc.png",
    "width": 500,
    "height": 500,
    "rel": ["full", "default"]
  }
]
```

## URL Patterns

### Site API Base URLs
- **Pattern**: `https://site.api.espn.com/apis/site/v2/sports/{sport}/{league}/{resource}`
- **Examples**:
  - Teams: `/sports/football/nfl/teams`
  - Team Details: `/sports/football/nfl/teams/{id}`
  - Scoreboard: `/sports/football/nfl/scoreboard`
  - News: `/sports/football/nfl/news`

### Sports Core API Base URLs
- **Pattern**: `https://sports.core.api.espn.com/v2/sports/{sport}/leagues/{league}/{resource}`
- **Examples**:
  - Athletes: `/v2/sports/football/leagues/nfl/athletes/{id}`
  - Events: `/v2/sports/football/leagues/nfl/events/{id}`
  - Seasons: `/v2/sports/football/leagues/nfl/seasons/{year}`

### CDN API Base URLs
- **Pattern**: `https://cdn.espn.com/core/{league}/{resource}`
- **Query**: Always requires `xhr=1`
- **Examples**:
  - Scoreboard: `/core/nfl/scoreboard?xhr=1`
  - Schedule: `/core/nfl/schedule?xhr=1&year=2024`

## Query Parameters

### Common Parameters
- `limit`: Number of results (default varies by endpoint)
- `dates`: YYYYMMDD or YYYYMMDD-YYYYMMDD
- `season`: Year (YYYY)
- `seasontype`: 1=preseason, 2=regular, 3=postseason
- `week`: Week number

### Sport-Specific Parameters
- **NFL**: `seasontype`, `week`
- **NBA/NHL**: `dates` (for daily schedules)
- **MLB**: `dates` (essential for 162-game season)

## Schema Reuse

### Commonly Reused Schemas
These schemas are used across multiple sports and endpoints:

1. **TeamsListResponse**: All `/teams` list endpoints
2. **TeamDetailsResponse**: All `/teams/{id}` endpoints
3. **Athlete**: Basic athlete info across sports
4. **Competition**: Game/event information
5. **Venue**: Stadium/arena information
6. **Link**: URL reference structure
7. **Logo**: Image reference structure
8. **Season**: Season information
9. **Week**: Week information (football)

### Sport-Agnostic Schemas
These work across all sports without modification:
- `Link`
- `Logo`
- `Image`
- `ErrorResponse`
- `Reference` (for $ref-only objects)

## Sport-Specific Notes

### NFL
- Uses week-based scheduling
- Season types: 1 (PRE), 2 (REG), 3 (POST), 4 (OFF)
- Conferences: AFC (id: 8), NFC (id: 7)
- Draft endpoints are more comprehensive

### NBA
- Uses date-based scheduling
- Season runs October-June
- 30 teams (not 32 like NFL/NHL)
- All-Star break affects scheduling

### MLB
- Longest season (162 games)
- Always use date parameters
- Spring training data separate
- Minor league data on different endpoints

### NHL
- 32 teams (expanded from 30)
- Uses points system for standings
- Playoff format differs from other sports
- International players common

## Implementation Tips

### Batch Similar Endpoints
When implementing, group these together:
1. All team list endpoints (same schema)
2. All team detail endpoints (same schema)
3. All scoreboard endpoints (similar structure)
4. All athlete endpoints (similar fields)

### Check Existing Tests First
```bash
# Before implementing, check if similar tests exist
grep -r "get_teams_list" tests/
grep -r "TeamsListResponse" models/
```

### Use Validation Script
```bash
# Quick validation before full implementation
python scripts/validate_endpoint.py "URL" --jq '.sports[0].leagues[0]'
```

### Common Gotchas
1. **Dates**: Some endpoints require dates, others forbid them
2. **IDs**: Can be numeric strings or abbreviations
3. **Logos**: Array can be empty for some teams
4. **Links**: Not all resources have all link types
5. **Seasons**: Different sports have different season structures

## Quick Reference Commands

### Explore endpoint structure
```bash
curl -s "URL" | jq 'keys'
curl -s "URL" | jq '.sports[0].leagues[0] | keys'
```

### Count items
```bash
curl -s "URL" | jq '.sports[0].leagues[0].teams | length'
```

### Extract specific fields
```bash
curl -s "URL" | jq '.sports[0].leagues[0].teams[] | {id, displayName, abbreviation}'
```

### Find by condition
```bash
curl -s "URL" | jq '.sports[0].leagues[0].teams[] | select(.abbreviation == "KC")'
```