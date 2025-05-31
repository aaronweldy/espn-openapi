import pytest
import json
from models.cdn_api.espn_cdn_nfl_api_client.api.default import get_core_nfl_game
from models.cdn_api.espn_cdn_nfl_api_client.models.nfl_game_response import NflGameResponse


@pytest.mark.api
def test_get_nfl_game(cdn_api_client, ensure_json_output_dir):
    """Test NFL game endpoint."""
    # Use an existing game ID from our test data
    game_id = "401547602"
    
    # Call the API
    response = get_core_nfl_game.sync_detailed(
        client=cdn_api_client,
        xhr=1,
        game_id=game_id
    )
    
    # Validate response
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Parse the response
    result = response.parsed
    assert isinstance(result, NflGameResponse), "Response should parse to NflGameResponse"
    
    # Basic field validation
    assert result.game_id == int(game_id), f"Expected game_id {game_id}, got {result.game_id}"
    assert result.type is not None, "Response should have a type field"
    
    # Check gamepackageJSON fields
    if result.gamepackage_json:
        # Boxscore section
        if result.gamepackage_json.boxscore:
            boxscore_dict = result.gamepackage_json.boxscore.to_dict() if hasattr(result.gamepackage_json.boxscore, 'to_dict') else {}
            assert isinstance(boxscore_dict, dict), "Boxscore should be a dict"
        
        # Drives section
        if result.gamepackage_json.drives:
            drives_dict = result.gamepackage_json.drives.to_dict() if hasattr(result.gamepackage_json.drives, 'to_dict') else {}
            assert isinstance(drives_dict, dict), "Drives should be a dict"
        
        # Leaders section
        if result.gamepackage_json.leaders:
            assert isinstance(result.gamepackage_json.leaders, list), "Leaders should be a list"
        
        # Scoring plays section
        if result.gamepackage_json.scoring_plays:
            assert isinstance(result.gamepackage_json.scoring_plays, list), "Scoring plays should be a list"
        
        # Videos section
        if result.gamepackage_json.videos:
            assert isinstance(result.gamepackage_json.videos, list), "Videos should be a list"
    
    # Save response for analysis
    with open(f"{ensure_json_output_dir}/nfl_game_{game_id}_processed.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    print(f"Successfully fetched game details for game {game_id}")