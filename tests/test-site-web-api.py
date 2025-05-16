#!/usr/bin/env python3
"""
Test ESPN Site Web API endpoints
Requires Python 3.10+
"""

import json
import os
from pprint import pprint
import traceback
from typing import Any, Dict, Optional

from models.site_web_api.espn_site_web_api_client import Client as EspnSiteWebApiClient
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
from models.site_web_api.espn_site_web_api_client.types import Response, UNSET
from models.site_web_api.espn_site_web_api_client.api.default.get_general_search_v2 import (
    sync_detailed as search_v2_sync_detailed,
)
from models.site_web_api.espn_site_web_api_client.models.search_v2_response import (
    SearchV2Response,
)

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
                    output.append(f"  - Team (Reference): [Could not extract ref URL]")

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


def test_get_athlete_overview(athlete_id: int = TEST_ATHLETE_ID_NFL):
    """Tests fetching and parsing the athlete overview."""
    print(f"\n--- Testing Athlete Overview (ID: {athlete_id}) --- ")
    # Use HTTPS as default, adjust if needed
    client = EspnSiteWebApiClient(base_url="https://site.web.api.espn.com")

    try:
        # Access endpoint via client.<tag>.<operation_id>
        api_func = get_athlete_overview_nfl

        response = api_func.sync_detailed(
            athlete_id=athlete_id,
            client=client,  # Pass client instance
        )

        # Check status code
        if response.status_code == 200:
            print(
                f"✓ Successfully fetched athlete overview (HTTP {response.status_code})"
            )
            result = response.parsed

            if not isinstance(result, AthleteOverviewResponse):
                print(f"✗ Parsed result is not AthleteOverviewResponse: {type(result)}")
                return False

                # Validate schema
                # if validate_athlete_overview_response(result):
                #     print("✓ Response structure matches expected schema.")
                # else:
                #     print("✗ Response structure does not match expected schema.")
                # Optionally dump flawed response
                # with open(f"json_output/athlete_{athlete_id}_overview_invalid.json", "w") as f:
                #     json.dump(result.to_dict(), f, indent=2)
                return False  # Fail the test if validation fails

            # Display formatted summary
            print("\n" + format_athlete_overview(result))

            # Save full response for analysis
            os.makedirs("json_output", exist_ok=True)
            with open(
                f"json_output/athlete_{athlete_id}_overview_processed.json", "w"
            ) as f:
                json.dump(result.to_dict(), f, indent=2)
            print(
                f"✓ Processed response saved to json_output/athlete_{athlete_id}_overview_processed.json"
            )
            return True

        elif response.status_code == 404:
            print(f"✓ Received HTTP 404 Not Found as expected for ID {athlete_id}.")
            # If testing for 404, this is a pass
            return True  # Or specific handling if testing invalid IDs

        else:
            print(f"✗ API returned unexpected status code {response.status_code}")
            try:
                # Try to parse as ErrorResponse if defined
                error_content = response.content.decode("utf-8")
                print(f"Raw error content: {error_content}")
                # error_data = ErrorResponse.from_dict(json.loads(error_content))
                # if error_data.message:
                #     print(f"Error Message: {error_data.message}")
            except Exception as parse_err:
                print(f"(Could not parse error response: {parse_err})")
            return False

    except Exception as e:
        print(f"✗ Error during athlete overview test: {e}")
        print(traceback.format_exc())
        return False


def test_search_v2():
    """Test the v2 search endpoint and model parsing."""
    print("\n--- Testing /apis/search/v2 ---")
    client = EspnSiteWebApiClient(base_url="https://site.web.api.espn.com")
    query = "Tom Brady"
    limit = 2
    response = search_v2_sync_detailed(client=client, query=query, limit=limit)
    if response.status_code == 200:
        print(f"✓ Successfully fetched v2 search results (HTTP {response.status_code})")
        result = response.parsed
        if not isinstance(result, SearchV2Response):
            print(f"✗ Parsed result is not SearchV2Response: {type(result)}")
            return False
        print(f"Total found: {result.total_found}")
        if result.results:
            group = result.results[0]
            print(
                f"First group: {getattr(group, 'display_name', '[no display_name]')} (type: {getattr(group, 'type', '[no type]')}, totalFound: {getattr(group, 'total_found', '[no total_found]')})"
            )
            if group.contents:
                item = group.contents[0]
                print(
                    f"First item: {getattr(item, 'display_name', '[no display_name]')} ({getattr(item, 'type', '[no type]')}) - {getattr(item, 'description', '[no description]')}"
                )
                link_web = getattr(getattr(item, "link", None), "web", None)
                image_default = getattr(getattr(item, "image", None), "default", None)
                print(f"  Link: {link_web}")
                print(f"  Image: {image_default}")
        # Save processed response
        os.makedirs("json_output", exist_ok=True)
        with open("json_output/search_v2_test_processed.json", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
        print(
            "✓ Processed v2 search response saved to json_output/search_v2_test_processed.json"
        )
        return True
    else:
        print(f"✗ API returned unexpected status code {response.status_code}")
        return False


# --- Main Execution ---


def main():
    """Runs all test functions for the Site Web API."""
    print("===== ESPN Site Web API Test Script =====")

    # Create output directory if it doesn't exist
    os.makedirs("json_output", exist_ok=True)

    results = []

    # Test athlete overview endpoint (valid ID)
    overview_result = test_get_athlete_overview(TEST_ATHLETE_ID_NFL)
    results.append(("Athlete Overview (Valid ID)", overview_result))

    # Optional: Test with an invalid ID if 404 handling is desired
    # overview_invalid_result = test_get_athlete_overview(TEST_ATHLETE_ID_INVALID)
    # results.append(("Athlete Overview (Invalid ID)", overview_invalid_result))

    # Test search v2 endpoint
    search_v2_result = test_search_v2()
    results.append(("Search V2", search_v2_result))

    # Add calls to other test functions here as they are created...

    # Summary
    print("\n===== Test Results Summary =====")
    all_passed = True
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{test_name}: {status}")
        if not result:
            all_passed = False

    if not all_passed:
        print("\nSome tests failed.")
        exit(1)
    else:
        print("\nAll tests passed.")
        exit(0)


if __name__ == "__main__":
    main()
