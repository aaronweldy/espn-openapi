"""Test college athlete statistics endpoints."""
import pytest
import json
from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_athlete_statistics
)


@pytest.mark.api
def test_get_college_football_athlete_statistics(sports_core_api_client, ensure_json_output_dir):
    """Test getting college football athlete statistics using generic endpoint."""
    # Using a known college football athlete ID
    athlete_id = "4426414"  # Example athlete ID
    
    response = get_athlete_statistics.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="college-football", 
        athlete_id=athlete_id
    )
    
    # Note: Some athletes may not have statistics (404), which is valid (e.g., offensive linemen)
    assert response.status_code in [200, 404], f"Unexpected status code: {response.status_code}"
    
    # Parse and validate response
    result = response.parsed
    assert result is not None, "Response should be parsed successfully"
    
    # Save response for analysis
    if result:
        with open(f"{ensure_json_output_dir}/college_football_athlete_statistics_{athlete_id}.json", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
    
    print(f"Successfully retrieved college football athlete {athlete_id} statistics")


@pytest.mark.api 
def test_get_mens_college_basketball_athlete_details(sports_core_api_client, ensure_json_output_dir):
    """Test getting men's college basketball athlete details using generic endpoint."""
    # Using a known men's college basketball athlete ID
    athlete_id = "4397189"  # Example athlete ID
    
    from models.sports_core_api.espn_sports_core_api_client.api.default import get_athlete_details
    
    response = get_athlete_details.sync_detailed(
        client=sports_core_api_client,
        sport="basketball",
        league="mens-college-basketball", 
        athlete_id=athlete_id
    )
    
    # Note: Some athletes may not have statistics (404), which is valid (e.g., offensive linemen)
    assert response.status_code in [200, 404], f"Unexpected status code: {response.status_code}"
    
    # Parse and validate response
    result = response.parsed
    assert result is not None, "Response should be parsed successfully"
    
    # Save response for analysis
    if result:
        with open(f"{ensure_json_output_dir}/mens_college_basketball_athlete_{athlete_id}.json", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
    
    print(f"Successfully retrieved men's college basketball athlete {athlete_id} details")


@pytest.mark.api 
def test_get_womens_college_basketball_athlete_details(sports_core_api_client, ensure_json_output_dir):
    """Test getting women's college basketball athlete details using generic endpoint."""
    # Using Sydney Affolter from Iowa
    athlete_id = "4898389"  # Sydney Affolter - Iowa Guard
    
    from models.sports_core_api.espn_sports_core_api_client.api.default import get_athlete_details
    
    response = get_athlete_details.sync_detailed(
        client=sports_core_api_client,
        sport="basketball",
        league="womens-college-basketball", 
        athlete_id=athlete_id
    )
    
    # Note: Some athletes may not have statistics (404), which is valid (e.g., offensive linemen)
    assert response.status_code in [200, 404], f"Unexpected status code: {response.status_code}"
    
    # Parse and validate response
    result = response.parsed
    assert result is not None, "Response should be parsed successfully"
    
    # Save response for analysis
    if result:
        with open(f"{ensure_json_output_dir}/womens_college_basketball_athlete_{athlete_id}.json", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
    
    print(f"Successfully retrieved women's college basketball athlete {athlete_id} details")