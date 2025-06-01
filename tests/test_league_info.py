"""Tests for league information endpoints."""
import pytest
import json
from models.sports_core_api.espn_sports_core_api_client.api.default import get_league_info


@pytest.mark.api
def test_get_nfl_league_info(sports_core_api_client, ensure_json_output_dir):
    """Test getting NFL league information."""
    response = get_league_info.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl"
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, "Response should parse to LeagueInfoResponse"
    
    # Validate response fields
    assert result.id == "28"
    assert result.name == "National Football League"
    assert result.display_name == "NFL"
    assert result.abbreviation == "NFL"
    assert result.slug == "nfl"
    assert result.is_tournament is False
    
    # Check season info
    if result.season:
        assert result.season.year is not None
        assert result.season.display_name is not None
    
    # Save response for reference
    if hasattr(result, 'to_dict'):
        with open(f"{ensure_json_output_dir}/nfl_league_info_test.json", "w") as f:
            json.dump(result.to_dict(), f, indent=2)


@pytest.mark.api
def test_get_college_football_league_info(sports_core_api_client, ensure_json_output_dir):
    """Test getting college football league information."""
    response = get_league_info.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="college-football"
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, "Response should parse to LeagueInfoResponse"
    
    # Validate response fields
    assert result.id == "23"
    assert result.display_name == "NCAA Football"
    assert result.abbreviation == "NCAAF"
    assert result.slug == "college-football"
    
    # Save response for reference
    if hasattr(result, 'to_dict'):
        with open(f"{ensure_json_output_dir}/college_football_league_info_test.json", "w") as f:
            json.dump(result.to_dict(), f, indent=2)


@pytest.mark.api
@pytest.mark.parametrize("sport,league,expected_name", [
    ("football", "nfl", "National Football League"),
    ("basketball", "nba", "National Basketball Association"),
    ("baseball", "mlb", "Major League Baseball"),
    ("hockey", "nhl", "National Hockey League"),
    ("basketball", "wnba", "Women's National Basketball Association"),
    ("football", "college-football", "NCAA - Football"),
    ("basketball", "mens-college-basketball", "NCAA - Men's Basketball"),
    ("basketball", "womens-college-basketball", "NCAA - Women's Basketball"),
])
def test_get_multiple_leagues_info(sports_core_api_client, sport, league, expected_name):
    """Test getting information for multiple leagues."""
    response = get_league_info.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league
    )
    
    assert response.status_code == 200, f"Failed for {sport}/{league}: {response.status_code}"
    assert response.parsed is not None
    assert response.parsed.name == expected_name