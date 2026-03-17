# ESPN Tournament Challenge vs APIs in this repo

**Tournament Challenge** is ESPN’s March Madness bracket game (men’s and women’s) on fantasy.espn.com. It is **not** the same as the **Gambit** “challenges” API in this repo (`spec-gambit.yaml`), which powers Pick’em-style games (e.g. NFL Pigskin Pick’em) on `gambit-api.fantasy.espn.com`.

There is **no OpenAPI spec in this repo** for Tournament Challenge–specific resources (your bracket, group standings, pick locks, etc.). Those flows are driven by authenticated fantasy experiences; public read endpoints for the classic `apis/v3/games/{gameCode}/seasons/...` pattern were not found for Tournament Challenge game codes (e.g. `tournament-challenge-bracket-2026` returns not found on `lm-api-reads.fantasy.espn.com`).

## Public data you can use for NCAA tournament context

The same games that appear in Tournament Challenge brackets are available from the **site scoreboard** as normal college basketball events.

| Goal | How |
|------|-----|
| NCAA tournament (or postseason) games | `GET /apis/site/v2/sports/basketball/mens-college-basketball/scoreboard?seasontype=3&dates=YYYYMMDD` (optionally a range `YYYYMMDD-YYYYMMDD`) |
| Women’s tournament | Same path with `womens-college-basketball` |
| Single game detail | Existing site / sports-core event and summary endpoints used elsewhere in this repo |

Example (historical first-round day):

```http
GET https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard?seasontype=3&dates=20250321
```

Use `YYYYMMDD` per day; some `YYYYMMDD-YYYYMMDD` ranges return 404 for this league. `seasontype=3` is postseason; without `dates`, behavior depends on the calendar (off-season may return few or no games).

## Tests

`tests/test_tournament_challenge_public_data.py` exercises the men’s postseason scoreboard for a fixed March window so CI can validate that tournament-game data remains reachable.
