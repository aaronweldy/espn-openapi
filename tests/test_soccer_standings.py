#!/usr/bin/env python3
"""
Test ESPN Soccer Standings Endpoint
"""

import json
import pytest
import logging

from models.site_api.espn_nfl_api_client.api.default import get_soccer_standings
from models.site_api.espn_nfl_api_client.models.soccer_standings_response import (
    SoccerStandingsResponse,
)
from models.site_api.espn_nfl_api_client.types import UNSET

# Set up logging
logger = logging.getLogger(__name__)


def validate_soccer_standings_response(data: SoccerStandingsResponse) -> None:
    """Validate if response matches expected schema structure using assertions."""
    logger.info("Validating soccer standings response structure")
    
    # Validate required fields
    assert data.id, "Missing id in response"
    assert data.name, "Missing name in response"
    assert data.abbreviation, "Missing abbreviation in response"
    assert data.children, "Missing children in response"
    
    logger.info(f"League: {data.name} ({data.abbreviation})")
    
    # Check children (standings groups)
    assert len(data.children) > 0, "Expected at least one standings group"
    logger.info(f"Found {len(data.children)} standings groups")
    
    for group in data.children:
        logger.info(f"Checking standings group: {group.name}")
        assert group.id, "Group should have an id"
        assert group.name, "Group should have a name"
        assert group.standings, "Group should have standings"
        
        standings = group.standings
        assert standings.entries, "Standings should have entries"
        logger.info(f"Found {len(standings.entries)} teams in {group.name}")
        
        # Check teams in standings
        for entry in standings.entries:
            assert entry.team, "Entry should have a team"
            assert entry.team.id, "Team should have an id"
            assert entry.team.display_name, "Team should have a display name"
            assert entry.stats, "Entry should have stats"
            
            # Check for common soccer stats
            stat_names = [stat.name for stat in entry.stats if stat.name]
            expected_stats = ["points", "wins", "losses", "ties", "gamesPlayed"]
            for stat in expected_stats:
                assert stat in stat_names, f"Missing expected stat: {stat}"
            
            logger.info(f"Validated team: {entry.team.display_name}")


def format_soccer_standings(data: SoccerStandingsResponse) -> str:
    """Format soccer standings for display."""
    output = []
    output.append(f"=== {data.name} Standings ===")
    
    for group in data.children:
        if group.standings and group.standings.entries:
            output.append(f"\n{group.name}")
            output.append("Pos  Team                     P   W   D   L   GF  GA  GD  Pts")
            output.append("-------------------------------------------------------------")
            
            for i, entry in enumerate(group.standings.entries, 1):
                if entry.team and entry.stats:
                    team_name = entry.team.display_name or entry.team.name
                    
                    # Extract stats
                    stats_dict = {}
                    for stat in entry.stats:
                        if stat.name and stat.value is not None and stat.value is not UNSET:
                            stats_dict[stat.name] = stat.value
                    
                    played = int(stats_dict.get("gamesPlayed", 0))
                    wins = int(stats_dict.get("wins", 0))
                    draws = int(stats_dict.get("ties", 0))
                    losses = int(stats_dict.get("losses", 0))
                    goals_for = int(stats_dict.get("pointsFor", 0))
                    goals_against = int(stats_dict.get("pointsAgainst", 0))
                    goal_diff = int(stats_dict.get("differential", 0))
                    points = int(stats_dict.get("points", 0))
                    
                    output.append(
                        f"{i:<4} {team_name:<25} {played:<3} {wins:<3} {draws:<3} {losses:<3} "
                        f"{goals_for:<3} {goals_against:<3} {goal_diff:>3} {points:>3}"
                    )
    
    return "\n".join(output)


@pytest.mark.api
@pytest.mark.parametrize("league,league_name", [
    ("eng.1", "English Premier League"),
    ("esp.1", "Spanish La Liga"),
    ("ger.1", "German Bundesliga"),
    ("ita.1", "Italian Serie A"),
    ("fra.1", "French Ligue 1"),
    ("uefa.champions", "UEFA Champions League"),
])
def test_soccer_standings(site_api_v2_client, ensure_json_output_dir, league, league_name):
    """Test fetching soccer standings for various leagues."""
    logger.info(f"Fetching {league_name} standings")
    
    response = get_soccer_standings.sync_detailed(
        client=site_api_v2_client,
        league=league
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Debug: Check what we actually got
    logger.info(f"Response content: {response.content}")
    if hasattr(response, 'json'):
        try:
            json_content = response.json()
            logger.info(f"Response JSON: {json_content}")
        except:
            pass
    
    standings_data = response.parsed
    assert isinstance(standings_data, SoccerStandingsResponse), (
        "Response should be a SoccerStandingsResponse"
    )
    
    try:
        # Validate schema
        logger.info("Validating response structure")
        validate_soccer_standings_response(standings_data)
        
        # Display formatted standings
        logger.info("Formatting standings for display")
        formatted_standings = format_soccer_standings(standings_data)
        print(f"\n{formatted_standings}")
        
        # Save response
        logger.info(f"Saving {league} standings to JSON file")
        with open(
            f"{ensure_json_output_dir}/soccer_{league.replace('.', '_')}_standings.json", "w"
        ) as f:
            json.dump(standings_data.to_dict(), f, indent=2)
        
        logger.info(f"Test completed successfully for {league_name}")
        
    except Exception as e:
        logger.error(f"Failed to parse {league_name} standings: {str(e)}")
        pytest.fail(f"Failed to parse {league_name} standings: {str(e)}")


@pytest.mark.api
def test_soccer_standings_with_season(site_api_v2_client, ensure_json_output_dir):
    """Test fetching soccer standings with specific season parameter."""
    league = "eng.1"
    season = 2023
    
    logger.info(f"Fetching {league} standings for season {season}")
    
    response = get_soccer_standings.sync_detailed(
        client=site_api_v2_client,
        league=league,
        season=season
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    standings_data = response.parsed
    assert isinstance(standings_data, SoccerStandingsResponse), (
        "Response should be a SoccerStandingsResponse"
    )
    
    # Verify it's showing the correct season
    if standings_data.children and standings_data.children[0].standings:
        standings = standings_data.children[0].standings
        if standings.season:
            assert standings.season == season, f"Expected season {season}, got {standings.season}"
    
    logger.info("Season parameter test completed successfully")


@pytest.mark.api
def test_soccer_standings_invalid_league(site_api_v2_client):
    """Test fetching standings with invalid league."""
    invalid_league = "invalid.league"
    
    logger.info(f"Testing invalid league: {invalid_league}")
    
    response = get_soccer_standings.sync_detailed(
        client=site_api_v2_client,
        league=invalid_league
    )
    
    # ESPN API typically returns 400 for invalid resources
    assert response.status_code in [400, 404], (
        f"Expected status code 400 or 404 for invalid league, got {response.status_code}"
    )
    
    logger.info("Invalid league test completed successfully")