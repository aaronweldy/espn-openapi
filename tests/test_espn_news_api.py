import pytest
import json
import logging
from models.sports_core_api.espn_sports_core_api_client import Client
from models.sports_core_api.espn_sports_core_api_client.api.default import get_sports_news

logging.basicConfig(level=logging.INFO)


@pytest.mark.api
def test_get_sports_news(ensure_json_output_dir):
    """Test getting sports news without filters."""
    # Create a client with the correct base URL for news API
    news_client = Client(base_url="https://now.core.api.espn.com")
    
    # Call the API
    response = get_sports_news.sync_detailed(
        client=news_client,
        limit=5
    )
    
    # Validate response
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Parse the response
    result = response.parsed
    assert result is not None, "Response should parse successfully"
    
    # Validate structure
    assert hasattr(result, 'headlines'), "Response should have headlines"
    assert hasattr(result, 'results_count'), "Response should have results_count"
    assert hasattr(result, 'results_limit'), "Response should have results_limit"
    assert hasattr(result, 'results_offset'), "Response should have results_offset"
    assert hasattr(result, 'status'), "Response should have status"
    assert hasattr(result, 'timestamp'), "Response should have timestamp"
    
    # Check headlines
    assert len(result.headlines) > 0, "Should have at least one headline"
    
    # Check first headline structure
    headline = result.headlines[0]
    assert hasattr(headline, 'id'), "Headline should have id"
    assert hasattr(headline, 'headline'), "Headline should have headline text"
    assert hasattr(headline, 'type'), "Headline should have type"
    
    # Save response
    with open(f"{ensure_json_output_dir}/espn_news_api_test.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    logging.info(f"Retrieved {len(result.headlines)} headlines")
    logging.info(f"Total results available: {result.results_count}")
    

@pytest.mark.api
def test_get_sports_news_filtered(ensure_json_output_dir):
    """Test getting sports news filtered by sport."""
    # Create a client with the correct base URL for news API
    news_client = Client(base_url="https://now.core.api.espn.com")
    
    # Call the API with sport filter
    response = get_sports_news.sync_detailed(
        client=news_client,
        sport="basketball",
        limit=3
    )
    
    # Validate response
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Parse the response
    result = response.parsed
    assert result is not None, "Response should parse successfully"
    
    # Validate we got results
    assert len(result.headlines) > 0, "Should have at least one headline"
    
    # Save response
    with open(f"{ensure_json_output_dir}/espn_news_api_basketball_test.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    logging.info(f"Retrieved {len(result.headlines)} basketball headlines")
    

@pytest.mark.api
@pytest.mark.parametrize("sport", [
    "football",
    "baseball", 
    "hockey",
    "golf",
    "tennis"
])
def test_get_sports_news_multiple_sports(sport):
    """Test getting news for multiple sports."""
    # Create a client with the correct base URL for news API
    news_client = Client(base_url="https://now.core.api.espn.com")
    
    # Call the API with sport filter
    response = get_sports_news.sync_detailed(
        client=news_client,
        sport=sport,
        limit=2
    )
    
    # Validate response
    assert response.status_code == 200, f"Expected status code 200 for {sport}, got {response.status_code}"
    
    # Parse the response
    result = response.parsed
    assert result is not None, f"Response should parse successfully for {sport}"
    
    # Log results
    logging.info(f"{sport}: {len(result.headlines)} headlines out of {result.results_count} total")