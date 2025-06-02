#!/usr/bin/env python3
"""
Test ESPN College Softball Scoreboard API
"""

import pytest
import json
import logging

from models.site_api.espn_nfl_api_client.api.default import (
    get_scoreboard,
)

logging.basicConfig(level=logging.INFO)


@pytest.mark.api
def test_college_softball_scoreboard(site_api_client, ensure_json_output_dir):
    """Test college softball scoreboard endpoint."""
    sport = "baseball"  # Softball is under baseball sport
    league = "college-softball"
    
    response = get_scoreboard.sync_detailed(
        client=site_api_client,
        sport=sport,
        league=league
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    
    # Check basic structure
    assert hasattr(result, 'leagues'), "Response should have leagues"
    assert hasattr(result, 'events'), "Response should have events"
    
    if result.leagues:
        league_info = result.leagues[0]
        assert hasattr(league_info, 'name'), "League should have name"
        assert hasattr(league_info, 'slug'), "League should have slug"
        
        logging.info(f"\nCollege Softball Scoreboard:")
        logging.info(f"League: {league_info.name} ({league_info.slug})")
        
        if hasattr(league_info, 'season') and league_info.season:
            logging.info(f"Season: {league_info.season.year} ({league_info.season.display_name})")
    
    # Check events
    if result.events:
        logging.info(f"Found {len(result.events)} events")
        
        # Log details of first event
        first_event = result.events[0]
        if hasattr(first_event, 'name') and first_event.name:
            logging.info(f"First event: {first_event.name}")
        
        if hasattr(first_event, 'competitions') and first_event.competitions:
            competition = first_event.competitions[0]
            if hasattr(competition, 'competitors') and competition.competitors:
                logging.info(f"Teams: {len(competition.competitors)} competitors")
                
                for i, competitor in enumerate(competition.competitors[:2]):
                    if hasattr(competitor, 'team') and competitor.team:
                        team_name = competitor.team.display_name if hasattr(competitor.team, 'display_name') else "Unknown"
                        score = competitor.score if hasattr(competitor, 'score') else "N/A"
                        logging.info(f"  Team {i+1}: {team_name} - {score}")
    else:
        logging.info("No events found (possibly off-season)")
    
    # Save response
    filename = f"college_softball_scoreboard_test.json"
    with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
        json.dump(result.to_dict() if hasattr(result, 'to_dict') else result.__dict__, f, indent=2)
    
    logging.info(f"✓ Saved response to {filename}")


@pytest.mark.api
def test_college_softball_scoreboard_with_date(site_api_client, ensure_json_output_dir):
    """Test college softball scoreboard with specific date."""
    sport = "baseball"
    league = "college-softball"
    # Use a date during college softball season (spring/early summer)
    test_date = "20250601"  # June 1st - World Series time
    
    response = get_scoreboard.sync_detailed(
        client=site_api_client,
        sport=sport,
        league=league,
        dates=test_date
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    
    logging.info(f"\nCollege Softball Scoreboard for {test_date}:")
    
    if result.events:
        logging.info(f"Found {len(result.events)} events on {test_date}")
        
        # Check that events are related to the specified date
        if hasattr(result, 'day') and result.day:
            if hasattr(result.day, 'date') and result.day.date:
                logging.info(f"Day filter: {result.day.date}")
    else:
        logging.info(f"No events on {test_date}")
    
    # Save response
    filename = f"college_softball_scoreboard_{test_date}.json"
    with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
        json.dump(result.to_dict() if hasattr(result, 'to_dict') else result.__dict__, f, indent=2)
    
    logging.info(f"✓ Saved response to {filename}")


@pytest.mark.api
def test_college_softball_season_info(site_api_client):
    """Test that we can get season information for college softball."""
    sport = "baseball"
    league = "college-softball"
    
    response = get_scoreboard.sync_detailed(
        client=site_api_client,
        sport=sport,
        league=league
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    
    # Verify we got league info
    assert result.leagues, "Should have league information"
    
    league_info = result.leagues[0]
    assert hasattr(league_info, 'slug'), "League should have slug"
    assert league_info.slug == "college-softball", f"Expected college-softball, got {league_info.slug}"
    
    # Check season information
    if hasattr(league_info, 'season') and league_info.season:
        logging.info(f"\nCollege Softball Season Info:")
        logging.info(f"  Year: {league_info.season.year}")
        if hasattr(league_info.season, 'display_name'):
            logging.info(f"  Display Name: {league_info.season.display_name}")
        if hasattr(league_info.season, 'start_date'):
            logging.info(f"  Start Date: {league_info.season.start_date}")
        if hasattr(league_info.season, 'end_date'):
            logging.info(f"  End Date: {league_info.season.end_date}")
    
    logging.info("✓ College softball season info retrieved successfully")


@pytest.mark.api
def test_college_softball_invalid_date(site_api_client):
    """Test college softball scoreboard with invalid date format."""
    sport = "baseball"
    league = "college-softball"
    
    response = get_scoreboard.sync_detailed(
        client=site_api_client,
        sport=sport,
        league=league,
        dates="invalid-date"
    )
    
    # Should handle gracefully - either 400 or 200 with no events
    assert response.status_code in [200, 400], f"Expected 200 or 400, got {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        # Should return no events for invalid date
        assert not result.events or len(result.events) == 0, "Should return no events for invalid date"
    
    logging.info("✓ Invalid date handled gracefully")