#!/usr/bin/env python3
"""
Test generic scoreboard endpoint across all sports.
"""

import pytest
import json
import logging
from datetime import datetime
from models.site_api.espn_nfl_api_client.api.default import get_scoreboard
from models.site_api.espn_nfl_api_client.models.generic_scoreboard_response import GenericScoreboardResponse
from models.site_api.espn_nfl_api_client.models.get_scoreboard_seasontype import GetScoreboardSeasontype
from models.site_api.espn_nfl_api_client.models.get_scoreboard_sport import GetScoreboardSport
from models.site_api.espn_nfl_api_client.types import UNSET

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize("sport,sport_enum,league,has_week,has_day", [
    ("football", GetScoreboardSport.FOOTBALL, "nfl", True, False),
    ("baseball", GetScoreboardSport.BASEBALL, "mlb", False, True),
    ("basketball", GetScoreboardSport.BASKETBALL, "nba", False, True),
    ("hockey", GetScoreboardSport.HOCKEY, "nhl", False, False),
])
def test_get_scoreboard(site_api_client, ensure_json_output_dir, sport, sport_enum, league, has_week, has_day):
    """Test the generic scoreboard endpoint for different sports."""
    today = datetime.now().strftime("%Y%m%d")
    
    # Call the generic endpoint
    response = get_scoreboard.sync_detailed(
        client=site_api_client,
        sport=sport_enum,
        league=league,
        dates=today
    )
    
    assert response.status_code == 200, f"Expected status code 200 for {sport}/{league}, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, GenericScoreboardResponse), f"Response should parse to GenericScoreboardResponse for {sport}/{league}"
    
    # Common validations
    assert result.leagues, f"{sport}/{league} should have leagues"
    assert len(result.leagues) > 0, f"{sport}/{league} should have at least one league"
    
    league_obj = result.leagues[0]
    assert league_obj.name, f"{sport}/{league} league should have a name"
    
    # Sport-specific validations
    if has_week and result.week is not UNSET:
        week_num = result.week.number if hasattr(result.week, 'number') else 'N/A'
        logger.info(f"{sport}/{league} - Week: {week_num}")
    
    if has_day and result.day is not UNSET:
        day_date = result.day.date if hasattr(result.day, 'date') else 'N/A'
        logger.info(f"{sport}/{league} - Day: {day_date}")
    
    # Check events
    if result.events:
        logger.info(f"{sport}/{league} - Found {len(result.events)} games")
        
        # Log first 3 games
        for event in result.events[:3]:
            if event.name:
                logger.info(f"  Game: {event.name}")
            
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
                        logger.info(f"    Scores: {' - '.join(scores)}")
                    
                    # Check status
                    if comp.status and comp.status.type:
                        status_desc = comp.status.type.description or "Unknown"
                        logger.info(f"    Status: {status_desc}")
    else:
        logger.info(f"{sport}/{league} - No games scheduled for {today}")
    
    # Save the response
    filename = f"{league}_scoreboard_generic.json"
    with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    logger.info(f"✓ {sport}/{league} scoreboard saved to {filename}")


@pytest.mark.api
def test_get_nfl_scoreboard_with_week(site_api_client, ensure_json_output_dir):
    """Test NFL scoreboard with week parameter."""
    response = get_scoreboard.sync_detailed(
        client=site_api_client,
        sport=GetScoreboardSport.FOOTBALL,
        league="nfl",
        week=1,
        seasontype=GetScoreboardSeasontype.VALUE_2  # Regular season
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, GenericScoreboardResponse), "Response should parse to GenericScoreboardResponse"
    
    # NFL should have week info
    assert result.week, "NFL scoreboard should have week information"
    assert result.season, "NFL scoreboard should have season information"
    
    logger.info(f"NFL Week {result.week.number if result.week else 'N/A'} - "
                f"Found {len(result.events) if result.events else 0} games")


@pytest.mark.api
@pytest.mark.parametrize("sport,sport_enum,league", [
    ("football", GetScoreboardSport.FOOTBALL, "college-football"),
    ("basketball", GetScoreboardSport.BASKETBALL, "mens-college-basketball"),
    ("basketball", GetScoreboardSport.BASKETBALL, "womens-college-basketball"),
    ("basketball", GetScoreboardSport.BASKETBALL, "wnba"),
])
def test_get_other_sports_scoreboard(site_api_client, sport, sport_enum, league):
    """Test scoreboard for other sports/leagues."""
    response = get_scoreboard.sync_detailed(
        client=site_api_client,
        sport=sport_enum,
        league=league
    )
    
    assert response.status_code == 200, f"Expected status code 200 for {sport}/{league}, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, GenericScoreboardResponse), f"Response should parse to GenericScoreboardResponse for {sport}/{league}"
    
    logger.info(f"{sport}/{league} - Found {len(result.events) if result.events else 0} games")