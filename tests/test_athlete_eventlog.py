from models.sports_core_api.espn_sports_core_api_client import Client
from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_nfl_athlete_eventlog,
)
from models.sports_core_api.espn_sports_core_api_client.models import (
    NflAthleteEventlogResponse,
    ErrorResponse,
)
from typing import Union


def test_get_nfl_athlete_eventlog():
    """Tests the get_nfl_athlete_eventlog endpoint."""
    print("Testing NFL Athlete Event Log endpoint...")
    client = Client(base_url="https://sports.core.api.espn.com")
    year = 2023
    athlete_id = "3139477"  # Example: Patrick Mahomes

    response: Union[NflAthleteEventlogResponse, ErrorResponse, None] = (
        get_nfl_athlete_eventlog.sync(
            client=client,
            year=year,
            athlete_id=athlete_id,
        )
    )

    if isinstance(response, ErrorResponse):
        print(
            f"\u2717 API returned an error response: {response.error.message if response.error else response}"
        )
        return False
    elif response is None:
        print("\u2717 API returned no response.")
        return False
    elif isinstance(response, NflAthleteEventlogResponse):
        print("\u2713 Successfully fetched athlete event log data.")
        assert response.events is not None, "Response events should not be None"
        assert response.teams is not None, "Response teams should not be None"
        print(f"Found {response.events.count} event log entries.")
        print("\u2713 Test passed!")

        print("\n--- Event Log Details ---")
        for item in response.events.items:
            event_ref = (
                item.event.ref if item.event and hasattr(item.event, "ref") else "N/A"
            )
            competition_ref = (
                item.competition.ref
                if item.competition and hasattr(item.competition, "ref")
                else "N/A"
            )
            stats_ref = (
                item.statistics.ref
                if item.statistics and hasattr(item.statistics, "ref")
                else "N/A"
            )
            print(
                f"Event: {event_ref}, Competition: {competition_ref}, Stats: {stats_ref}, TeamId: {item.team_id}, Played: {item.played}"
            )
        return True
    else:
        print(f"\u2717 Unexpected response type: {type(response)}")
        return False


def main():
    """Runs the NFL Athlete Event Log test."""
    print("===== ESPN Sports Core API - NFL Athlete Event Log Test Script =====")
    test_get_nfl_athlete_eventlog()
    print("===== Test Script Finished =====")


if __name__ == "__main__":
    main()
