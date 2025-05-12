# ESPN API OpenAPI Schema Checklist

## NFL Endpoints

- [x] `/sports/football/nfl/scoreboard` - Already implemented
- [x] `/sports/football/nfl/teams` - Already implemented
- [x] `/sports/football/nfl/teams/{teamId}` - Already implemented
- [x] `/sports/football/nfl/summary` - Already implemented
- [x] `/sports/football/nfl/news` - Implemented
- [x] `/v2/sports/football/nfl/standings` - Implemented
- [x] `/sports/football/nfl/teams/{teamId}/roster` - Implemented
- [ ] `/sports/football/nfl/athletes/{athleteId}`
- [ ] `/sports/football/nfl/athletes/{athleteId}/stats`

## MLB Endpoints

- [ ] `/sports/baseball/mlb/scoreboard`
- [ ] `/sports/baseball/mlb/news`
- [ ] `/sports/baseball/mlb/teams`
- [ ] `/sports/baseball/mlb/teams/{teamId}`
- [ ] `/sports/baseball/mlb/summary?event={gameId}`
- [ ] `/sports/baseball/mlb/teams/{teamId}/roster`
- [ ] `/sports/baseball/mlb/athletes/{athleteId}`
- [ ] `/sports/baseball/mlb/athletes/{athleteId}/stats`

## NHL Endpoints

- [ ] `/sports/hockey/nhl/scoreboard`
- [ ] `/sports/hockey/nhl/news`
- [ ] `/sports/hockey/nhl/teams`
- [ ] `/sports/hockey/nhl/teams/{teamId}`
- [ ] `/sports/hockey/nhl/summary?event={gameId}`
- [ ] `/sports/hockey/nhl/teams/{teamId}/roster`
- [ ] `/sports/hockey/nhl/athletes/{athleteId}`
- [ ] `/sports/hockey/nhl/athletes/{athleteId}/stats`

## NBA Endpoints

- [ ] `/sports/basketball/nba/scoreboard`
- [ ] `/sports/basketball/nba/news`
- [ ] `/sports/basketball/nba/teams`
- [ ] `/sports/basketball/nba/teams/{teamId}`
- [ ] `/sports/basketball/nba/summary?event={gameId}`
- [ ] `/sports/basketball/nba/teams/{teamId}/roster`
- [ ] `/sports/basketball/nba/athletes/{athleteId}`
- [ ] `/sports/basketball/nba/athletes/{athleteId}/stats`

## College Football Endpoints

- [ ] `/sports/football/college-football/scoreboard`
- [ ] `/sports/football/college-football/news`
- [ ] `/sports/football/college-football/teams`
- [ ] `/sports/football/college-football/teams/{teamId}`
- [ ] `/sports/football/college-football/summary?event={gameId}`
- [ ] `/sports/football/college-football/rankings`
- [ ] `/sports/football/college-football/teams/{teamId}/roster`
- [ ] `/sports/football/college-football/athletes/{athleteId}`
- [ ] `/sports/football/college-football/athletes/{athleteId}/stats`

## College Basketball Endpoints

- [ ] `/sports/basketball/mens-college-basketball/scoreboard`
- [ ] `/sports/basketball/mens-college-basketball/news`
- [ ] `/sports/basketball/mens-college-basketball/teams`
- [ ] `/sports/basketball/mens-college-basketball/teams/{teamId}`
- [ ] `/sports/basketball/mens-college-basketball/summary?event={gameId}`
- [ ] `/sports/basketball/mens-college-basketball/rankings`
- [ ] `/sports/basketball/mens-college-basketball/teams/{teamId}/roster`
- [ ] `/sports/basketball/mens-college-basketball/athletes/{athleteId}`
- [ ] `/sports/basketball/mens-college-basketball/athletes/{athleteId}/stats`

## General/Core Endpoints

- [ ] `/apis/common/v3/search`
- [ ] `/apis/search/v2`
- [ ] `/v2/sports/{sport}/leagues/{league}/calendar`
- [ ] `/v2/sports/{sport}/leagues/{league}/venues`
- [ ] `/v2/sports/{sport}/leagues/{league}/franchises`
- [ ] `/v2/sports/{sport}/leagues/{league}/seasons/{year}`
- [ ] `/v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{seasonType}/weeks`
- [ ] `/v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{seasonType}/weeks/{weekNumber}`
- [ ] `/v2/sports/{sport}/leagues/{league}/events`
- [ ] `/apis/v2/scoreboard/header`

## Additional Endpoint Types

### Fantasy Sports Endpoints
- [ ] `/apis/v3/games/ffl/seasons/{year}/segments/{segment}/leagues/{leagueId}`
- [ ] `/apis/v3/games/ffl/seasons/{year}/segments/{segment}/leagues/{leagueId}/teams/{teamId}`
- [ ] `/apis/v3/games/ffl/seasons/{year}/segments/{segment}/leagues/{leagueId}/players/available`

### Stats Endpoints
- [ ] `/apis/v3/stats/football/nfl/playbyplay/{eventId}`
- [ ] `/apis/v3/stats/basketball/nba/playbyplay/{eventId}`
- [ ] `/apis/v3/stats/baseball/mlb/playbyplay/{eventId}`
- [ ] `/apis/v3/stats/hockey/nhl/playbyplay/{eventId}`

## Implementation Plan

1. Complete NFL endpoints first (most popular and already started)
2. Add individual athlete endpoints for NFL
3. Add MLB endpoints
4. Add NBA endpoints
5. Add NHL endpoints
6. Add college sports endpoints
7. Add fantasy sports endpoints
8. Add stats-specific endpoints
9. Add general/core endpoints

## Considerations for Each Endpoint

For each endpoint, the following steps should be completed:
1. Fetch sample response from the API and save it to the json_output directory
2. Document the response format in the OpenAPI schema (spec.yaml)
3. Generate models using openapi-python-client
4. Write tests to validate the generated models (in tests directory)
5. Verify all required fields are captured in the schema
6. Add the endpoint to the Python client with proper documentation