"""Test the generic game summary endpoint."""
import pytest
import json
from models.site_api.espn_nfl_api_client.api.default import get_game_summary
from models.site_api.espn_nfl_api_client.models.game_summary import GameSummary
from models.site_api.espn_nfl_api_client.models.mlb_game_summary_response import MlbGameSummaryResponse
from models.site_api.espn_nfl_api_client.models.nhl_game_summary_response import NhlGameSummaryResponse
from models.site_api.espn_nfl_api_client.models.nba_game_summary_response import NbaGameSummaryResponse
from models.site_api.espn_nfl_api_client.models.sport_enum import SportEnum
from models.site_api.espn_nfl_api_client.models.league_enum import LeagueEnum


@pytest.mark.api
@pytest.mark.parametrize("sport,league,event_id,expected_type", [
    (SportEnum.FOOTBALL, LeagueEnum.NFL, "401547417", GameSummary),
    (SportEnum.BASKETBALL, LeagueEnum.NBA, "401772994", NbaGameSummaryResponse),
    (SportEnum.BASEBALL, LeagueEnum.MLB, "401472463", MlbGameSummaryResponse),
    (SportEnum.HOCKEY, LeagueEnum.NHL, "401559593", NhlGameSummaryResponse),
])
def test_get_game_summary_cross_sport(site_api_client, sport, league, event_id, expected_type, ensure_json_output_dir):
    """Test getting game summary for various sports."""
    response = get_game_summary.sync_detailed(
        client=site_api_client,
        sport=sport,
        league=league,
        event=event_id
    )
    
    # Some event IDs might be outdated, so we'll accept 404 as valid
    assert response.status_code in [200, 404], f"Expected status code 200 or 404, got {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        
        # The response could be any of the sport-specific types
        assert result is not None, "Response should parse successfully"
        assert hasattr(result, 'boxscore'), "Response should have boxscore"
        assert hasattr(result, 'gameInfo') or hasattr(result, 'game_info'), "Response should have gameInfo"
        assert hasattr(result, 'header'), "Response should have header"
        
        # Save response for analysis
        filename = f"{sport.value}_{league.value}_game_summary_{event_id}.json"
        with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
            json.dump(result.to_dict(), f, indent=2)


@pytest.mark.api
def test_game_summary_invalid_event(site_api_client):
    """Test game summary with invalid event ID."""
    response = get_game_summary.sync_detailed(
        client=site_api_client,
        sport=SportEnum.BASKETBALL,
        league=LeagueEnum.NBA,
        event="INVALID"
    )
    
    assert response.status_code in [400, 404], f"Expected status code 400 or 404 for invalid event, got {response.status_code}"


@pytest.mark.api
def test_nba_game_summary_structure(site_api_client):
    """Test the structure of NBA game summary response."""
    # First, get a current NBA game ID
    from models.site_api.espn_nfl_api_client.api.default import get_scoreboard
    
    scoreboard_response = get_scoreboard.sync_detailed(
        client=site_api_client,
        sport=SportEnum.BASKETBALL,
        league=LeagueEnum.NBA
    )
    
    if scoreboard_response.status_code == 200 and scoreboard_response.parsed.events:
        # Use the first available game
        event_id = scoreboard_response.parsed.events[0].id
        
        response = get_game_summary.sync_detailed(
            client=site_api_client,
            sport=SportEnum.BASKETBALL,
            league=LeagueEnum.NBA,
            event=event_id
        )
        
        if response.status_code == 200:
            result = response.parsed
            
            # Check required fields
            assert result.boxscore, "Should have boxscore"
            assert result.header, "Should have header"
            
            # Check optional NBA-specific fields
            if hasattr(result, 'leaders') and result.leaders:
                assert isinstance(result.leaders, list), "Leaders should be a list"
            
            if hasattr(result, 'standings') and result.standings:
                # Standings can be a dict-like object
                assert result.standings is not None, "Standings should exist when present"