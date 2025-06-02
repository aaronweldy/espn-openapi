import pytest
import json
import logging
from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_competition_odds_head_to_heads,
)
from models.sports_core_api.espn_sports_core_api_client.models import (
    SportEnum,
    LeagueEnum,
    HeadToHeadsListResponse,
    Reference,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league,event_id,provider_id",
    [
        (SportEnum.FOOTBALL, LeagueEnum.NFL, "401547602", "58"),  # ESPN BET
        (SportEnum.FOOTBALL, LeagueEnum.NFL, "401547417", "40"),  # DraftKings
        (SportEnum.BASKETBALL, LeagueEnum.NBA, "401584793", "58"),  # ESPN BET
        (SportEnum.BASKETBALL, LeagueEnum.NBA, "401584793", "40"),  # DraftKings
        (SportEnum.BASEBALL, LeagueEnum.MLB, "401472463", "58"),
        pytest.param(
            SportEnum.HOCKEY, LeagueEnum.NHL, "401559593", "58",
            marks=pytest.mark.xfail(reason="NHL event returns 500 error")
        ),
    ],
)
def test_get_competition_odds_head_to_heads(
    sports_core_api_client,
    ensure_json_output_dir,
    sport,
    league,
    event_id,
    provider_id,
):
    """Test getting head-to-head odds from different providers across sports."""
    response = get_competition_odds_head_to_heads.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=event_id,  # Usually the same as event_id
        provider_id=provider_id,
    )

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, HeadToHeadsListResponse), "Response should parse to HeadToHeadsListResponse"
    
    # Validate pagination fields
    assert isinstance(result.count, int), "Count should be an integer"
    assert result.count >= 0, "Count should be non-negative"
    assert isinstance(result.page_index, int), "Page index should be an integer"
    assert result.page_index >= 0, "Page index should be non-negative"
    assert result.page_size > 0, "Page size should be positive"
    assert isinstance(result.page_count, int), "Page count should be an integer"
    assert result.page_count >= 0, "Page count should be non-negative"
    assert isinstance(result.items, list), "Items should be a list"
    
    # If there are items, validate them
    if result.items:
        for item in result.items:
            assert isinstance(item, Reference), "Item should be a Reference"
            assert item.ref, "Reference should have a URL"
            logger.info(f"Head-to-head reference: {item.ref}")
    
    logger.info(
        f"{sport.value} {league.value} Event {event_id} Provider {provider_id}: "
        f"Found {result.count} head-to-head odds"
    )
    
    # Save one example
    if sport == SportEnum.FOOTBALL and provider_id == "58":
        filename = f"{sport.value}_{league.value}_odds_head_to_heads_{event_id}_provider_{provider_id}.json"
        with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
        logger.info(f"✓ Saved head-to-heads response to {filename}")


@pytest.mark.api
def test_head_to_heads_invalid_provider(sports_core_api_client):
    """Test requesting head-to-heads for an invalid provider ID."""
    response = get_competition_odds_head_to_heads.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        event_id="401547602",
        competition_id="401547602",
        provider_id="99999",  # Invalid provider ID
    )
    
    # ESPN API might return 404 or empty results for invalid provider
    assert response.status_code in [200, 404], f"Expected status code 200 or 404, got {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        assert result.count == 0, "Should have no results for invalid provider"


@pytest.mark.api
def test_head_to_heads_invalid_event(sports_core_api_client):
    """Test requesting head-to-heads for an invalid event ID."""
    response = get_competition_odds_head_to_heads.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        event_id="99999999",
        competition_id="99999999",
        provider_id="58",
    )
    
    # ESPN API returns 400 for invalid event
    assert response.status_code in [400, 404], f"Expected status code 400 or 404, got {response.status_code}"