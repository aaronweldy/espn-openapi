#!/usr/bin/env python3
"""
Test ESPN Power Index API
"""

import pytest
import json
import logging

from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_competition_powerindex,
)

logging.basicConfig(level=logging.INFO)


@pytest.mark.api
def test_get_competition_powerindex_nfl(sports_core_api_client, ensure_json_output_dir):
    """Test fetching power index data for NFL games."""
    sport = "football"
    league = "nfl"
    event_id = "401437954"
    competition_id = "401437954"
    team_id = "30"  # Jacksonville Jaguars
    
    response = get_competition_powerindex.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        team_id=team_id
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    
    # Check structure
    assert hasattr(result, 'team'), "Result should have team reference"
    assert hasattr(result, 'season'), "Result should have season"
    assert hasattr(result, 'stats'), "Result should have stats"
    
    logging.info(f"\nPower Index for {sport.upper()} {league.upper()} Event {event_id}, Team {team_id}:")
    logging.info(f"Season: {result.season}")
    
    # Log stats
    if result.stats:
        logging.info("\nPower Index Stats:")
        for stat in result.stats:
            if hasattr(stat, 'display_name') and hasattr(stat, 'display_value'):
                logging.info(f"  {stat.display_name}: {stat.display_value}")
                if hasattr(stat, 'description'):
                    logging.info(f"    Description: {stat.description}")
    
    # Save response
    filename = f"powerindex_{sport}_{league}_event_{event_id}_team_{team_id}.json"
    with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
        json.dump(result.to_dict() if hasattr(result, 'to_dict') else result.__dict__, f, indent=2)
    
    logging.info(f"\n✓ Saved response to {filename}")


@pytest.mark.api
@pytest.mark.parametrize("sport,league,event_id,team_id", [
    # Pro Football
    ("football", "nfl", "401547602", "12"),  # Kansas City Chiefs
    ("football", "nfl", "401437954", "30"),  # Jacksonville Jaguars (known working)
    
    # Pro Basketball
    ("basketball", "nba", "401584793", "13"),  # LA Lakers
    ("basketball", "wnba", "401577566", "5"),  # Phoenix Mercury
    
    # College Sports
    ("football", "college-football", "401525517", "333"),  # Alabama
    ("basketball", "mens-college-basketball", "401524202", "150"),  # Duke
    ("basketball", "womens-college-basketball", "401524812", "52"),  # South Carolina
    
    # Baseball
    ("baseball", "mlb", "401472463", "10"),  # Yankees
    ("baseball", "college-baseball", "401514749", "236"),  # LSU
    
    # Hockey
    ("hockey", "nhl", "401559593", "10"),  # Toronto Maple Leafs
    
    # Soccer
    ("soccer", "mls", "401453140", "360"),  # LA Galaxy
    ("soccer", "eng.1", "401547845", "364"),  # Manchester United
    ("soccer", "uefa.champions", "401449051", "86"),  # Real Madrid
    
    # Other Sports
    ("golf", "pga", "401465533", "1810"),  # Scottie Scheffler
    ("racing", "f1", "401439649", "5502"),  # Red Bull Racing
    ("tennis", "atp", "401450810", "1972"),  # Carlos Alcaraz
])
def test_get_competition_powerindex_multiple_sports(
    sports_core_api_client, sport, league, event_id, team_id, ensure_json_output_dir
):
    """Test power index across different sports."""
    response = get_competition_powerindex.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=event_id,  # Usually same as event_id
        team_id=team_id
    )
    
    # Power index might not be available for all sports/events
    if response.status_code == 404:
        pytest.skip(f"Power index not available for {sport}/{league} event {event_id}")
    
    # Some endpoints return 500 errors (API issues)
    if response.status_code == 500:
        pytest.skip(f"API error (500) for {sport}/{league} event {event_id}")
    
    # Some sport/league combinations are not valid
    if response.status_code == 400:
        error_msg = "Unknown error"
        if response.parsed and hasattr(response.parsed, 'error') and hasattr(response.parsed.error, 'message'):
            error_msg = response.parsed.error.message
        pytest.skip(f"Invalid request for {sport}/{league}: {error_msg}")
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    
    logging.info(f"\n{sport.upper()} ({league.upper()}) Power Index:")
    logging.info(f"  Event: {event_id}, Team: {team_id}")
    logging.info(f"  Season: {getattr(result, 'season', 'N/A')}")
    
    # Find win probability stat
    if hasattr(result, 'stats') and result.stats:
        for stat in result.stats:
            if hasattr(stat, 'name') and stat.name == 'gameprojection':
                logging.info(f"  Win Probability: {getattr(stat, 'display_value', 'N/A')}")
                break


@pytest.mark.api
def test_powerindex_invalid_team(sports_core_api_client):
    """Test power index with invalid team ID."""
    response = get_competition_powerindex.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        event_id="401437954",
        competition_id="401437954",
        team_id="99999"  # Invalid team
    )
    
    assert response.status_code == 404, f"Expected 404 for invalid team, got {response.status_code}"