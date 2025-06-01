import pytest
import json
from models.sports_core_api.espn_sports_core_api_client.models import CalendarListResponse, Reference, CoachDetailsResponse
from models.sports_core_api.espn_sports_core_api_client.models.sport_enum import SportEnum
from models.sports_core_api.espn_sports_core_api_client.models.league_enum import LeagueEnum
from models.sports_core_api.espn_sports_core_api_client.api.default import get_season_coaches, get_season_coach_details
from models.sports_core_api.espn_sports_core_api_client.types import UNSET


@pytest.mark.api
@pytest.mark.parametrize("sport,league,year", [
    (SportEnum.FOOTBALL, LeagueEnum.NFL, 2024),
    (SportEnum.BASKETBALL, LeagueEnum.NBA, 2024),
    (SportEnum.BASEBALL, LeagueEnum.MLB, 2024),
    (SportEnum.HOCKEY, LeagueEnum.NHL, 2024),
])
def test_get_season_coaches(sports_core_api_client, ensure_json_output_dir, sport, league, year):
    """Test retrieving coaches list for different sports."""
    response = get_season_coaches.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=year,
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, CalendarListResponse), "Response should parse to CalendarListResponse"
    
    # Validate response structure
    assert result.count > 0, "Should have at least one coach"
    assert result.page_index == 1, "Default page index should be 1"
    assert result.page_size > 0, "Page size should be positive"
    assert result.page_count >= 1, "Should have at least one page"
    assert result.items, "Items list should not be empty"
    
    # Validate that items are References
    for item in result.items:
        assert isinstance(item, Reference), "Each item should be a Reference"
        assert item.ref, "Reference should have a $ref URL"
        assert item.ref.startswith("http"), "Reference URL should start with http"
        assert f"/coaches/" in item.ref, "Reference URL should contain /coaches/"
        assert str(year) in item.ref, "Reference URL should contain the year"
    
    # Save response for analysis
    response_dict = {
        "count": result.count,
        "pageIndex": result.page_index,
        "pageSize": result.page_size,
        "pageCount": result.page_count,
        "items": [{"$ref": item.ref} for item in result.items]
    }
    
    filename = f"coaches_{sport.value}_{league.value}_{year}_test.json"
    with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
        json.dump(response_dict, f, indent=2)
    
    print(f"Successfully retrieved {result.count} coaches for {sport.value}/{league.value} {year}")


@pytest.mark.api
def test_get_season_coaches_pagination(sports_core_api_client):
    """Test pagination parameters for coaches endpoint."""
    # Test with custom page size
    response = get_season_coaches.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2024,
        limit=10,
        page=2,
    )
    
    if response.status_code == 200:
        result = response.parsed
        assert result.page_size <= 10, "Page size should respect the limit parameter"
        assert result.page_index == 2, "Page index should match the requested page"


@pytest.mark.api
def test_get_season_coaches_invalid_year(sports_core_api_client):
    """Test coaches endpoint with invalid year."""
    response = get_season_coaches.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=1900,  # Too old
    )
    
    # ESPN might return 200 with empty results or 404
    assert response.status_code in [200, 404], f"Expected 200 or 404 for invalid year, got {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        # If 200, it might have 0 coaches
        assert result.count == 0, "Should have no coaches for invalid year"


@pytest.mark.api
@pytest.mark.parametrize("sport,league,year,coach_id", [
    (SportEnum.FOOTBALL, LeagueEnum.NFL, 2024, "17751"),
    (SportEnum.BASKETBALL, LeagueEnum.NBA, 2024, "52120"),
])
def test_get_season_coach_details(sports_core_api_client, ensure_json_output_dir, sport, league, year, coach_id):
    """Test retrieving details for a specific coach."""
    response = get_season_coach_details.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=year,
        coach_id=coach_id,
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, CoachDetailsResponse), "Response should parse to CoachDetailsResponse"
    
    # Validate response structure
    assert result.id == coach_id, f"Coach ID should match requested ID {coach_id}"
    assert result.first_name, "Coach should have a first name"
    assert result.last_name, "Coach should have a last name"
    
    # Optional fields that may be present
    if result.uid:
        assert f"co:{coach_id}" in result.uid, "UID should contain coach ID"
    
    if result.date_of_birth:
        # Date is parsed as datetime object
        from datetime import datetime
        assert isinstance(result.date_of_birth, datetime), "Date of birth should be a datetime object"
    
    if result.experience is not UNSET:
        assert isinstance(result.experience, int), "Experience should be an integer"
        assert result.experience >= 0, "Experience should be non-negative"
    
    if result.team:
        assert isinstance(result.team, Reference), "Team should be a Reference"
        assert result.team.ref, "Team reference should have a URL"
    
    if result.records:
        assert isinstance(result.records, list), "Records should be a list"
    
    # Save response for analysis
    with open(f"{ensure_json_output_dir}/coach_{sport.value}_{league.value}_{year}_{coach_id}.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    print(f"Successfully retrieved coach details: {result.first_name} {result.last_name} ({sport.value}/{league.value})")


@pytest.mark.api  
def test_get_season_coach_details_invalid_id(sports_core_api_client):
    """Test coach details endpoint with invalid ID."""
    response = get_season_coach_details.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2024,
        coach_id="99999999",  # Invalid ID
    )
    
    assert response.status_code == 404, f"Expected 404 for invalid coach ID, got {response.status_code}"