import pytest
import json
import logging
from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_providers_list,
    get_provider_details,
)
from models.sports_core_api.espn_sports_core_api_client.models import (
    SportEnum,
    LeagueEnum,
    ProvidersListResponse,
    ProviderDetails,
    Reference,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league,expected_min_count",
    [
        (SportEnum.FOOTBALL, LeagueEnum.NFL, 50),
        (SportEnum.BASKETBALL, LeagueEnum.NBA, 50),
        (SportEnum.BASEBALL, LeagueEnum.MLB, 40),
        (SportEnum.HOCKEY, LeagueEnum.NHL, 30),  # NHL has fewer providers
    ],
)
def test_get_providers_list(
    sports_core_api_client,
    ensure_json_output_dir,
    sport,
    league,
    expected_min_count,
):
    """Test getting list of betting providers across different sports."""
    response = get_providers_list.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
    )

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, ProvidersListResponse), "Response should parse to ProvidersListResponse"
    
    # Validate pagination fields
    assert result.count >= expected_min_count, f"Should have at least {expected_min_count} providers"
    assert result.page_index >= 1, "Page index should be 1-based"
    assert result.page_size > 0, "Page size should be positive"
    assert result.page_count > 0, "Should have at least one page"
    assert result.items, "Should have items in the response"
    
    # Validate items
    assert len(result.items) <= result.page_size, "Items count should not exceed page size"
    
    # Check first few items
    for item in result.items[:5]:
        assert isinstance(item, Reference), "Item should be a Reference"
        assert item.ref, "Reference should have a URL"
        assert f"/providers/" in item.ref, "Reference URL should contain /providers/"
    
    logger.info(f"{sport.value} {league.value}: Found {result.count} providers across {result.page_count} pages")
    
    # Save response for first sport
    if sport == SportEnum.FOOTBALL:
        filename = f"{sport.value}_{league.value}_providers_list.json"
        with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
        logger.info(f"✓ Saved providers list to {filename}")


@pytest.mark.api
def test_providers_list_with_pagination(sports_core_api_client):
    """Test providers list with pagination parameters."""
    # Test with custom limit
    response = get_providers_list.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        limit=10,
    )
    
    assert response.status_code == 200
    result = response.parsed
    assert len(result.items) <= 10, "Should respect limit parameter"
    
    # Test with page parameter
    response_page2 = get_providers_list.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        page=2,
    )
    
    assert response_page2.status_code == 200
    result_page2 = response_page2.parsed
    assert result_page2.page_index == 2, "Should return page 2"
    
    # Ensure different items on different pages
    if result.items and result_page2.items:
        assert result.items[0].ref != result_page2.items[0].ref, "Different pages should have different items"


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league,provider_id,expected_name",
    [
        (SportEnum.FOOTBALL, LeagueEnum.NFL, "58", "ESPN BET"),
        (SportEnum.BASKETBALL, LeagueEnum.NBA, "58", "ESPN BET"),
        (SportEnum.FOOTBALL, LeagueEnum.NFL, "40", "DraftKings"),
        (SportEnum.BASKETBALL, LeagueEnum.NBA, "1", "Caesars Sportsbook"),
    ],
)
def test_get_provider_details(
    sports_core_api_client,
    ensure_json_output_dir,
    sport,
    league,
    provider_id,
    expected_name,
):
    """Test getting specific provider details."""
    response = get_provider_details.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        provider_id=provider_id,
    )

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, ProviderDetails), "Response should parse to ProviderDetails"
    
    # Validate fields
    assert result.ref, "Should have a reference URL"
    assert result.id == provider_id, f"Provider ID should be {provider_id}"
    assert result.name == expected_name, f"Provider name should be {expected_name}"
    
    # Priority is optional but if present should be positive
    if hasattr(result, 'priority') and result.priority is not None:
        assert result.priority > 0, "Priority should be positive"
    
    logger.info(f"Provider {provider_id}: {result.name}")
    
    # Save one example
    if sport == SportEnum.FOOTBALL and provider_id == "58":
        filename = f"{sport.value}_{league.value}_provider_{provider_id}.json"
        with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
        logger.info(f"✓ Saved provider details to {filename}")


@pytest.mark.api
def test_provider_details_invalid_id(sports_core_api_client):
    """Test requesting details for an invalid provider ID."""
    response = get_provider_details.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        provider_id="99999",  # Invalid provider ID
    )
    
    # ESPN API returns 404 for invalid provider
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"