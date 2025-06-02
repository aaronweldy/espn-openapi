#!/usr/bin/env python3
"""
Test ESPN Competitor Statistics API
"""

import pytest
import json
import logging

from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_competitor_statistics,
)

logging.basicConfig(level=logging.INFO)


@pytest.mark.api
def test_get_competitor_statistics_nfl(sports_core_api_client, ensure_json_output_dir):
    """Test fetching competitor statistics for NFL games."""
    sport = "football"
    league = "nfl"
    event_id = "401437954"  # Historical NFL game
    competition_id = "401437954"
    competitor_id = "30"  # Jacksonville Jaguars
    
    response = get_competitor_statistics.sync_detailed(
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
    assert hasattr(result, 'ref'), "Result should have ref"
    assert hasattr(result, 'splits'), "Result should have splits"
    
    logging.info(f"\nCompetitor Statistics for {sport.upper()} {league.upper()}:")
    logging.info(f"Event: {event_id}, Competitor: {competitor_id}")
    
    # Log splits info
    if result.splits:
        logging.info(f"\nSplits: {result.splits.name}")
        if result.splits.categories:
            logging.info(f"Categories: {len(result.splits.categories)}")
            
            # Log first few categories
            for i, category in enumerate(result.splits.categories[:3]):
                logging.info(f"\n  {i+1}. {category.display_name}:")
                if category.stats:
                    logging.info(f"     Stats count: {len(category.stats)}")
                    # Show first few stats
                    for j, stat in enumerate(category.stats[:3]):
                        if hasattr(stat, 'display_value'):
                            logging.info(f"     - {stat.display_name}: {stat.display_value}")
    
    # Save response
    filename = f"competitor_statistics_{sport}_{league}_{event_id}_competitor{competitor_id}.json"
    with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
        json.dump(result.to_dict() if hasattr(result, 'to_dict') else result.__dict__, f, indent=2)
    
    logging.info(f"\n✓ Saved response to {filename}")


@pytest.mark.api
@pytest.mark.parametrize("sport,league,event_id,competitor_id", [
    # NFL - Known working
    ("football", "nfl", "401437954", "30"),  # Jacksonville
    ("football", "nfl", "401437954", "33"),  # Baltimore (opponent)
    
    # College Football
    ("football", "college-football", "401547417", "130"),  # Michigan
    
    # NBA - Test if available
    ("basketball", "nba", "401360638", "13"),  # Lakers (older game)
    
    # NHL
    ("hockey", "nhl", "401559593", "10"),  # Toronto
    
    # MLB
    ("baseball", "mlb", "401472463", "15"),  # Colorado
])
def test_get_competitor_statistics_multiple_sports(
    sports_core_api_client, sport, league, event_id, competitor_id, ensure_json_output_dir
):
    """Test competitor statistics across different sports."""
    response = get_competitor_statistics.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=event_id,  # Usually same as event_id
        competitor_id=competitor_id
    )
    
    # Statistics might not be available for all games/sports
    if response.status_code == 404:
        error_msg = "Not found"
        if response.parsed and hasattr(response.parsed, 'error') and hasattr(response.parsed.error, 'message'):
            error_msg = response.parsed.error.message
        pytest.skip(f"Statistics not available for {sport}/{league} event {event_id}: {error_msg}")
    
    # Some endpoints return 500 errors (API issues)
    if response.status_code == 500:
        pytest.skip(f"API error (500) for {sport}/{league} event {event_id}")
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    
    logging.info(f"\n{sport.upper()} ({league.upper()}) Competitor Statistics:")
    logging.info(f"  Event: {event_id}, Competitor: {competitor_id}")
    
    if hasattr(result, 'splits') and result.splits:
        logging.info(f"  Splits: {getattr(result.splits, 'name', 'Unknown')}")
        if hasattr(result.splits, 'categories'):
            logging.info(f"  Categories: {len(result.splits.categories)}")
            
            # Show category names
            category_names = [cat.name for cat in result.splits.categories if hasattr(cat, 'name')]
            if category_names:
                logging.info(f"  Category types: {', '.join(category_names[:5])}")


@pytest.mark.api
def test_competitor_statistics_categories_nfl(sports_core_api_client):
    """Test specific statistics categories for NFL."""
    response = get_competitor_statistics.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        event_id="401437954",
        competition_id="401437954",
        competitor_id="30"
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result.splits, "Should have splits"
    assert result.splits.categories, "Should have categories"
    
    # Check for expected NFL categories
    category_names = [cat.name for cat in result.splits.categories]
    
    # NFL should have these categories
    expected_categories = ["general", "passing", "rushing", "receiving", "defensive"]
    for expected in expected_categories:
        if expected in category_names:
            logging.info(f"✓ Found expected category: {expected}")
        else:
            logging.info(f"✗ Missing expected category: {expected}")
    
    # Check passing stats
    passing_cat = next((cat for cat in result.splits.categories if cat.name == "passing"), None)
    if passing_cat and passing_cat.stats:
        logging.info("\nPassing stats sample:")
        for stat in passing_cat.stats[:5]:
            if hasattr(stat, 'display_name') and hasattr(stat, 'display_value'):
                logging.info(f"  {stat.display_name}: {stat.display_value}")


@pytest.mark.api
def test_competitor_statistics_invalid_competitor(sports_core_api_client):
    """Test competitor statistics with invalid competitor ID."""
    response = get_competitor_statistics.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        event_id="401437954",
        competition_id="401437954",
        competitor_id="99999"  # Invalid competitor
    )
    
    # Should return 404
    assert response.status_code == 404, f"Expected 404 for invalid competitor, got {response.status_code}"