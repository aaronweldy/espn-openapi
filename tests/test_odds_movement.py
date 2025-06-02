#!/usr/bin/env python3
"""
Test ESPN Odds Movement History API
"""

import pytest
import json
import logging

from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_competition_odds_movement,
)

logging.basicConfig(level=logging.INFO)


@pytest.mark.api
def test_get_odds_movement_nfl(sports_core_api_client, ensure_json_output_dir):
    """Test fetching odds movement history for NFL games."""
    sport = "football"
    league = "nfl"
    event_id = "401249063"  # Historical NFL game
    competition_id = "401249063"
    provider_id = "1002"  # teamrankings
    history_type = "0"  # moneyline
    
    response = get_competition_odds_movement.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        provider_id=provider_id,
        history_type=history_type,
        limit=100
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    
    # Check structure
    assert hasattr(result, 'count'), "Result should have count"
    assert hasattr(result, 'page_index'), "Result should have page_index"
    assert hasattr(result, 'page_size'), "Result should have page_size"
    assert hasattr(result, 'page_count'), "Result should have page_count"
    assert hasattr(result, 'items'), "Result should have items"
    
    logging.info(f"\nOdds Movement History for {sport.upper()} {league.upper()}:")
    logging.info(f"Event: {event_id}, Provider: {provider_id}, Type: {'moneyline' if history_type == '0' else 'spread' if history_type == '1' else 'total'}")
    logging.info(f"Total movements: {result.count}")
    logging.info(f"Page: {result.page_index}/{result.page_count}, Size: {result.page_size}")
    
    # Log some movement details
    if result.items:
        logging.info("\nFirst few movements:")
        for i, movement in enumerate(result.items[:5]):
            logging.info(f"  {i+1}. {movement.line_date}: Away={movement.away_odds}, Home={movement.home_odds}")
            if movement.line != 0:
                logging.info(f"     Line: {movement.line}")
    
    # Save response
    filename = f"odds_movement_{sport}_{league}_{event_id}_provider{provider_id}_type{history_type}.json"
    with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
        json.dump(result.to_dict() if hasattr(result, 'to_dict') else result.__dict__, f, indent=2)
    
    logging.info(f"\n✓ Saved response to {filename}")


@pytest.mark.api
@pytest.mark.parametrize("sport,league,event_id,provider_id,history_type", [
    # NFL - Historical game with known data
    ("football", "nfl", "401249063", "1002", "0"),  # moneyline
    ("football", "nfl", "401249063", "1002", "1"),  # spread
    ("football", "nfl", "401249063", "1002", "2"),  # total
    
    # NBA - Test with different provider
    ("basketball", "nba", "401584793", "58", "0"),  # ESPN BET moneyline
    
    # MLB - Recent game
    ("baseball", "mlb", "401695789", "1002", "0"),  # moneyline
])
def test_get_odds_movement_multiple_sports(
    sports_core_api_client, sport, league, event_id, provider_id, history_type, ensure_json_output_dir
):
    """Test odds movement across different sports and bet types."""
    response = get_competition_odds_movement.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=event_id,  # Usually same as event_id
        provider_id=provider_id,
        history_type=history_type,
        limit=10  # Small limit for testing
    )
    
    # Movement data might not be available for all combinations
    if response.status_code == 404:
        pytest.skip(f"Odds movement not available for {sport}/{league} event {event_id}")
    
    # Some endpoints return 500 errors (API issues)
    if response.status_code == 500:
        pytest.skip(f"API error (500) for {sport}/{league} event {event_id}")
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    
    bet_type = "moneyline" if history_type == "0" else "spread" if history_type == "1" else "total"
    logging.info(f"\n{sport.upper()} ({league.upper()}) Odds Movement - {bet_type}:")
    logging.info(f"  Event: {event_id}, Provider: {provider_id}")
    logging.info(f"  Total movements: {getattr(result, 'count', 0)}")
    
    if hasattr(result, 'items') and result.items:
        first = result.items[0]
        last = result.items[-1]
        logging.info(f"  First: {first.line_date} - Away: {first.away_odds}, Home: {first.home_odds}")
        logging.info(f"  Last: {last.line_date} - Away: {last.away_odds}, Home: {last.home_odds}")


@pytest.mark.api
def test_odds_movement_pagination(sports_core_api_client):
    """Test pagination of odds movement history."""
    response = get_competition_odds_movement.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        event_id="401249063",
        competition_id="401249063",
        provider_id="1002",
        history_type="0",
        limit=5  # Small page size
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    
    # Check pagination
    assert result.page_size <= 5, "Page size should respect limit"
    if result.count > 5:
        assert result.page_count > 1, "Should have multiple pages"
    
    logging.info(f"\nPagination test:")
    logging.info(f"  Total items: {result.count}")
    logging.info(f"  Page size: {result.page_size}")
    logging.info(f"  Total pages: {result.page_count}")


@pytest.mark.api
def test_odds_movement_invalid_history_type(sports_core_api_client):
    """Test odds movement with invalid history type."""
    response = get_competition_odds_movement.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        event_id="401249063",
        competition_id="401249063",
        provider_id="1002",
        history_type="99",  # Invalid type
        limit=10
    )
    
    # API might return 404 or empty results for invalid types
    assert response.status_code in [200, 404], f"Expected 200 or 404, got {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        assert result.count == 0, "Should return empty results for invalid history type"