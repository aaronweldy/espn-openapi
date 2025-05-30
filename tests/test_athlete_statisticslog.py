"""
Test athlete statistics log endpoints across different sports.
"""

import pytest
from models.sports_core_api.espn_sports_core_api_client.api.default.get_athlete_statistics_log import (
    sync_detailed,
)
from models.sports_core_api.espn_sports_core_api_client.models.athlete_statistics_log_response import (
    AthleteStatisticsLogResponse,
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
class TestAthleteStatisticsLog:
    """Test athlete statistics log endpoints for various sports."""

    @pytest.mark.parametrize(
        "sport,league,athlete_id,athlete_name",
        [
            ("football", "nfl", "3139477", "Patrick Mahomes"),  # NFL QB
            ("basketball", "nba", "6583", "LeBron James"),  # NBA Player
            ("baseball", "mlb", "33192", "Aaron Judge"),  # MLB Player
            ("hockey", "nhl", "3024816", "Austin Czarnik"),  # NHL Player
        ],
    )
    def test_get_athlete_statistics_log_success(
        self, sports_core_api_client, sport, league, athlete_id, athlete_name
    ):
        """Test getting athlete statistics log for various sports and athletes."""
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
        assert isinstance(result, AthleteStatisticsLogResponse), (
            "Response should parse to AthleteStatisticsLogResponse"
        )

        # Verify required fields
        assert result.ref, "Response should have a $ref field"
        assert result.entries, "Response should have entries"

        # Verify entries structure
        for entry in result.entries:
            assert entry.season, "Entry should have a season"
            assert entry.season.ref, "Season should have a $ref"
            assert entry.statistics, "Entry should have statistics"

            # Verify statistics structure
            for stat in entry.statistics:
                assert stat.type, "Statistic should have a type"
                assert stat.statistics, "Statistic should have statistics"
                assert stat.statistics.ref, "Statistics should have a $ref"

    def test_get_athlete_statistics_log_invalid_athlete(self, sports_core_api_client):
        """Test getting athlete statistics log for a non-existent athlete."""
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

    @pytest.mark.parametrize(
        "sport,league",
        [
            ("football", "nfl"),
            ("baseball", "mlb"),
            ("basketball", "nba"),
            ("hockey", "nhl"),
        ],
    )
    def test_get_athlete_statistics_log_sport_coverage(
        self, sports_core_api_client, sport, league
    ):
        """Test that the statistics log endpoint works for all major sports."""
        # Use known athletes for each sport
        athlete_ids = {
            ("football", "nfl"): "3139477",  # Patrick Mahomes
            ("baseball", "mlb"): "33192",  # Aaron Judge
            ("basketball", "nba"): "6583",  # LeBron James
            ("hockey", "nhl"): "3024816",  # Austin Czarnik
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

        # Should get a successful response
        assert response.status_code == 200, (
            f"Expected status code 200 for {sport}/{league}, got {response.status_code}"
        )

        result = response.parsed
        assert isinstance(result, AthleteStatisticsLogResponse), (
            f"Response for {sport}/{league} should parse to AthleteStatisticsLogResponse"
        )
        assert result.entries, f"Response for {sport}/{league} should have entries"