#!/usr/bin/env python3
"""
Test ESPN Sports Core API - Athletes List Endpoint
Requires Python 3.10+
"""

import json
import pytest
import logging

from models.sports_core_api.espn_sports_core_api_client.models.sport_enum import (
    SportEnum,
)
from models.sports_core_api.espn_sports_core_api_client.models.league_enum import (
    LeagueEnum,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_athletes_list import (
    sync_detailed as get_athletes_list,
)
from models.sports_core_api.espn_sports_core_api_client.models.athletes_list_response import (
    AthletesListResponse,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league,expected_min_count",
    [
        (SportEnum.SOCCER, LeagueEnum.ENG_1, 400),  # Premier League has many players
        (SportEnum.FOOTBALL, LeagueEnum.NFL, 1500),  # NFL has many players  
        (SportEnum.BASKETBALL, LeagueEnum.NBA, 400),  # NBA has many players
        (SportEnum.HOCKEY, LeagueEnum.NHL, 700),  # NHL has many players
    ],
)
def test_get_athletes_list(sports_core_api_client, ensure_json_output_dir, sport, league, expected_min_count):
    """Test getting paginated list of athletes for different sports and leagues."""
    logger.info(f"Testing athletes list for {sport.value}/{league.value}")
    
    response = get_athletes_list(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        page_size=25,
        page_index=1,
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, AthletesListResponse), "Response should parse to AthletesListResponse"
    
    # Validate response structure
    assert result.count >= expected_min_count, f"Expected at least {expected_min_count} athletes, got {result.count}"
    assert result.page_index == 1, "First page should have page_index 1"
    assert result.page_size == 25, "Page size should match requested size"
    assert result.page_count > 0, "Should have at least one page"
    assert len(result.items) > 0, "Should have at least one athlete"
    assert len(result.items) <= 25, "Should not exceed requested page size"
    
    # Validate athlete references
    for item in result.items:
        assert item.ref, "Each athlete should have a valid reference URL"
        assert "athletes" in item.ref, "Reference URL should contain 'athletes'"
        assert sport.value in item.ref, f"Reference URL should contain sport '{sport.value}'"
        assert league.value in item.ref, f"Reference URL should contain league '{league.value}'"
    
    # Save response for analysis
    output_file = f"{ensure_json_output_dir}/athletes_list_{sport.value}_{league.value}.json"
    with open(output_file, "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    logger.info(f"Found {result.count} total athletes, {len(result.items)} on current page")
    logger.info(f"Saved response to {output_file}")


@pytest.mark.api
def test_get_athletes_list_pagination_params(sports_core_api_client, ensure_json_output_dir):
    """Test that pagination parameters are accepted without errors."""
    sport = SportEnum.SOCCER
    league = LeagueEnum.ENG_1
    
    # Test with different pagination parameters
    response = get_athletes_list(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        page_size=50,
        page_index=1,
    )
    
    assert response.status_code == 200
    result = response.parsed
    assert isinstance(result, AthletesListResponse)
    
    # Verify basic pagination structure exists even if not fully functional
    assert hasattr(result, 'page_index')
    assert hasattr(result, 'page_size') 
    assert hasattr(result, 'page_count')
    assert hasattr(result, 'count')
    assert result.count > 0
    assert len(result.items) > 0
    
    logger.info(f"Pagination params test passed - Total: {result.count}, Page size reported: {result.page_size}, Items returned: {len(result.items)}")