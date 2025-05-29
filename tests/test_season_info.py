"""Test cases for the season info endpoint across multiple sports."""

import json
import pytest

from models.site_web_api.espn_site_web_api_client.api.default import get_season_info
from models.site_web_api.espn_site_web_api_client.models import (
    SeasonInfoResponse,
    SeasonTypeInfo,
)
from models.site_web_api.espn_site_web_api_client.models.sport_enum import SportEnum
from models.site_web_api.espn_site_web_api_client.models.league_enum import LeagueEnum


@pytest.mark.api
def test_get_nfl_season_info(site_web_api_client, ensure_json_output_dir):
    """Test getting NFL season information."""
    response = get_season_info.sync_detailed(
        client=site_web_api_client, sport=SportEnum.FOOTBALL, league=LeagueEnum.NFL
    )

    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, SeasonInfoResponse), (
        "Response should be SeasonInfoResponse"
    )

    # Validate required fields
    assert result.year, "Season year is required"
    assert result.display_name, "Display name is required"
    assert result.start_date, "Start date is required"
    assert result.end_date, "End date is required"
    assert result.types, "Season types are required"

    # Validate season types
    assert len(result.types) > 0, "Should have at least one season type"

    for season_type in result.types:
        assert isinstance(season_type, SeasonTypeInfo), (
            "Each type should be SeasonTypeInfo"
        )
        assert season_type.id, "Season type ID is required"
        assert season_type.type, "Season type number is required"
        assert season_type.name, "Season type name is required"
        assert season_type.start_date, "Season type start date is required"
        assert season_type.end_date, "Season type end date is required"

    # Save response for analysis
    with open(f"{ensure_json_output_dir}/test_nfl_season_info.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)

    print(f"NFL Season: {result.display_name}, Year: {result.year}")
    print(f"Season runs from {result.start_date} to {result.end_date}")
    print(f"Number of season types: {len(result.types)}")


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league,expected_types",
    [
        (
            SportEnum.FOOTBALL,
            LeagueEnum.NFL,
            ["Preseason", "Regular Season", "Postseason", "Off Season"],
        ),
        (
            SportEnum.BASKETBALL,
            LeagueEnum.NBA,
            [
                "Preseason",
                "Regular Season",
                "Postseason",
                "Off Season",
                "Play-In Season",
            ],
        ),
        (
            SportEnum.BASEBALL,
            LeagueEnum.MLB,
            ["Spring Training", "Regular Season", "Postseason", "Off Season"],
        ),
        (
            SportEnum.HOCKEY,
            LeagueEnum.NHL,
            ["Preseason", "Regular Season", "Postseason", "Off Season"],
        ),
        (
            SportEnum.BASKETBALL,
            LeagueEnum.WNBA,
            ["Preseason", "Regular Season", "Postseason", "Off Season"],
        ),
        (
            SportEnum.FOOTBALL,
            LeagueEnum.COLLEGE_FOOTBALL,
            ["Preseason", "Regular Season", "Postseason", "Off Season"],
        ),
        (
            SportEnum.BASKETBALL,
            LeagueEnum.MENS_COLLEGE_BASKETBALL,
            ["Preseason", "Regular Season", "Postseason", "Off Season"],
        ),
        (
            SportEnum.BASKETBALL,
            LeagueEnum.WOMENS_COLLEGE_BASKETBALL,
            ["Preseason", "Regular Season", "Postseason", "Off Season"],
        ),
        (
            SportEnum.BASEBALL,
            LeagueEnum.COLLEGE_BASEBALL,
            [
                "Preseason",
                "Regular Season",
                "Regionals",
                "Super Regionals",
                "World Series",
            ],
        ),
    ],
)
def test_get_season_info_cross_sport(
    site_web_api_client, ensure_json_output_dir, sport, league, expected_types
):
    """Test getting season information across multiple sports."""
    response = get_season_info.sync_detailed(
        client=site_web_api_client, sport=sport, league=league
    )

    assert response.status_code == 200, (
        f"Expected status code 200 for {sport}/{league}, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, SeasonInfoResponse), (
        "Response should be SeasonInfoResponse"
    )

    # Validate basic fields
    assert result.year, f"{sport}/{league} season year is required"
    assert result.display_name, f"{sport}/{league} display name is required"
    assert result.types, f"{sport}/{league} season types are required"

    # Check that we have the expected season type names
    actual_type_names = [t.name for t in result.types]
    for expected_type in expected_types:
        assert expected_type in actual_type_names, (
            f"Expected to find '{expected_type}' in {sport}/{league} season types"
        )

    # Save response for analysis
    filename = f"test_{league.value}_season_info.json"
    with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
        json.dump(result.to_dict(), f, indent=2)

    print(f"\n{sport.value}/{league.value} Season: {result.display_name}")
    print(f"Season types: {', '.join(actual_type_names)}")


@pytest.mark.api
def test_get_season_info_invalid_sport(site_web_api_client):
    """Test getting season info with invalid sport/league combination."""
    import httpx

    # Try an invalid combination (e.g., hockey league with football sport)
    # Use httpx directly to avoid parsing issues with empty response
    url = f"{site_web_api_client._base_url}/apis/common/v3/sports/football/mlb/season"
    response = httpx.get(url)

    # ESPN API returns 200 but with empty response for invalid combinations
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    # The response body is empty for invalid combinations
    assert response.content == b"", "Expected empty response for invalid combination"


@pytest.mark.api
def test_season_type_mapping(site_web_api_client):
    """Test that season type integers map correctly."""
    response = get_season_info.sync_detailed(
        client=site_web_api_client, sport=SportEnum.FOOTBALL, league=LeagueEnum.NFL
    )

    assert response.status_code == 200
    assert isinstance(response.parsed, SeasonInfoResponse), (
        "Response should be SeasonInfoResponse"
    )
    result = response.parsed

    # Check known mappings for NFL
    type_mapping = {
        1: "Preseason",
        2: "Regular Season",
        3: "Postseason",
        4: "Off Season",
    }

    for season_type in result.types:
        if season_type.type in type_mapping:
            assert season_type.name == type_mapping[season_type.type], (
                f"Type {season_type.type} should be '{type_mapping[season_type.type]}', got '{season_type.name}'"
            )
