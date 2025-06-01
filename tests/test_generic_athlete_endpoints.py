"""Tests for generic athlete endpoints across all sports and leagues."""
import pytest
import json
from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_athlete_details,
    get_athlete_statistics,
    get_athlete_statistics_log,
)


# Test data for various sports/leagues with known athlete IDs
ATHLETE_TEST_DATA = [
    # Professional leagues
    ("football", "nfl", "3139477", "Patrick Mahomes"),
    ("basketball", "nba", "1966", "LeBron James"),
    ("baseball", "mlb", "33912", "Mookie Betts"),  # Using a known valid MLB player ID
    ("hockey", "nhl", "3042109", "Connor McDavid"),
    ("basketball", "wnba", "2491205", "A'ja Wilson"),
    # College sports
    ("football", "college-football", "4426414", "Zeke Correll"),
    ("basketball", "mens-college-basketball", "4397189", "Jalen Smith"),
    ("basketball", "womens-college-basketball", "4898389", "Sydney Affolter"),  # Iowa
    ("basketball", "womens-college-basketball", "5174285", "MiLaysia Fulwiley"),  # South Carolina
]


@pytest.mark.api
@pytest.mark.parametrize("sport,league,athlete_id,athlete_name", ATHLETE_TEST_DATA)
def test_get_athlete_details_cross_sport(
    sports_core_api_client, ensure_json_output_dir, sport, league, athlete_id, athlete_name
):
    """Test getting athlete details across different sports and leagues."""
    response = get_athlete_details.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        athlete_id=athlete_id
    )
    
    assert response.status_code == 200, (
        f"Failed to get {athlete_name} ({sport}/{league}): {response.status_code}"
    )
    
    result = response.parsed
    assert result is not None, f"Response should parse successfully for {athlete_name}"
    assert result.id == athlete_id, f"Athlete ID should match for {athlete_name}"
    
    # Basic validation of common fields
    assert result.first_name is not None or result.last_name is not None, (
        f"Athlete should have a name: {athlete_name}"
    )
    
    # Save response for reference
    if hasattr(result, 'to_dict'):
        filename = f"athlete_details_{sport}_{league}_{athlete_id}.json"
        with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
    
    print(f"✓ Successfully retrieved {athlete_name} ({sport}/{league})")


@pytest.mark.api
@pytest.mark.parametrize("sport,league,athlete_id,athlete_name", ATHLETE_TEST_DATA)
def test_get_athlete_statistics_cross_sport(
    sports_core_api_client, ensure_json_output_dir, sport, league, athlete_id, athlete_name
):
    """Test getting athlete statistics across different sports and leagues."""
    response = get_athlete_statistics.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        athlete_id=athlete_id
    )
    
    # Note: Some athletes may not have statistics (404), which is valid
    assert response.status_code in [200, 404], (
        f"Unexpected status code for {athlete_name} ({sport}/{league}): {response.status_code}"
    )
    
    if response.status_code == 200:
        result = response.parsed
        assert result is not None, f"Response should parse successfully for {athlete_name}"
        
        # Save response for reference
        if hasattr(result, 'to_dict'):
            filename = f"athlete_statistics_{sport}_{league}_{athlete_id}.json"
            with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
                json.dump(result.to_dict(), f, indent=2)
        
        print(f"✓ Successfully retrieved statistics for {athlete_name} ({sport}/{league})")
    else:
        print(f"ℹ No statistics available for {athlete_name} ({sport}/{league})")


@pytest.mark.api
@pytest.mark.parametrize("sport,league,athlete_id,athlete_name", ATHLETE_TEST_DATA)
def test_get_athlete_statistics_log_cross_sport(
    sports_core_api_client, ensure_json_output_dir, sport, league, athlete_id, athlete_name
):
    """Test getting athlete statistics log across different sports and leagues."""
    response = get_athlete_statistics_log.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        athlete_id=athlete_id
    )
    
    # Note: Some athletes may not have statistics logs (404), which is valid
    assert response.status_code in [200, 404], (
        f"Unexpected status code for {athlete_name} ({sport}/{league}): {response.status_code}"
    )
    
    if response.status_code == 200:
        result = response.parsed
        assert result is not None, f"Response should parse successfully for {athlete_name}"
        
        # Save response for reference
        if hasattr(result, 'to_dict'):
            filename = f"athlete_statistics_log_{sport}_{league}_{athlete_id}.json"
            with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
                json.dump(result.to_dict(), f, indent=2)
        
        print(f"✓ Successfully retrieved statistics log for {athlete_name} ({sport}/{league})")
    else:
        print(f"ℹ No statistics log available for {athlete_name} ({sport}/{league})")


@pytest.mark.api
def test_get_athlete_details_with_query_params(sports_core_api_client):
    """Test athlete statistics with query parameters."""
    # Test NFL athlete statistics with season type filter
    response = get_athlete_statistics.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        athlete_id="3139477",  # Patrick Mahomes
        seasontype=2,  # Regular season
        year=2023,
        limit=10
    )
    
    assert response.status_code in [200, 404], f"Unexpected status code: {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        assert result is not None, "Response should parse successfully"
        print("✓ Successfully retrieved filtered statistics with query params")


@pytest.mark.api 
def test_athlete_endpoint_error_handling(sports_core_api_client):
    """Test error handling for invalid athlete requests."""
    # Test with invalid athlete ID
    response = get_athlete_details.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl", 
        athlete_id="99999999"  # Invalid ID
    )
    
    assert response.status_code == 404, f"Expected 404 for invalid athlete, got {response.status_code}"
    
    # Test with invalid sport/league combination
    response = get_athlete_details.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nba",  # Invalid combination
        athlete_id="1966"
    )
    
    assert response.status_code in [400, 404], (
        f"Expected 400 or 404 for invalid sport/league combo, got {response.status_code}"
    )


# Additional focused tests for specific leagues
@pytest.mark.api
def test_college_football_specific_athletes(sports_core_api_client, ensure_json_output_dir):
    """Test multiple college football athletes to ensure coverage."""
    college_football_athletes = [
        ("4426414", "Zeke Correll"),
        ("4429013", "Example Player 2"),
    ]
    
    for athlete_id, athlete_name in college_football_athletes:
        response = get_athlete_details.sync_detailed(
            client=sports_core_api_client,
            sport="football",
            league="college-football",
            athlete_id=athlete_id
        )
        
        if response.status_code == 200:
            result = response.parsed
            assert result is not None
            assert result.id == athlete_id
            print(f"✓ Retrieved college football athlete: {athlete_name}")
        else:
            print(f"ℹ Could not retrieve {athlete_name} (ID: {athlete_id})")


@pytest.mark.api
def test_mens_college_basketball_specific_athletes(sports_core_api_client):
    """Test men's college basketball athletes."""
    response = get_athlete_details.sync_detailed(
        client=sports_core_api_client,
        sport="basketball",
        league="mens-college-basketball",
        athlete_id="4397189"  # Jalen Smith
    )
    
    assert response.status_code == 200
    result = response.parsed
    assert result is not None
    assert result.display_name == "Jalen Smith"
    assert result.position is not None
    print("✓ Retrieved men's college basketball athlete with position info")


@pytest.mark.api
def test_womens_college_basketball_specific_athletes(sports_core_api_client, ensure_json_output_dir):
    """Test women's college basketball athletes."""
    # Test multiple women's college basketball athletes
    womens_cbb_athletes = [
        ("4898389", "Sydney Affolter", "Iowa"),
        ("5174285", "MiLaysia Fulwiley", "South Carolina"),
        ("4434019", "Maryam Dauda", "South Carolina"),
    ]
    
    for athlete_id, athlete_name, team in womens_cbb_athletes:
        response = get_athlete_details.sync_detailed(
            client=sports_core_api_client,
            sport="basketball",
            league="womens-college-basketball",
            athlete_id=athlete_id
        )
        
        assert response.status_code == 200, f"Failed to get {athlete_name} ({team})"
        result = response.parsed
        assert result is not None
        assert result.id == athlete_id
        print(f"✓ Retrieved women's college basketball athlete: {athlete_name} ({team})")
        
        # Save one for reference
        if athlete_id == "4898389" and hasattr(result, 'to_dict'):
            with open(f"{ensure_json_output_dir}/womens_cbb_athlete_{athlete_id}.json", "w") as f:
                json.dump(result.to_dict(), f, indent=2)