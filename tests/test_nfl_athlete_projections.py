import pytest
import json
import os
from models.sports_core_api.espn_sports_core_api_client.api.default import get_nfl_athlete_projections
from models.sports_core_api.espn_sports_core_api_client.models.athlete_statistics_response import AthleteStatisticsResponse
from models.sports_core_api.espn_sports_core_api_client.types import UNSET


@pytest.mark.api
def test_get_nfl_athlete_projections(sports_core_api_client, ensure_json_output_dir):
    """Test NFL athlete projections endpoint."""
    
    # Test with Jalen Hurts (Eagles QB) for 2024 season
    response = get_nfl_athlete_projections.sync_detailed(
        client=sports_core_api_client,
        year=2024,
        seasontype=2,  # Regular season
        athlete_id="4040715"
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, AthleteStatisticsResponse), "Response should parse to AthleteStatisticsResponse"
    
    # Verify the structure
    assert result.ref, "Response should have a $ref field"
    assert result.season, "Response should have season info"
    assert result.athlete, "Response should have athlete info"
    assert result.splits, "Response should have splits data"
    
    # Check the splits structure
    assert result.splits.id == "0", "Splits ID should be 0"
    assert result.splits.name == "All Splits", "Splits name should be 'All Splits'"
    assert result.splits.categories, "Splits should have categories"
    
    # Look for key projection categories
    category_names = [cat.name for cat in result.splits.categories if cat.name]
    assert "passing" in category_names, "Should have passing projections"
    assert "rushing" in category_names, "Should have rushing projections"
    
    # Save the response
    output_path = os.path.join(ensure_json_output_dir, "nfl_athlete_projections_test.json")
    with open(output_path, "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    print(f"✓ NFL athlete projections test passed for athlete 4040715")


@pytest.mark.api
def test_get_nfl_athlete_projections_not_found(sports_core_api_client):
    """Test NFL athlete projections endpoint with invalid athlete ID."""
    
    response = get_nfl_athlete_projections.sync_detailed(
        client=sports_core_api_client,
        year=2024,
        seasontype=2,
        athlete_id="99999999"  # Invalid ID
    )
    
    # The API returns 404 for invalid athlete IDs
    assert response.status_code == 404, f"Expected status code 404 for invalid athlete, got {response.status_code}"


@pytest.mark.api
@pytest.mark.parametrize("year,seasontype,athlete_id", [
    (2024, 2, "4040715"),  # Jalen Hurts - Eagles QB
    (2024, 2, "3139477"),  # Patrick Mahomes - Chiefs QB (this might return 404 based on earlier test)
])
def test_get_nfl_athlete_projections_multiple_athletes(sports_core_api_client, year, seasontype, athlete_id):
    """Test NFL athlete projections for multiple athletes."""
    
    response = get_nfl_athlete_projections.sync_detailed(
        client=sports_core_api_client,
        year=year,
        seasontype=seasontype,
        athlete_id=athlete_id
    )
    
    # Some athletes may not have projections available
    assert response.status_code in [200, 404], f"Expected status code 200 or 404, got {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        assert isinstance(result, AthleteStatisticsResponse), "Response should parse to AthleteStatisticsResponse"
        print(f"✓ Found projections for athlete {athlete_id}")
    else:
        print(f"✗ No projections available for athlete {athlete_id}")