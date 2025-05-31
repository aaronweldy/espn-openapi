import pytest
import json
from models.cdn_api.espn_cdn_nfl_api_client.api.default import get_core_nfl_recap
from models.cdn_api.espn_cdn_nfl_api_client.models.nfl_recap_response import NflRecapResponse


@pytest.mark.api
def test_get_nfl_recap(cdn_api_client, ensure_json_output_dir):
    """Test NFL recap endpoint."""
    # Use an existing game ID from our test data
    game_id = "401547602"
    
    # Call the API
    response = get_core_nfl_recap.sync_detailed(
        client=cdn_api_client,
        xhr=1,
        game_id=game_id
    )
    
    # Validate response
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Parse the response
    result = response.parsed
    assert isinstance(result, NflRecapResponse), "Response should parse to NflRecapResponse"
    
    # Basic field validation
    assert result.game_id == int(game_id), f"Expected game_id {game_id}, got {result.game_id}"
    assert result.type is not None, "Response should have a type field"
    
    # Check gamepackageJSON fields
    if result.gamepackage_json:
        # News section
        if result.gamepackage_json.news:
            # The news object might have additional_properties
            news_dict = result.gamepackage_json.news.to_dict() if hasattr(result.gamepackage_json.news, 'to_dict') else {}
            assert 'header' in news_dict or 'link' in news_dict, \
                "News should have header or link"
        
        # Check if broadcasts exist
        if result.gamepackage_json.broadcasts:
            assert isinstance(result.gamepackage_json.broadcasts, list), "Broadcasts should be a list"
    
    # Save response for analysis
    with open(f"{ensure_json_output_dir}/nfl_recap_{game_id}_processed.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    print(f"Successfully fetched recap for game {game_id}")