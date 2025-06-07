"""Tests for Team Injuries endpoints."""
import pytest
import json
from models.sports_core_api.espn_sports_core_api_client.api.default import get_team_injuries
from models.sports_core_api.espn_sports_core_api_client.models.paginated_reference_list_response import PaginatedReferenceListResponse
from models.sports_core_api.espn_sports_core_api_client.types import UNSET


@pytest.mark.api
@pytest.mark.parametrize("sport,league,team_id", [
    ("football", "nfl", "8"),    # Miami Dolphins
    ("baseball", "mlb", "15"),    # Milwaukee Brewers  
    ("hockey", "nhl", "1"),       # Anaheim Ducks
    ("basketball", "nba", "13"),  # Los Angeles Lakers (might have no injuries)
])
def test_get_team_injuries_cross_sport(sports_core_api_client, ensure_json_output_dir, sport, league, team_id):
    """Test getting team injuries across different sports."""
    response = get_team_injuries.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        team_id=team_id,
        limit=100
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, PaginatedReferenceListResponse), "Response should parse to PaginatedReferenceListResponse"
    
    # Validate response structure
    assert result.count is not UNSET, "Count should be set"
    assert result.page_index is not UNSET, "Page index should be set"
    assert result.page_size is not UNSET, "Page size should be set"
    assert result.page_count is not UNSET, "Page count should be set"
    assert result.items is not UNSET, "Items should be set"
    
    # Check that items is a list
    assert isinstance(result.items, list), "Items should be a list"
    
    # If there are injuries, validate the reference structure
    if result.count > 0:
        assert len(result.items) > 0, "Items list should not be empty when count > 0"
        first_item = result.items[0]
        assert first_item.ref is not UNSET, "Reference should have a $ref URL"
        assert first_item.ref.startswith("http://sports.core.api.espn.com"), "$ref should be a valid ESPN API URL"
        assert f"/sports/{sport}/leagues/{league}/" in first_item.ref, f"$ref should contain the correct sport/league path"
        assert "/injuries/" in first_item.ref, "$ref should point to an injury resource"
    
    # Save response for analysis
    with open(f"{ensure_json_output_dir}/team_injuries_{sport}_{league}_{team_id}.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    print(f"\n{sport.upper()} {league.upper()} Team {team_id} has {result.count} injuries listed")