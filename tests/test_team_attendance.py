import pytest
import json
import logging
from models.sports_core_api.espn_sports_core_api_client.api.default import get_team_attendance
from models.sports_core_api.espn_sports_core_api_client.models import (
    SportEnum,
    LeagueEnum,
    TeamAttendanceResponse,
    AttendanceCategory,
    AttendanceStat,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league,year,seasontype,team_id,team_name",
    [
        (SportEnum.FOOTBALL, LeagueEnum.NFL, 2024, 2, "12", "Kansas City Chiefs"),
        (SportEnum.BASKETBALL, LeagueEnum.NBA, 2024, 2, "13", "Los Angeles Lakers"),
        (SportEnum.BASEBALL, LeagueEnum.MLB, 2024, 2, "10", "New York Yankees"),
        pytest.param(SportEnum.HOCKEY, LeagueEnum.NHL, 2024, 2, "10", "Toronto Maple Leafs", marks=pytest.mark.xfail(reason="NHL may not have attendance data for all teams")),
    ],
)
def test_get_team_attendance(
    sports_core_api_client,
    ensure_json_output_dir,
    sport,
    league,
    year,
    seasontype,
    team_id,
    team_name,
):
    """Test getting team attendance statistics across different sports."""
    response = get_team_attendance.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=year,
        seasontype=seasontype,
        team_id=team_id,
    )

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, TeamAttendanceResponse), "Response should parse to TeamAttendanceResponse"
    
    # Validate basic fields
    assert result.ref, "Should have a reference URL"
    assert result.id is not None, "Should have an ID"
    assert result.name, "Should have a name"
    assert result.abbreviation, "Should have an abbreviation"
    assert result.categories, "Should have categories"
    
    # Validate categories
    assert len(result.categories) > 0, "Should have at least one category"
    
    # Check for standard categories (home, away, all/overall)
    category_names = [cat.name for cat in result.categories]
    logger.info(f"Found attendance categories for {team_name}: {category_names}")
    
    # Validate each category
    for category in result.categories:
        assert isinstance(category, AttendanceCategory), "Category should be AttendanceCategory"
        assert category.name, "Category should have a name"
        assert category.display_name, "Category should have a display name"
        assert category.stats, "Category should have stats"
        
        # Validate stats in each category
        for stat in category.stats:
            assert isinstance(stat, AttendanceStat), "Stat should be AttendanceStat"
            assert stat.name, "Stat should have a name"
            assert stat.display_name, "Stat should have a display name"
            assert stat.abbreviation, "Stat should have an abbreviation"
            assert stat.value is not None, "Stat should have a value"
            assert stat.display_value, "Stat should have a display value"
            
            # Log some interesting stats
            if stat.name == "avg" and category.name == "home":
                logger.info(f"{team_name} home average attendance: {stat.display_value}")
            elif stat.name == "total" and category.name == "all":
                logger.info(f"{team_name} total attendance: {stat.display_value}")
    
    # Save response for first sport
    if sport == SportEnum.FOOTBALL:
        filename = f"{sport.value}_{league.value}_team_attendance_{year}.json"
        with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
        logger.info(f"✓ Saved attendance data to {filename}")


@pytest.mark.api
def test_team_attendance_invalid_team(sports_core_api_client):
    """Test requesting attendance for an invalid team ID."""
    response = get_team_attendance.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2024,
        seasontype=2,
        team_id="99999",  # Invalid team ID
    )
    
    # ESPN API returns 404 for invalid team
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"


@pytest.mark.api
def test_team_attendance_future_season(sports_core_api_client):
    """Test requesting attendance for a future season."""
    response = get_team_attendance.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2026,  # Future season
        seasontype=2,
        team_id="12",
    )
    
    # Future seasons might return 404 or empty data
    assert response.status_code in [404, 200], f"Unexpected status code: {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        # Future season might have zero values
        if result and result.categories:
            for category in result.categories:
                for stat in category.stats:
                    if stat.name == "games":
                        logger.info(f"Games for future season: {stat.value}")