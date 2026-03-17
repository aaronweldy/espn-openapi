# ESPN Tournament Challenge API Notes

This repo did not previously map Tournament Challenge explicitly. The live API is part of the existing ESPN Gambit surface at `https://gambit-api.fantasy.espn.com`, but the Tournament Challenge aliases, season keys, and `/apis/v1/propositions` response shape were not documented here.

## Verified challenge keys

These values were verified against the live site and Gambit API on 2026-03-17.

| Product | Fantasy page alias | Gambit alias | Canonical challenge key | Challenge ID | Game ID | League mapping |
| --- | --- | --- | --- | --- | --- | --- |
| Men's Tournament Challenge | `https://fantasy.espn.com/games/tcmen` | `tcmen` | `tournament-challenge-bracket-2026` | `277` | `72` | `mens-college-basketball` |
| Women's Tournament Challenge | `https://fantasy.espn.com/games/tcwomen` | `tcwomen` | `tournament-challenge-bracket-women-2026` | `278` | `73` | `womens-college-basketball` |

The short aliases and the season-specific keys both work on the Gambit endpoints. The response `key` normalizes to the season-specific canonical key.

## Working endpoints

### Challenge details

Use the alias or canonical key:

- `GET https://gambit-api.fantasy.espn.com/apis/v1/challenges/tcmen?view=details`
- `GET https://gambit-api.fantasy.espn.com/apis/v1/challenges/tcwomen?view=details`
- `GET https://gambit-api.fantasy.espn.com/apis/v1/challenges/tournament-challenge-bracket-2026?view=details`
- `GET https://gambit-api.fantasy.espn.com/apis/v1/challenges/tournament-challenge-bracket-women-2026?view=details`

This response contains the canonical `key`, numeric `id`, `gameType`, `mappings`, `featuredGroupIds`, scoring periods, and an embedded `propositions` list.

## Leaderboard

- `GET https://gambit-api.fantasy.espn.com/apis/v1/challenges/tcmen/leaderboard?view=ranks&limit=10`
- `GET https://gambit-api.fantasy.espn.com/apis/v1/challenges/tcwomen/leaderboard?view=ranks&limit=10`

The leaderboard response uses the numeric `challengeId` and returns `entries` objects with nested `member`, `name`, `score`, and `picks` data.

## Group lookup

Use a `groupId` from `featuredGroupIds` in the challenge details response or from a group URL on the fantasy site:

- `GET https://gambit-api.fantasy.espn.com/apis/v1/challenges/tcmen/groups/{groupId}`

Example verified group:

- `GET https://gambit-api.fantasy.espn.com/apis/v1/challenges/tcmen/groups/6e682872-7e5f-3aa2-84bf-003cb6a630ae`

## Propositions

Use the numeric `challengeId` from challenge details:

- `GET https://gambit-api.fantasy.espn.com/apis/v1/propositions?challengeId=277`
- `GET https://gambit-api.fantasy.espn.com/apis/v1/propositions?challengeId=278`

Important: this endpoint returns a top-level JSON array, not an object wrapper.

For Tournament Challenge, each proposition maps back to ESPN basketball data through `mappings` such as:

- `LEAGUE`
- `COMPETITION_ID`
- `EVENT_ID`
- `COMPETITOR_ID`
- `URL_DESKTOP`

The live propositions also include `possibleOutcomes`, which is the bracket-team choice set for each matchup.

## Discovery workflow

If the season-specific keys change in a future year, the fastest way to rediscover them is:

1. Load the fantasy pages for `tcmen` or `tcwomen`.
2. Inspect the server-rendered HTML for `challengeKey`, `challengeId`, and `gameId`.
3. Call `GET /apis/v1/challenges/{challengeName}?view=details`.
4. Use the returned numeric `id` with `GET /apis/v1/propositions?challengeId=...`.

The page HTML currently embeds all three values, so the browser page is enough to recover the Gambit mapping without reverse-engineering the JS bundles.
