import pytest
import logging
from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_draft_athlete,
)
from models.sports_core_api.espn_sports_core_api_client.models import (
    DraftAthleteResponse,
    ErrorResponse,
    SportEnum,
    LeagueEnum,
)
import json

logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league,year,athlete_id,expected_name",
    [
        (SportEnum.FOOTBALL, LeagueEnum.NFL, 2023, "106308", "Bryce Young"),  # NFL QB
        (
            SportEnum.BASKETBALL,
            LeagueEnum.NBA,
            2023,
            "106535",
            "Victor Wembanyama",
        ),  # NBA Center
    ],
)
def test_get_draft_athlete(
    sports_core_api_client,
    ensure_json_output_dir,
    sport,
    league,
    year,
    athlete_id,
    expected_name,
):
    """Tests the get_draft_athlete endpoint for multiple sports."""
    logger.info(f"Testing Draft Athlete Details endpoint for {sport}/{league}...")

    logger.info(
        f"Fetching draft athlete details for ID {athlete_id} from {sport}/{league} {year}"
    )
    response = get_draft_athlete.sync(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=year,
        athlete_id=athlete_id,
    )

    assert not isinstance(response, ErrorResponse), (
        f"API returned an error response: {response.error.message if response.error else response}"
    )
    assert response is not None, "API returned no response."
    assert isinstance(response, DraftAthleteResponse), (
        "Response should be of type DraftAthleteResponse"
    )

    assert response.full_name, "Full name should not be empty"
    assert response.id == athlete_id, "Returned athlete ID should match requested ID"
    assert expected_name in response.full_name, (
        f"Expected name '{expected_name}' not found in '{response.full_name}'"
    )

    # Save response to JSON file
    output_path = f"{ensure_json_output_dir}/draft_athlete_{sport}_{league}_{year}_{athlete_id}_response.json"
    with open(output_path, "w") as f:
        json.dump(response.to_dict(), f, indent=2)
    logger.info(f"Saved response to {output_path}")

    # Log information about the response
    logger.info(
        f"Successfully fetched draft athlete details for {response.full_name} (ID: {response.id}) from {sport}/{league}"
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

    # Verify sport-specific fields
    if sport == SportEnum.FOOTBALL:
        # NFL-specific checks
        assert response.position, "NFL athlete should have a position"
        assert response.position.abbreviation in [
            "QB",
            "RB",
            "WR",
            "TE",
            "OL",
            "DL",
            "LB",
            "DB",
            "K",
            "P",
        ], f"Unexpected NFL position: {response.position.abbreviation}"
    elif sport == SportEnum.BASKETBALL:
        # NBA-specific checks
        assert response.position, "NBA athlete should have a position"
        assert response.position.abbreviation in [
            "PG",
            "SG",
            "SF",
            "PF",
            "C",
            "G",
            "F",
        ], f"Unexpected NBA position: {response.position.abbreviation}"

    # Common checks for all sports
    assert response.attributes, "Athlete should have attributes"
    assert response.analysis, "Athlete should have analysis"
    assert response.pick, "Athlete should have pick information"
    assert response.athlete, "Athlete should have athlete reference"


@pytest.mark.api
def test_get_draft_athlete_invalid_sport(sports_core_api_client):
    """Tests the get_draft_athlete endpoint with an unsupported sport."""
    logger.info("Testing Draft Athlete Details endpoint with unsupported sport...")

    response = get_draft_athlete.sync(
        client=sports_core_api_client,
        sport=SportEnum.BASEBALL,  # MLB doesn't have draft athletes in this API
        league=LeagueEnum.MLB,
        year=2023,
        athlete_id="123456",
    )

    # Should return an error for unsupported sport
    assert isinstance(response, ErrorResponse), (
        "Expected ErrorResponse for unsupported sport"
    )
    assert response.error and response.error.code == 404, (
        "Expected 404 error for unsupported sport"
    )


@pytest.mark.api
def test_get_draft_athlete_invalid_id(sports_core_api_client):
    """Tests the get_draft_athlete endpoint with an invalid athlete ID."""
    logger.info("Testing Draft Athlete Details endpoint with invalid athlete ID...")

    response = get_draft_athlete.sync(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2023,
        athlete_id="999999",  # Invalid ID
    )

    # Should return an error for invalid athlete ID
    assert isinstance(response, ErrorResponse), (
        "Expected ErrorResponse for invalid athlete ID"
    )
    assert response.error and response.error.code == 404, (
        "Expected 404 error for invalid athlete ID"
    )
