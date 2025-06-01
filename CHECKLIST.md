I. General & Cross-Sport Endpoints
site.api.espn.com
[x] /apis/site/v2/sports/{sport}/{league}/news - List News (League). Path Params: {sport}, {league}. Query Params: limit
(Note: NFL-specific news was marked implemented, this is generic. If NFL covers the pattern, this might be implicitly partially done)
site.web.api.espn.com
[x] /apis/common/v3/search - General Search. Query Params: query, limit, mode (e.g., prefix) - Implemented from NFL section
[x] /apis/search/v2 - General Search (v2). Query Params: query, limit - Implemented from NFL section
[x] /apis/v2/scoreboard/header - Scoreboard Header. Query Params: sport, league
sports.core.api.espn.com
[x] /v2/sports/{sport}/leagues/{league}/calendar/ondays - Calendar - Ondays. Path Params: {sport}, {league} - Derived from Implemented General Calendar
[x] /v2/sports/{sport}/leagues/{league}/calendar/offdays - Calendar - Offdays. Path Params: {sport}, {league} - Derived from Implemented General Calendar
[x] /v2/sports/{sport}/leagues/{league}/calendar/whitelist - Calendar - Whitelist. Path Params: {sport}, {league} - Derived from Implemented General Calendar
[x] /v2/sports/{sport}/leagues/{league}/calendar/blacklist - Calendar - Blacklist. Path Params: {sport}, {league} - Derived from Implemented General Calendar
[x] /v2/sports/{sport}/leagues/{league}/venues - List Venues. Path Params: {sport}, {league}. Query Params: limit - Implemented
[x] /v2/sports/{sport}/leagues/{league}/franchises - List Franchises. Path Params: {sport}, {league}. Query Params: limit - Implemented
[x] /v2/sports/{sport}/leagues/{league}/seasons - List Seasons. Path Params: {sport}, {league}. Query Params: limit - Implemented
[x] /v2/sports/{sport}/leagues/{league}/seasons/{year} - Get Season Details. Path Params: {sport}, {league}, {year} - Implemented
[x] /v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{seasontype}/weeks - List Weeks for Season. Path Params: {sport}, {league}, {year}, {seasontype} (e.g., 1=pre, 2=reg, 3=post) - Implemented
[x] /v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{seasontype}/weeks/{weeknum} - Get Week Details. Path Params: {sport}, {league}, {year}, {seasontype}, {weeknum} - Implemented
[x] /v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{season_type}/groups - List Groups for Season. Path Params: {sport}, {league}, {year}, {season_type} - Implemented
[x] /v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{season_type}/corrections - List Statistical Corrections for Season. Path Params: {sport}, {league}, {year}, {season_type} - Implemented
[x] /v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{season_type}/groups/{group_id} - Get Group Details. Path Params: {sport}, {league}, {year}, {season_type}, {group_id} - Implemented
[x] /v2/sports/{sport}/leagues/{league}/events - List Events (Games). Path Params: {sport}, {league}. Query Params: dates (e.g., YYYYMMDD, YYYYMMDD-YYYYMMDD, YYYY), limit - Implemented
[x] /v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{seasontype}/weeks/{week}/events - List Events by Week. Path Params: {sport}, {league}, {year}, {seasontype}, {week} - Implemented
[x] /v2/sports/{sport}/leagues/{league}/events/{event_id} - Get Specific Event. Path Params: {sport}, {league}, {event_id} - Derived from Implemented General Events
[x] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}
[x] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/situation
[x] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/status
[x] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/odds
[x] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/broadcasts
[x] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/officials
[x] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/leaders
[x] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/competitors/{competitor_id}/roster/{athlete_id}/statistics/{page} - Athlete Statistics. Path Params: {sport}, {league}, {event_id}, {competition_id}, {competitor_id}, {athlete_id}, {page}
[x] /v2/sports/{sport}/leagues/{league}/athletes/{athlete_id}/statistics - Athlete Statistics. Path Params: {sport}, {league}, {athlete_id}. Query params: limit, seasontype, year, week - Generic endpoint (consolidates NFL, NBA, MLB, NHL)
[x] /v2/sports/{sport}/leagues/{league}/athletes/{athlete_id}/statisticslog - Athlete Statistics Log. Path Params: {sport}, {league}, {athlete_id} - Generic endpoint (consolidates NFL, NBA, MLB, NHL)
[x] /v2/sports/{sport}/leagues/{league}/athletes/{athlete_id}/contracts - Athlete Contracts. Path Params: {sport}, {league}, {athlete_id}
[x] /v2/sports/{sport}/leagues/{league}/athletes/{athlete_id}/contracts/{year} - Athlete Contract by Year. Path Params: {sport}, {league}, {athlete_id}, {year}
II. NFL Endpoints
site.api.espn.com/apis/site/v2
[x] /sports/{sport}/{league}/scoreboard - Generic Scoreboard Endpoint. Path Params: {sport}, {league}. Query Params: dates, week (football only), seasontype (football only) - Implemented as generic endpoint
[x] /sports/football/nfl/teams - NFL Teams List - Already implemented
[x] /sports/football/nfl/teams/{team_id} - NFL Specific Team (ID or Abbreviation). Path Param: {team_id} - Already implemented (path refined)
[x] /sports/football/nfl/summary - NFL Game Summary. Query Param: event={event_id} - Already implemented
[x] /sports/football/nfl/news - NFL News. Query Params: limit - Implemented
[x] /sports/football/nfl/news?team={team_id} - NFL News (Team Specific). Query Params: team={team_id}
[x] /sports/football/nfl/teams/{team_id}/roster - NFL Team Roster. Path Param: {team_id}. Query Params: enable=roster,projection,stats - Implemented (path refined)
[x] /sports/football/nfl/standings - NFL Standings. Query Param: season - Implemented
[x] /sports/football/nfl/teams/{team_id}/schedule - NFL Team Schedule. Path Param: {team_id}. Query Param: season - Implemented as generic /sports/{sport}/{league}/teams/{team_id_or_abbrev}/schedule
[x] /apis/site/v2/mondaynightfootball - Specific Night Football
[x] /apis/site/v2/thursdaynightfootball - Specific Night Football
[x] /apis/site/v2/sundaynightfootball - Specific Night Football
cdn.espn.com
[x] /core/nfl/scoreboard - NFL Scoreboard (CDN). Params: xhr=1, limit ✓
[x] /core/nfl/schedule - NFL Schedule (CDN). Params: xhr=1, year, week ✓
[x] /core/nfl/standings - NFL Standings (CDN). Params: xhr=1, season ✓ (original had season, README table has xhr=1 only) - Note: Initial checklist param season might be for site.api, CDN version shows xhr=1 in README table.
[x] /core/nfl/boxscore - NFL Game Boxscore (CDN). Params: xhr=1, gameId={event_id} ✓
[x] /core/nfl/playbyplay - NFL Game Play-by-Play (CDN). Params: xhr=1, gameId={event_id} ✓
[x] /core/nfl/recap - NFL Game Recap (CDN). Params: xhr=1, gameId={event_id}
[x] /core/nfl/game - NFL Game Details (CDN). Params: xhr=1, gameId={event_id}
[x] /core/nfl/matchup - NFL Game Matchup (CDN). Params: xhr=1, gameId={event_id}
sports.core.api.espn.com
[x] /v3/sports/football/nfl/athletes - List NFL Athletes (v3). Query Params: limit, active=true, page - (Matches broadly with /v2/.../athletes/ from initial checklist which was marked implemented)
[x] /v2/sports/football/leagues/nfl/athletes/{athlete_id} - Detailed NFL athlete information. Path Param: {athlete_id} - (This is more specific than the list, matches original athletes/ part)
[x] /v2/sports/football/leagues/nfl/athletes/{athlete_id}/statistics - NFL Athlete statistics. Path Param: {athlete_id} - Covered by generic /v2/sports/{sport}/leagues/{league}/athletes/{athlete_id}/statistics
[x] /v2/sports/football/leagues/nfl/athletes/{athlete_id}/statisticslog - NFL Athlete statistics log. Path Param: {athlete_id} - Covered by generic /v2/sports/{sport}/leagues/{league}/athletes/{athlete_id}/statisticslog
[x] /v2/sports/football/leagues/nfl/events/{event_id}/competitions/{event_id}/plays - NFL Game Plays. Path Param: {event_id}. Query Param: limit (e.g., 300+) - (Matches original)
[x] /v2/sports/football/leagues/nfl/events/{event_id}/competitions/{event_id}/drives - NFL Game Drives. Path Param: {event_id} - (Matches original)
[x] /v2/sports/football/leagues/nfl/seasons/{year}/teams/{team_id} - NFL Get Team (Core API). Path Params: {year}, {team_id}
[x] /v2/sports/football/leagues/nfl/teams/{team_id}/injuries - NFL Team Injuries. Path Param: {team_id}
[x] /v2/sports/football/leagues/nfl/seasons/{year}/teams/{team_id}/depthcharts - NFL Team Depth Chart. Path Params: {year}, {team_id}
[x] /v2/sports/football/leagues/nfl/seasons/{year}/athletes/{athlete_id}/eventlog - NFL Athlete Eventlog. Path Params: {year}, {athlete_id}
[x] /v2/sports/football/leagues/nfl/seasons/{year}/types/{seasontype}/leaders - NFL Leaders (Core API). Path Params: {year}, {seasontype}
[x] /v2/sports/football/leagues/nfl/seasons/{year}/draft - NFL Draft. Path Param: {year}
[x] /v2/sports/football/leagues/nfl/seasons/{year}/draft/rounds - NFL Draft Rounds. Path Param: {year}
[x] /v2/sports/football/leagues/nfl/seasons/{year}/draft/athletes/{athlete_id} - NFL Draft Athlete Details. Path Params: {year}, {athlete_id}
[x] /v2/sports/football/leagues/nfl/seasons/{year}/types/{seasontype}/groups/{group_id}/standings - NFL Conference Standings. Path Params: {year}, {seasontype}, {group_id} (e.g., 7=NFC, 8=AFC)
site.web.api.espn.com
[x] /apis/common/v3/sports/football/nfl/athletes/{athlete_id}/overview - NFL Athlete overview. Path Param: {athlete_id} - (Matches original)
[x] /apis/common/v3/sports/football/nfl/athletes/{athlete_id}/gamelog - NFL Athlete game log. Path Param: {athlete_id} - (Matches original)
[x] /apis/common/v3/sports/football/nfl/athletes/{athlete_id}/splits - NFL Athlete Splits. Path Param: {athlete_id}
III. MLB Endpoints
site.api.espn.com/apis/site
[x] /v2/sports/baseball/mlb/scoreboard - MLB Scoreboard. Query Param: dates (YYYYMMDD) - Covered by generic /sports/{sport}/{league}/scoreboard endpoint
[x] /v2/sports/baseball/mlb/news - MLB News
[x] /v2/sports/baseball/mlb/teams - MLB Teams List
[x] /v2/sports/baseball/mlb/teams/{team_id_or_abbrev} - MLB Specific Team. Path Param: {team_id_or_abbrev}
[x] /v2/sports/baseball/mlb/summary?event={event_id} - MLB Game Summary. Query Param: event={event_id} (implemented)
[x] /v2/sports/baseball/mlb/teams/{team_id_or_abbrev}/roster - MLB Team Roster. Path Param: {team_id_or_abbrev}
sports.core.api.espn.com
[x] /v2/sports/baseball/leagues/mlb/athletes/{athlete_id} - Detailed MLB athlete information. Path Param: {athlete_id}
[x] /apis/common/v3/sports/baseball/mlb/athletes/{athlete_id} - MLB Player Details. Path Param: {athlete_id}
site.web.api.espn.com
IV. NHL Endpoints
site.api.espn.com/apis/site
[x] /v2/sports/hockey/nhl/scoreboard - NHL Scoreboard. Query Param: dates (YYYYMMDD) - Covered by generic /sports/{sport}/{league}/scoreboard endpoint
[x] /v2/sports/hockey/nhl/teams - NHL Teams List
[x] /v2/sports/hockey/nhl/teams/{team_id_or_abbrev} - NHL Specific Team. Path Param: {team_id_or_abbrev}
[x] /v2/sports/hockey/nhl/summary?event={event_id} - NHL Game Summary. Query Param: event={event_id}
[x] /v2/sports/hockey/nhl/teams/{team_id_or_abbrev}/roster - NHL Team Roster. Path Param: {team_id_or_abbrev}
[x] /v2/sports/hockey/nhl/statistics/players - NHL Aggregate Player Statistics - DOES NOT EXIST
sports.core.api.espn.com
[x] /v2/sports/hockey/leagues/nhl/athletes/{athlete_id} - Detailed NHL athlete information. Path Param: {athlete_id} - Covered by generic endpoint
[x] /v2/sports/hockey/leagues/nhl/athletes/{athlete_id}/statistics - NHL Athlete statistics. Path Param: {athlete_id} - Covered by generic endpoint
V. NBA Endpoints
site.api.espn.com/apis/site/v2
[x] /sports/basketball/nba/scoreboard - NBA Scoreboard. Query Param: dates (YYYYMMDD) - Covered by generic /sports/{sport}/{league}/scoreboard endpoint
[x] /sports/basketball/nba/news - NBA News - Covered by generic /sports/{sport}/{league}/news endpoint
[x] /sports/basketball/nba/teams - NBA Teams List - Covered by generic /sports/{sport}/{league}/teams endpoint
[x] /sports/basketball/nba/teams/{team_id_or_abbrev} - NBA Specific Team. Path Param: {team_id_or_abbrev} - Covered by generic /sports/{sport}/{league}/teams/{team_id_or_abbrev} endpoint
[x] /sports/basketball/nba/summary?event={event_id} - NBA Game Summary. Query Param: event={event_id} - Covered by generic /sports/{sport}/{league}/summary endpoint
[x] /sports/basketball/nba/teams/{team_id_or_abbrev}/roster - NBA Team Roster. Path Param: {team_id_or_abbrev} - Covered by generic /sports/{sport}/{league}/teams/{team_id_or_abbrev}/roster endpoint
[x] /sports/basketball/nba/{team_id_or_abbrev}/schedule - NBA Team Schedule. Path Param: {team_id_or_abbrev}. Query Param: season - Implemented as generic /sports/{sport}/{league}/teams/{team_id_or_abbrev}/schedule
sports.core.api.espn.com
[x] /v2/sports/basketball/leagues/nba/athletes/{athlete_id} - Detailed NBA athlete information. Path Param: {athlete_id} - Covered by generic /v2/sports/{sport}/leagues/{league}/athletes/{athlete_id}
[x] /v2/sports/basketball/leagues/nba/athletes/{athlete_id}/statistics - NBA Athlete statistics. Path Param: {athlete_id} - Covered by generic /v2/sports/{sport}/leagues/{league}/athletes/{athlete_id}/statistics
VI. WNBA Endpoints
site.api.espn.com/apis/site/v2
[x] /sports/basketball/wnba/scoreboard - WNBA Scoreboard. Query Param: dates (YYYYMMDD) - Covered by generic /sports/{sport}/{league}/scoreboard endpoint
[x] /sports/basketball/wnba/news - WNBA News - Covered by generic /sports/{sport}/{league}/news endpoint
[x] /sports/basketball/wnba/teams - WNBA Teams List - Covered by generic /sports/{sport}/{league}/teams endpoint
[x] /sports/basketball/wnba/teams/{team_id_or_abbrev} - WNBA Specific Team. Path Param: {team_id_or_abbrev} - Covered by generic /sports/{sport}/{league}/teams/{team_id_or_abbrev} endpoint
VII. College Football Endpoints
site.api.espn.com/apis/site/v2
[x] /sports/football/college-football/scoreboard - College Football Scoreboard. Query Params: dates, groups (Conference ID), week - Covered by generic /sports/{sport}/{league}/scoreboard endpoint
[x] /sports/football/college-football/news - College Football News - Covered by generic /sports/{sport}/{league}/news endpoint
[x] /sports/football/college-football/teams - College Football Teams List - Covered by generic /sports/{sport}/{league}/teams endpoint
[x] /sports/football/college-football/teams/{team_abbrev_or_id} - College Football Specific Team. Path Param: {team_abbrev_or_id} - Covered by generic /sports/{sport}/{league}/teams/{team_id_or_abbrev} endpoint
[x] /sports/football/college-football/summary?event={event_id} - College Football Game Summary. Query Param: event={event_id} - Covered by generic /sports/{sport}/{league}/summary endpoint
[x] /sports/football/college-football/rankings - College Football Rankings (AP, Coaches, CFP) - Implemented as generic /sports/{sport}/{league}/rankings
[ ] /sports/football/college-football/teams/{team_abbrev_or_id}/roster - College Football Team Roster. Path Param: {team_abbrev_or_id}
site.api.espn.com/apis/common/v3
[x] /sports/football/college-football/season - College Football Season Info (start/end dates, types) - Implemented as generic /apis/common/v3/sports/{sport}/{league}/season
sports.core.api.espn.com
[ ] /v2/sports/football/leagues/college-football/athletes/{athlete_id} - Detailed College Football athlete. Path Param: {athlete_id}
[ ] /v2/sports/football/leagues/college-football/athletes/{athlete_id}/statistics - College Football Athlete statistics. Path Param: {athlete_id}
[ ] /v2/sports/football/leagues/college-football/ - Core College Football League Info (root endpoint)
VIII. College Basketball Endpoints (Men's)
site.api.espn.com/apis/site/v2
[x] /sports/basketball/mens-college-basketball/scoreboard - Men's College Basketball Scoreboard. Query Param: dates - Covered by generic /sports/{sport}/{league}/scoreboard endpoint
[x] /sports/basketball/mens-college-basketball/news - Men's College Basketball News - Covered by generic /sports/{sport}/{league}/news endpoint
[x] /sports/basketball/mens-college-basketball/teams - Men's College Basketball Teams List - Covered by generic /sports/{sport}/{league}/teams endpoint
[x] /sports/basketball/mens-college-basketball/teams/{team_abbrev_or_id} - Men's College Basketball Specific Team. Path Param: {team_abbrev_or_id} - Covered by generic /sports/{sport}/{league}/teams/{team_id_or_abbrev} endpoint
[x] /sports/basketball/mens-college-basketball/summary?event={event_id} - Men's College Basketball Game Summary. Query Param: event={event_id} - Covered by generic /sports/{sport}/{league}/summary endpoint
[x] /sports/basketball/mens-college-basketball/rankings - Men's College Basketball Rankings - Implemented as generic /sports/{sport}/{league}/rankings
[ ] /sports/basketball/mens-college-basketball/teams/{team_abbrev_or_id}/roster - Men's College Basketball Team Roster. Path Param: {team_abbrev_or_id}
sports.core.api.espn.com
[ ] /v2/sports/basketball/leagues/mens-college-basketball/athletes/{athlete_id} - Detailed Men's College Basketball athlete. Path Param: {athlete_id}
[ ] /v2/sports/basketball/leagues/mens-college-basketball/athletes/{athlete_id}/statistics - Men's College Basketball Athlete statistics. Path Param: {athlete_id}
[ ] /v2/sports/basketball/leagues/mens-college-basketball/tournaments/22/seasons/{season}/bracketology - Men's Bracketology (Historical). Path Param: {season}
fcast.espncdn.com
[ ] /FastcastService/pubsub/profiles/12000/topic/bracket-basketball-mens-college-basketball-22-en/message/24624/checkpoint - Men's Bracket Fastcast (Observed)
IX. College Basketball Endpoints (Women's)
site.api.espn.com/apis/site/v2
[x] /sports/basketball/womens-college-basketball/scoreboard - Women's College Basketball Scoreboard. Query Param: dates - Covered by generic /sports/{sport}/{league}/scoreboard endpoint
[x] /sports/basketball/womens-college-basketball/news - Women's College Basketball News - Covered by generic /sports/{sport}/{league}/news endpoint
[x] /sports/basketball/womens-college-basketball/teams - Women's College Basketball Teams List - Covered by generic /sports/{sport}/{league}/teams endpoint
[x] /sports/basketball/womens-college-basketball/teams/{team_abbrev_or_id} - Women's College Basketball Specific Team. Path Param: {team_abbrev_or_id} - Covered by generic /sports/{sport}/{league}/teams/{team_id_or_abbrev} endpoint
[x] /sports/basketball/womens-college-basketball/summary?event={event_id} - Women's College Basketball Game Summary. Query Param: event={event_id} - Covered by generic /sports/{sport}/{league}/summary endpoint
[x] /sports/basketball/womens-college-basketball/rankings - Women's College Basketball Rankings - Implemented as generic /sports/{sport}/{league}/rankings
[ ] /sports/basketball/womens-college-basketball/teams/{team_abbrev_or_id}/roster - Women's College Basketball Team Roster. Path Param: {team_abbrev_or_id}
sports.core.api.espn.com
[ ] /v2/sports/basketball/leagues/womens-college-basketball/athletes/{athlete_id} - Detailed Women's College Basketball athlete. Path Param: {athlete_id}
[ ] /v2/sports/basketball/leagues/womens-college-basketball/athletes/{athlete_id}/statistics - Women's College Basketball Athlete statistics. Path Param: {athlete_id}
X. College Baseball Endpoints
site.api.espn.com/apis/site/v2
[x] /sports/baseball/college-baseball/scoreboard - College Baseball Scoreboard. Query Param: dates - Covered by generic /sports/{sport}/{league}/scoreboard endpoint
site.api.espn.com/apis/common/v3
[x] /sports/baseball/college-baseball/season - College Baseball Season Info - Implemented as generic /apis/common/v3/sports/{sport}/{league}/season
XI. Soccer Endpoints
site.api.espn.com/apis/site/v2
[ ] /sports/soccer - List Soccer Leagues (provides slugs)
[ ] /sports/soccer/{league_slug}/scoreboard - Soccer Scoreboard/Schedule. Path Param: {league_slug}. Query Param: dates
[ ] /sports/soccer/{league_slug}/standings - Soccer Standings. Path Param: {league_slug}. Query Param: season (YYYY)
[ ] /sports/soccer/{league_slug}/teams - Soccer Teams List. Path Param: {league_slug}
[ ] /sports/soccer/{league_slug}/players - Soccer Players List. Path Param: {league_slug}
[ ] /sports/soccer/{league_slug}/statistics/players - Soccer Aggregate Player Statistics. Path Param: {league_slug}
[ ] /sports/soccer/{league_slug}/news - Soccer News. Path Param: {league_slug}
[ ] /sports/soccer/{competition_slug}/teams/{team_id}/schedule - Soccer Team Schedule. Path Params: {competition_slug}, {team_id}
XII. Other Sports Endpoints (Examples)
site.api.espn.com/apis/site/v2 (Pattern)
[ ] /sports/golf/{league_slug}/players - e.g., Golf Players. Path Param: {league_slug} (pga, lpga, etc.)
[ ] /sports/golf/{league_slug}/statistics/players - e.g., Golf Player Stats. Path Param: {league_slug}
[ ] /sports/racing/{league_slug}/... - e.g., Racing data. Path Param: {league_slug} (f1, nascar-premier, etc.)
[ ] /sports/tennis/{tour}/players - Tennis Players. Path Param: {tour} (atp, wta)
[ ] /sports/tennis/{tour}/statistics/players - Tennis Player Statistics. Path Param: {tour}
[ ] /sports/hockey/{league_slug}/... - Other Hockey Leagues (e.g., mens-college-hockey)
XIII. Fantasy Sports Endpoints
fantasy.espn.com (or lm-api-reads.fantasy.espn.com)
[ ] /apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{league_id} - Fantasy League Data (Current >2018). Path Params: {year}, {league_id}. Query Params: view={view_name} (e.g., mTeam, mRoster, mSettings). Headers: X-Fantasy-Filter (JSON string), Cookies: espn_s2, SWID (for private leagues)
[ ] /apis/v3/games/ffl/leagueHistory/{league_id}?seasonId={year} - Fantasy League Data (Historical <2018). Path Param: {league_id}. Query Params: seasonId={year}, view={view_name}. Headers: X-Fantasy-Filter, Cookies.
[ ] /apis/v3/games/ffl/seasons/{year}/players?view=players_wl - Fantasy Player Info List. Path Param: {year}. Query Param: view=players_wl. Headers: X-Fantasy-Filter (for filtering by ID, stat, etc.)
[ ] /apis/v3/games/ffl/seasons/{year}/segments/0/leaguedefaults/{PPR_ID}?view=kona_player_info - Detailed Fantasy Player Info. Path Params: {year}, {PPR_ID}. Query Param: view=kona_player_info. Headers: X-Fantasy-Filter.
[ ] /apis/v3/games/ffl/seasons/{year}?view=proTeamSchedules_wl - Fantasy Team Bye Weeks/Pro Schedules. Path Param: {year}. Query Param: view=proTeamSchedules_wl.
[ ] /apis/v3/games/ffl/seasons/{year}/players?scoringPeriodId=0&view=players_wl - Get % Owned Players (use with X-Fantasy-Filter). Path Param: {year}. Query Params: scoringPeriodId, view. Headers: X-Fantasy-Filter.
(The initial checklist had specific FFL league/team/players/available endpoints. These are generally covered by the main league endpoint with different view params or X-Fantasy-Filter on players endpoint.)
[ ] /apis/v3/games/ffl/seasons/{year}/segments/{segment_id}/leagues/{league_id} (More generic from checklist)
[ ] /apis/v3/games/ffl/seasons/{year}/segments/{segment_id}/leagues/{league_id}/teams/{team_id} (Likely view=mTeam or similar on league endpoint)
[ ] /apis/v3/games/ffl/seasons/{year}/segments/{segment_id}/leagues/{league_id}/players/available (Likely player list with filters)
site.api.espn.com
[ ] /apis/fantasy/v2/games/ffl/news/players - Fantasy Player News. Query Params: playerId={athlete_id}, limit
site.web.api.espn.com
[ ] /apis/fantasy/v2/games/ffl/games - Fantasy Games List. Query Params: dates (YYYYMMDD or YYYYMMDD-YYYYMMDD)
gambit-api.fantasy.espn.com
[ ] /apis/v1/challenges/{challenge_name}?scoringPeriodId={week}&view={view} - Pick'em Challenge Scoring. Path Params: {challenge_name}. Query Params: scoringPeriodId={week}, view
[ ] /apis/v1/challenges/{challenge_name}/groups/{group_id}?view={view} - Pick'em Challenge Group. Path Params: {challenge_name}, {group_id}. Query Param: view
[ ] /apis/v1/challenges/{challenge_name}/entries/{user_id}?view={view} - Pick'em Challenge User Entry. Path Params: {challenge_name}, {user_id}. Query Param: view
[ ] /apis/v1/challenges/{challenge_name}/leaderboard?view={view} - Pick'em Challenge Leaderboard. Path Param: {challenge_name}. Query Param: view
[ ] /apis/v1/propositions?challengeId={challenge_id}&view={view} - Pick'em Propositions. Query Params: challengeId={challenge_id}, view
XIV. Stats Endpoints (Play-by-Play)
site.api.espn.com
[ ] /apis/v3/stats/football/nfl/playbyplay/{event_id} - NFL Play-by-Play. Path Param: {event_id} (Path structure based on initial checklist, param assumed)
[ ] /apis/v3/stats/basketball/nba/playbyplay/{event_id} - NBA Play-by-Play. Path Param: {event_id}
[ ] /apis/v3/stats/baseball/mlb/playbyplay/{event_id} - MLB Play-by-Play. Path Param: {event_id}
[ ] /apis/v3/stats/hockey/nhl/playbyplay/{event_id} - NHL Play-by-Play. Path Param: {event_id}
XV. Betting & Odds Endpoints (NFL Example, pattern for other sports)
sports.core.api.espn.com
[ ] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{event_id}/probabilities - Game Win Probabilities. Path Params: {sport}, {league}, {event_id}. Query Param: limit
[ ] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{event_id}/odds - List Odds Providers for Game. Path Params: {sport}, {league}, {event_id}
[ ] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{event_id}/odds/{provider_id} - Odds from Specific Provider. Path Params: {sport}, {league}, {event_id}, {provider_id}
[ ] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{event_id}/odds/{provider_id}/history/0/movement - Odds History/Movement. Path Params & Query: As above, limit
[ ] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{event_id}/odds/{provider_id}/head-to-heads - Head-to-Head Odds. Path Params: As above.
[ ] /v2/sports/{sport}/leagues/{league}/seasons/{year}/futures - Futures Bets. Path Params: {sport}, {league}, {year}
[ ] /v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{seasontype}/teams/{team_id}/ats - Team ATS Records. Path Params: {sport}, {league}, {year}, {seasontype}, {team_id}
[ ] /v2/sports/{sport}/leagues/{league}/seasons/{year}/types/0/teams/{team_id}/odds-records - Team Odds Records. Path Params: As above (type often 0)
[ ] /v2/sports/{sport}/leagues/{league}/teams/{team_id}/odds/{provider_id}/past-performances - Team Past Performance vs Odds. Path Params & Query: As above, limit
[ ] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{event_id}/predictor - ESPN Predictor Metrics. Path Params: As above.
[ ] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{event_id}/powerindex/{team_id} - ESPN Power Index for Game. Path Params: As above.
XVI. Utility & Miscellaneous Endpoints (NFL Example, pattern for other sports)
sports.core.api.espn.com
[x] /v2/sports/{sport}/leagues/{league}/positions - List Player Positions. Path Params: {sport}, {league}. Query Param: limit
[x] /v2/sports/{sport}/leagues/{league}/transactions - List Transactions. Path Params: {sport}, {league}
[x] /v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{seasontype}/weeks/{week}/talentpicks - Weekly Talent Picks. Path Params & Query: As above, limit
[x] /v2/sports/{sport}/leagues/{league}/athletes/{athlete_id}/statistics - Athlete Statistics. Path Params: {sport}, {league}, {athlete_id}. Query params: limit, seasontype, year, week - Generic endpoint (consolidates NFL, NBA, MLB, NHL)
[x] /v2/sports/{sport}/leagues/{league}/seasons/{year}/draft/athletes/{athlete_id} -  Draft Athlete Details. Path Params: {year}, {athlete_id}
[x] /v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{season_type}/groups
[x] /v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{season_type}/groups/{group_id}
[x] /v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{season_type}/weeks
[x] /v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{season_type}/corrections
[x] /v2/sports/{sport}/leagues/{league}/seasons/{year}/types/{season_type}/groups/{group_id}
[ ] /v2/sports/{sport}/leagues/{league}/seasons/{year}/draft/athletes/{athlete_id}/statisticslog-  Draft Athlete Contracts. Path Params: {year}, {athlete_id}
[x] /v2/sports/{sport}/leagues/{league}/seasons/{year}/coaches -  Coaches. 
[ ] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/odds/{provider_id}
[ ] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/odds/{provider_id}/history/0/movement
[ ] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/odds/{provider_id}/head-to-heads
[ ] /v2/sports/{sport}/leagues/{league}/events/{event_id}/competitions/{competition_id}/odds/{provider_id}/predictors
[ ] /v2/sports/{sport}/leagues/{league}/teams/{team_id}/odds/{provider_id}/past-performances
XVII. Additional Endpoints from ESPN API Documentation
site.api.espn.com
[ ] /apis/site/v3/sports/football/nfl/leaders - NFL Leaders (Site API v3). Query Params: season
site.web.api.espn.com  
[ ] /apis/site/v3/sports/football/nfl/teamleaders - NFL Team Leaders (Site API v3)
[ ] /apis/common/v3/sports/football/nfl/athletes/{athlete_id}/bio - NFL Athlete Bio
[ ] /apis/common/v3/sports/football/nfl/athletes/{athlete_id}/stats - NFL Athlete Stats
sports.core.api.espn.com
[ ] /v2/sports/football/leagues/nfl/athletes/{athlete_id}/statistics/0 - NFL Athlete Statistics (Specific Category)
[ ] /v2/sports/football/leagues/nfl/events/{event_id}/competitions/{event_id}/competitors/{team_id}/linescores - NFL Game Linescores
[ ] /v2/sports/football/leagues/nfl/events/{event_id}/competitions/{event_id}/competitors/{team_id}/records - NFL Team Records for Event
[ ] /v2/sports/football/leagues/nfl/events/{event_id}/competitions/{event_id}/competitors/{team_id}/statistics - NFL Team Statistics for Event
[ ] /v2/sports/football/leagues/nfl/events/{event_id}/competitions/{event_id}/probabilities/{play_id} - NFL Play Probability
[ ] /v2/sports/football/leagues/nfl/seasons/{year}/athletes/{athlete_id}/notes - NFL Athlete Season Notes
[x] /v2/sports/football/leagues/nfl/seasons/{year}/coaches - NFL Coaches List - Covered by generic /v2/sports/{sport}/leagues/{league}/seasons/{year}/coaches
[ ] /v2/sports/football/leagues/nfl/seasons/{year}/draft/status - NFL Draft Status
[ ] /v2/sports/football/leagues/nfl/seasons/{year}/types/{seasontype}/athletes/{athlete_id}/projections - NFL Athlete Projections
[ ] /v2/sports/football/leagues/nfl/seasons/{year}/types/{seasontype}/teams/{team_id}/attendance - NFL Team Attendance
[ ] /v2/sports/football/leagues/nfl/seasons/{year}/types/{seasontype}/teams/{team_id}/leaders - NFL Team Leaders
[ ] /v2/sports/football/leagues/nfl/seasons/{year}/types/{seasontype}/teams/{team_id}/record - NFL Team Record
[ ] /v2/sports/football/leagues/nfl/seasons/{year}/types/{seasontype}/weeks/{week}/qbr/10000 - NFL Weekly QBR
[ ] /v2/sports/football/leagues/nfl/providers - NFL Betting Providers List
[ ] /v2/sports/football/leagues/nfl/providers/{provider_id} - NFL Betting Provider Details
now.core.api.espn.com
[ ] /v1/sports/news - ESPN News API. Query Params: limit, sport
XVIII. Golf Endpoints
site.api.espn.com
[ ] /apis/site/v2/sports/golf/pga/scoreboard - PGA Tournament Scoreboard
site.web.api.espn.com
[ ] /apis/common/v3/sports/golf/athletes/{playerId}/stats - Golf Player Stats. Query Params: season
sports.core.api.espn.com
[ ] /v2/sports/golf/leagues/pga/seasons/{year}/athletes/{playerId}/eventlog - Golf Player Event Log
XIX. Additional Soccer Endpoints
sports.core.api.espn.com
[ ] /v2/sports/soccer/leagues/{league}/seasons/{year}/types/1/standings - Soccer League Standings
[ ] /v2/sports/soccer/leagues/{league}/seasons/{year}/teams/{teamId}/athletes?active=true - Soccer Team Active Players
XX. Other Sports Endpoints
site.web.api.espn.com
[ ] /apis/site/v2/sports/baseball/college-softball/scoreboard - College Softball Scoreboard
sports.core.api.espn.com
[ ] /v2/sports/basketball/leagues/mens-college-basketball/events?dates={startDate}-{endDate} - College Basketball Events by Date Range