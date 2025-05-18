import pytest
import logging
from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_nfl_draft_athlete,
)
from models.sports_core_api.espn_sports_core_api_client.models import (
    NflDraftAthleteResponse,
    ErrorResponse,
)
import json

logger = logging.getLogger(__name__)


@pytest.mark.api
def test_get_nfl_draft_athlete(sports_core_api_client, ensure_json_output_dir):
    """Tests the get_nfl_draft_athlete endpoint."""
    logger.info("Testing NFL Draft Athlete Details endpoint...")
    year = 2023
    athlete_id = "106308"  # Example: Bryce Young

    logger.info(f"Fetching draft athlete details for ID {athlete_id} from year {year}")
    response = get_nfl_draft_athlete.sync(
        client=sports_core_api_client,
        year=year,
        athlete_id=athlete_id,
    )

    assert not isinstance(response, ErrorResponse), (
        f"API returned an error response: {response.error.message if response.error else response}"
    )
    assert response is not None, "API returned no response."
    assert isinstance(response, NflDraftAthleteResponse), (
        "Response should be of type NflDraftAthleteResponse"
    )

    assert response.full_name, "Full name should not be empty"
    assert response.id == athlete_id, "Returned athlete ID should match requested ID"

    # Save response to JSON file
    output_path = f"{ensure_json_output_dir}/nfl_draft_athlete_response.json"
    with open(output_path, "w") as f:
        json.dump(response.to_dict(), f, indent=2)
    logger.info(f"Saved response to {output_path}")

    # Log information about the response
    logger.info(
        f"Successfully fetched draft athlete details for {response.full_name} (ID: {response.id})"
    )
    logger.debug(f"First Name: {response.first_name}")
    logger.debug(f"Last Name: {response.last_name}")
    logger.debug(f"Display Name: {response.display_name}")
    logger.debug(f"Height: {response.height}, Weight: {response.weight}")
    logger.debug(f"Links: {len(response.links)} found")
    logger.debug(f"Positions: {len(response.positions)} found")
    logger.debug(f"Attributes: {len(response.attributes)} found")
    logger.debug(f"Analysis: {len(response.analysis)} found")
    logger.debug(f"Logo: {response.logo.href if response.logo else 'None'}")
