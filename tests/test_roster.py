"""
Test ESPN NFL API - Team Roster Endpoint
"""

import json
import logging
import pytest

from models.site_api.espn_nfl_api_client.api.default.get_nfl_team_roster import sync
from models.site_api.espn_nfl_api_client.models.error_response import ErrorResponse
from models.site_api.espn_nfl_api_client.models.position import Position
from models.site_api.espn_nfl_api_client.models.team_roster_response import (
    TeamRosterResponse,
)
from models.site_api.espn_nfl_api_client.types import UNSET

from models.site_api.espn_nfl_api_client.api.default.get_mlb_team_roster import (
    sync as mlb_sync,
)
from models.site_api.espn_nfl_api_client.models.mlb_team_roster_response import (
    MlbTeamRosterResponse,
)
from models.site_api.espn_nfl_api_client.models.get_mlb_team_roster_team_id_or_abbrev import (
    GetMLBTeamRosterTeamIdOrAbbrev,
)


def validate_schema_response(data: TeamRosterResponse) -> bool:
    """Validate if response matches expected schema structure."""
    required_attrs = ["athletes", "season", "timestamp", "status"]
    for attr in required_attrs:
        if hasattr(data, attr):
            if getattr(data, attr) is UNSET:
                print(f"Missing required attribute: {attr}")
                return False
        else:
            print(f"Missing required attribute: {attr}")
            return False

    athletes = data.athletes
    if not athletes:
        print("No athlete position groups found")
        return False

    # Check if we have position groups (offense, defense, special teams)
    for position_group in athletes:
        if position_group.position is UNSET:
            print("Missing position group name")
            return False

        if position_group.items is UNSET or not position_group.items:
            print(f"No players found in position group: {position_group.position}")
            continue

        # Check basic structure of first player's data in this position group
        player = position_group.items[0]
        if not hasattr(player, "id") or player.id is UNSET:
            print("Player missing ID")
            return False

    return True


def format_roster_data(data: TeamRosterResponse) -> str:
    """Format roster data for display."""
    if not data.athletes:
        return "No roster data available"

    output = []
    output.append("=== ESPN NFL Team Roster ===")

    season_info = "Current Season"
    if data.season:
        season_year = ""
        if data.season.year:
            if data.season.year is not UNSET:
                season_year = data.season.year

        season_name = ""
        if data.season.slug:
            if data.season.slug is not UNSET:
                season_name = data.season.slug

        if season_year and season_name:
            season_info = f"{season_year} {season_name}"
        elif season_year:
            season_info = f"{season_year}"

    output.append(f"Season: {season_info}")
    output.append("")

    for position_group in data.athletes:
        position_name = position_group.position
        if isinstance(position_name, str):
            position_title = position_name.upper()
        else:
            position_title = "POSITION GROUP"

        output.append(f"--- {position_title} ---")

        if not position_group.items:
            output.append("  No players listed")
            continue

        for player in position_group.items:
            # Extract player name details
            first_name = ""
            if hasattr(player, "first_name"):
                if player.first_name is not UNSET:
                    first_name = player.first_name

            last_name = ""
            if hasattr(player, "last_name"):
                if player.last_name is not UNSET:
                    last_name = player.last_name

            player_name = (
                f"{first_name} {last_name}"
                if first_name and last_name
                else "Unknown Player"
            )

            # Add jersey number if available
            jersey = ""
            if hasattr(player, "jersey"):
                if player.jersey is not UNSET:
                    jersey = player.jersey
            jersey_str = f"#{jersey} " if jersey else ""

            # Add position information
            position_str = ""
            position = UNSET
            if hasattr(player, "position"):
                position = player.position

            if position:
                position_str = (
                    f" ({position.name})"
                    if isinstance(position, Position)
                    else f" ({position})"
                )

            # Add college information
            college_str = ""
            college = UNSET
            if hasattr(player, "college"):
                college = player.college

            if college:
                college_name = ""
                if college.name:
                    college_name = college.name
                if college_name:
                    college_str = f" - {college_name}"

            # Add experience information
            experience_str = ""
            experience = UNSET
            if hasattr(player, "experience"):
                experience = player.experience

            if experience:
                exp_years = None
                if experience.years:
                    if exp_years == 0:
                        experience_str = " (Rookie)"
                    elif isinstance(exp_years, int):
                        experience_str = (
                            f" ({exp_years} yr{'s' if exp_years > 1 else ''})"
                        )

            output.append(
                f"  {jersey_str}{player_name}{position_str}{college_str}{experience_str}"
            )

    return "\n".join(output)


@pytest.mark.api
def test_get_nfl_team_roster(site_api_client, ensure_json_output_dir):
    """Test the ESPN NFL Team Roster API."""
    test_team_id = "12"  # Kansas City Chiefs

    # Get roster data
    roster_data = sync(client=site_api_client, team_id=test_team_id)

    assert not isinstance(roster_data, ErrorResponse), (
        f"API returned an error response: {roster_data.error.message if hasattr(roster_data, 'error') and roster_data.error and hasattr(roster_data.error, 'message') else str(roster_data)}"
    )
    assert isinstance(roster_data, TeamRosterResponse), (
        "Failed to fetch roster data or unexpected response type"
    )

    # Save response for future reference
    with open(
        f"{ensure_json_output_dir}/nfl_roster_response_{test_team_id}.json", "w"
    ) as f:
        json.dump(roster_data.to_dict(), f, indent=2)
    logging.info(
        f"Full response saved to {ensure_json_output_dir}/nfl_roster_response_{test_team_id}.json"
    )

    # Validate schema
    assert validate_schema_response(roster_data), (
        "Response does not match expected schema structure"
    )

    # Log formatted summary
    logging.info("===== FULL NFL ROSTER =====\n" + format_roster_data(roster_data))


def validate_mlb_schema_response(data: MlbTeamRosterResponse) -> bool:
    required_attrs = ["athletes", "season", "timestamp", "status", "coach", "team"]
    for attr in required_attrs:
        if hasattr(data, attr):
            if getattr(data, attr) is UNSET:
                print(f"Missing required attribute: {attr}")
                return False
        else:
            print(f"Missing required attribute: {attr}")
            return False
    if not data.athletes:
        print("No athlete position groups found")
        return False
    for position_group in data.athletes:
        if not hasattr(position_group, "position") or position_group.position is UNSET:
            print("Missing position group name")
            return False
        if not hasattr(position_group, "items") or position_group.items is UNSET:
            print(
                f"No players found in position group: {getattr(position_group, 'position', None)}"
            )
            continue
        if position_group.items:
            player = position_group.items[0]
            if not hasattr(player, "id") or player.id is UNSET:
                print("Player missing ID")
                return False
    return True


@pytest.mark.api
def test_get_mlb_team_roster(site_api_client, ensure_json_output_dir):
    """Test the ESPN MLB Team Roster API for a specific team (Boston Red Sox)."""
    test_team_id = GetMLBTeamRosterTeamIdOrAbbrev.BOS  # Boston Red Sox
    roster_data = mlb_sync(team_id_or_abbrev=test_team_id, client=site_api_client)

    # Assert the response is not an error
    assert not isinstance(roster_data, ErrorResponse), (
        f"API returned an error response: {getattr(getattr(roster_data, 'error', None), 'message', str(roster_data))}"
    )
    # Assert the response is the correct model
    assert isinstance(roster_data, MlbTeamRosterResponse), (
        "Failed to fetch MLB roster data or unexpected response type"
    )

    # Save response for future reference
    out_path = f"{ensure_json_output_dir}/mlb_roster_response_{test_team_id}.json"
    with open(out_path, "w") as f:
        json.dump(roster_data.to_dict(), f, indent=2)
    logging.info(f"Full response saved to {out_path}")

    # Print the full roster in a readable format
    mlb_roster_lines = []
    mlb_roster_lines.append("===== FULL MLB ROSTER =====")
    if not roster_data.athletes:
        mlb_roster_lines.append("No roster data available")
    else:
        for group in roster_data.athletes:
            position_name = (
                group.position.upper()
                if isinstance(group.position, str)
                else str(group.position)
            )
            mlb_roster_lines.append(f"--- {position_name} ---")
            if not group.items:
                mlb_roster_lines.append("  No players listed")
                continue
            for player in group.items:
                first_name = getattr(player, "first_name", "") or ""
                last_name = getattr(player, "last_name", "") or ""
                player_name = f"{first_name} {last_name}".strip() or "Unknown Player"
                jersey = getattr(player, "jersey", "")
                jersey_str = f"#{jersey} " if jersey else ""
                pos = getattr(player, "position", None)
                pos_name = pos.name if pos and hasattr(pos, "name") else ""
                college = getattr(player, "college", None)
                college_name = getattr(college, "name", "") if college else ""
                college_str = f" - {college_name}" if college_name else ""
                experience = getattr(player, "experience", None)
                exp_years = getattr(experience, "years", None) if experience else None
                experience_str = ""
                if exp_years == 0:
                    experience_str = " (Rookie)"
                elif isinstance(exp_years, int):
                    experience_str = f" ({exp_years} yr{'s' if exp_years > 1 else ''})"
                mlb_roster_lines.append(
                    f"  {jersey_str}{player_name} ({pos_name}){college_str}{experience_str}"
                )
    logging.info("\n".join(mlb_roster_lines))

    # Print the full roster with index (legacy, still useful for debugging)
    total_players = 0
    for group in roster_data.athletes:
        for i, player in enumerate(group.items):
            name = f"{getattr(player, 'first_name', '')} {getattr(player, 'last_name', '')}".strip()
            jersey = getattr(player, "jersey", "")
            pos = getattr(player, "position", None)
            pos_name = pos.name if pos and hasattr(pos, "name") else ""
            logging.info(f"Player {i}: {name} ({pos_name})")
            total_players += 1
    logging.info(f"Total players returned: {total_players}")
