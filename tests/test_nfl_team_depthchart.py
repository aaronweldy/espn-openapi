from models.sports_core_api.espn_sports_core_api_client import Client
from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_nfl_team_depthchart,
)
from models.sports_core_api.espn_sports_core_api_client.models import (
    NflTeamDepthchartResponse,
    ErrorResponse,
)
from typing import Optional, Union


def test_get_nfl_team_depthchart():
    """Tests the get_nfl_team_depthchart endpoint."""
    print("Testing NFL Team Depth Chart endpoint...")
    client = Client(base_url="https://sports.core.api.espn.com")
    year = 2023
    team_id = "12"  # Seattle Seahawks

    response: Union[NflTeamDepthchartResponse, ErrorResponse, None] = (
        get_nfl_team_depthchart.sync(
            client=client,
            year=year,
            team_id=team_id,
        )
    )

    if isinstance(response, ErrorResponse):
        print(
            f"✗ API returned an error response: {response.error.message if response.error else response}"
        )
        return False
    elif response is None:
        print("✗ API returned no response.")
        return False
    elif isinstance(response, NflTeamDepthchartResponse):
        print("✓ Successfully fetched depth chart data.")
        assert response.items is not None, "Response items should not be None"
        assert len(response.items) > 0, "Response items should not be empty"
        print(f"Found {len(response.items)} depth chart entries.")
        print("✓ Test passed!")

        print("\n--- Depth Chart Details ---")
        for item in response.items:
            print(f"\nDepth Chart Group: {item.name}")
            if item.positions and item.positions.additional_properties:
                # Iterate through positions within the group
                for (
                    position_name,
                    position_value,
                ) in item.positions.additional_properties.items():
                    # Use the position object for display name/abbreviation if available
                    pos_display_name = (
                        position_value.position.display_name
                        if position_value.position
                        and position_value.position.display_name
                        else position_name
                    )
                    pos_abbreviation = (
                        position_value.position.abbreviation
                        if position_value.position
                        and position_value.position.abbreviation
                        else ""
                    )
                    print(f"  Position: {pos_display_name} ({pos_abbreviation})")
                    if position_value.athletes:
                        # Sort athletes by rank for better readability
                        sorted_athletes = sorted(
                            position_value.athletes, key=lambda x: x.rank
                        )
                        for athlete_entry in sorted_athletes:
                            # Display athlete rank/slot and their reference URL
                            athlete_ref = (
                                athlete_entry.athlete.ref
                                if athlete_entry.athlete
                                else "N/A"
                            )
                            print(
                                f"    - Rank {athlete_entry.rank} (Slot {athlete_entry.slot}): Athlete Ref: {athlete_ref}"
                            )
                    else:
                        print("    No athletes listed for this position.")
            else:
                print("  No positions listed for this group.")

        return True
    else:
        print(f"✗ Unexpected response type: {type(response)}")
        return False


def main():
    """Runs the NFL Team Depth Chart test."""
    print("===== ESPN Sports Core API - NFL Team Depth Chart Test Script =====")
    test_get_nfl_team_depthchart()
    print("===== Test Script Finished =====")


if __name__ == "__main__":
    main()
