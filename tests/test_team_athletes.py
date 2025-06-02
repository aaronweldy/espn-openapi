#!/usr/bin/env python3
"""
Test ESPN Team Athletes API
"""

import pytest
import json
import logging

from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_team_athletes,
)

logging.basicConfig(level=logging.INFO)


@pytest.mark.api
def test_get_team_athletes_soccer(sports_core_api_client, ensure_json_output_dir):
    """Test fetching team athletes for soccer."""
    sport = "soccer"
    league = "eng.1"
    year = "2024"
    team_id = "359"  # Manchester United
    
    response = get_team_athletes.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=year,
        team_id=team_id,
        active=True
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
    
    logging.info(f"\nTeam Athletes for {sport.upper()} {league.upper()}:")
    logging.info(f"Team: {team_id}, Year: {year}")
    logging.info(f"Total active athletes: {result.count}")
    logging.info(f"Pages: {result.page_count}")
    
    # Log some athlete references
    if result.items:
        logging.info("\nFirst few athlete references:")
        for i, athlete_ref in enumerate(result.items[:5]):
            if hasattr(athlete_ref, 'ref'):
                # Extract athlete ID from the reference URL
                athlete_id = athlete_ref.ref.split('/athletes/')[-1].split('?')[0]
                logging.info(f"  {i+1}. Athlete ID: {athlete_id}")
    
    # Save response
    filename = f"team_athletes_{sport}_{league}_{year}_team{team_id}.json"
    with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
        json.dump(result.to_dict() if hasattr(result, 'to_dict') else result.__dict__, f, indent=2)
    
    logging.info(f"\n✓ Saved response to {filename}")


@pytest.mark.api
@pytest.mark.parametrize("sport,league,year,team_id,expected_min_count", [
    # Soccer - English Premier League
    ("soccer", "eng.1", "2024", "359", 20),  # Manchester United
    ("soccer", "eng.1", "2024", "364", 20),  # Liverpool
    
    # NFL
    ("football", "nfl", "2024", "12", 50),  # Kansas City Chiefs
    ("football", "nfl", "2024", "1", 50),    # Atlanta Falcons
    
    # NBA
    ("basketball", "nba", "2024", "13", 15),  # Lakers
    ("basketball", "nba", "2024", "2", 15),   # Boston Celtics
    
    # NHL
    ("hockey", "nhl", "2024", "10", 20),  # Toronto Maple Leafs
    
    # MLB
    ("baseball", "mlb", "2024", "10", 25),  # New York Yankees
])
def test_get_team_athletes_multiple_sports(
    sports_core_api_client, sport, league, year, team_id, expected_min_count, ensure_json_output_dir
):
    """Test team athletes across different sports."""
    response = get_team_athletes.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=year,
        team_id=team_id,
        active=True  # Get only active athletes
    )
    
    # Team might not exist or have no data
    if response.status_code == 404:
        pytest.skip(f"Team athletes not available for {sport}/{league} team {team_id}")
    
    # Some endpoints return 500 errors (API issues)
    if response.status_code == 500:
        pytest.skip(f"API error (500) for {sport}/{league} team {team_id}")
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    
    logging.info(f"\n{sport.upper()} ({league.upper()}) Team Athletes:")
    logging.info(f"  Team: {team_id}, Year: {year}")
    logging.info(f"  Active athletes: {result.count}")
    
    # Most teams should have at least some minimum number of active players
    if result.count > 0:
        assert result.count >= expected_min_count, f"Expected at least {expected_min_count} athletes, got {result.count}"
    
    # Check pagination is working
    if result.count > result.page_size:
        assert result.page_count > 1, "Should have multiple pages for large rosters"


@pytest.mark.api
def test_team_athletes_pagination(sports_core_api_client):
    """Test pagination of team athletes."""
    response_page1 = get_team_athletes.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        year="2024",
        team_id="12",  # Kansas City Chiefs
        active=True,
        limit=10  # Small page size
    )
    
    assert response_page1.status_code == 200, f"Expected status code 200, got {response_page1.status_code}"
    
    result1 = response_page1.parsed
    assert result1, "Response should parse successfully"
    
    # Check pagination
    assert result1.page_size <= 10, "Page size should respect limit"
    if result1.count > 10:
        assert result1.page_count > 1, "Should have multiple pages"
        
        # Try to get page 2
        response_page2 = get_team_athletes.sync_detailed(
            client=sports_core_api_client,
            sport="football",
            league="nfl",
            year="2024",
            team_id="12",
            active=True,
            page_index=2,
            limit=10
        )
        
        if response_page2.status_code == 200:
            result2 = response_page2.parsed
            assert result2.page_index == 2, "Should be on page 2"
            
            # Ensure different athletes on different pages
            if result1.items and result2.items:
                page1_refs = {item.ref for item in result1.items if hasattr(item, 'ref')}
                page2_refs = {item.ref for item in result2.items if hasattr(item, 'ref')}
                assert len(page1_refs & page2_refs) == 0, "Pages should have different athletes"


@pytest.mark.api
def test_team_athletes_inactive_filter(sports_core_api_client):
    """Test fetching all athletes (including inactive) vs only active."""
    # Get active athletes
    response_active = get_team_athletes.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        year="2024",
        team_id="12",
        active=True
    )
    
    # Get all athletes (no active filter)
    response_all = get_team_athletes.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        year="2024",
        team_id="12"
        # No active parameter
    )
    
    if response_active.status_code == 200 and response_all.status_code == 200:
        active_count = response_active.parsed.count
        all_count = response_all.parsed.count
        
        logging.info(f"\nActive filter test:")
        logging.info(f"  Active athletes: {active_count}")
        logging.info(f"  All athletes: {all_count}")
        
        # All athletes should be >= active athletes
        assert all_count >= active_count, "Total athletes should be >= active athletes"


@pytest.mark.api
def test_team_athletes_invalid_team(sports_core_api_client):
    """Test team athletes with invalid team ID."""
    response = get_team_athletes.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        year="2024",
        team_id="99999",  # Invalid team
        active=True
    )
    
    # Should return 404 or empty results
    assert response.status_code in [404, 200], f"Expected 404 or 200, got {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        assert result.count == 0, "Should return no athletes for invalid team"