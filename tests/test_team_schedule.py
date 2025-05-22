#!/usr/bin/env python3
"""
Test ESPN NFL API - Team Schedule Endpoint
"""

import json
import logging
import pytest

from models.site_api.espn_nfl_api_client.api.default.get_nfl_team_schedule import sync
from models.site_api.espn_nfl_api_client.models.nfl_team_schedule_response import (
    NFLTeamScheduleResponse,
)


@pytest.mark.api
def test_get_nfl_team_schedule(site_api_client, ensure_json_output_dir):
    """Test fetching an NFL team's schedule."""
    # Set up logging
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger(__name__)

    team_id = "12"  # Kansas City Chiefs
    logger.info(f"Fetching schedule for team ID: {team_id}")

    response = sync(team_id=team_id, client=site_api_client)
    logger.info(f"Received response for team: {team_id}")

    # Validate response type
    assert isinstance(response, NFLTeamScheduleResponse), (
        "Response should be an NFLTeamScheduleResponse"
    )

    # Validate required fields
    assert response.timestamp, "Response should have a timestamp"
    assert response.status, "Response should have a status"
    assert response.team, "Response should have team data"
    assert response.team.display_name, "Team should have a display name"
    assert response.season, "Response should have season data"
    assert response.season.year, "Season should have a year"
    assert response.events is not None, (
        "Response should have events list (even if empty)"
    )

    # Log useful information about the response
    logger.info(f"Response timestamp: {response.timestamp}")
    logger.info(f"Response status: {response.status}")
    logger.info(f"Team name: {response.team.display_name}")
    logger.info(f"Season year: {response.season.year}")
    logger.info(f"Total events: {len(response.events)} games")

    # Log details about the schedule
    home_games = 0
    away_games = 0
    completed_games = 0

    for event in response.events:
        if event.competitions and event.competitions[0].competitors:
            for competitor in event.competitions[0].competitors:
                if (
                    competitor.team
                    and competitor.team.id == team_id
                    and competitor.home_away == "home"
                ):
                    home_games += 1
                elif (
                    competitor.team
                    and competitor.team.id == team_id
                    and competitor.home_away == "away"
                ):
                    away_games += 1

        if (
            event.competitions
            and event.competitions[0].status
            and event.competitions[0].status.type
            and event.competitions[0].status.type.completed
        ):
            completed_games += 1

    logger.info(f"Home games: {home_games}")
    logger.info(f"Away games: {away_games}")
    logger.info(f"Completed games: {completed_games}")
    logger.info(f"Upcoming games: {len(response.events) - completed_games}")

    if response.events:
        logger.info(
            f"First event: {response.events[0].name} on {response.events[0].date}"
        )
        # Validate event structure for the first event
        first_event = response.events[0]
        assert first_event.id, "Event should have an ID"
        assert first_event.name, "Event should have a name"
        assert first_event.date, "Event should have a date"

        # Log information about the first event
        logger.info(f"First event ID: {first_event.id}")
        if first_event.competitions and first_event.competitions[0].venue:
            venue = first_event.competitions[0].venue
            venue_name = venue.full_name if venue.full_name else "Unknown"
            logger.info(f"First event venue: {venue_name}")

    if response.bye_week:
        logger.info(f"Bye week: {response.bye_week}")
    else:
        logger.info("No bye week information available")

    # Save the response data to a file without logging the content
    output_path = f"{ensure_json_output_dir}/nfl_team_schedule_response_processed.json"
    with open(output_path, "w") as f:
        json.dump(response.to_dict(), f, indent=2)

    logger.info(f"Schedule response saved to {output_path}")
