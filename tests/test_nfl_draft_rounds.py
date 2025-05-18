import pytest
from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_nfl_draft_rounds,
    get_nfl_draft_athlete,
)
from models.sports_core_api.espn_sports_core_api_client.models import (
    NflDraftRoundsResponse,
    ErrorResponse,
    NflDraftAthleteResponse,
    Reference,
)
from typing import Union
import re
import json


def extract_athlete_id_from_ref(ref_url: str) -> str:
    """Extracts the athlete ID from a $ref URL."""
    match = re.search(r"athletes/(\d+)", ref_url)
    if match:
        return match.group(1)
    raise ValueError(f"Could not extract athlete_id from ref: {ref_url}")


@pytest.mark.api
def test_get_nfl_draft_rounds_and_follow_reference(
    sports_core_api_client, ensure_json_output_dir
):
    """Tests the get_nfl_draft_rounds endpoint and follows the athlete reference for the first pick."""
    print("Testing NFL Draft Rounds endpoint and following athlete reference...")
    year = 2023

    response: Union[NflDraftRoundsResponse, ErrorResponse, None] = (
        get_nfl_draft_rounds.sync(
            client=sports_core_api_client,
            year=year,
        )
    )

    assert not isinstance(response, ErrorResponse), (
        f"API returned an error response: {response.error.message if response.error else response}"
    )
    assert response is not None, "API returned no response."
    assert isinstance(response, NflDraftRoundsResponse), (
        "Response should be of type NflDraftRoundsResponse"
    )

    print("\u2713 Successfully fetched draft rounds data.")
    assert response.items is not None, "Response items should not be None"
    assert len(response.items) > 0, "Response items should not be empty"
    print(f"Found {len(response.items)} draft rounds.")

    # Follow the athlete reference for the first pick in the first round
    first_round = response.items[0]
    first_pick = first_round.picks[0]
    athlete_ref = (
        first_pick.athlete.ref
        if first_pick.athlete and hasattr(first_pick.athlete, "ref")
        else None
    )
    print(f"First pick athlete $ref: {athlete_ref}")
    assert athlete_ref, "First pick athlete reference should not be None"
    athlete_id = extract_athlete_id_from_ref(athlete_ref)
    print(f"Extracted athlete_id: {athlete_id}")

    # Save response to JSON file
    with open(f"{ensure_json_output_dir}/nfl_draft_rounds_response.json", "w") as f:
        json.dump(response.to_dict(), f, indent=2)
