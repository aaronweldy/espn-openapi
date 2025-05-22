#!/usr/bin/env python3
"""
Test ESPN Site Web API endpoints
Requires Python 3.10+
"""

import json
import logging
import traceback
import pytest

from models.site_web_api.espn_site_web_api_client.models.athlete_details import (
    AthleteDetails,
)
from models.site_web_api.espn_site_web_api_client.models.athlete_overview_response import (
    AthleteOverviewResponse,
)

from models.site_web_api.espn_site_web_api_client.api.nfl_athletes import (
    get_athlete_overview_nfl,
)
from models.site_web_api.espn_site_web_api_client.models.team import Team
from models.site_web_api.espn_site_web_api_client.models.team_reference import (
    TeamReference,
)
from models.site_web_api.espn_site_web_api_client.models.position import Position
from models.site_web_api.espn_site_web_api_client.models.career_statistics import (
    CareerStatistics,
)
from models.site_web_api.espn_site_web_api_client.models.news_item_detailed import (
    NewsItemDetailed,
)
from models.site_web_api.espn_site_web_api_client.types import UNSET
from models.site_web_api.espn_site_web_api_client.models.sport_enum import SportEnum
from models.site_web_api.espn_site_web_api_client.models.league_enum import LeagueEnum
from models.site_web_api.espn_site_web_api_client.api.default.get_general_search_v2 import (
    sync_detailed as search_v2_sync_detailed,
)
from models.site_web_api.espn_site_web_api_client.models.search_v2_response import (
    SearchV2Response,
)
from models.site_web_api.espn_site_web_api_client.api.default import (
    get_scoreboard_header,
    get_nfl_athlete_splits,
)
from models.site_web_api.espn_site_web_api_client.models.scoreboard_header_response import (
    ScoreboardHeaderResponse,
)
from models.site_web_api.espn_site_web_api_client.models import (
    AthleteSplitsResponse,
)
from models.site_web_api.espn_site_web_api_client.api.nfl_athletes.get_athlete_profile_nfl import (
    sync_detailed as get_athlete_profile_nfl_sync_detailed,
)
from models.site_web_api.espn_site_web_api_client.models.athlete_profile_response import (
    AthleteProfileResponse,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants for athlete IDs used in tests
TEST_ATHLETE_ID_NFL = 4430191  # Skyy Moore
TEST_ATHLETE_ID_INVALID = 99999999  # Example invalid ID

# --- Formatting Functions ---


def format_athlete_overview(data: AthleteOverviewResponse) -> str:
    """Format athlete overview data for display."""
    output = []
    output.append("=== ESPN Athlete Overview (Site Web API) ===")

    if data.athlete is UNSET or not isinstance(data.athlete, AthleteDetails):
        return "\n".join(output) + "\nAthlete details missing or invalid."

    athlete = data.athlete
    output.append(f"Athlete: {athlete.full_name} (ID: {athlete.id})")

    if (
        athlete.position
        and isinstance(athlete.position, Position)
        and athlete.position.display_name
    ):
        output.append(f"Position: {athlete.position.display_name}")

    if athlete.display_height and athlete.display_weight:
        output.append(f"Ht/Wt: {athlete.display_height} / {athlete.display_weight}")

    if athlete.age:
        output.append(f"Age: {athlete.age}")

    # Display Teams (handling oneOf)
    if athlete.teams:
        output.append("\n--- Teams ---")
        for team_info in athlete.teams:
            if isinstance(team_info, Team) and team_info.display_name:
                output.append(f"  - Team (Full): {team_info.display_name}")
            elif isinstance(team_info, TeamReference):
                # Try accessing $ref - adjust based on actual generated attribute name
                ref_val = getattr(
                    team_info, "ref", getattr(team_info, "dollar_ref", None)
                )
                if (
                    not ref_val
                    and hasattr(team_info, "additional_properties")
                    and isinstance(team_info.additional_properties, dict)
                ):
                    ref_val = team_info.additional_properties.get("$ref")

                if ref_val:
                    output.append(f"  - Team (Reference): {ref_val}")
                else:
                    output.append("  - Team (Reference): [Could not extract ref URL]")

            else:
                output.append("  - Team info in unexpected format")

    # Display Career Stats Summary
    if (
        data.statistics
        and isinstance(data.statistics, CareerStatistics)
        and data.statistics.display_name
    ):
        output.append("\n--- Career Statistics ---")
        output.append(f"Type: {data.statistics.display_name}")
        if data.statistics.splits:
            # Just show the first split summary for brevity
            split = data.statistics.splits[0]
            output.append(f"Split: {split.display_name}")
            if split.stats and data.statistics.labels:
                stats_summary = ", ".join([
                    f"{label}={val}"
                    for label, val in zip(data.statistics.labels, split.stats)
                ])
                output.append(f"Stats: {stats_summary}")

    # Display News Summary
    if data.news:
        output.append("\n--- Recent News ---")
        for i, news_item in enumerate(data.news[:3]):  # Show first 3 news items
            if isinstance(news_item, NewsItemDetailed) and news_item.headline:
                output.append(f"  {i + 1}. {news_item.headline}")

    return "\n".join(output)


# --- Test Functions ---


@pytest.mark.api
def test_get_athlete_overview(
    site_web_api_client, ensure_json_output_dir, athlete_id: int = TEST_ATHLETE_ID_NFL
):
    """Tests fetching and parsing the athlete overview."""
    try:
        api_func = get_athlete_overview_nfl
        response = api_func.sync_detailed(
            athlete_id=athlete_id,
            client=site_web_api_client,
        )

        assert response.status_code == 200, (
            f"Expected status code 200, got {response.status_code}"
        )
        result = response.parsed
        assert isinstance(result, AthleteOverviewResponse), (
            "Response should parse to AthleteOverviewResponse"
        )

        # Display formatted summary
        logger.info("\n" + format_athlete_overview(result))

        # Save full response for analysis
        with open(
            f"{ensure_json_output_dir}/athlete_{athlete_id}_overview_processed.json",
            "w",
        ) as f:
            json.dump(result.to_dict(), f, indent=2)
        logger.info(
            f"✓ Processed response saved to {ensure_json_output_dir}/athlete_{athlete_id}_overview_processed.json"
        )

    except Exception as e:
        logger.error(f"✗ Error during athlete overview test: {e}")
        logger.error(traceback.format_exc())
        pytest.fail(f"Exception during test: {str(e)}")


@pytest.mark.api
def test_search_v2(site_web_api_client, ensure_json_output_dir):
    """Test the v2 search endpoint and model parsing."""
    query = "Tom Brady"
    limit = 2
    response = search_v2_sync_detailed(
        client=site_web_api_client, query=query, limit=limit
    )

    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )
    result = response.parsed
    assert isinstance(result, SearchV2Response), (
        "Response should parse to SearchV2Response"
    )

    logger.info(f"Total found: {result.total_found}")
    if result.results:
        group = result.results[0]
        logger.info(
            f"First group: {getattr(group, 'display_name', '[no display_name]')} (type: {getattr(group, 'type', '[no type]')}, totalFound: {getattr(group, 'total_found', '[no total_found]')})"
        )
        if group.contents:
            item = group.contents[0]
            logger.info(
                f"First item: {getattr(item, 'display_name', '[no display_name]')} ({getattr(item, 'type', '[no type]')}) - {getattr(item, 'description', '[no description]')}"
            )
            link_web = getattr(getattr(item, "link", None), "web", None)
            image_default = getattr(getattr(item, "image", None), "default", None)
            logger.info(f"  Link: {link_web}")
            logger.info(f"  Image: {image_default}")

    # Save processed response
    with open(f"{ensure_json_output_dir}/search_v2_test_processed.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    logger.info(
        f"✓ Processed v2 search response saved to {ensure_json_output_dir}/search_v2_test_processed.json"
    )


@pytest.mark.api
def test_get_scoreboard_header(site_web_api_client, ensure_json_output_dir):
    """Test fetching and parsing the scoreboard header (site.web.api.espn.com/apis/v2/scoreboard/header)."""
    try:
        response = get_scoreboard_header.sync_detailed(
            client=site_web_api_client,
            sport=SportEnum.FOOTBALL,
            league=LeagueEnum.NFL,
        )

        assert response.status_code == 200, (
            f"Expected status code 200, got {response.status_code}"
        )
        result = response.parsed
        assert isinstance(result, ScoreboardHeaderResponse), (
            "Response should parse to ScoreboardHeaderResponse"
        )

        # Basic validation of some key fields
        assert result.sports is not None, "Response should have sports data"
        if result.sports:
            sport = result.sports[0]
            assert sport.name, "Sport should have a name"
            logger.info(f"\nScoreboard Header - Sport: {sport.name}")

            if sport.leagues:
                league = sport.leagues[0]
                logger.info(f"League: {league.name} ({league.abbreviation})")

                # Check if season attribute exists before accessing it
                if (
                    hasattr(league, "additional_properties")
                    and "season" in league.additional_properties
                ):
                    season = league.additional_properties["season"]
                    logger.info(
                        f"Season: {season.get('displayName', 'Unknown')} ({season.get('year', 'Unknown')})"
                    )

        # Save processed response
        with open(
            f"{ensure_json_output_dir}/scoreboard_header_processed.json", "w"
        ) as f:
            json.dump(result.to_dict(), f, indent=2)
        logger.info(
            f"✓ Processed scoreboard header saved to {ensure_json_output_dir}/scoreboard_header_processed.json"
        )

    except Exception as e:
        logger.error(f"✗ Error during scoreboard header test: {e}")
        logger.error(traceback.format_exc())
        pytest.fail(f"Exception during test: {str(e)}")


@pytest.mark.api
def test_nfl_athlete_splits(site_web_api_client, ensure_json_output_dir):
    """Test fetching and parsing NFL athlete splits statistics."""
    try:
        # Use a well-known NFL athlete ID - Tom Brady as an example
        athlete_id = "2330"  # Tom Brady

        response = get_nfl_athlete_splits.sync_detailed(
            client=site_web_api_client,
            athlete_id=athlete_id,
        )

        assert response.status_code == 200, (
            f"Expected status code 200, got {response.status_code}"
        )
        result = response.parsed
        assert isinstance(result, AthleteSplitsResponse), (
            "Response should parse to AthleteSplitsResponse"
        )

        assert result.categories is not None, "Response should have categories data"
        logger.info(f"\n--- NFL Athlete Splits for athlete ID {athlete_id} ---")

        # Output some basic information about categories
        if result.categories:
            categories = result.categories
            logger.info(f"Found {len(categories)} categories")

            # Show detail for categories
            for category in categories:
                category_name = (
                    category.display_name if category.display_name else "Unnamed"
                )
                logger.info(f"\nCategory: {category_name}")

                # Safely check for stats
                if (
                    hasattr(category, "additional_properties")
                    and "stats" in category.additional_properties
                ):
                    stats = category.additional_properties["stats"]
                    logger.info("Statistics:")
                    # Show first few stats in the category
                    for stat in stats[:3]:  # Show first 3 stats
                        if (
                            isinstance(stat, dict)
                            and "name" in stat
                            and "value" in stat
                        ):
                            logger.info(f"  {stat['name']}: {stat['value']}")

        # Save processed response
        with open(
            f"{ensure_json_output_dir}/athlete_{athlete_id}_splits_processed.json", "w"
        ) as f:
            json.dump(result.to_dict(), f, indent=2)
        logger.info(
            f"✓ Processed athlete splits saved to {ensure_json_output_dir}/athlete_{athlete_id}_splits_processed.json"
        )

    except Exception as e:
        logger.error(f"✗ Error during athlete splits test: {e}")
        logger.error(traceback.format_exc())
        pytest.fail(f"Exception during test: {str(e)}")


@pytest.mark.api
def test_get_athlete_profile(
    site_web_api_client, ensure_json_output_dir, athlete_id: int = TEST_ATHLETE_ID_NFL
):
    """Tests fetching and parsing the athlete profile."""
    try:
        response = get_athlete_profile_nfl_sync_detailed(
            athlete_id=athlete_id,
            client=site_web_api_client,
        )

        assert response.status_code == 200, (
            f"Expected status code 200, got {response.status_code}"
        )
        result = response.parsed
        assert isinstance(result, AthleteProfileResponse), (
            "Response should parse to AthleteProfileResponse"
        )

        athlete = result.athlete
        assert athlete is not None, "Athlete data should be present"

        logger.info(
            f"\n--- NFL Athlete Profile for {athlete.full_name} (ID: {athlete.id}) ---"
        )
        # Print basic athlete info
        if athlete.position and athlete.position.abbreviation:
            position_str = f"({athlete.position.abbreviation})"
        else:
            position_str = ""

        logger.info(f"Name: {athlete.full_name} {position_str}")

        # Print additional data if available
        if hasattr(athlete, "college") and athlete.college:
            logger.info(f"College: {athlete.college.name}")

        # Print team info if available
        if (
            athlete.team
            and hasattr(athlete.team, "display_name")
            and athlete.team.display_name
        ):
            logger.info(f"Team: {athlete.team.display_name}")

        # Print jersey number if available
        if athlete.jersey:
            logger.info(f"Jersey: #{athlete.jersey}")

        # Save processed response
        with open(
            f"{ensure_json_output_dir}/athlete_{athlete_id}_profile_processed.json", "w"
        ) as f:
            json.dump(result.to_dict(), f, indent=2)
        logger.info(
            f"✓ Processed athlete profile saved to {ensure_json_output_dir}/athlete_{athlete_id}_profile_processed.json"
        )

    except Exception as e:
        logger.error(f"✗ Error during athlete profile test: {e}")
        logger.error(traceback.format_exc())
        pytest.fail(f"Exception during test: {str(e)}")


@pytest.mark.api
@pytest.mark.parametrize(
    "athlete_id, expect_success",
    [
        (TEST_ATHLETE_ID_NFL, True),
        (TEST_ATHLETE_ID_INVALID, False),
    ],
)
def test_athlete_profile_parametrized(
    site_web_api_client, ensure_json_output_dir, athlete_id, expect_success
):
    """Parametrized test for athlete profile with valid and invalid IDs."""
    try:
        response = get_athlete_profile_nfl_sync_detailed(
            athlete_id=athlete_id,
            client=site_web_api_client,
        )

        if expect_success:
            assert response.status_code == 200, (
                f"Expected status code 200, got {response.status_code}"
            )
            result = response.parsed
            assert isinstance(result, AthleteProfileResponse), (
                "Response should parse to AthleteProfileResponse"
            )
            logger.info(f"✓ Successfully retrieved profile for athlete ID {athlete_id}")
        else:
            assert response.status_code != 200, (
                f"Expected non-200 status code, got {response.status_code}"
            )
            logger.info(
                f"✓ Correctly received error response for invalid athlete ID {athlete_id}"
            )

    except Exception as e:
        if not expect_success:
            logger.info(f"✓ Expected exception for invalid athlete ID: {str(e)}")
        else:
            logger.error(f"✗ Unexpected error: {str(e)}")
            pytest.fail(f"Exception during test: {str(e)}")


@pytest.mark.api
def test_get_athlete_profile_mlb(site_web_api_client, ensure_json_output_dir):
    """Test fetching and parsing the MLB athlete details endpoint."""
    from models.site_web_api.espn_site_web_api_client.api.mlb_athletes.get_athlete_profile_mlb import (
        sync_detailed as get_athlete_profile_mlb_sync_detailed,
    )
    from models.site_web_api.espn_site_web_api_client.models.mlb_athlete_details_response import (
        MLBAthleteDetailsResponse,
    )

    athlete_id = 36071  # Nick Pivetta
    response = get_athlete_profile_mlb_sync_detailed(
        athlete_id=athlete_id,
        client=site_web_api_client,
    )
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )
    result = response.parsed
    assert isinstance(result, MLBAthleteDetailsResponse), (
        "Response should parse to MLBAthleteDetailsResponse"
    )

    # Save processed response for analysis
    with open(f"{ensure_json_output_dir}/mlb_athlete_36071_processed.json", "w") as f:
        import json

        json.dump(result.to_dict(), f, indent=2)
    logger.info(
        f"✓ Processed response saved to {ensure_json_output_dir}/mlb_athlete_36071_processed.json"
    )
