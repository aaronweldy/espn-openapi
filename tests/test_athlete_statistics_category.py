"""Tests for athlete statistics by category endpoints."""
import pytest
import json
from models.sports_core_api.espn_sports_core_api_client.api.default import get_athlete_statistics_by_category
from models.sports_core_api.espn_sports_core_api_client.models.sport_enum import SportEnum
from models.sports_core_api.espn_sports_core_api_client.models.league_enum import LeagueEnum


@pytest.mark.api
@pytest.mark.parametrize("sport,league,athlete_id", [
    (SportEnum.FOOTBALL, LeagueEnum.NFL, "3139477"),  # Patrick Mahomes
    (SportEnum.BASKETBALL, LeagueEnum.NBA, "1966"),   # LeBron James 
    (SportEnum.BASEBALL, LeagueEnum.MLB, "33912"),    # Mookie Betts
])
def test_get_athlete_statistics_by_category(sports_core_api_client, ensure_json_output_dir, sport, league, athlete_id):
    """Test getting athlete statistics broken down by categories."""
    response = get_athlete_statistics_by_category.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        athlete_id=athlete_id,
        category_id="0"
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, "Response should parse to AthleteStatisticsByCategoryResponse"
    
    # Validate response structure
    assert result.ref, "Response should have a $ref field"
    assert result.athlete, "Response should have an athlete field"
    assert result.splits, "Response should have a splits field"
    
    # Validate splits structure
    assert result.splits.id == "0", "Splits should have id '0'"
    assert result.splits.name, "Splits should have a name"
    assert result.splits.categories, "Splits should have categories"
    assert len(result.splits.categories) > 0, "Should have at least one category"
    
    # Validate first category structure
    first_category = result.splits.categories[0]
    assert first_category.name, "Category should have a name"
    assert first_category.display_name, "Category should have a display name"
    assert first_category.stats, "Category should have stats"
    assert len(first_category.stats) > 0, "Category should have at least one stat"
    
    # Validate first stat structure
    first_stat = first_category.stats[0]
    assert first_stat.name, "Stat should have a name"
    assert first_stat.display_name, "Stat should have a display name"
    assert first_stat.abbreviation, "Stat should have an abbreviation"
    assert first_stat.value is not None, "Stat should have a value"
    assert first_stat.display_value, "Stat should have a display value"
    
    # Save response for reference
    if hasattr(result, 'to_dict'):
        filename = f"athlete_statistics_category_{sport.value}_{league.value}_{athlete_id}.json"
        with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
            json.dump(result.to_dict(), f, indent=2)


@pytest.mark.api
def test_get_athlete_statistics_by_category_invalid_athlete(sports_core_api_client):
    """Test getting statistics for an invalid athlete ID."""
    response = get_athlete_statistics_by_category.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        athlete_id="99999999",  # Invalid athlete ID
        category_id="0"
    )
    
    assert response.status_code == 404, f"Expected status code 404 for invalid athlete, got {response.status_code}"