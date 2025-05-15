import json
import sys
from typing import cast
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

# Mahomes ID: 3139477
ATHLETE_ID = "3139477"


def format_gamelog(games):
    """Format game log into a nice table-like display."""
    if not games:
        return "No games available"

    # Count wins and losses
    wins = sum(
        1 for game in games if game.game_result and game.game_result.value == "W"
    )
    losses = sum(
        1 for game in games if game.game_result and game.game_result.value == "L"
    )
    ties = sum(
        1 for game in games if game.game_result and game.game_result.value == "T"
    )

    # Sort games by date (most recent first)
    sorted_games = sorted(games, key=lambda x: x.game_date, reverse=True)

    # Build header
    header = f"{'DATE':<12} {'OPPONENT':<25} {'RESULT':<8} {'SCORE':<10} {'HOME/AWAY':<10} {'WEEK':<6}"
    divider = "-" * 75

    # Build rows
    rows = []
    for game in sorted_games:
        date = game.game_date.strftime("%Y-%m-%d") if game.game_date else "N/A"
        opponent = (
            game.opponent.display_name
            if game.opponent and game.opponent.display_name
            else "Unknown"
        )
        result = game.game_result.value if game.game_result else "N/A"
        score = game.score if game.score else "N/A"
        home_away = "Home" if game.at_vs and game.at_vs.value == "vs" else "Away"
        week = f"Week {game.week}" if game.week else "N/A"

        row = f"{date:<12} {opponent:<25} {result:<8} {score:<10} {home_away:<10} {week:<6}"
        rows.append(row)

    # Build season stats
    record = f"Record: {wins}-{losses}" + (f"-{ties}" if ties > 0 else "")

    # Combine all parts
    return "\n".join([
        f"\n{'=' * 75}",
        f"GAME LOG FOR ATHLETE ID: {ATHLETE_ID}",
        f"{record}",
        f"{'=' * 75}",
        header,
        divider,
        "\n".join(rows),
    ])


def test_athlete_gamelog():
    """Test fetching an NFL athlete's game log data."""
    client = Client(
        base_url="https://site.web.api.espn.com", timeout=httpx.Timeout(30.0)
    )

    # Fetch data
    response = sync_detailed(
        athlete_id=ATHLETE_ID,
        client=client,
    )

    # Check if request was successful
    if response.status_code == 200 and isinstance(
        response.parsed, AthleteGameLogResponse
    ):
        print(f"Successfully retrieved game log for athlete ID: {ATHLETE_ID}")

        # Parse response as AthleteGameLogResponse
        game_log = cast(AthleteGameLogResponse, response.parsed)

        # Print available seasons
        if game_log.season:
            print("\nAVAILABLE SEASONS:")
            if game_log.season.types:
                for season_type in game_log.season.types:
                    start_date = (
                        season_type.start_date if season_type.start_date else "N/A"
                    )
                    end_date = season_type.end_date if season_type.end_date else "N/A"
                    print(
                        f"  • {season_type.name} ({season_type.type}): {start_date} to {end_date}"
                    )

        # Print requested season info
        if game_log.requested_season:
            season = game_log.requested_season
            print(f"\nDisplaying games for: {season.display_name}")

        # Format and print games
        if game_log.events and game_log.events.additional_properties:
            games = list(game_log.events.additional_properties.values())
            formatted_gamelog = format_gamelog(games)
            print(formatted_gamelog)

        print("\nTest successful!")
        return True
    else:
        print(f"Error fetching data: {response.status_code}")
        print(response.content)
        return False


if __name__ == "__main__":
    test_athlete_gamelog()
