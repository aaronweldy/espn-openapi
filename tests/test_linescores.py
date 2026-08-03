#!/usr/bin/env python3
"""
Test ESPN Competitor Linescores API
"""

import pytest
import json
import logging

from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_competitor_linescores,
)

logging.basicConfig(level=logging.INFO)


@pytest.mark.api
def test_get_linescores_nfl(sports_core_api_client, ensure_json_output_dir):
    """Test fetching linescores for NFL games."""
    sport = "football"
    league = "nfl"
    event_id = "401437954"  # Historical NFL game
    competition_id = "401437954"
    competitor_id = "30"  # Jacksonville Jaguars
    
    response = get_competitor_linescores.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        competitor_id=competitor_id
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
    
    logging.info(f"\nLinescores for {sport.upper()} {league.upper()}:")
    logging.info(f"Event: {event_id}, Competitor: {competitor_id}")
    logging.info(f"Total periods: {result.count}")
    
    # Log linescore details
    if result.items:
        logging.info("\nScoring by period:")
        total_score = 0
        for item in result.items:
            logging.info(f"  Period {item.period}: {item.display_value} points")
            total_score += item.value
        logging.info(f"  Total: {total_score} points")
    
    # Save response
    filename = f"linescores_{sport}_{league}_{event_id}_competitor{competitor_id}.json"
    with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
        json.dump(result.to_dict() if hasattr(result, 'to_dict') else result.__dict__, f, indent=2)
    
    logging.info(f"\n✓ Saved response to {filename}")


@pytest.mark.api
@pytest.mark.parametrize("sport,league,event_id,competitor_id,expected_periods", [
    # NFL - 4 quarters
    ("football", "nfl", "401437954", "30", 4),  # Jacksonville Jaguars
    ("football", "nfl", "401437954", "10", 4),  # Tennessee Titans

    # NBA - 4 quarters (or more with OT)
    ("basketball", "nba", "401584793", "15", 4),  # Milwaukee Bucks

    # NHL - 3 periods
    ("hockey", "nhl", "401559593", "7", 3),  # Carolina Hurricanes

    # MLB - at least 8 half-innings recorded for the winning home side
    ("baseball", "mlb", "401472463", "23", 8),  # Pittsburgh Pirates

    # College Football - 4 quarters
    ("football", "college-football", "401628566", "194", 4),  # Ohio State Buckeyes
])
def test_get_linescores_multiple_sports(
    sports_core_api_client, sport, league, event_id, competitor_id, expected_periods, ensure_json_output_dir
):
    """Test linescores across different sports."""
    response = get_competitor_linescores.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=event_id,  # Usually same as event_id
        competitor_id=competitor_id
    )
    
    # A 404 means the event/competitor pairing is stale, not that the endpoint
    # is unsupported - surface it rather than skipping silently.
    if response.status_code == 404:
        pytest.fail(
            f"Competitor {competitor_id} is not part of {sport}/{league} event {event_id}"
        )

    # Upstream 500s are transient infrastructure blips, not schema changes
    if response.status_code == 500:
        pytest.skip(f"API error (500) for {sport}/{league} event {event_id}")

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    result = response.parsed
    assert result, "Response should parse successfully"

    # This endpoint answers 200 with an empty item list when the competitor did
    # not play in the event, so an empty payload means the fixture has drifted.
    assert result.count > 0, (
        f"No linescores returned for {sport}/{league} event {event_id} "
        f"competitor {competitor_id} - the fixture is likely stale"
    )
    assert len(result.items) == result.count, "Count should match number of items"

    logging.info(f"\n{sport.upper()} ({league.upper()}) Linescores:")
    logging.info(f"  Event: {event_id}, Competitor: {competitor_id}")
    logging.info(f"  Periods: {getattr(result, 'count', 0)}")
    
    # Check expected number of periods if specified
    if expected_periods:
        assert result.count >= expected_periods, f"Expected at least {expected_periods} periods, got {result.count}"

    if hasattr(result, 'items') and result.items:
        # Log first and last period scores
        first = result.items[0]
        last = result.items[-1]
        logging.info(f"  First period: {first.display_value}")
        logging.info(f"  Last period: {last.display_value}")
        
        # Calculate total
        total = sum(item.value for item in result.items)
        logging.info(f"  Total score: {total}")


@pytest.mark.api
def test_linescores_empty_result(sports_core_api_client):
    """Test linescores endpoint shape for a game that may or may not be completed."""
    response = get_competitor_linescores.sync_detailed(
        client=sports_core_api_client,
        sport="basketball",
        league="nba",
        event_id="401766122",  # Future NBA game
        competition_id="401766122",
        competitor_id="25"  # Oklahoma City Thunder
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    
    if result.count == 0:
        assert len(result.items) == 0, "Empty linescore responses should have no items"
        logging.info("\nLinescores test:")
        logging.info("  ✓ No linescores returned")
    else:
        assert len(result.items) == result.count, "Count should match number of items"
        assert all(item.period for item in result.items), "All returned linescores should include period numbers"
        logging.info("\nLinescores test:")
        logging.info(f"  ✓ Returned {result.count} linescores")


@pytest.mark.api
def test_linescores_invalid_competitor(sports_core_api_client):
    """Test linescores with invalid competitor ID."""
    response = get_competitor_linescores.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        event_id="401437954",
        competition_id="401437954",
        competitor_id="99999"  # Invalid competitor
    )
    
    # Should return 404 or empty results
    assert response.status_code in [200, 404], f"Expected 200 or 404, got {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        assert result.count == 0, "Should return empty results for invalid competitor"