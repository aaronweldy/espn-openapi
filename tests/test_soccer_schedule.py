#!/usr/bin/env python3
"""
Test Soccer Team Schedule using generic schedule endpoint
"""

import pytest
import logging
from models.site_api.espn_nfl_api_client.api.default import get_team_schedule
from models.site_api.espn_nfl_api_client.models.team_schedule_response import TeamScheduleResponse
from models.site_api.espn_nfl_api_client.models.sport_enum import SportEnum

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize("league,team_id,team_name", [
    ("eng.1", "360", "Manchester United"),
    ("eng.1", "364", "Liverpool"),
    ("usa.1", "20232", "Inter Miami"),
])
def test_soccer_team_schedule_generic(site_api_client, league, team_id, team_name):
    """Test that soccer team schedules work with the generic team schedule endpoint."""
    response = get_team_schedule.sync_detailed(
        client=site_api_client,
        sport=SportEnum.SOCCER,
        league=league,
        team_id_or_abbrev=team_id
    )
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, TeamScheduleResponse), "Response should parse to TeamScheduleResponse"
    
    # Verify basic fields
    assert result.status == "success", "Status should be success"
    assert result.team, "Should have team information"
    assert result.events is not None, "Should have events (can be empty list)"
    
    logger.info(f"{team_name} Schedule:")
    logger.info(f"  Team: {result.team.display_name}")
    logger.info(f"  Number of matches: {len(result.events)}")
    
    # Log upcoming matches
    if result.events:
        upcoming = [e for e in result.events[:5]]
        for event in upcoming:
            if hasattr(event, 'name') and event.name:
                logger.info(f"  - {event.name}")
                if hasattr(event, 'date') and event.date:
                    logger.info(f"    Date: {event.date}")
                if hasattr(event, 'competitions') and event.competitions:
                    comp = event.competitions[0]
                    if hasattr(comp, 'venue') and comp.venue and hasattr(comp.venue, 'full_name'):
                        logger.info(f"    Venue: {comp.venue.full_name}")