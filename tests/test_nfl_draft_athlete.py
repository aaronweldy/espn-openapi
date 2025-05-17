from models.sports_core_api.espn_sports_core_api_client import Client
from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_nfl_draft_athlete,
)
from models.sports_core_api.espn_sports_core_api_client.models import (
    NflDraftAthleteResponse,
    ErrorResponse,
)
from typing import Union


def test_get_nfl_draft_athlete():
    """Tests the get_nfl_draft_athlete endpoint."""
    print("Testing NFL Draft Athlete Details endpoint...")
    client = Client(base_url="https://sports.core.api.espn.com")
    year = 2023
    athlete_id = "106308"  # Example: Bryce Young

    response: Union[NflDraftAthleteResponse, ErrorResponse, None] = (
        get_nfl_draft_athlete.sync(
            client=client,
            year=year,
            athlete_id=athlete_id,
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
    elif isinstance(response, NflDraftAthleteResponse):
        print(
            f"\u2713 Successfully fetched draft athlete details for {response.full_name} (ID: {response.id})"
        )
        assert response.full_name, "Full name should not be empty"
        assert response.id == athlete_id, (
            "Returned athlete ID should match requested ID"
        )
        print(f"First Name: {response.first_name}")
        print(f"Last Name: {response.last_name}")
        print(f"Display Name: {response.display_name}")
        print(f"Height: {response.height}, Weight: {response.weight}")
        print(f"Links: {len(response.links)} found")
        print(f"Positions: {len(response.positions)} found")
        print(f"Attributes: {len(response.attributes)} found")
        print(f"Analysis: {len(response.analysis)} found")
        print(f"Logo: {response.logo.href if response.logo else 'None'}")
        print("\u2713 Test passed!")
        return True
    else:
        print(f"\u2717 Unexpected response type: {type(response)}")
        return False


def main():
    """Runs the NFL Draft Athlete Details test."""
    print("===== ESPN Sports Core API - NFL Draft Athlete Details Test Script =====")
    test_get_nfl_draft_athlete()
    print("===== Test Script Finished =====")


if __name__ == "__main__":
    main()
