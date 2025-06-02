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
    # Pro Football - valid future events
    ("football", "nfl", "401772510", "21"),  # Philadelphia Eagles (Sept 2025)
    ("football", "nfl", "401772510", "6"),   # Dallas Cowboys
    ("football", "nfl", "401437954", "30"),  # Jacksonville Jaguars (known working from 2022)
    
    # Pro Basketball - valid future events
    ("basketball", "nba", "401766122", "25"),  # Oklahoma City Thunder (June 2025 Finals)
    ("basketball", "nba", "401766122", "11"),  # Indiana Pacers
    ("basketball", "wnba", "401736152", "9"),  # New York Liberty (June 2025)
    
    # College Sports - valid future events
    ("football", "college-football", "401756846", "2306"),  # Kansas State (Aug 2025)
    ("football", "college-football", "401756846", "66"),    # Iowa State
    ("basketball", "mens-college-basketball", "401746082", "248"),  # Houston (April 2025 Championship)
    ("basketball", "mens-college-basketball", "401746082", "57"),   # Florida
    
    # Baseball - valid current event
    ("baseball", "mlb", "401695789", "13"),  # Texas Rangers (June 2025)
    ("baseball", "mlb", "401695789", "24"),  # St. Louis Cardinals
    
    # Hockey - valid future event
    ("hockey", "nhl", "401777455", "6"),   # Edmonton Oilers (June 2025 Finals)
    ("hockey", "nhl", "401777455", "26"),  # Florida Panthers
    
    # Soccer - valid current event
    ("soccer", "usa.1", "727049", "9726"),    # Seattle Sounders (MLS - June 2025)
    ("soccer", "usa.1", "727049", "17362"),   # Minnesota United
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