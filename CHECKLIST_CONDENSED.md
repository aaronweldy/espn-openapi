# ESPN API Endpoints Checklist (Condensed)

## I. General & Cross-Sport Endpoints

### site.api.espn.com
- [ ] `/apis/site/v2/sports` - List all available sports
- [ ] `/apis/site/v2/sports/{sport}` - List leagues for a specific sport
- [x] `/apis/site/v2/sports/{sport}/{league}/news` - List News (League). Query: limit
- [x] `/apis/site/v2/sports/{sport}/{league}/scoreboard` - Scoreboard. Query: dates, week, seasontype
- [x] `/apis/site/v2/sports/{sport}/{league}/teams` - Teams List
- [x] `/apis/site/v2/sports/{sport}/{league}/teams/{team_id}` - Specific Team (ID or Abbreviation)
- [x] `/apis/site/v2/sports/{sport}/{league}/summary` - Game Summary. Query: event={event_id}
- [x] `/apis/site/v2/sports/{sport}/{league}/teams/{team_id}/roster` - Team Roster. Query: enable=roster,projection,stats
- [x] `/apis/site/v2/sports/{sport}/{league}/standings` - Standings. Query: season
- [x] `/apis/site/v2/sports/{sport}/{league}/teams/{team_id}/schedule` - Team Schedule. Query: season
- [ ] `/apis/site/v2/sports/{sport}/{league}/rankings` - Rankings (for applicable sports)

### site.web.api.espn.com
- [x] `/apis/common/v3/search` - General Search. Query: query, limit, mode
- [x] `/apis/search/v2` - General Search (v2). Query: query, limit
- [x] `/apis/v2/scoreboard/header` - Scoreboard Header. Query: sport, league
- [x] `/apis/common/v3/sports/{sport}/{league}/athletes/{athlete_id}/overview` - Athlete overview
- [x] `/apis/common/v3/sports/{sport}/{league}/athletes/{athlete_id}/gamelog` - Athlete game log
- [x] `/apis/common/v3/sports/{sport}/{league}/athletes/{athlete_id}/splits` - Athlete Splits
- [x] `/apis/common/v3/sports/{sport}/{league}/season` - Season Info (start/end dates, types)

### sports.core.api.espn.com
- [x] `/v2/sports/{sport}/leagues/{league}/calendar/ondays` - Calendar - Ondays
- [x] `/v2/sports/{sport}/leagues/{league}/calendar/offdays` - Calendar - Offdays
- [x] `/v2/sports/{sport}/leagues/{league}/calendar/whitelist` - Calendar - Whitelist
- [x] `/v2/sports/{sport}/leagues/{league}/calendar/blacklist` - Calendar - Blacklist
- [x] `/v2/sports/{sport}/leagues/{league}/venues` - List Venues. Query: limit
- [x] `/v2/sports/{sport}/leagues/{league}/franchises` - List Franchises. Query: limit
- [x] `/v2/sports/{sport}/leagues/{league}/seasons` - List Seasons. Query: limit
- [x] `/v2/sports/{sport}/leagues/{league}/seasons/{year}` - Get Season Details
- [x] `/v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{seasontype}/weeks` - List Weeks for Season
- [ ] `/v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{seasontype}/weeks/{weeknum}` - Get Week Details
- [x] `/v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{season_type}/groups` - List Groups for Season
- [x] `/v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{season_type}/corrections` - List Statistical Corrections
- [x] `/v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{season_type}/groups/{group_id}` - Get Group Details
- [x] `/v2/sports/{sport}/leagues/{league}/events` - List Events (Games). Query: dates, limit
- [ ] `/v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{seasontype}/weeks/{week}/events` - List Events by Week
- [x] `/v2/sports/{sport}/leagues/{league}/events/{event_id}` - Get Specific Event
- [x] `/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}` - Competition Details
- [x] `/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/situation` - Competition Situation
- [x] `/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/status` - Competition Status
- [x] `/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/odds` - Competition Odds
- [x] `/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/broadcasts` - Competition Broadcasts
- [x] `/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/officials` - Competition Officials
- [x] `/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/leaders` - Competition Leaders
- [x] `/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/competitors/{competitor_id}/roster/{athlete_id}/statistics/{page}` - Athlete Statistics
- [x] `/v2/sports/{sport}/leagues/{league}/athletes/{athlete_id}` - Detailed athlete information
- [x] `/v2/sports/{sport}/leagues/{league}/athletes/{athlete_id}/statistics` - Athlete Statistics. Query: limit, seasontype, year, week
- [x] `/v2/sports/{sport}/leagues/{league}/athletes/{athlete_id}/contracts` - Athlete Contracts
- [ ] `/v2/sports/{sport}/leagues/{league}/seasons/{yr}/freeagents` - Free agents
- [x] `/v2/sports/{sport}/leagues/{league}/athletes/{athlete_id}/contracts/{year}` - Athlete Contract by Year
- [x] `/v2/sports/{sport}/leagues/{league}/positions` - List Player Positions. Query: limit
- [x] `/v2/sports/{sport}/leagues/{league}/transactions` - List Transactions
- [x] `/v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{seasontype}/weeks/{week}/talentpicks` - Weekly Talent Picks
- [x] `/v2/sports/{sport}/leagues/{league}/seasons/{year}/draft/athletes/{athlete_id}` - Draft Athlete Details
- [x] `/v3/sports/{sport}/{league}/athletes` - List Athletes (v3). Query: limit, active=true, page
- [ ] `/v2/sports/{sport}/leagues/{league}/seasons/{year}/coaches` - Coaches
- [ ] `/v2/sports/{sport}/leagues/{league}/seasons/{year}/draft/athletes/{athlete_id}/statisticslog` - Draft Athlete Stats Log

## II. Sport-Specific Endpoints

### NFL-Specific
#### site.api.espn.com
- [x] `/apis/site/v2/mondaynightfootball` - Monday Night Football
- [x] `/apis/site/v2/thursdaynightfootball` - Thursday Night Football
- [x] `/apis/site/v2/sundaynightfootball` - Sunday Night Football

#### cdn.espn.com
- [x] `/core/nfl/scoreboard` - NFL Scoreboard (CDN). Params: xhr=1, limit
- [x] `/core/nfl/schedule` - NFL Schedule (CDN). Params: xhr=1, year, week
- [x] `/core/nfl/standings` - NFL Standings (CDN). Params: xhr=1, season
- [x] `/core/nfl/boxscore` - NFL Game Boxscore (CDN). Params: xhr=1, gameId={event_id}
- [x] `/core/nfl/playbyplay` - NFL Game Play-by-Play (CDN). Params: xhr=1, gameId={event_id}

#### sports.core.api.espn.com
- [x] `/v2/sports/football/leagues/nfl/athletes/{athlete_id}/statisticslog` - NFL Athlete statistics log
- [x] `/v2/sports/football/leagues/nfl/events/{event_id}/competitions/{event_id}/plays` - NFL Game Plays. Query: limit
- [x] `/v2/sports/football/leagues/nfl/events/{event_id}/competitions/{event_id}/drives` - NFL Game Drives
- [x] `/v2/sports/football/leagues/nfl/seasons/{year}/teams/{team_id}` - NFL Get Team (Core API)
- [x] `/v2/sports/football/leagues/nfl/teams/{team_id}/injuries` - NFL Team Injuries
- [x] `/v2/sports/football/leagues/nfl/seasons/{year}/teams/{team_id}/depthcharts` - NFL Team Depth Chart
- [x] `/v2/sports/football/leagues/nfl/seasons/{year}/athletes/{athlete_id}/eventlog` - NFL Athlete Eventlog
- [x] `/v2/sports/football/leagues/nfl/seasons/{year}/types/{seasontype}/leaders` - NFL Leaders (Core API)
- [x] `/v2/sports/football/leagues/nfl/seasons/{year}/draft` - NFL Draft
- [x] `/v2/sports/football/leagues/nfl/seasons/{year}/draft/rounds` - NFL Draft Rounds
- [x] `/v2/sports/football/leagues/nfl/seasons/{year}/types/{seasontype}/groups/{group_id}/standings` - NFL Conference Standings

### NBA-Specific
- [ ] `/apis/site/v2/sports/basketball/nba/{team_id_or_abbrev}/schedule` - NBA Team Schedule (different path structure)

### Soccer-Specific
#### site.api.espn.com
- [ ] `/apis/site/v2/sports/soccer` - List Soccer Leagues (provides slugs)
- [ ] `/apis/site/v2/sports/soccer/{league_slug}/scoreboard` - Soccer Scoreboard/Schedule
- [ ] `/apis/site/v2/sports/soccer/{league_slug}/standings` - Soccer Standings
- [ ] `/apis/site/v2/sports/soccer/{league_slug}/teams` - Soccer Teams List
- [ ] `/apis/site/v2/sports/soccer/{league_slug}/players` - Soccer Players List
- [ ] `/apis/site/v2/sports/soccer/{competition_slug}/teams/{team_id}/schedule` - Soccer Team Schedule

### College Sports Patterns
- Use `college-football`, `mens-college-basketball`, `womens-college-basketball`, `college-baseball` as the league parameter
- Additional endpoints:
  - [ ] Scoreboard with `groups` parameter for conferences
  - [ ] `/v2/sports/basketball/leagues/mens-college-basketball/tournaments/22/seasons/{season}/bracketology` - Bracketology

### Other Sports Patterns
- Golf: `/sports/golf/{league_slug}/players` (league_slug: pga, lpga)
- Tennis: `/sports/tennis/{tour}/players` (tour: atp, wta)
- Racing: `/sports/racing/{league_slug}/...` (league_slug: f1, nascar-premier)

## III. Fantasy Sports Endpoints

### fantasy.espn.com / lm-api-reads.fantasy.espn.com
- [ ] `/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{league_id}` - Fantasy League Data. Query: view. Headers: X-Fantasy-Filter, Cookies
- [ ] `/apis/v3/games/ffl/leagueHistory/{league_id}` - Fantasy League History. Query: seasonId, view
- [ ] `/apis/v3/games/ffl/seasons/{year}/players` - Fantasy Player Info. Query: view=players_wl
- [ ] `/apis/v3/games/ffl/seasons/{year}/segments/0/leaguedefaults/{PPR_ID}` - Detailed Fantasy Player Info
- [ ] `/apis/v3/games/ffl/seasons/{year}` - Fantasy Team Schedules. Query: view=proTeamSchedules_wl

### site.api.espn.com
- [ ] `/apis/fantasy/v2/games/ffl/news/players` - Fantasy Player News. Query: playerId, limit

### site.web.api.espn.com
- [ ] `/apis/fantasy/v2/games/ffl/games` - Fantasy Games List. Query: dates

### gambit-api.fantasy.espn.com
- [ ] `/apis/v1/challenges/{challenge_name}` - Pick'em Challenges
- [ ] `/apis/v1/propositions` - Pick'em Propositions

### now.core.api.espn.com
- [ ] `/v1/sports/news` - General news feed. Query: sport (optional), limit

## IV. Stats Endpoints (Play-by-Play)

### site.api.espn.com
- [ ] `/apis/v3/stats/{sport}/{league}/playbyplay/{event_id}` - Play-by-Play for all sports

## V. Betting & Odds Endpoints

### sports.core.api.espn.com
- [ ] `/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{event_id}/probabilities` - Win Probabilities
- [ ] `/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{event_id}/odds/{provider_id}` - Odds from Provider
- [ ] `/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{event_id}/odds/{provider_id}/history/0/movement` - Odds Movement
- [ ] `/v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{event_id}/predictor` - ESPN Predictor
- [ ] `/v2/sports/{sport}/leagues/{league}/seasons/{year}/futures` - Futures Bets
- [ ] `/v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{seasontype}/teams/{team_id}/ats` - Team ATS Records
- [ ] `/v2/sports/{sport}/leagues/{league}/teams/{team_id}/odds/{provider_id}/past-performances` - Team Past Performance

## Notes
- `{sport}` values: football, basketball, baseball, hockey, soccer, golf, tennis, racing
- `{league}` values: nfl, nba, mlb, nhl, wnba, college-football, mens-college-basketball, etc.
- `{seasontype}` values: 1=preseason, 2=regular, 3=postseason, 4=offseason
- CDN endpoints use `xhr=1` parameter
- Some endpoints require authentication (Fantasy) or special headers