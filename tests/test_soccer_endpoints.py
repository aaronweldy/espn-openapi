#!/usr/bin/env python3
"""
Test ESPN API - Soccer Endpoints
"""

import json
import pytest
import logging
from datetime import datetime

from models.site_api.espn_nfl_api_client.api.default import get_scoreboard
from models.site_api.espn_nfl_api_client.models.generic_scoreboard_response import (
    GenericScoreboardResponse,
)
from models.site_api.espn_nfl_api_client.models.get_scoreboard_sport import (
    GetScoreboardSport,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize(
    "league_slug,league_name",
    [
        ("eng.1", "English Premier League"),
        ("usa.1", "MLS"),
        ("uefa.champions", "UEFA Champions League"),
        ("esp.1", "Spanish La Liga"),
        ("ger.1", "German Bundesliga"),
        ("ita.1", "Italian Serie A"),
        ("fra.1", "French Ligue 1"),
    ],
)
def test_soccer_scoreboard_generic(site_api_client, ensure_json_output_dir, league_slug, league_name):
    """Test that soccer leagues work with the generic scoreboard endpoint."""
    today = datetime.now().strftime("%Y%m%d")
    
    # Call the generic endpoint
    response = get_scoreboard.sync_detailed(
        client=site_api_client, 
        sport=GetScoreboardSport.SOCCER, 
        league=league_slug,
        dates=today
    )
    
    assert response.status_code == 200, (
        f"Expected status code 200 for soccer/{league_slug}, got {response.status_code}"
    )
    
    result = response.parsed
    assert isinstance(result, GenericScoreboardResponse), (
        f"Response should parse to GenericScoreboardResponse for soccer/{league_slug}"
    )
    
    # Validate structure
    assert result.leagues, f"soccer/{league_slug} should have leagues"
    assert len(result.leagues) > 0, f"soccer/{league_slug} should have at least one league"
    
    league_obj = result.leagues[0]
    assert league_obj.name, f"soccer/{league_slug} league should have a name"
    
    # Log league info
    logger.info(f"Soccer League: {league_obj.name} ({league_slug})")
    
    # Check for season
    if result.season:
        logger.info(f"Season: {result.season.year} (Type: {result.season.type})")
    
    # Check events
    if result.events:
        logger.info(f"Found {len(result.events)} matches for {league_name}")
        
        # Log first 3 matches
        for event in result.events[:3]:
            if event.name:
                logger.info(f"  Match: {event.name}")
            
            if event.competitions:
                comp = event.competitions[0]
                if comp.competitors:
                    teams = []
                    scores = []
                    for c in comp.competitors:
                        if c.team and c.team.display_name:
                            teams.append(c.team.display_name)
                            scores.append(str(c.score) if c.score else "0")
                    
                    if teams:
                        logger.info(f"    Teams: {' vs '.join(teams)}")
                        logger.info(f"    Score: {' - '.join(scores)}")
                    
                    # Check status
                    if comp.status and comp.status.type:
                        status_desc = comp.status.type.description or "Unknown"
                        logger.info(f"    Status: {status_desc}")
    else:
        logger.info(f"No matches scheduled for {league_name} on {today}")
    
    # Save the response for one league as example
    if league_slug == "eng.1":
        filename = f"soccer_{league_slug.replace('.', '_')}_scoreboard_processed.json"
        with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
        logger.info(f"✓ Soccer scoreboard saved to {filename}")


@pytest.mark.api
def test_soccer_scoreboard_with_date_range(site_api_client):
    """Test soccer scoreboard with date range."""
    # Use a date range for more matches
    date_range = "20241201-20241207"
    
    response = get_scoreboard.sync_detailed(
        client=site_api_client,
        sport=GetScoreboardSport.SOCCER,
        league="eng.1",
        dates=date_range
    )
    
    assert response.status_code == 200
    result = response.parsed
    assert isinstance(result, GenericScoreboardResponse)
    
    # With a date range, we should have multiple matches
    if result.events:
        logger.info(f"Premier League matches from {date_range}: {len(result.events)} matches")
        
        # Group by date
        matches_by_date = {}
        for event in result.events:
            if event.date:
                # Handle both string and datetime objects
                if hasattr(event.date, 'strftime'):
                    date_str = event.date.strftime('%Y-%m-%d')
                else:
                    date_str = str(event.date).split('T')[0]
                if date_str not in matches_by_date:
                    matches_by_date[date_str] = []
                matches_by_date[date_str].append(event.name or "Unknown match")
        
        # Log matches by date
        for date, matches in sorted(matches_by_date.items()):
            logger.info(f"  {date}: {len(matches)} matches")