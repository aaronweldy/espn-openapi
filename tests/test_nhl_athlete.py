import pytest
import json
from models.sports_core_api.espn_sports_core_api_client.api.default import get_athlete_details, get_athlete_statistics
from models.sports_core_api.espn_sports_core_api_client.models.athlete_details_response import AthleteDetailsResponse
from models.sports_core_api.espn_sports_core_api_client.models.athlete_statistics_response import AthleteStatisticsResponse
from models.sports_core_api.espn_sports_core_api_client.models.sport_enum import SportEnum
from models.sports_core_api.espn_sports_core_api_client.models.league_enum import LeagueEnum


@pytest.mark.api
def test_get_nhl_athlete_details(sports_core_api_client, ensure_json_output_dir):
    """Test getting NHL athlete details."""
    athlete_id = "3024816"  # Austin Czarnik
    
    response = get_athlete_details.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.HOCKEY,
        league=LeagueEnum.NHL,
        athlete_id=athlete_id
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, AthleteDetailsResponse), "Response should parse to AthleteDetailsResponse"
    
    # Basic assertions
    assert result.id == athlete_id
    assert result.type == "hockey"
    assert result.display_name
    assert result.full_name
    
    # NHL-specific fields might be in additional_properties
    raw_json = response.content.decode('utf-8')
    data = json.loads(raw_json)
    
    # Check for NHL-specific fields in raw response
    assert "hand" in data or "shoots" in data or "catches" in data, "Should have NHL-specific hand/shoots/catches field"
    
    # Save the response
    with open(f"{ensure_json_output_dir}/nhl_athlete_{athlete_id}_core.json", "w") as f:
        json.dump(data, f, indent=2)


@pytest.mark.api
def test_get_nhl_athlete_statistics(sports_core_api_client, ensure_json_output_dir):
    """Test getting NHL athlete statistics."""
    athlete_id = "3024816"  # Austin Czarnik
    
    response = get_athlete_statistics.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.HOCKEY,
        league=LeagueEnum.NHL,
        athlete_id=athlete_id
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, AthleteStatisticsResponse), "Response should parse to AthleteStatisticsResponse"
    
    # Save the response
    raw_json = response.content.decode('utf-8')
    data = json.loads(raw_json)
    with open(f"{ensure_json_output_dir}/nhl_athlete_{athlete_id}_statistics.json", "w") as f:
        json.dump(data, f, indent=2)