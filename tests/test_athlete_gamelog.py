import json
import sys
from typing import cast, Dict, Any, List, Optional
from pathlib import Path
from datetime import datetime

import httpx

sys.path.append(str(Path(__file__).parent.parent))

from models.site_web_api.espn_site_web_api_client.api.default.get_nfl_athlete_game_log import (
    sync_detailed,
)
from models.site_web_api.espn_site_web_api_client.client import Client
from models.site_web_api.espn_site_web_api_client.models.athlete_game_log_response import (
    AthleteGameLogResponse,
)
from models.site_web_api.espn_site_web_api_client.models.game_event import GameEvent

# Patrick Mahomes ID: 3139477
ATHLETE_ID = "3139477"


def format_gamelog(games: dict[str, GameEvent], season_stats=None):
    """Format game log into a nice table-like display using real stats."""
    if not games:
        return "No games available"

    # Count wins and losses
    wins = sum(
        1 for game in games.values() if game.game_result and game.game_result == "W"
    )
    losses = sum(
        1 for game in games.values() if game.game_result and game.game_result == "L"
    )

    # Format header
    header = (
        f"\n{'DATE':^12} {'OPPONENT':^18} {'RESULT':^8} {'SCORE':^10} "
        f"{'CMP/ATT':^10} {'YARDS':^7} {'TD':^4} {'INT':^4} {'RATING':^8}\n"
        f"{'-' * 85}\n"
    )

    # Format rows for each game
    rows = []

    # Default empty event stats dictionary
    event_stats = {}

    # If we have the raw JSON response with stats included
    if season_stats:
        # Map event IDs to their corresponding stats from the seasonTypes data
        for season_type in season_stats.get("seasonTypes", []):
            for category in season_type.get("categories", []):
                if category.get("type") == "event":
                    for event in category.get("events", []):
                        event_id = event.get("eventId")
                        stats = event.get("stats", [])
                        if event_id and stats:
                            event_stats[event_id] = stats

    # Get labels/positions of stats in the array
    stat_positions = None
    if season_stats:
        # Get positions of stats we care about
        labels = season_stats.get("labels", [])
        if labels:
            stat_positions = {
                "CMP": labels.index("CMP") if "CMP" in labels else None,
                "ATT": labels.index("ATT") if "ATT" in labels else None,
                "YDS": labels.index("YDS") if "YDS" in labels else None,
                "TD": labels.index("TD") if "TD" in labels else None,
                "INT": labels.index("INT") if "INT" in labels else None,
                "RTG": labels.index("RTG") if "RTG" in labels else None,
            }

    for game in sorted(
        games.values(), key=lambda g: g.game_date if g.game_date else "", reverse=True
    ):
        if not game.game_date:
            continue

        # Parse date safely
        date = game.game_date.strftime("%Y-%m-%d")
        opponent = ""
        if game.opponent and game.opponent.abbreviation:
            opponent = game.opponent.abbreviation
            if game.at_vs:
                if game.at_vs == "@":
                    opponent = f"@ {opponent}"
                else:
                    opponent = f"vs {opponent}"

        result = game.game_result or ""

        score = ""
        if game.away_team_score and game.home_team_score:
            if game.at_vs == "@":  # Away game
                score = f"{game.away_team_score}-{game.home_team_score}"
            else:  # Home game
                score = f"{game.home_team_score}-{game.away_team_score}"

        # Use real stats from the API response if available
        cmp = "-"
        att = "-"
        yards = "-"
        td = "-"
        ints = "-"
        rating = "-"

        if season_stats and stat_positions and game.id in event_stats:
            stats = event_stats[game.id]
            if stat_positions["CMP"] is not None and stat_positions["CMP"] < len(stats):
                cmp = stats[stat_positions["CMP"]]
            if stat_positions["ATT"] is not None and stat_positions["ATT"] < len(stats):
                att = stats[stat_positions["ATT"]]
            if stat_positions["YDS"] is not None and stat_positions["YDS"] < len(stats):
                yards = stats[stat_positions["YDS"]]
            if stat_positions["TD"] is not None and stat_positions["TD"] < len(stats):
                td = stats[stat_positions["TD"]]
            if stat_positions["INT"] is not None and stat_positions["INT"] < len(stats):
                ints = stats[stat_positions["INT"]]
            if stat_positions["RTG"] is not None and stat_positions["RTG"] < len(stats):
                rating = stats[stat_positions["RTG"]]

        rows.append(
            f"{date:12} {opponent:18} {result:^8} {score:^10} "
            f"{cmp}/{att:^10} {yards:^7} "
            f"{td:^4} {ints:^4} {rating:^8}"
        )

    return (
        f"Game Log for Athlete ID: {ATHLETE_ID}\n"
        f"Record: {wins}-{losses}\n\n"
        f"{header}{''.join(rows)}"
    )


def display_game_stats(game_id: str, raw_stats=None):
    """Display detailed statistics for a specific game using real data."""
    if not raw_stats:
        print(f"\nNo detailed statistics available for Game ID: {game_id}")
        return

    # Find stats for this specific game
    game_stats = {}
    labels = raw_stats.get("labels", [])
    display_names = raw_stats.get("displayNames", [])

    # Map of stat labels to their display names
    stat_map = {
        labels[i]: display_names[i]
        for i in range(len(labels))
        if i < len(display_names)
    }

    # Find this game in the events
    for season_type in raw_stats.get("seasonTypes", []):
        for category in season_type.get("categories", []):
            if category.get("type") == "event":
                for event in category.get("events", []):
                    if event.get("eventId") == game_id:
                        stats = event.get("stats", [])
                        if stats:
                            # Create a map of stat display names to values
                            for i, label in enumerate(labels):
                                if i < len(stats):
                                    display_name = stat_map.get(label, label)
                                    game_stats[display_name] = stats[i]

    if not game_stats:
        print(f"\nNo detailed statistics available for Game ID: {game_id}")
        return

    print(f"\nDetailed Statistics for Game ID: {game_id}")
    for name, value in game_stats.items():
        print(f"{name}: {value}")


def test_athlete_gamelog():
    """Test fetching an NFL athlete's game log data."""
    client = Client(
        base_url="https://site.web.api.espn.com", timeout=httpx.Timeout(30.0)
    )

    print(f"Fetching gamelog for athlete ID: {ATHLETE_ID}")

    # Fetch data
    response = sync_detailed(
        athlete_id=ATHLETE_ID,
        client=client,
    )

    # Check if request was successful
    if response.status_code == 200 and isinstance(
        response.parsed, AthleteGameLogResponse
    ):
        game_log = response.parsed

        # Get all events/games
        events: dict[str, GameEvent] = {}
        if game_log.events:
            for game_id, game in game_log.events.additional_properties.items():
                events[game_id] = game

        # Also load raw JSON for detailed stats
        raw_response = json.loads(response.content)

        # Print formatted game log
        formatted_log = format_gamelog(events, raw_response)
        print(formatted_log)

        # If there are games, display detailed stats for the first one
        if events:
            # Get the first game ID
            first_game_id = next(iter(events.keys()))
            display_game_stats(first_game_id, raw_response)

        # Get season information
        if game_log.requested_season:
            season = game_log.requested_season
            season_type_name = ""
            if season.type:
                # Convert to string representation
                season_type_name = str(season.type)
            print(f"\nRequested Season: {season.year} {season_type_name}")

        # Additional information about the data
        print(f"\nTotal Games Found: {len(events)}")
        return True
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        if response.content:
            print(response.content)
        return False


if __name__ == "__main__":
    test_athlete_gamelog()

    # Uncomment to test with the Peyton Manning example
    # test_manning_gamelog()
