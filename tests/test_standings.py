#!/usr/bin/env python3
"""
Test ESPN NFL API - Standings Endpoint using CDN API
Requires Python 3.10+
"""

import json
import pytest
import logging

from models.cdn_api.espn_cdn_nfl_api_client.api.default.get_core_nfl_standings import (
    sync,
)
from models.cdn_api.espn_cdn_nfl_api_client.models.nfl_standings_response import (
    NflStandingsResponse,
)
from models.cdn_api.espn_cdn_nfl_api_client.types import UNSET

# Set up logging
logger = logging.getLogger(__name__)


def validate_nfl_standings_response(data: NflStandingsResponse) -> None:
    """Validate if response matches expected schema structure using assertions."""
    logger.info("Validating NFL standings response structure")
    assert data.content, "Missing content in response"
    assert data.content.standings, "Missing standings in content"
    assert data.content.standings.groups, "Missing groups in standings"

    # Check for NFL conferences
    conferences = data.content.standings.groups
    assert len(conferences) >= 2, "Expected at least 2 conferences (AFC/NFC)"
    logger.info(f"Found {len(conferences)} conferences")

    # Check a conference for divisions
    for conference in conferences:
        logger.info(f"Checking conference: {conference.name}")
        assert conference.name, "Conference should have a name"
        assert conference.groups, "Conference should have groups (divisions)"

        # Check divisions
        logger.info(f"Found {len(conference.groups)} divisions in {conference.name}")
        for division in conference.groups:
            logger.info(f"Checking division: {division.name}")
            assert division.name, "Division should have a name"
            assert division.standings, "Division should have standings"
            assert division.standings.entries, "Standings should have entries"

            # Check teams in division
            logger.info(
                f"Found {len(division.standings.entries)} teams in {division.name}"
            )
            for entry in division.standings.entries:
                assert entry.team, "Entry should have a team"
                assert entry.team.name, "Team should have a name"
                assert entry.team.abbreviation, "Team should have an abbreviation"
                assert entry.stats, "Entry should have stats"

                # Check for common stats
                stat_types = [stat.name for stat in entry.stats if stat.name]
                required_stats = ["wins", "losses", "ties", "winPercent"]
                for stat_type in required_stats:
                    assert stat_type in stat_types, (
                        f"Missing required stat: {stat_type}"
                    )

                logger.info(f"Validated team: {entry.team.name}")


def format_standings_data(data: NflStandingsResponse) -> str:
    """Format standings data for display."""
    if (
        not data.content
        or not data.content.standings
        or not data.content.standings.groups
    ):
        return "Invalid data format: missing standings structure"

    output = []
    output.append("=== NFL Standings ===")

    for conference in data.content.standings.groups:
        output.append(f"\n--- {conference.name} ---")

        if conference.groups and conference.groups is not UNSET:
            for division in conference.groups:
                output.append(f"\n{division.name}")
                output.append(
                    "Team                W-L-T   PCT    PF    PA   DIFF  STRK"
                )
                output.append(
                    "--------------------------------------------------------"
                )

                if (
                    division.standings
                    and division.standings.entries
                    and division.standings.entries is not UNSET
                ):
                    for entry in division.standings.entries:
                        if entry.team and entry.team is not UNSET:
                            team = entry.team

                            if entry.stats and entry.stats is not UNSET:
                                # Extract stats for display - safely handle None/UNSET values
                                wins = next(
                                    (
                                        s.value
                                        for s in entry.stats
                                        if s.name == "wins"
                                        and s.value is not None
                                        and s.value is not UNSET
                                    ),
                                    "0",
                                )
                                losses = next(
                                    (
                                        s.value
                                        for s in entry.stats
                                        if s.name == "losses"
                                        and s.value is not None
                                        and s.value is not UNSET
                                    ),
                                    "0",
                                )
                                ties = next(
                                    (
                                        s.value
                                        for s in entry.stats
                                        if s.name == "ties"
                                        and s.value is not None
                                        and s.value is not UNSET
                                    ),
                                    "0",
                                )
                                win_pct = next(
                                    (
                                        s.display_value
                                        for s in entry.stats
                                        if s.name == "winPercent"
                                        and s.display_value is not None
                                        and s.display_value is not UNSET
                                    ),
                                    ".000",
                                )
                                points_for = next(
                                    (
                                        s.value
                                        for s in entry.stats
                                        if s.name == "pointsFor"
                                        and s.value is not None
                                        and s.value is not UNSET
                                    ),
                                    "0",
                                )
                                points_against = next(
                                    (
                                        s.value
                                        for s in entry.stats
                                        if s.name == "pointsAgainst"
                                        and s.value is not None
                                        and s.value is not UNSET
                                    ),
                                    "0",
                                )
                                diff = next(
                                    (
                                        s.display_value
                                        for s in entry.stats
                                        if s.name == "differential"
                                        and s.display_value is not None
                                        and s.display_value is not UNSET
                                    ),
                                    "0",
                                )
                                streak = next(
                                    (
                                        s.display_value
                                        for s in entry.stats
                                        if s.name == "streak"
                                        and s.display_value is not None
                                        and s.display_value is not UNSET
                                    ),
                                    "",
                                )

                                team_name = (
                                    team.display_name
                                    if team.display_name
                                    else team.name
                                )

                                output.append(
                                    f"{team_name:<20} {wins}-{losses}-{ties}  {win_pct:<5} {points_for:<5} {points_against:<5} {diff:<6} {streak}"
                                )

    return "\n".join(output)


@pytest.mark.api
def test_nfl_standings(cdn_api_client, ensure_json_output_dir):
    """Test fetching and formatting NFL standings from the CDN API."""

    logger.info("Fetching NFL standings from CDN API")
    # Call the CDN API with xhr=1 to get the JSON format
    standings_response = sync(client=cdn_api_client, xhr=1)

    # Verify the response is of the correct type
    assert isinstance(standings_response, NflStandingsResponse), (
        "Response should be an NflStandingsResponse"
    )

    try:
        # Validate schema
        logger.info("Validating response structure")
        validate_nfl_standings_response(standings_response)

        # Display formatted output
        logger.info("Formatting standings for display")
        formatted_standings = format_standings_data(standings_response)
        print("\n" + formatted_standings)

        # Save processed response
        logger.info("Saving processed response to JSON file")
        with open(
            f"{ensure_json_output_dir}/nfl_standings_cdn_processed.json", "w"
        ) as f:
            json.dump(standings_response.to_dict(), f, indent=2)

        logger.info("Test completed successfully")

    except Exception as e:
        logger.error(f"Failed to parse standings JSON: {str(e)}")
        pytest.fail(f"Failed to parse standings JSON: {str(e)}")
