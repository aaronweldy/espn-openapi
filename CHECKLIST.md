# ESPN API OpenAPI Schema Checklist

## Base URLs
The ESPN API uses multiple base URLs for different types of endpoints:
- **site.api.espn.com/apis/site/v2** - General site data: scores, news, teams, summaries, standings
- **sports.core.api.espn.com** - Core sports data: athletes, seasons, detailed stats, plays
- **site.web.api.espn.com** - Web-specific APIs: search, athlete details
- **fantasy.espn.com** - Fantasy sports data
- **cdn.espn.com** - Content delivery for scoreboards, schedules

## NFL Endpoints

### site.api.espn.com/apis/site/v2
- [x] `/sports/football/nfl/scoreboard` - Already implemented
- [x] `/sports/football/nfl/teams` - Already implemented
- [x] `/sports/football/nfl/teams/{teamId}` - Already implemented
- [x] `/sports/football/nfl/summary` - Already implemented
- [x] `/sports/football/nfl/news` - Implemented
- [x] `/sports/football/nfl/teams/{teamId}/roster` - Implemented

### cdn.espn.com
- [x] `/core/nfl/scoreboard` Params: xhr, limit
- [x] `/core/nfl/schedule` Params: xhr, limit, year, week
- [ ] `/core/nfl/standings` Params: season
- [ ] `/core/nfl/boxscore` Params: xhr (=1), gameid (={event_id})
- [ ] `/core/nfl/playbyplay` Params: xhr (=1), gameid (=event_id)

### sports.core.api.espn.com
- [x] `/v2/sports/football/leagues/nfl/athletes/{athleteId}` - Detailed athlete information
- [x] `/v2/sports/football/leagues/nfl/athletes/{athleteId}/statistics` - Athlete statistics
- [x] `/v2/sports/football/leagues/nfl/athletes/{athleteId}/statisticslog` - Athlete statistics log
- [x] `/v2/sports/football/leagues/nfl/events/{eid}/competitions/{eid}/plays`
- [x] `/v2/sports/football/leagues/nfl/events/{eid}/competitions/{eid}/drives`

### site.web.api.espn.com
- [x] `/apis/common/v3/sports/football/nfl/athletes/{athleteId}/overview` - Athlete overview
- [x] `/apis/common/v3/sports/football/nfl/athletes/{athleteId}/gamelog` - Athlete game log
- [x] `/apis/common/v3/search` - General Search
- [x] `/apis/search/v2` - General Search (v2)

### General 
- [x] `/v2/sports/football/nfl/standings` - Implemented (site.api.espn.com)

## MLB Endpoints

### site.api.espn.com/apis/site/v2
- [ ] `/sports/baseball/mlb/scoreboard`
- [ ] `/sports/baseball/mlb/news`
- [ ] `/sports/baseball/mlb/teams`
- [ ] `/sports/baseball/mlb/teams/{teamId}`
- [ ] `/sports/baseball/mlb/summary?event={gameId}`
- [ ] `/sports/baseball/mlb/teams/{teamId}/roster`

### sports.core.api.espn.com
- [ ] `/v2/sports/baseball/leagues/mlb/athletes/{athleteId}`
- [ ] `/v2/sports/baseball/leagues/mlb/athletes/{athleteId}/statistics`

## NHL Endpoints

### site.api.espn.com/apis/site/v2
- [ ] `/sports/hockey/nhl/scoreboard`
- [ ] `/sports/hockey/nhl/news`
- [ ] `/sports/hockey/nhl/teams`
- [ ] `/sports/hockey/nhl/teams/{teamId}`
- [ ] `/sports/hockey/nhl/summary?event={gameId}`
- [ ] `/sports/hockey/nhl/teams/{teamId}/roster`

### sports.core.api.espn.com
- [ ] `/v2/sports/hockey/leagues/nhl/athletes/{athleteId}`
- [ ] `/v2/sports/hockey/leagues/nhl/athletes/{athleteId}/statistics`

## NBA Endpoints

### site.api.espn.com/apis/site/v2
- [ ] `/sports/basketball/nba/scoreboard`
- [ ] `/sports/basketball/nba/news`
- [ ] `/sports/basketball/nba/teams`
- [ ] `/sports/basketball/nba/teams/{teamId}`
- [ ] `/sports/basketball/nba/summary?event={gameId}`
- [ ] `/sports/basketball/nba/teams/{teamId}/roster`

### sports.core.api.espn.com
- [ ] `/v2/sports/basketball/leagues/nba/athletes/{athleteId}`
- [ ] `/v2/sports/basketball/leagues/nba/athletes/{athleteId}/statistics`

## College Football Endpoints

### site.api.espn.com/apis/site/v2
- [ ] `/sports/football/college-football/scoreboard`
- [ ] `/sports/football/college-football/news`
- [ ] `/sports/football/college-football/teams`
- [ ] `/sports/football/college-football/teams/{teamId}`
- [ ] `/sports/football/college-football/summary?event={gameId}`
- [ ] `/sports/football/college-football/rankings`
- [ ] `/sports/football/college-football/teams/{teamId}/roster`

### sports.core.api.espn.com
- [ ] `/v2/sports/football/leagues/college-football/athletes/{athleteId}`
- [ ] `/v2/sports/football/leagues/college-football/athletes/{athleteId}/statistics`

## College Basketball Endpoints

### site.api.espn.com/apis/site/v2
- [ ] `/sports/basketball/mens-college-basketball/scoreboard`
- [ ] `/sports/basketball/mens-college-basketball/news`
- [ ] `/sports/basketball/mens-college-basketball/teams`
- [ ] `/sports/basketball/mens-college-basketball/teams/{teamId}`
- [ ] `/sports/basketball/mens-college-basketball/summary?event={gameId}`
- [ ] `/sports/basketball/mens-college-basketball/rankings`
- [ ] `/sports/basketball/mens-college-basketball/teams/{teamId}/roster`

### sports.core.api.espn.com
- [ ] `/v2/sports/basketball/leagues/mens-college-basketball/athletes/{athleteId}`
- [ ] `/v2/sports/basketball/leagues/mens-college-basketball/athletes/{athleteId}/statistics`

## General/Core Endpoints

### site.web.api.espn.com
- [ ] `/apis/common/v3/search`
- [ ] `/apis/search/v2`

### sports.core.api.espn.com
- [x] `/v2/sports/{sport}/leagues/{league}/calendar`
- [x] `/v2/sports/{sport}/leagues/{league}/venues`
- [x] `/v2/sports/{sport}/leagues/{league}/franchises`
- [x] `/v2/sports/{sport}/leagues/{league}/seasons`
- [x] `/v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{seasonType}/weeks`
- [x] `/v2/sports/{sport}/leagues/{league}/events`
- [x] `/v2/sports/{sport}/leagues/{league}/events/{eventId}`

### site.web.api.espn.com
- [ ] `/apis/v2/scoreboard/header`

## Additional Endpoint Types

### Fantasy Sports Endpoints (fantasy.espn.com)
- [ ] `/apis/v3/games/ffl/seasons/{year}/segments/{segment}/leagues/{leagueId}`
- [ ] `/apis/v3/games/ffl/seasons/{year}/segments/{segment}/leagues/{leagueId}/teams/{teamId}`
- [ ] `/apis/v3/games/ffl/seasons/{year}/segments/{segment}/leagues/{leagueId}/players/available`

### Stats Endpoints (site.api.espn.com)
- [ ] `/apis/v3/stats/football/nfl/playbyplay/{eventId}`
- [ ] `/apis/v3/stats/basketball/nba/playbyplay/{eventId}`
- [ ] `/apis/v3/stats/baseball/mlb/playbyplay/{eventId}`
- [ ] `/apis/v3/stats/hockey/nhl/playbyplay/{eventId}`

## Implementation Plan for Multiple Base URLs

To handle multiple base URLs in our OpenAPI specification, we will:

1. Create separate OpenAPI specification files for each base URL domain:
   - `spec-site-api.yaml` - For site.api.espn.com endpoints
   - `spec-sports-core-api.yaml` - For sports.core.api.espn.com endpoints
   - `spec-site-web-api.yaml` - For site.web.api.espn.com endpoints
   - `spec-fantasy.yaml` - For fantasy.espn.com endpoints

2. Each specification file will define:
   - Its own servers section with the appropriate base URL
   - Only the paths relevant to that base URL
   - Shared schemas/components will be duplicated where needed

3. Deployment-specific considerations:
   - Generate separate client libraries for each specification
   - Create a unified client wrapper that imports from all generated clients

4. For development, prioritize completing one base URL specification at a time:
   1. Complete site.api.espn.com endpoints first (most frequently used)
   2. Then address sports.core.api.espn.com endpoints
   3. Follow with other base URLs based on priority

5. Testing will be organized by base URL to ensure efficient validation of each API domain.- [x] Fetch and print games for each week of the regular season using the week param in test-cdn.py
