import json

import pytest

from models.gambit_api.espn_gambit_api_client.api.default import (
    get_challenge_details,
    get_challenge_leaderboard,
    get_propositions,
)
from models.gambit_api.espn_gambit_api_client.models import (
    ChallengeResponse,
    GetChallengeDetailsView,
    GetChallengeLeaderboardView,
    LeaderboardResponse,
    Proposition,
)


def get_mapping_value(mappings, mapping_type):
    for mapping in mappings:
        if mapping.get("type") == mapping_type:
            return mapping.get("value")
    return None


@pytest.mark.api
def test_get_mens_tournament_challenge_details(
    gambit_api_client, ensure_json_output_dir
):
    response = get_challenge_details.sync_detailed(
        client=gambit_api_client,
        challenge_name="tcmen",
        view=GetChallengeDetailsView.DETAILS,
    )

    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, ChallengeResponse)
    assert result.key.startswith("tournament-challenge-bracket-")
    assert result.active is True
    assert result["gameType"] == "BRACKET"

    mappings = result["mappings"]
    assert get_mapping_value(mappings, "LEAGUE") == "mens-college-basketball"
    assert result["featuredGroupIds"], "Challenge should expose featured group IDs"

    sample_data = {
        "alias": "tcmen",
        "canonical_key": result.key,
        "challenge_id": result.id,
        "game_id": result.game_id,
        "game_type": result["gameType"],
        "league": get_mapping_value(mappings, "LEAGUE"),
    }

    with open(
        f"{ensure_json_output_dir}/gambit_tournament_challenge_details_sample.json",
        "w",
    ) as f:
        json.dump(sample_data, f, indent=2)


@pytest.mark.api
def test_get_womens_tournament_challenge_alias_and_leaderboard(gambit_api_client):
    details_response = get_challenge_details.sync_detailed(
        client=gambit_api_client,
        challenge_name="tcwomen",
        view=GetChallengeDetailsView.DETAILS,
    )

    assert details_response.status_code == 200, (
        f"Expected status code 200, got {details_response.status_code}"
    )

    details = details_response.parsed
    assert isinstance(details, ChallengeResponse)
    assert details.key.startswith("tournament-challenge-bracket-women-")

    canonical_response = get_challenge_details.sync_detailed(
        client=gambit_api_client,
        challenge_name=details.key,
        view=GetChallengeDetailsView.DETAILS,
    )

    assert canonical_response.status_code == 200, (
        f"Expected status code 200, got {canonical_response.status_code}"
    )

    canonical = canonical_response.parsed
    assert isinstance(canonical, ChallengeResponse)
    assert canonical.id == details.id

    leaderboard_response = get_challenge_leaderboard.sync_detailed(
        client=gambit_api_client,
        challenge_name="tcwomen",
        view=GetChallengeLeaderboardView.RANKS,
        limit=5,
    )

    assert leaderboard_response.status_code == 200, (
        f"Expected status code 200, got {leaderboard_response.status_code}"
    )

    leaderboard = leaderboard_response.parsed
    assert isinstance(leaderboard, LeaderboardResponse)
    assert leaderboard.challenge_id == details.id
    assert leaderboard.entries, "Leaderboard should include entries"
    assert leaderboard.entries[0]["member"], "Entries should include member data"


@pytest.mark.api
def test_get_tournament_challenge_propositions(gambit_api_client):
    details_response = get_challenge_details.sync_detailed(
        client=gambit_api_client,
        challenge_name="tcmen",
        view=GetChallengeDetailsView.DETAILS,
    )

    assert details_response.status_code == 200, (
        f"Expected status code 200, got {details_response.status_code}"
    )

    details = details_response.parsed
    assert isinstance(details, ChallengeResponse)

    response = get_propositions.sync_detailed(
        client=gambit_api_client,
        challenge_id=details.id,
    )

    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, list)
    assert result, "Propositions response should include matchup propositions"
    assert isinstance(result[0], Proposition)
    assert result[0]["challengeId"] == details.id
    assert get_mapping_value(result[0]["mappings"], "COMPETITION_ID")
    assert result[0]["possibleOutcomes"], "Proposition should include bracket outcomes"
