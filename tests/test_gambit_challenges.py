import pytest
import json
import logging
from models.gambit_api.espn_gambit_api_client.api.default import (
    get_challenge_details,
    get_challenge_leaderboard
)
from models.gambit_api.espn_gambit_api_client.models import (
    ChallengeResponse,
    LeaderboardResponse,
    GetChallengeDetailsView,
    GetChallengeLeaderboardView
)

logging.basicConfig(level=logging.INFO)


@pytest.mark.api
def test_get_challenge_details(gambit_api_client, ensure_json_output_dir):
    """Test fetching NFL Pick'em challenge details."""
    
    # Fetch challenge details for 2025 NFL Pick'em
    response = get_challenge_details.sync_detailed(
        client=gambit_api_client,
        challenge_name="nfl-pigskin-pickem-2025",
        scoring_period_id=1,
        view=GetChallengeDetailsView.PICKS
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, ChallengeResponse), "Response should parse to ChallengeResponse"
    
    # Check challenge properties
    assert result.key == "nfl-pigskin-pickem-2025", "Challenge key should match"
    assert result.name, "Challenge should have a name"
    assert result.active is not None, "Challenge should have active status"
    
    logging.info(f"Challenge: {result.name}")
    logging.info(f"Active: {result.active}")
    logging.info(f"Current scoring period: {result.current_scoring_period}")
    logging.info(f"State: {result.state}")
    
    # Check propositions if available
    if result.propositions:
        logging.info(f"Number of propositions: {len(result.propositions)}")
        first_prop = result.propositions[0]
        logging.info(f"First proposition: {first_prop.text if first_prop.text else 'No text'}")
    
    # Save a sample of the challenge data
    sample_data = {
        "id": result.id,
        "key": result.key,
        "name": result.name,
        "active": result.active,
        "state": result.state,
        "current_scoring_period": result.current_scoring_period,
        "start_date": result.start_date,
        "end_date": result.end_date,
        "proposition_count": len(result.propositions) if result.propositions else 0
    }
    
    with open(f"{ensure_json_output_dir}/gambit_challenge_details_sample.json", "w") as f:
        json.dump(sample_data, f, indent=2)


@pytest.mark.api
def test_get_challenge_leaderboard(gambit_api_client, ensure_json_output_dir):
    """Test fetching NFL Pick'em challenge leaderboard."""
    
    # Fetch leaderboard for 2025 NFL Pick'em
    response = get_challenge_leaderboard.sync_detailed(
        client=gambit_api_client,
        challenge_name="nfl-pigskin-pickem-2025",
        view=GetChallengeLeaderboardView.RANKS,
        limit=10  # Get top 10 entries
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, LeaderboardResponse), "Response should parse to LeaderboardResponse"
    
    # Check leaderboard properties
    assert result.challenge_id, "Should have challenge ID"
    assert result.size is not None, "Should have size"
    assert result.entries is not None, "Should have entries"
    
    logging.info(f"Challenge ID: {result.challenge_id}")
    logging.info(f"Total entries: {result.size}")
    logging.info(f"Entries returned: {len(result.entries) if result.entries else 0}")
    
    # Log top entries
    if result.entries:
        logging.info("\nTop entries:")
        for i, entry in enumerate(result.entries[:5], 1):
            logging.info(f"{i}. {entry.display_name if entry.display_name else 'Unknown'} - "
                        f"Score: {entry.score}, Rank: {entry.rank}")
    
    # Save leaderboard sample
    sample_data = {
        "challenge_id": result.challenge_id,
        "total_entries": result.size,
        "locked": result.locked,
        "top_entries": [
            {
                "rank": entry.rank,
                "display_name": entry.display_name,
                "score": entry.score,
                "percentile": entry.percentile
            }
            for entry in (result.entries or [])[:10]
        ]
    }
    
    with open(f"{ensure_json_output_dir}/gambit_leaderboard_sample.json", "w") as f:
        json.dump(sample_data, f, indent=2)


@pytest.mark.api
@pytest.mark.xfail(reason="Challenge name with year might vary")
def test_challenge_not_found(gambit_api_client):
    """Test handling of non-existent challenge."""
    
    response = get_challenge_details.sync_detailed(
        client=gambit_api_client,
        challenge_name="non-existent-challenge-2025"
    )
    
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"