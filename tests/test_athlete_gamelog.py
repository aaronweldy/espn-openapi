import json
import sys
from typing import cast
from pathlib import Path

import httpx

sys.path.append(str(Path(__file__).parent.parent))

from models.site_web_api.espn_site_web_api_client.api.default.get_nfl_athlete_game_log import (
    sync_detailed,
)
from models.site_web_api.espn_site_web_api_client.client import Client
from models.site_web_api.espn_site_web_api_client.models.athlete_game_log_response import (
    AthleteGameLogResponse,
)

# Mahomes ID: 3139477
ATHLETE_ID = "3139477"


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
            print("\nAvailable season types:")
            if game_log.season.types:
                for season_type in game_log.season.types:
                    start_date = (
                        season_type.start_date if season_type.start_date else "N/A"
                    )
                    end_date = season_type.end_date if season_type.end_date else "N/A"
                    print(
                        f"  - {season_type.name} ({season_type.type}): {start_date} to {end_date}"
                    )

        # Print events (games)
        if game_log.events:
            events_count = len(game_log.events.additional_properties)
            print(f"\nTotal games: {events_count}")

            # Get list of games
            games = list(game_log.events.additional_properties.values())

            # Print a few games as example
            print("\nRecent games:")
            for i, game in enumerate(games[:5]):
                result = game.game_result.value if game.game_result else "N/A"
                score = game.score if game.score else "N/A"
                date = game.game_date.strftime("%Y-%m-%d") if game.game_date else "N/A"
                opponent = (
                    game.opponent.display_name
                    if game.opponent and game.opponent.display_name
                    else "Unknown"
                )

                print(f"  {i + 1}. {date} - {opponent}: {result} {score}")

        # Print requested season info
        if game_log.requested_season:
            season = game_log.requested_season
            print(f"\nRequested season: {season.display_name}")

        print("\nTest successful!")
        return True
    else:
        print(f"Error fetching data: {response.status_code}")
        print(response.content)
        return False


if __name__ == "__main__":
    test_athlete_gamelog()
