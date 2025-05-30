"""
Test athlete statistics endpoints across different sports.
"""

import pytest
from models.sports_core_api.espn_sports_core_api_client.api.default.get_athlete_statistics import (
    sync_detailed,
)
from models.sports_core_api.espn_sports_core_api_client.models.athlete_statistics_response import (
    AthleteStatisticsResponse,
)
from models.sports_core_api.espn_sports_core_api_client.models.error_response import (
    ErrorResponse,
)
from models.sports_core_api.espn_sports_core_api_client.models.sport_enum import (
    SportEnum,
)
from models.sports_core_api.espn_sports_core_api_client.models.league_enum import (
    LeagueEnum,
)


@pytest.mark.api
class TestAthleteStatistics:
    """Test athlete statistics endpoints for various sports."""

    @pytest.mark.parametrize(
        "sport,league,athlete_id,athlete_name",
        [
            ("football", "nfl", "3139477", "Patrick Mahomes"),  # NFL QB
            ("baseball", "mlb", "1759", "MLB Player"),  # MLB Player
            ("basketball", "nba", "6583", "LeBron James"),  # NBA Player
            ("hockey", "nhl", "3024816", "NHL Player"),  # NHL Player
            ("football", "nfl", "4426502", "Travis Kelce"),  # NFL TE
            ("baseball", "mlb", "33192", "MLB Player 2"),  # Another MLB Player
        ],
    )
    def test_get_athlete_statistics_success(
        self, sports_core_api_client, sport, league, athlete_id, athlete_name
    ):
        """Test getting athlete statistics for various sports and athletes."""
        response = sync_detailed(
            sport=SportEnum(sport),
            league=LeagueEnum(league),
            athlete_id=athlete_id,
            client=sports_core_api_client,
        )

        assert response.status_code == 200, (
            f"Expected status code 200, got {response.status_code}"
        )

        # Parse the response
        result = response.parsed
        assert isinstance(result, AthleteStatisticsResponse), (
            "Response should parse to AthleteStatisticsResponse"
        )

        # Verify required fields
        assert result.ref, "Response should have a $ref field"
        assert result.athlete, "Response should have an athlete field"
        assert result.athlete.ref, "Athlete should have a $ref field"
        assert result.splits, "Response should have a splits field"

        # Verify splits structure
        assert result.splits.id, "Splits should have an id"
        assert result.splits.name, "Splits should have a name"
        assert result.splits.abbreviation, "Splits should have an abbreviation"
        assert result.splits.categories, "Splits should have categories"

        # Verify categories structure
        for category in result.splits.categories:
            assert category.name, "Category should have a name"
            assert category.display_name, "Category should have a display_name"
            assert category.abbreviation, "Category should have an abbreviation"
            assert category.stats, "Category should have stats"

            # Verify stats structure
            for stat in category.stats:
                assert stat.name, "Stat should have a name"
                assert stat.display_name, "Stat should have a display_name"
                assert stat.abbreviation, "Stat should have an abbreviation"
                assert stat.value is not None, "Stat should have a value"
                assert stat.display_value, "Stat should have a display_value"

    @pytest.mark.parametrize(
        "sport,league,athlete_id",
        [
            ("football", "nfl", "3139477"),  # NFL
            ("baseball", "mlb", "1759"),  # MLB
            ("basketball", "nba", "6583"),  # NBA
            ("hockey", "nhl", "3024816"),  # NHL
        ],
    )
    def test_get_athlete_statistics_with_query_params(
        self, sports_core_api_client, sport, league, athlete_id
    ):
        """Test getting athlete statistics with various query parameters."""
        # Test with limit parameter
        response = sync_detailed(
            sport=SportEnum(sport),
            league=LeagueEnum(league),
            athlete_id=athlete_id,
            client=sports_core_api_client,
            limit=50,
        )

        assert response.status_code == 200, (
            f"Expected status code 200, got {response.status_code}"
        )
        result = response.parsed
        assert isinstance(result, AthleteStatisticsResponse), (
            "Response should parse to AthleteStatisticsResponse"
        )

    @pytest.mark.parametrize(
        "sport,league,athlete_id",
        [
            ("basketball", "nba", "4432932"),  # NBA athlete that might not have stats
            ("hockey", "nhl", "4003240"),  # NHL athlete that might not have stats
        ],
    )
    def test_get_athlete_statistics_no_stats_found(
        self, sports_core_api_client, sport, league, athlete_id
    ):
        """Test getting athlete statistics for athletes that might not have statistics available."""
        response = sync_detailed(
            sport=SportEnum(sport),
            league=LeagueEnum(league),
            athlete_id=athlete_id,
            client=sports_core_api_client,
        )

        # This could be either 200 with data or 404 with no stats found
        if response.status_code == 404:
            # Parse as error response
            error_result = response.parsed
            assert isinstance(error_result, ErrorResponse), (
                "404 response should parse to ErrorResponse"
            )
            assert error_result.error, "Error response should have error field"
            assert error_result.error.message, "Error should have a message"
        elif response.status_code == 200:
            # Parse as successful response
            result = response.parsed
            assert isinstance(result, AthleteStatisticsResponse), (
                "200 response should parse to AthleteStatisticsResponse"
            )
        else:
            pytest.fail(f"Unexpected status code: {response.status_code}")

    def test_get_athlete_statistics_invalid_athlete(self, sports_core_api_client):
        """Test getting athlete statistics for a non-existent athlete."""
        response = sync_detailed(
            sport=SportEnum("football"),
            league=LeagueEnum("nfl"),
            athlete_id="999999999",  # Non-existent athlete
            client=sports_core_api_client,
        )

        # Should return 404 for non-existent athlete
        assert response.status_code == 404, (
            f"Expected status code 404, got {response.status_code}"
        )

        error_result = response.parsed
        assert isinstance(error_result, ErrorResponse), (
            "404 response should parse to ErrorResponse"
        )

    def test_get_athlete_statistics_invalid_sport_league(self, sports_core_api_client):
        """Test getting athlete statistics with invalid sport/league combination."""
        # Note: This test may not work as expected since the enums will validate the values
        # But we can test with valid enum values that might not have data
        response = sync_detailed(
            sport=SportEnum("tennis"),
            league=LeagueEnum("atp"),
            athlete_id="3139477",
            client=sports_core_api_client,
        )

        # Should return 400 or 404 for invalid sport/league
        assert response.status_code in [400, 404], (
            f"Expected status code 400 or 404, got {response.status_code}"
        )

    @pytest.mark.parametrize(
        "sport,league",
        [
            ("football", "nfl"),
            ("baseball", "mlb"),
            ("basketball", "nba"),
            ("hockey", "nhl"),
        ],
    )
    def test_get_athlete_statistics_sport_specific_categories(
        self, sports_core_api_client, sport, league
    ):
        """Test that different sports return appropriate statistical categories."""
        # Use known athletes for each sport
        athlete_ids = {
            ("football", "nfl"): "3139477",  # Patrick Mahomes
            ("baseball", "mlb"): "1759",  # MLB player
            ("basketball", "nba"): "6583",  # LeBron James
            ("hockey", "nhl"): "3024816",  # NHL player
        }

        athlete_id = athlete_ids.get((sport, league))
        if not athlete_id:
            pytest.skip(f"No test athlete defined for {sport}/{league}")

        response = sync_detailed(
            sport=SportEnum(sport),
            league=LeagueEnum(league),
            athlete_id=athlete_id,
            client=sports_core_api_client,
        )

        if response.status_code == 404:
            pytest.skip(
                f"No statistics available for {sport}/{league} athlete {athlete_id}"
            )

        assert response.status_code == 200, (
            f"Expected status code 200, got {response.status_code}"
        )

        result = response.parsed
        assert isinstance(result, AthleteStatisticsResponse), (
            "Response should parse to AthleteStatisticsResponse"
        )

        # Check for sport-specific categories
        category_names = [cat.name for cat in result.splits.categories]

        if sport == "football":
            # NFL should have passing, rushing, receiving, defensive categories
            expected_categories = ["passing", "rushing", "receiving"]
            for expected in expected_categories:
                if expected in category_names:
                    break
            else:
                pytest.fail(
                    f"Expected at least one of {expected_categories} in NFL categories: {category_names}"
                )

        elif sport == "baseball":
            # MLB should have batting, fielding, pitching categories
            expected_categories = ["batting", "fielding"]
            for expected in expected_categories:
                if expected in category_names:
                    break
            else:
                pytest.fail(
                    f"Expected at least one of {expected_categories} in MLB categories: {category_names}"
                )

        elif sport == "basketball":
            # NBA should have offensive, defensive, general categories
            expected_categories = ["offensive", "defensive", "general"]
            for expected in expected_categories:
                if expected in category_names:
                    break
            else:
                pytest.fail(
                    f"Expected at least one of {expected_categories} in NBA categories: {category_names}"
                )
