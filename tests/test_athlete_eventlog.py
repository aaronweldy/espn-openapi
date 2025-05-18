import pytest
import json
import logging
from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_nfl_athlete_eventlog,
)
from models.sports_core_api.espn_sports_core_api_client.models import (
    NflAthleteEventlogResponse,
    ErrorResponse,
)


@pytest.mark.api
def test_get_nfl_athlete_eventlog(sports_core_api_client, ensure_json_output_dir):
    """Tests the get_nfl_athlete_eventlog endpoint."""
    logging.info("Testing NFL Athlete Event Log endpoint...")
    year = 2023
    athlete_id = "3139477"  # Example: Patrick Mahomes

    response = get_nfl_athlete_eventlog.sync(
        client=sports_core_api_client,
        year=year,
        athlete_id=athlete_id,
    )

    # Check response type and content
    assert not isinstance(response, ErrorResponse), (
        f"API returned an error response: {response.error.message if response.error else response}"
    )
    assert response is not None, "API returned no response"
    assert isinstance(response, NflAthleteEventlogResponse), (
        f"Unexpected response type: {type(response)}"
    )

    # Validate response data
    assert response.events is not None, "Response events should not be None"
    assert response.teams is not None, "Response teams should not be None"

    # Log event details
    logging.info("--- Event Log Details ---")
    event_details = []
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
        event_details.append({
            "event": event_ref,
            "competition": competition_ref,
            "stats": stats_ref,
            "team_id": item.team_id,
            "played": item.played,
        })

        logging.info(
            f"Event: {event_ref}, Competition: {competition_ref}, Stats: {stats_ref}, TeamId: {item.team_id}, Played: {item.played}"
        )

    # Save response for analysis
    with open(
        f"{ensure_json_output_dir}/nfl_athlete_eventlog_{athlete_id}_{year}.json", "w"
    ) as f:
        json.dump(response.to_dict(), f, indent=2)

    logging.info("Successfully fetched athlete event log data.")
    logging.info(f"Found {response.events.count} event log entries.")
