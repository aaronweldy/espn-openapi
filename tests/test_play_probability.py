"""Test the play probability endpoint."""

import json
import pytest
from models.sports_core_api.espn_sports_core_api_client.api.default import get_play_probability
from models.sports_core_api.espn_sports_core_api_client.models import ProbabilityItem
from models.sports_core_api.espn_sports_core_api_client.types import UNSET


@pytest.mark.api
def test_get_nfl_play_probability(sports_core_api_client, ensure_json_output_dir):
    """Test getting win probability for a specific NFL play."""
    # Known NFL event and play IDs
    event_id = "401547417"
    play_id = "4015474171"
    
    response = get_play_probability.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        event_id=event_id,
        competition_id=event_id,
        play_id=play_id
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, ProbabilityItem), "Response should parse to ProbabilityItem"
    
    # Verify required fields
    assert result.ref, "Should have a reference URL"
    assert result.competition, "Should have competition reference"
    assert result.play, "Should have play reference"
    assert result.home_team, "Should have home team reference"
    assert result.away_team, "Should have away team reference"
    assert result.tie_percentage is not UNSET, "Should have tie percentage"
    assert result.home_win_percentage is not UNSET, "Should have home win percentage"
    assert result.away_win_percentage is not UNSET, "Should have away win percentage"
    assert result.last_modified, "Should have last modified timestamp"
    assert result.sequence_number, "Should have sequence number"
    assert result.source, "Should have source information"
    
    # Verify probability values are valid
    assert 0 <= result.home_win_percentage <= 1, "Home win percentage should be between 0 and 1"
    assert 0 <= result.away_win_percentage <= 1, "Away win percentage should be between 0 and 1"
    assert 0 <= result.tie_percentage <= 1, "Tie percentage should be between 0 and 1"
    
    # For NFL, tie percentage should be 0 (no ties in regular play)
    assert result.tie_percentage == 0, "NFL should have 0 tie percentage"
    
    # Probabilities should sum to 1 (within floating point tolerance)
    total_prob = result.home_win_percentage + result.away_win_percentage + result.tie_percentage
    assert abs(total_prob - 1.0) < 0.01, f"Probabilities should sum to 1, got {total_prob}"
    
    # Save response for analysis
    with open(f"{ensure_json_output_dir}/nfl_play_probability_{event_id}_{play_id}_test.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2, default=str)


@pytest.mark.api
@pytest.mark.parametrize("sport,league,event_id,play_id", [
    pytest.param("basketball", "nba", "401584793", "4015847931", marks=pytest.mark.xfail(reason="NBA play IDs may differ")),
    pytest.param("baseball", "mlb", "401472463", "4014724631", marks=pytest.mark.xfail(reason="MLB may not have play probabilities")),
    pytest.param("hockey", "nhl", "401559593", "4015595931", marks=pytest.mark.xfail(reason="NHL play IDs may differ")),
])
def test_get_play_probability_other_sports(sports_core_api_client, sport, league, event_id, play_id):
    """Test getting play probability for other sports (may not be available)."""
    response = get_play_probability.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=event_id,
        play_id=play_id
    )
    
    # These might return 404 if play probabilities aren't available
    assert response.status_code in [200, 404], f"Expected status code 200 or 404, got {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        assert isinstance(result, ProbabilityItem), "Response should parse to ProbabilityItem"


@pytest.mark.api
def test_get_play_probability_invalid_play(sports_core_api_client):
    """Test getting probability for an invalid play ID."""
    response = get_play_probability.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        event_id="401547417",
        competition_id="401547417",
        play_id="9999999999"  # Invalid play ID
    )
    
    assert response.status_code == 404, f"Expected status code 404 for invalid play, got {response.status_code}"