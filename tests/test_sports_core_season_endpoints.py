import pytest
from models.sports_core_api.espn_sports_core_api_client.models.paginated_reference_list_response import (
    PaginatedReferenceListResponse,
)
from models.sports_core_api.espn_sports_core_api_client.models.stat_corrections_response import (
    StatCorrectionsResponse,
)
from models.sports_core_api.espn_sports_core_api_client.models.reference import (
    Reference,
)
from models.sports_core_api.espn_sports_core_api_client.models.sport_enum import (
    SportEnum,
)
from models.sports_core_api.espn_sports_core_api_client.models.league_enum import (
    LeagueEnum,
)
from models.sports_core_api.espn_sports_core_api_client.models.get_league_season_groups_season_type import (
    GetLeagueSeasonGroupsSeasonType,
)
from models.sports_core_api.espn_sports_core_api_client.models.get_league_season_weeks_season_type import (
    GetLeagueSeasonWeeksSeasonType,
)
from models.sports_core_api.espn_sports_core_api_client.models.get_league_season_corrections_season_type import (
    GetLeagueSeasonCorrectionsSeasonType,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_league_season_groups import (
    sync_detailed as get_league_season_groups,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_league_season_weeks import (
    sync_detailed as get_league_season_weeks,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_league_season_corrections import (
    sync_detailed as get_league_season_corrections,
)


@pytest.mark.api
def test_get_league_season_groups(sports_core_api_client, ensure_json_output_dir):
    """Test the groups endpoint for NFL 2024 regular season."""
    response = get_league_season_groups(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2024,
        season_type=GetLeagueSeasonGroupsSeasonType.VALUE_2,  # regular season
    )

    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, PaginatedReferenceListResponse), (
        "Response should parse to PaginatedReferenceListResponse"
    )

    # Should have 2 groups for NFL (AFC and NFC)
    assert result.count == 2, f"Expected 2 groups for NFL, got {result.count}"
    assert result.page_index == 1, "Page index should be 1"
    assert result.page_count == 1, "Page count should be 1"
    assert len(result.items) == 2, f"Expected 2 items, got {len(result.items)}"

    # Verify all items are Reference objects
    for item in result.items:
        assert isinstance(item, Reference), "Each item should be a Reference"
        assert item.ref, "Each reference should have a $ref URL"
        assert "groups" in item.ref, "Reference URL should contain 'groups'"


@pytest.mark.api
def test_get_league_season_weeks(sports_core_api_client, ensure_json_output_dir):
    """Test the weeks endpoint for NFL 2024 regular season."""
    response = get_league_season_weeks(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2024,
        season_type=GetLeagueSeasonWeeksSeasonType.VALUE_2,  # regular season
    )

    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, PaginatedReferenceListResponse), (
        "Response should parse to PaginatedReferenceListResponse"
    )

    # NFL regular season should have 18 weeks
    assert result.count == 18, (
        f"Expected 18 weeks for NFL regular season, got {result.count}"
    )
    assert result.page_index == 1, "Page index should be 1"
    assert result.page_count == 1, "Page count should be 1"
    assert len(result.items) == 18, f"Expected 18 items, got {len(result.items)}"

    # Verify all items are Reference objects
    for item in result.items:
        assert isinstance(item, Reference), "Each item should be a Reference"
        assert item.ref, "Each reference should have a $ref URL"
        assert "weeks" in item.ref, "Reference URL should contain 'weeks'"


@pytest.mark.api
def test_get_league_season_corrections(sports_core_api_client, ensure_json_output_dir):
    """Test the corrections endpoint for NFL 2024 regular season."""
    response = get_league_season_corrections(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2024,
        season_type=GetLeagueSeasonCorrectionsSeasonType.VALUE_2,  # regular season
    )

    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, StatCorrectionsResponse), (
        "Response should parse to StatCorrectionsResponse"
    )

    # Basic pagination structure
    assert hasattr(result, "count"), "Response should have count field"
    assert hasattr(result, "page_index"), "Response should have page_index field"
    assert hasattr(result, "page_size"), "Response should have page_size field"
    assert hasattr(result, "page_count"), "Response should have page_count field"
    assert hasattr(result, "items"), "Response should have items field"

    # If there are corrections, verify their structure
    if result.count > 0:
        assert len(result.items) > 0, "Should have items if count > 0"

        # Check first correction item structure
        first_correction = result.items[0]
        assert hasattr(first_correction, "split_stats"), (
            "Correction should have split_stats"
        )
        assert hasattr(first_correction, "competition"), (
            "Correction should have competition"
        )
        assert hasattr(first_correction, "athlete"), "Correction should have athlete"
        assert hasattr(first_correction, "team"), "Correction should have team"

        # Verify split_stats structure
        split_stats = first_correction.split_stats
        assert hasattr(split_stats, "id"), "SplitStats should have id"
        assert hasattr(split_stats, "name"), "SplitStats should have name"
        assert hasattr(split_stats, "abbreviation"), (
            "SplitStats should have abbreviation"
        )
        assert hasattr(split_stats, "categories"), "SplitStats should have categories"

        if split_stats.categories:
            # Check first category structure
            first_category = split_stats.categories[0]
            assert hasattr(first_category, "name"), "Category should have name"
            assert hasattr(first_category, "display_name"), (
                "Category should have display_name"
            )
            assert hasattr(first_category, "stats"), "Category should have stats"

            if first_category.stats:
                # Check first stat structure
                first_stat = first_category.stats[0]
                assert hasattr(first_stat, "name"), "Stat should have name"
                assert hasattr(first_stat, "display_name"), (
                    "Stat should have display_name"
                )
                assert hasattr(first_stat, "value"), "Stat should have value"
                assert hasattr(first_stat, "display_value"), (
                    "Stat should have display_value"
                )
    else:
        # If no corrections, items should be empty
        assert len(result.items) == 0, "Should have no items if count is 0"


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league",
    [
        (SportEnum.FOOTBALL, LeagueEnum.NFL),
        (SportEnum.BASKETBALL, LeagueEnum.NBA),
    ],
)
def test_get_league_season_groups_multiple_sports(
    sports_core_api_client, sport, league
):
    """Test the groups endpoint for multiple sports."""
    response = get_league_season_groups(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=2024,
        season_type=GetLeagueSeasonGroupsSeasonType.VALUE_2,  # regular season
    )

    assert response.status_code == 200, (
        f"Expected status code 200 for {sport}/{league}, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, PaginatedReferenceListResponse), (
        f"Response should parse to PaginatedReferenceListResponse for {sport}/{league}"
    )

    # Should have at least 2 groups for major leagues
    assert result.count >= 2, (
        f"Expected at least 2 groups for {sport}/{league}, got {result.count}"
    )


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league",
    [
        (SportEnum.FOOTBALL, LeagueEnum.NFL),
        (SportEnum.BASKETBALL, LeagueEnum.NBA),
    ],
)
def test_get_league_season_weeks_multiple_sports(sports_core_api_client, sport, league):
    """Test the weeks endpoint for multiple sports."""
    response = get_league_season_weeks(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=2024,
        season_type=GetLeagueSeasonWeeksSeasonType.VALUE_2,  # regular season
    )

    assert response.status_code == 200, (
        f"Expected status code 200 for {sport}/{league}, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, PaginatedReferenceListResponse), (
        f"Response should parse to PaginatedReferenceListResponse for {sport}/{league}"
    )

    # Should have at least 1 week for any league
    assert result.count >= 1, (
        f"Expected at least 1 week for {sport}/{league}, got {result.count}"
    )
