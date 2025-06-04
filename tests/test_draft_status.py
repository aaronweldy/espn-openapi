import pytest
import json
import logging
from models.sports_core_api.espn_sports_core_api_client.api.default import get_draft_status
from models.sports_core_api.espn_sports_core_api_client.models import (
    DraftStatusResponse,
    SportEnum,
    LeagueEnum
)

logging.basicConfig(level=logging.INFO)


@pytest.mark.api
@pytest.mark.parametrize("sport,league,year", [
    (SportEnum.FOOTBALL, LeagueEnum.NFL, 2024),
    (SportEnum.BASKETBALL, LeagueEnum.NBA, 2024),
    (SportEnum.BASEBALL, LeagueEnum.MLB, 2024),
])
def test_get_draft_status(sports_core_api_client, ensure_json_output_dir, sport, league, year):
    """Test fetching draft status for various sports."""
    
    # Fetch draft status
    response = get_draft_status.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=year
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, DraftStatusResponse), "Response should parse to DraftStatusResponse"
    
    # Validate required fields
    assert result.ref, "Should have a reference URL"
    assert result.round_ is not None, "Should have a round number"
    assert result.type, "Should have a type"
    
    # Validate type object
    assert result.type.id is not None, "Type should have an ID"
    assert result.type.name, "Type should have a name"
    assert result.type.state, "Type should have a state"
    assert result.type.description, "Type should have a description"
    
    logging.info(f"Draft status for {sport.value} {league.value} {year}:")
    logging.info(f"  Round: {result.round_}")
    logging.info(f"  Type: {result.type.name} ({result.type.description})")
    logging.info(f"  State: {result.type.state}")
    
    # Save sample data
    sample_data = {
        "sport": sport.value,
        "league": league.value,
        "year": year,
        "round": result.round_,
        "type": {
            "id": result.type.id,
            "name": result.type.name,
            "state": result.type.state,
            "description": result.type.description
        }
    }
    
    filename = f"draft_status_{sport.value}_{league.value}_{year}.json"
    with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
        json.dump(sample_data, f, indent=2)


@pytest.mark.api
def test_draft_status_not_found(sports_core_api_client):
    """Test handling of draft status for sport that doesn't have drafts."""
    
    # Hockey doesn't typically have ESPN draft coverage
    response = get_draft_status.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.HOCKEY,
        league=LeagueEnum.NHL,
        year=2024
    )
    
    # NHL actually has draft data, so it might return 200
    assert response.status_code in [200, 404], f"Expected status code 200 or 404, got {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        logging.info(f"NHL draft status found: Round {result.round_}, Type: {result.type.name}")


@pytest.mark.api
def test_draft_status_historical(sports_core_api_client, ensure_json_output_dir):
    """Test fetching historical draft status."""
    
    # Test NFL draft from 2023 (should be completed)
    response = get_draft_status.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2023
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, DraftStatusResponse), "Response should parse to DraftStatusResponse"
    
    # 2023 NFL draft should be completed
    assert result.type.name == "COMPLETED", "2023 NFL draft should be completed"
    assert result.type.state == "post", "Completed draft should be in post state"
    
    logging.info(f"2023 NFL Draft Status:")
    logging.info(f"  Round: {result.round_} (total rounds)")
    logging.info(f"  Status: {result.type.description}")