import pytest
import json
from models.cdn_api.espn_cdn_nfl_api_client.api.default import get_core_nfl_matchup
from models.cdn_api.espn_cdn_nfl_api_client.models.nfl_matchup_response import NflMatchupResponse


@pytest.mark.api
def test_get_nfl_matchup(cdn_api_client, ensure_json_output_dir):
    """Test NFL matchup endpoint."""
    # Use an existing game ID from our test data
    game_id = "401547602"
    
    # Call the API
    response = get_core_nfl_matchup.sync_detailed(
        client=cdn_api_client,
        xhr=1,
        game_id=game_id
    )
    
    # Validate response
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Parse the response
    result = response.parsed
    assert isinstance(result, NflMatchupResponse), "Response should parse to NflMatchupResponse"
    
    # Basic field validation
    assert result.game_id == int(game_id), f"Expected game_id {game_id}, got {result.game_id}"
    assert result.type is not None, "Response should have a type field"
    
    # Check gamepackageJSON fields
    if result.gamepackage_json:
        # Boxscore section
        if result.gamepackage_json.boxscore:
            boxscore_dict = result.gamepackage_json.boxscore.to_dict() if hasattr(result.gamepackage_json.boxscore, 'to_dict') else {}
            assert isinstance(boxscore_dict, dict), "Boxscore should be a dict"
        
        # Game info section
        if result.gamepackage_json.game_info:
            game_info_dict = result.gamepackage_json.game_info.to_dict() if hasattr(result.gamepackage_json.game_info, 'to_dict') else {}
            assert isinstance(game_info_dict, dict), "Game info should be a dict"
        
        # Leaders section
        if result.gamepackage_json.leaders:
            assert isinstance(result.gamepackage_json.leaders, list), "Leaders should be a list"
        
        # Pickcenter section (matchup-specific betting data)
        if result.gamepackage_json.pickcenter:
            assert isinstance(result.gamepackage_json.pickcenter, list), "Pickcenter should be a list"
        
        # Win probability section
        if result.gamepackage_json.winprobability:
            assert isinstance(result.gamepackage_json.winprobability, list), "Win probability should be a list"
    
    # Save response for analysis
    with open(f"{ensure_json_output_dir}/nfl_matchup_{game_id}_processed.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    print(f"Successfully fetched matchup data for game {game_id}")