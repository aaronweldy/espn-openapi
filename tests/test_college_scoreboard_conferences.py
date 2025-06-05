import pytest
import json
from models.site_api.espn_nfl_api_client.api.default import get_scoreboard
from models.site_api.espn_nfl_api_client.models.college_football_conference_enum import CollegeFootballConferenceEnum
from models.site_api.espn_nfl_api_client.models.college_basketball_conference_enum import CollegeBasketballConferenceEnum


# Conference mappings for readability
FOOTBALL_CONFERENCES = {
    "SEC": "8",
    "ACC": "1", 
    "BIG_TEN": "5",
    "BIG_12": "4",
    "PAC_12": "9",
    "ALL_FBS": "80"
}

BASKETBALL_CONFERENCES = {
    "ACC": "2",
    "SEC": "23",
    "BIG_TEN": "7",
    "BIG_12": "8",
    "BIG_EAST": "4",
    "NCAA_DIVISION_I": "50"
}


@pytest.mark.api
def test_college_football_scoreboard_with_conference(site_api_client, ensure_json_output_dir):
    """Test college football scoreboard filtered by conference."""
    # Test with SEC conference (ID: 8)
    response = get_scoreboard.sync_detailed(
        client=site_api_client,
        sport="football",
        league="college-football",
        groups=FOOTBALL_CONFERENCES["SEC"]
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should have parsed data"
    
    # Save response for analysis
    with open(f"{ensure_json_output_dir}/college_football_scoreboard_sec_filter.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    # Verify we have events
    if result.events:
        # When filtering by conference, all games should involve at least one SEC team
        print(f"Found {len(result.events)} SEC games")


@pytest.mark.api
def test_college_basketball_scoreboard_with_conference(site_api_client, ensure_json_output_dir):
    """Test college basketball scoreboard filtered by conference."""
    # Test with ACC conference (ID: 2)
    response = get_scoreboard.sync_detailed(
        client=site_api_client,
        sport="basketball",
        league="mens-college-basketball",
        groups=BASKETBALL_CONFERENCES["ACC"]
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result, "Response should have parsed data"
    
    # Save response for analysis
    with open(f"{ensure_json_output_dir}/college_basketball_scoreboard_acc_filter.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    # Verify we have events
    if result.events:
        print(f"Found {len(result.events)} ACC games")


@pytest.mark.api
def test_conference_enum_exists():
    """Test that conference enums were generated correctly."""
    # Check that football conference enum exists and has values
    football_values = [e.value for e in CollegeFootballConferenceEnum]
    assert "8" in football_values, "SEC (8) should be in football conference enum"
    assert "1" in football_values, "ACC (1) should be in football conference enum"
    assert "5" in football_values, "Big Ten (5) should be in football conference enum"
    assert "80" in football_values, "All FBS (80) should be in football conference enum"
    
    # Check that basketball conference enum exists and has values
    basketball_values = [e.value for e in CollegeBasketballConferenceEnum]
    assert "2" in basketball_values, "ACC (2) should be in basketball conference enum"
    assert "23" in basketball_values, "SEC (23) should be in basketball conference enum"
    assert "7" in basketball_values, "Big Ten (7) should be in basketball conference enum"
    assert "50" in basketball_values, "NCAA Division I (50) should be in basketball conference enum"
    
    print(f"Football conference enum has {len(football_values)} values")
    print(f"Basketball conference enum has {len(basketball_values)} values")


@pytest.mark.api
@pytest.mark.parametrize("conference_id,conference_name", [
    (FOOTBALL_CONFERENCES["SEC"], "SEC"),
    (FOOTBALL_CONFERENCES["ACC"], "ACC"),
    (FOOTBALL_CONFERENCES["BIG_TEN"], "Big Ten"),
    (FOOTBALL_CONFERENCES["BIG_12"], "Big 12"),
])
def test_multiple_football_conferences(site_api_client, conference_id, conference_name):
    """Test scoreboard with different football conferences."""
    response = get_scoreboard.sync_detailed(
        client=site_api_client,
        sport="football",
        league="college-football",
        groups=conference_id
    )
    
    assert response.status_code == 200, f"Failed to get {conference_name} scoreboard"
    result = response.parsed
    assert result, f"Response should have parsed data for {conference_name}"
    
    print(f"{conference_name} scoreboard: {len(result.events) if result.events else 0} games")