#!/usr/bin/env python3
"""
Test Soccer Teams using generic teams endpoint
"""

import pytest
import logging
from models.site_api.espn_nfl_api_client.api.default import get_teams_list
from models.site_api.espn_nfl_api_client.models.sport_enum import SportEnum

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize("league_slug", ["eng.1", "usa.1", "esp.1"])
def test_soccer_teams_generic(site_api_client, league_slug):
    """Test that soccer teams work with the generic teams endpoint."""
    response = get_teams_list.sync_detailed(
        client=site_api_client,
        sport=SportEnum.SOCCER,
        league=league_slug
    )
    
    assert response.status_code == 200
    result = response.parsed
    
    # Check structure
    assert hasattr(result, 'sports'), "Response should have sports"
    assert len(result.sports) > 0, "Should have at least one sport"
    
    sport = result.sports[0]
    assert sport.name == "Soccer", f"Sport name should be Soccer, got {sport.name}"
    
    # Check leagues
    assert hasattr(sport, 'leagues'), "Sport should have leagues"
    assert len(sport.leagues) > 0, "Should have at least one league"
    
    league = sport.leagues[0]
    assert hasattr(league, 'teams'), "League should have teams"
    assert len(league.teams) > 0, "League should have teams"
    
    logger.info(f"Soccer league {league_slug}: {league.name} - {len(league.teams)} teams")
    
    # Log first few teams
    for team_entry in league.teams[:5]:
        team = team_entry.team
        logger.info(f"  Team: {team.display_name} ({team.abbreviation})")