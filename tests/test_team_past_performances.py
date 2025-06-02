#!/usr/bin/env python3
"""
Test ESPN Team Past Performances API
"""

import pytest
import json
import logging
from datetime import datetime

from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_team_past_performances,
)

logging.basicConfig(level=logging.INFO)


@pytest.mark.api
def test_get_team_past_performances_nfl(sports_core_api_client, ensure_json_output_dir):
    """Test fetching team past performances vs odds."""
    sport = "football"
    league = "nfl"
    team_id = "8"  # Denver Broncos
    provider_id = "1002"
    
    response = get_team_past_performances.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        team_id=team_id,
        provider_id=provider_id,
        limit=140
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    
    # Check pagination info
    assert hasattr(result, 'count'), "Result should have count"
    assert hasattr(result, 'page_index'), "Result should have page_index"
    assert hasattr(result, 'page_size'), "Result should have page_size"
    assert hasattr(result, 'page_count'), "Result should have page_count"
    assert hasattr(result, 'items'), "Result should have items"
    
    logging.info(f"Team Past Performances: {result.count} total performances")
    logging.info(f"Page {result.page_index} of {result.page_count}")
    
    # Check items structure
    if result.items:
        item = result.items[0]
        assert hasattr(item, 'spread'), "Performance should have spread"
        assert hasattr(item, 'line_date'), "Performance should have line_date"
        assert hasattr(item, 'moneyline_winner'), "Performance should have moneyline_winner"
        assert hasattr(item, 'spread_winner'), "Performance should have spread_winner"
        assert hasattr(item, 'past_competition'), "Performance should have past_competition"
        
        # Log sample performance
        logging.info(f"\nSample Performance:")
        logging.info(f"  Date: {item.line_date}")
        logging.info(f"  Spread: {item.spread}")
        logging.info(f"  Money Line Odds: {getattr(item, 'money_line_odds', 'N/A')}")
        logging.info(f"  Moneyline Winner: {item.moneyline_winner}")
        logging.info(f"  Spread Winner: {item.spread_winner}")
        if hasattr(item, 'total_line'):
            logging.info(f"  Total Line: {item.total_line}")
        if hasattr(item, 'total_result'):
            logging.info(f"  Total Result: {item.total_result}")
    
    # Save response
    with open(f"{ensure_json_output_dir}/team_past_performances_{league}_{team_id}_provider_{provider_id}.json", "w") as f:
        json.dump(result.to_dict() if hasattr(result, 'to_dict') else result.__dict__, f, indent=2)
    
    logging.info(f"\n✓ Saved response to json_output/")


@pytest.mark.api
@pytest.mark.parametrize("sport,league,team_id,provider_id", [
    ("football", "nfl", "12", "58"),  # Kansas City Chiefs with Caesars
    ("basketball", "nba", "13", "58"),  # LA Lakers with Caesars
    ("baseball", "mlb", "15", "58"),  # Colorado Rockies with Caesars
])
def test_get_team_past_performances_multiple_sports(sports_core_api_client, sport, league, team_id, provider_id, ensure_json_output_dir):
    """Test fetching team past performances across multiple sports."""
    response = get_team_past_performances.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        team_id=team_id,
        provider_id=provider_id,
        limit=50
    )
    
    # Some sport/provider combinations might not be available
    if response.status_code == 404:
        pytest.skip(f"Past performances not available for {sport}/{league} team {team_id} with provider {provider_id}")
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    
    logging.info(f"\n{sport.upper()} ({league.upper()}) Team {team_id} Past Performances:")
    logging.info(f"  Provider: {provider_id}")
    logging.info(f"  Total performances: {getattr(result, 'count', 0)}")
    
    if hasattr(result, 'items') and result.items:
        recent_perf = result.items[0]
        logging.info(f"  Most recent performance date: {getattr(recent_perf, 'line_date', 'N/A')}")