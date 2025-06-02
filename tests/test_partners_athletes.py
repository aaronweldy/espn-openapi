"""Test Partners API Athletes endpoint"""
import json
import logging
import pytest
from models.partners_api.espn_partners_api_client.api.default import get_athletes_list
from models.partners_api.espn_partners_api_client.models import AthletesListResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize("sport,league,limit", [
    ("football", "nfl", 100),
    ("basketball", "nba", 50),
    ("baseball", "mlb", 50),
    ("hockey", "nhl", 50),
])
def test_get_athletes_list(partners_api_client, sport, league, limit, ensure_json_output_dir):
    """Test getting athletes list from partners API for different sports."""
    response = get_athletes_list.sync_detailed(
        client=partners_api_client,
        sport=sport,
        league=league,
        limit=limit
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, AthletesListResponse), "Response should parse to AthletesListResponse"
    
    # Validate response structure
    assert len(result.athletes) > 0, "Should have at least one athlete"
    assert result.count > 0, "Total count should be positive"
    assert result.page_index == 1, "Page index should be 1"
    assert result.page_size == limit, f"Page size should be {limit}"
    assert result.page_count > 0, "Page count should be positive"
    
    # Log some info
    logger.info(f"{sport.upper()}/{league.upper()} Athletes: Found {result.count} total, showing {len(result.athletes)}")
    
    # Validate first few athletes
    for i, athlete in enumerate(result.athletes[:3]):
        assert athlete.id, "Athlete should have ID"
        assert athlete.display_name, "Athlete should have display name"
        
        logger.info(f"  {i+1}. {athlete.display_name}")
        if athlete.team:
            logger.info(f"     Team: {athlete.team.display_name}")
        if athlete.position:
            logger.info(f"     Position: {athlete.position.abbreviation}")
        if athlete.jersey:
            logger.info(f"     Jersey: {athlete.jersey}")
    
    # Save response for analysis
    output_file = f"{ensure_json_output_dir}/partners_{sport}_{league}_athletes.json"
    with open(output_file, "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    logger.info(f"Saved response to {output_file}")


@pytest.mark.api
def test_get_athletes_large_limit(partners_api_client, ensure_json_output_dir):
    """Test getting athletes with a large limit to verify the endpoint supports it."""
    sport = "football"
    league = "nfl"
    limit = 1000  # Large limit
    
    response = get_athletes_list.sync_detailed(
        client=partners_api_client,
        sport=sport,
        league=league,
        limit=limit
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, AthletesListResponse), "Response should parse to AthletesListResponse"
    
    # Verify we got the requested number (or all available if less)
    actual_count = len(result.athletes)
    logger.info(f"Requested {limit} athletes, got {actual_count} (total available: {result.count})")
    
    if result.count >= limit:
        assert actual_count == limit, f"Should return exactly {limit} athletes when available"
    else:
        assert actual_count == result.count, "Should return all available athletes when less than limit"
    
    # Verify pagination info is correct
    assert result.page_size == actual_count, "Page size should match actual returned count"


@pytest.mark.api
@pytest.mark.parametrize("sport,league", [
    ("football", "college-football"),
    ("basketball", "wnba"),
    ("soccer", "eng.1"),
])
def test_get_athletes_other_leagues(partners_api_client, sport, league):
    """Test getting athletes for other leagues."""
    response = get_athletes_list.sync_detailed(
        client=partners_api_client,
        sport=sport,
        league=league,
        limit=10
    )
    
    # These might work or return 404/400 depending on what's supported
    if response.status_code == 200:
        result = response.parsed
        logger.info(f"{sport.upper()}/{league.upper()} Athletes: Found {result.count} total")
    else:
        logger.info(f"{sport.upper()}/{league.upper()} Athletes: Status {response.status_code} - might not be supported")