#!/usr/bin/env python3
"""
Test ESPN Events API Date Range Filtering
"""

import pytest
import json
import logging
from datetime import datetime, timedelta

from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_league_events,
)

logging.basicConfig(level=logging.INFO)


@pytest.mark.api
def test_events_single_date(sports_core_api_client, ensure_json_output_dir):
    """Test fetching events for a single date."""
    sport = "basketball"
    league = "nba"
    # Use a date during NBA season
    single_date = "20250301"
    
    response = get_league_events.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        dates=single_date
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    
    logging.info(f"\nEvents for {sport.upper()} {league.upper()} on {single_date}:")
    logging.info(f"Total events: {result.count}")
    
    # Save response
    filename = f"events_{sport}_{league}_single_date_{single_date}.json"
    with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
        json.dump(result.to_dict() if hasattr(result, 'to_dict') else result.__dict__, f, indent=2)
    
    logging.info(f"✓ Saved response to {filename}")


@pytest.mark.api
def test_events_date_range(sports_core_api_client, ensure_json_output_dir):
    """Test fetching events for a date range."""
    sport = "basketball"
    league = "mens-college-basketball"
    # Use March dates when college basketball is active
    date_range = "20250301-20250307"
    
    response = get_league_events.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        dates=date_range
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    
    logging.info(f"\nEvents for {sport.upper()} {league.upper()} from {date_range}:")
    logging.info(f"Total events: {result.count}")
    
    # Should have multiple events during March Madness season
    assert result.count > 0, "Should have events during March"
    
    # Save response
    filename = f"events_{sport}_{league}_date_range_{date_range.replace('-', '_')}.json"
    with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
        json.dump(result.to_dict() if hasattr(result, 'to_dict') else result.__dict__, f, indent=2)
    
    logging.info(f"✓ Saved response to {filename}")


@pytest.mark.api
def test_events_full_year(sports_core_api_client, ensure_json_output_dir):
    """Test fetching events for a full year."""
    sport = "football"
    league = "nfl"
    year = "2024"
    
    response = get_league_events.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        dates=year
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    
    logging.info(f"\nEvents for {sport.upper()} {league.upper()} in year {year}:")
    logging.info(f"Total events: {result.count}")
    
    # NFL season has 272 regular season games (17 games × 32 teams ÷ 2)
    # Plus preseason and playoffs
    assert result.count > 250, f"Expected more than 250 NFL events in a year, got {result.count}"
    
    # Save first page of response (full year might be huge)
    filename = f"events_{sport}_{league}_full_year_{year}.json"
    with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
        json.dump(result.to_dict() if hasattr(result, 'to_dict') else result.__dict__, f, indent=2)
    
    logging.info(f"✓ Saved response to {filename}")


@pytest.mark.api
@pytest.mark.parametrize("sport,league,dates,expected_min_events", [
    # Single dates during active seasons
    ("basketball", "nba", "20250301", 5),  # NBA games on a Saturday
    ("hockey", "nhl", "20250301", 5),      # NHL games on a Saturday
    ("baseball", "mlb", "20250701", 10),    # MLB games in July
    
    # Date ranges
    ("football", "college-football", "20250901-20250907", 50),  # Opening week
    ("basketball", "mens-college-basketball", "20250315-20250321", 20),  # March Madness
    
    # Full years
    ("football", "nfl", "2024", 250),       # Full NFL season
    ("basketball", "nba", "2024", 1000),    # Full NBA season (82 games × 30 teams ÷ 2)
])
def test_events_various_date_formats(
    sports_core_api_client, sport, league, dates, expected_min_events
):
    """Test events endpoint with various date formats across different sports."""
    response = get_league_events.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        dates=dates
    )
    
    # Some date ranges might not have events
    if response.status_code == 404:
        pytest.skip(f"No events found for {sport}/{league} on {dates}")
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    
    logging.info(f"\n{sport.upper()} ({league.upper()}) events for {dates}:")
    logging.info(f"  Found {result.count} events")
    
    # Check we got a reasonable number of events
    if result.count > 0:
        assert result.count >= expected_min_events, \
            f"Expected at least {expected_min_events} events, got {result.count}"


@pytest.mark.api
def test_events_date_range_pagination(sports_core_api_client):
    """Test that date range filtering works with pagination."""
    sport = "basketball"
    league = "nba"
    # A week in NBA season should have many games
    date_range = "20250301-20250307"
    
    # First request with limit
    response = get_league_events.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        dates=date_range,
        limit=10
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    
    # Should respect the limit
    if result.items:
        assert len(result.items) <= 10, "Should respect the limit parameter"
    
    # If there are more events, we should have multiple pages
    if result.count > 10:
        assert result.page_count > 1, "Should have multiple pages for large result sets"
    
    logging.info(f"\nPagination test for date range {date_range}:")
    logging.info(f"  Total events: {result.count}")
    logging.info(f"  Items on page: {len(result.items) if result.items else 0}")
    logging.info(f"  Total pages: {result.page_count}")


@pytest.mark.api
def test_events_invalid_date_format(sports_core_api_client):
    """Test events endpoint with invalid date format."""
    response = get_league_events.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        dates="invalid-date"
    )
    
    # API might return 400 for invalid format or 200 with no results
    assert response.status_code in [200, 400], \
        f"Expected status code 200 or 400 for invalid date, got {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        # Should return empty results for invalid date
        assert result.count == 0, "Should return no events for invalid date format"