#!/usr/bin/env python3
"""
Test ESPN CDN NFL API - Scoreboard and Schedule Endpoints
Requires Python 3.10+
"""

import pprint
from models.cdn_api.espn_cdn_nfl_api_client import Client
from models.cdn_api.espn_cdn_nfl_api_client.api.default import (
    get_core_nfl_scoreboard,
    get_core_nfl_schedule,
    get_core_nfl_standings,
    get_core_nfl_boxscore,
    get_core_nfl_playbyplay,
)
from models.cdn_api.espn_cdn_nfl_api_client.models import (
    NflScoreboardResponse,
    NflScheduleResponse,
    NflStandingsResponse,
    NflBoxscoreResponse,
    NflPlayByPlayResponse,
)
from models.cdn_api.espn_cdn_nfl_api_client.types import UNSET, Unset
import datetime
import textwrap

BASE_URL = "https://cdn.espn.com"


def validate_scoreboard_response(data: NflScoreboardResponse) -> bool:
    if not data.type or not data.content:
        print("Missing required top-level fields: type or content")
        return False
    content = data.content
    if not content or not content.sb_data:
        print("Missing sb_data in content")
        return False
    sb_data = content.sb_data
    if not sb_data or not sb_data.events:
        print("No events found in sb_data")
        return False
    event = sb_data.events[0]
    if not event or not event.competitions:
        print("No competitions found in event")
        return False
    competition = event.competitions[0]
    if not competition or not competition.competitors:
        print("No competitors found in competition")
        return False
    competitor = competition.competitors[0]
    if not competitor or not competitor.team or not competitor.team.display_name:
        print("Missing team or display_name in competitor")
        return False
    return True


def format_scoreboard(data: NflScoreboardResponse) -> str:
    if not data.type or not data.content:
        return "Invalid data format: missing type or content"
    content = data.content
    if not content or not content.sb_data or not content.sb_data.events:
        return "Invalid data format: missing sb_data or events"
    sb_data = content.sb_data
    output = []
    output.append(f"=== CDN NFL Scoreboard ({data.type}) ===")
    for event in sb_data.events or []:
        if not event:
            continue
        output.append(f"\nGame: {getattr(event, 'name', 'Unknown')}")
        if not event.competitions:
            output.append("No competition data available")
            continue
        competition = event.competitions[0]
        if not competition or not competition.competitors:
            continue
        competitors = competition.competitors if competition.competitors else []
        away_team = next(
            (c for c in competitors if c and getattr(c, "home_away", None) == "away"),
            None,
        )
        home_team = next(
            (c for c in competitors if c and getattr(c, "home_away", None) == "home"),
            None,
        )
        if (
            home_team
            and away_team
            and home_team.team
            and away_team.team
            and home_team.team.display_name
            and away_team.team.display_name
        ):
            output.append(
                f"Teams: {away_team.team.display_name} @ {home_team.team.display_name}"
            )
    return "\n".join(output)


def format_schedule(data: NflScheduleResponse) -> str:
    if not data.content or not data.content.calendar:
        return "Invalid data format: missing or empty calendar"
    output = ["=== CDN NFL Schedule ==="]
    for cal in data.content.calendar:
        label = getattr(cal, "label", "Unknown")
        output.append(f"Calendar: {label}")
        entries = getattr(cal, "entries", [])
        for entry in entries:
            entry_label = getattr(entry, "label", "Unknown")
            output.append(f"  Entry: {entry_label}")
    # Print games for each week of the regular season
    output.append("\n=== Regular Season Games by Week ===")
    regular_season = next(
        (
            cal
            for cal in data.content.calendar
            if getattr(cal, "label", "").lower() == "regular season"
        ),
        None,
    )
    if (
        regular_season
        and regular_season.entries is not UNSET
        and isinstance(regular_season.entries, list)
    ):
        schedule = data.content.schedule
        for week_entry in regular_season.entries:
            week_label = getattr(week_entry, "label", "Unknown")
            week_start = getattr(week_entry, "start_date", None)
            week_end = getattr(week_entry, "end_date", None)
            output.append(f"Week: {week_label}")
            if schedule and week_start and week_end:
                # Convert to datetime for comparison
                try:
                    week_start_dt = (
                        week_start
                        if isinstance(week_start, datetime.datetime)
                        else datetime.datetime.fromisoformat(
                            str(week_start).replace("Z", "+00:00")
                        )
                    )
                    week_end_dt = (
                        week_end
                        if isinstance(week_end, datetime.datetime)
                        else datetime.datetime.fromisoformat(
                            str(week_end).replace("Z", "+00:00")
                        )
                    )
                except Exception:
                    output.append("  Invalid week date format.")
                    continue
                found_game = False
                for date_key in sorted(schedule.additional_keys):
                    try:
                        date_dt = datetime.datetime.strptime(date_key, "%Y%m%d")
                    except Exception:
                        continue
                    if week_start_dt.date() <= date_dt.date() <= week_end_dt.date():
                        games_obj = schedule[date_key]
                        games = getattr(games_obj, "games", [])
                        for game in games:
                            name = getattr(game, "name", None) or getattr(
                                game, "short_name", "Unknown"
                            )
                            game_date = getattr(game, "date", "Unknown")
                            output.append(f"  Game: {name} at {game_date}")
                            found_game = True
                if not found_game:
                    output.append("  No games found for this week.")
            else:
                output.append("  No games found for this week.")
    else:
        output.append("No regular season weeks found in calendar.")
    return "\n".join(output)


def format_standings_table(data: NflStandingsResponse) -> str:
    if (
        not data.content
        or not data.content.standings
        or not data.content.standings.groups
    ):
        return "No standings data available."
    output = []
    # Top-level: conferences
    for conf in data.content.standings.groups:
        conf_name = getattr(conf, "name", "Unknown Conference")
        output.append(f"\n=== {conf_name} ===")
        # Next level: divisions
        divisions = getattr(conf, "groups", [])
        if not divisions:
            output.append("No divisions in this conference.")
            continue
        for div in divisions:
            div_name = getattr(div, "name", "Unknown Division")
            output.append(f"\n{div_name}")
            standings = getattr(div, "standings", None)
            entries = (
                getattr(standings, "entries", None)
                if standings not in (UNSET, None)
                else None
            )
            if entries in (UNSET, None) or not isinstance(entries, list):
                output.append("No teams in this division.")
                continue
            # Table header
            header = f"{'Team':<25} {'W':>2} {'L':>2} {'T':>2} {'PCT':>5} {'PF':>4} {'PA':>4} {'DIFF':>5} {'STRK':>5}"
            output.append(header)
            output.append("-" * len(header))
            for entry in entries:
                team = (
                    entry.team.display_name
                    if entry.team and entry.team.display_name
                    else "?"
                )
                # Extract stats by name
                stats = {
                    s.name: s.display_value
                    for s in entry.stats
                    if s.name and s.display_value
                }
                w = stats.get("wins", "-")
                l = stats.get("losses", "-")
                t = stats.get("ties", "-")
                pct = stats.get("winPercent", "-")
                pf = stats.get("pointsFor", "-")
                pa = stats.get("pointsAgainst", "-")
                diff = stats.get("differential", "-")
                strk = stats.get("streak", "-")
                output.append(
                    f"{team:<25} {w:>2} {l:>2} {t:>2} {pct:>5} {pf:>4} {pa:>4} {diff:>5} {strk:>5}"
                )
    return "\n".join(output)


def test_get_core_nfl_scoreboard():
    client = Client(base_url=BASE_URL)
    response = get_core_nfl_scoreboard.sync(client=client, xhr=1, limit=1)
    assert isinstance(response, NflScoreboardResponse)
    assert validate_scoreboard_response(response)
    print(format_scoreboard(response))


def test_get_core_nfl_schedule():
    client = Client(base_url=BASE_URL)
    response = get_core_nfl_schedule.sync(
        client=client, xhr=1, limit=1, year=2024, week=1
    )
    assert isinstance(response, NflScheduleResponse)
    assert response.content is not None
    print(format_schedule(response))


def test_get_core_nfl_schedule_by_week():
    client = Client(base_url=BASE_URL)
    # Fetch the calendar to get the list of regular season weeks and the year
    initial_response = get_core_nfl_schedule.sync(
        client=client, xhr=1, limit=1, year=2025
    )
    assert isinstance(initial_response, NflScheduleResponse)
    assert initial_response.content is not None
    content = initial_response.content
    year = 2025
    defaults = getattr(content, "defaults", UNSET)
    if isinstance(defaults, dict) and "year" in defaults:
        year = defaults["year"]
    calendar = getattr(content, "calendar", UNSET)
    calendar = calendar if isinstance(calendar, list) else []
    regular_season = next(
        (
            cal
            for cal in calendar
            if getattr(cal, "label", "").lower() == "regular season"
        ),
        None,
    )
    entries = getattr(regular_season, "entries", UNSET) if regular_season else UNSET
    if not regular_season or entries is UNSET or not isinstance(entries, list):
        print("No regular season weeks found in calendar.")
        return
    print("\n=== Regular Season Games by Week (fetched individually) ===")
    for week_entry in entries:
        week_label = getattr(week_entry, "label", "Unknown")
        week_value = getattr(week_entry, "value", None)
        if not week_value:
            continue
        response = get_core_nfl_schedule.sync(
            client=client, xhr=1, year=year, week=int(week_value)
        )
        assert isinstance(response, NflScheduleResponse)
        if not response.content or not response.content.schedule:
            print(f"Week: {week_label}\n  No games found for this week.")
            continue
        found_game = False
        for date_key in sorted(response.content.schedule.additional_keys):
            games_obj = response.content.schedule[date_key]
            games = getattr(games_obj, "games", [])
            for game in games:
                name = getattr(game, "name", None) or getattr(
                    game, "short_name", "Unknown"
                )
                game_date = getattr(game, "date", "Unknown")
                if not found_game:
                    print(f"Week: {week_label}")
                    found_game = True
                print(f"  Game: {name} at {game_date}")
        if not found_game:
            print(f"Week: {week_label}\n  No games found for this week.")


def test_get_core_nfl_standings():
    client = Client(base_url=BASE_URL)
    response = get_core_nfl_standings.sync(client=client, season=2023, xhr=1)
    assert isinstance(response, NflStandingsResponse)
    print("\n=== CDN NFL Standings ===")
    print(format_standings_table(response))


def test_get_core_nfl_boxscore():
    client = Client(base_url=BASE_URL)
    response = get_core_nfl_boxscore.sync(client=client, xhr=1, gameid="401547602")
    assert isinstance(response, NflBoxscoreResponse)
    print("\n=== CDN NFL Boxscore ===")
    d = response.to_dict()
    print(sorted(d.keys()))


def test_get_core_nfl_playbyplay():
    client = Client(base_url=BASE_URL)
    response = get_core_nfl_playbyplay.sync(client=client, xhr=1, gameid="401547602")
    assert isinstance(response, NflPlayByPlayResponse)
    print("\n=== CDN NFL PlayByPlay ===")
    d = response.to_dict()
    print(sorted(d.keys()))


def main():
    print("\nRunning CDN NFL API tests...")
    test_get_core_nfl_scoreboard()
    test_get_core_nfl_schedule()
    test_get_core_nfl_schedule_by_week()
    test_get_core_nfl_standings()
    test_get_core_nfl_boxscore()
    test_get_core_nfl_playbyplay()
    print("\nAll CDN NFL API tests passed.")


if __name__ == "__main__":
    main()
