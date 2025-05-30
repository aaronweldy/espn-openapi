import pytest
import json
from models.site_api.espn_nfl_api_client.api.default import get_nhl_game_summary
from models.site_api.espn_nfl_api_client.models.nhl_game_summary_response import NhlGameSummaryResponse
from models.site_api.espn_nfl_api_client.types import UNSET


@pytest.mark.api
def test_get_nhl_game_summary(site_api_client, ensure_json_output_dir):
    """Test getting NHL game summary data."""
    # Use a known NHL game event ID
    event_id = "401774292"
    
    response = get_nhl_game_summary.sync_detailed(
        client=site_api_client,
        event=event_id
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, NhlGameSummaryResponse), "Response should parse to NhlGameSummaryResponse"
    
    # Validate key properties exist
    # Since the schema uses generic objects, properties are in additional_properties
    if result.header:
        header_dict = result.header.to_dict() if hasattr(result.header, 'to_dict') else result.header
        if isinstance(header_dict, dict):
            assert 'id' in header_dict, "Header should have an id"
            assert 'competitions' in header_dict, "Header should have competitions"
    
    if result.boxscore:
        boxscore_dict = result.boxscore.to_dict() if hasattr(result.boxscore, 'to_dict') else result.boxscore
        if isinstance(boxscore_dict, dict):
            assert 'teams' in boxscore_dict, "Boxscore should have teams"
    
    if result.game_info:
        game_info_dict = result.game_info.to_dict() if hasattr(result.game_info, 'to_dict') else result.game_info
        if isinstance(game_info_dict, dict):
            assert 'venue' in game_info_dict, "GameInfo should have venue"
    
    # Save the response for analysis
    response_dict = result.to_dict()
    with open(f"{ensure_json_output_dir}/nhl_game_summary_{event_id}_test.json", "w") as f:
        json.dump(response_dict, f, indent=2)
    
    print(f"Successfully fetched NHL game summary for event {event_id}")
    
    # Log some interesting information
    if result.header:
        header_dict = result.header.to_dict() if hasattr(result.header, 'to_dict') else result.header
        if isinstance(header_dict, dict) and 'competitions' in header_dict:
            competitions = header_dict['competitions']
            if competitions and len(competitions) > 0:
                competition = competitions[0]
                if 'competitors' in competition:
                    home_team = next((c for c in competition['competitors'] if c.get('homeAway') == "home"), None)
                    away_team = next((c for c in competition['competitors'] if c.get('homeAway') == "away"), None)
                    
                    if home_team and away_team:
                        home_name = home_team.get('team', {}).get('displayName', 'Unknown')
                        away_name = away_team.get('team', {}).get('displayName', 'Unknown')
                        print(f"Game: {away_name} @ {home_name}")
                        print(f"Score: {away_team.get('score', '0')} - {home_team.get('score', '0')}")


@pytest.mark.api
@pytest.mark.parametrize("event_id", [
    pytest.param("999999999", marks=pytest.mark.xfail(reason="Invalid event ID should fail")),
])
def test_get_nhl_game_summary_invalid(site_api_client, event_id):
    """Test getting NHL game summary with invalid event ID."""
    response = get_nhl_game_summary.sync_detailed(
        client=site_api_client,
        event=event_id
    )
    
    # ESPN API returns 400 for invalid event IDs
    assert response.status_code == 400, f"Expected status code 400 for invalid event, got {response.status_code}"