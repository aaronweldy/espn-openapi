from models.sports_core_api.espn_sports_core_api_client import Client
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


def extract_athlete_id_from_ref(ref_url: str) -> str:
    """Extracts the athlete ID from a $ref URL."""
    match = re.search(r"athletes/(\d+)", ref_url)
    if match:
        return match.group(1)
    raise ValueError(f"Could not extract athlete_id from ref: {ref_url}")


def test_get_nfl_draft_rounds_and_follow_reference():
    """Tests the get_nfl_draft_rounds endpoint and follows the athlete reference for the first pick."""
    print("Testing NFL Draft Rounds endpoint and following athlete reference...")
    client = Client(base_url="https://sports.core.api.espn.com")
    year = 2023

    response: Union[NflDraftRoundsResponse, ErrorResponse, None] = (
        get_nfl_draft_rounds.sync(
            client=client,
            year=year,
        )
    )

    if isinstance(response, ErrorResponse):
        print(
            f"\u2717 API returned an error response: {response.error.message if response.error else response}"
        )
        return False
    elif response is None:
        print("\u2717 API returned no response.")
        return False
    elif isinstance(response, NflDraftRoundsResponse):
        print("\u2713 Successfully fetched draft rounds data.")
        assert response.items is not None, "Response items should not be None"
        assert len(response.items) > 0, "Response items should not be empty"
        print(f"Found {len(response.items)} draft rounds.")
        print("\u2713 Test passed!")

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

        # Print the entire first round in the requested format
        print("\n--- First Round Picks ---")
        for pick in first_round.picks:
            # Get athlete ID from $ref
            athlete_ref = (
                pick.athlete.ref
                if pick.athlete and hasattr(pick.athlete, "ref")
                else None
            )
            athlete_id = (
                extract_athlete_id_from_ref(athlete_ref) if athlete_ref else None
            )
            athlete_name = "?"
            college_name = "?"
            team_name = "?"
            orig_team_name = None
            # Fetch draft athlete details
            if athlete_id:
                draft_athlete_details = get_nfl_draft_athlete.sync(
                    year=year,
                    athlete_id=athlete_id,
                    client=client,
                )
                from models.sports_core_api.espn_sports_core_api_client.models import (
                    NflDraftAthleteResponse,
                )

                if isinstance(draft_athlete_details, NflDraftAthleteResponse):
                    athlete_name = draft_athlete_details.full_name
                    if draft_athlete_details.college and hasattr(
                        draft_athlete_details.college, "ref"
                    ):
                        college_ref = draft_athlete_details.college.ref
                        college_name = college_ref.rstrip("/").split("/")[-1]
            # Get team ID from $ref
            team_ref = (
                pick.team.ref if pick.team and hasattr(pick.team, "ref") else None
            )
            team_id = None
            if team_ref:
                # Try to extract the team ID from the ref (should be last segment before ?)
                team_id = team_ref.rstrip("/").split("/")[-1].split("?")[0]
            # Fetch team display name
            if team_id:
                from models.sports_core_api.espn_sports_core_api_client.api.default.get_nfl_season_team import (
                    sync as get_nfl_season_team,
                )

                team_details = get_nfl_season_team(
                    year=year, team_id=team_id, client=client
                )
                from models.sports_core_api.espn_sports_core_api_client.models import (
                    CoreNflSeasonTeamResponse,
                )

                if isinstance(team_details, CoreNflSeasonTeamResponse):
                    team_name = team_details.display_name
            # Handle traded picks (if traded, try to get orig team from tradeNote)
            traded_str = ""
            if pick.traded and pick.trade_note:
                # Try to parse trade note for original team (best effort)
                traded_str = f" (traded: {pick.trade_note})"
            print(
                f"Pick {pick.pick}: {athlete_name}, {college_name} - {team_name}{traded_str}"
            )

        return True
    else:
        print(f"\u2717 Unexpected response type: {type(response)}")
        return False


def main():
    """Runs the NFL Draft Rounds reference-following test."""
    print("===== ESPN Sports Core API - NFL Draft Rounds Reference Test Script =====")
    test_get_nfl_draft_rounds_and_follow_reference()
    print("===== Test Script Finished =====")


if __name__ == "__main__":
    main()
