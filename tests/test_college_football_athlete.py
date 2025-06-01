"""Test college football athlete endpoints."""
import pytest
import json
from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_athlete_details
)


@pytest.mark.api
def test_get_college_football_athlete_details(sports_core_api_client, ensure_json_output_dir):
    """Test getting college football athlete details using generic endpoint."""
    # Using a known college football athlete ID
    athlete_id = "4426414"  # Example athlete ID
    
    response = get_athlete_details.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="college-football", 
        athlete_id=athlete_id
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Parse and validate response
    result = response.parsed
    assert result is not None, "Response should be parsed successfully"
    
    # Save response for analysis
    if result:
        with open(f"{ensure_json_output_dir}/college_football_athlete_{athlete_id}.json", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
    
    print(f"Successfully retrieved college football athlete {athlete_id} details")


@pytest.mark.api 
@pytest.mark.parametrize("athlete_id", [
    "4426414",  # Example athlete 1
    "4429013",  # Example athlete 2
])
def test_multiple_college_football_athletes(sports_core_api_client, athlete_id):
    """Test getting details for multiple college football athletes."""
    response = get_athlete_details.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="college-football",
        athlete_id=athlete_id
    )
    
    assert response.status_code == 200, f"Failed to get athlete {athlete_id}: {response.status_code}"
    assert response.parsed is not None, f"Failed to parse response for athlete {athlete_id}"