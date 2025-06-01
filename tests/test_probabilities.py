import pytest
import json
from models.sports_core_api.espn_sports_core_api_client.models import (
    ProbabilitiesListResponse, 
    ProbabilityItem,
    ProbabilitySource,
    Reference
)
from models.sports_core_api.espn_sports_core_api_client.models.sport_enum import SportEnum
from models.sports_core_api.espn_sports_core_api_client.models.league_enum import LeagueEnum
from models.sports_core_api.espn_sports_core_api_client.api.default import get_game_probabilities
from models.sports_core_api.espn_sports_core_api_client.types import UNSET


@pytest.mark.api
@pytest.mark.parametrize("sport,league,event_id", [
    (SportEnum.FOOTBALL, LeagueEnum.NFL, "401547417"),
    (SportEnum.BASKETBALL, LeagueEnum.NBA, "401584793"),
])
def test_get_game_probabilities(sports_core_api_client, ensure_json_output_dir, sport, league, event_id):
    """Test retrieving game win probabilities for different sports."""
    response = get_game_probabilities.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=event_id,  # Usually the same as event_id
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, ProbabilitiesListResponse), "Response should parse to ProbabilitiesListResponse"
    
    # Validate response structure
    assert result.count > 0, "Should have at least one probability entry"
    assert result.page_index == 1, "Default page index should be 1"
    assert result.page_size > 0, "Page size should be positive"
    assert result.page_count >= 1, "Should have at least one page"
    assert result.items, "Items list should not be empty"
    
    # Validate first probability item
    first_item = result.items[0]
    assert isinstance(first_item, ProbabilityItem), "Each item should be a ProbabilityItem"
    
    # Check required fields
    assert first_item.ref, "Probability item should have a $ref URL"
    assert first_item.ref.startswith("http"), "Reference URL should start with http"
    assert f"/probabilities/" in first_item.ref, "Reference URL should contain /probabilities/"
    
    # Check references
    assert isinstance(first_item.competition, Reference), "Competition should be a Reference"
    assert isinstance(first_item.play, Reference), "Play should be a Reference"
    assert isinstance(first_item.home_team, Reference), "Home team should be a Reference"
    assert isinstance(first_item.away_team, Reference), "Away team should be a Reference"
    
    # Check probability values
    assert 0 <= first_item.home_win_percentage <= 1, "Home win percentage should be between 0 and 1"
    assert 0 <= first_item.away_win_percentage <= 1, "Away win percentage should be between 0 and 1"
    assert first_item.tie_percentage >= 0, "Tie percentage should be non-negative"
    
    # For most sports, probabilities should sum to 1 (allowing small floating point errors)
    total_prob = first_item.home_win_percentage + first_item.away_win_percentage + first_item.tie_percentage
    assert 0.99 <= total_prob <= 1.01, f"Probabilities should sum to 1, got {total_prob}"
    
    # Check other fields
    assert first_item.last_modified, "Should have a last modified timestamp"
    assert first_item.sequence_number, "Should have a sequence number"
    
    # Check source
    assert isinstance(first_item.source, ProbabilitySource), "Source should be a ProbabilitySource"
    assert first_item.source.id, "Source should have an ID"
    assert first_item.source.description, "Source should have a description"
    assert first_item.source.state, "Source should have a state"
    
    # Check optional fields
    if sport == SportEnum.FOOTBALL and first_item.seconds_left is not UNSET:
        assert first_item.seconds_left >= 0, "Seconds left should be non-negative"
    
    # Save response for analysis
    response_dict = {
        "count": result.count,
        "pageIndex": result.page_index,
        "pageSize": result.page_size,
        "pageCount": result.page_count,
        "sampleItems": [
            {
                "$ref": item.ref,
                "homeWinPercentage": item.home_win_percentage,
                "awayWinPercentage": item.away_win_percentage,
                "tiePercentage": item.tie_percentage,
                "sequenceNumber": item.sequence_number,
                "secondsLeft": item.seconds_left if item.seconds_left is not UNSET else None
            }
            for item in result.items[:5]  # Just save first 5 items
        ]
    }
    
    filename = f"probabilities_{sport.value}_{league.value}_{event_id}_test.json"
    with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
        json.dump(response_dict, f, indent=2)
    
    print(f"Successfully retrieved {result.count} probability entries for {sport.value}/{league.value} event {event_id}")


@pytest.mark.api
def test_get_game_probabilities_pagination(sports_core_api_client):
    """Test pagination parameters for probabilities endpoint."""
    # Test with custom page size
    response = get_game_probabilities.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        event_id="401547417",
        competition_id="401547417",
        limit=10,
        page=2,
    )
    
    if response.status_code == 200:
        result = response.parsed
        assert result.page_size <= 10, "Page size should respect the limit parameter"
        assert result.page_index == 2, "Page index should match the requested page"


@pytest.mark.api
def test_get_game_probabilities_invalid_event(sports_core_api_client):
    """Test probabilities endpoint with invalid event ID."""
    response = get_game_probabilities.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        event_id="99999999",
        competition_id="99999999",
    )
    
    # ESPN might return 200 with empty results or 404
    assert response.status_code in [200, 404], f"Expected 200 or 404 for invalid event, got {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        # If 200, it might have 0 probabilities
        assert result.count == 0, "Should have no probabilities for invalid event"