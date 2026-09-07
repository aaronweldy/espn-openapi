import pytest
import json
from models.site_web_api.espn_site_web_api_client.api.default import get_team_leaders
from models.site_web_api.espn_site_web_api_client.models.team_leaders_response import TeamLeadersResponse


def skip_on_transient_gateway_error(response, description):
    """Skip instead of failing when ESPN's gateway times out upstream.

    The teamleaders endpoint intermittently returns 502/503/504 ("timeout
    occurred waiting for core endpoint") on a cold cache, which survives all
    retries and is unrelated to the response shape under test.
    """
    if response.status_code in [502, 503, 504]:
        pytest.skip(
            f"Transient gateway error ({response.status_code}) for {description}"
        )


@pytest.mark.api
def test_get_nfl_teamleaders(site_web_api_client, ensure_json_output_dir):
    """Test NFL team leaders endpoint."""
    response = get_team_leaders.sync_detailed(
        client=site_web_api_client,
        sport="football",
        league="nfl"
    )

    skip_on_transient_gateway_error(response, "football/nfl")

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    result = response.parsed
    assert isinstance(result, TeamLeadersResponse), "Response should parse to TeamLeadersResponse"

    # Validate structure
    assert result.current_season, "Should have current season"
    assert result.requested_season, "Should have requested season"
    assert result.team_leaders, "Should have team leaders"
    
    # Check team leaders structure
    assert result.team_leaders.categories, "Should have categories"
    assert len(result.team_leaders.categories) > 0, "Should have at least one category"
    
    # Check first category
    first_category = result.team_leaders.categories[0]
    assert first_category.display_name, "Category should have display name"
    assert first_category.name, "Category should have name"
    assert first_category.abbreviation, "Category should have abbreviation"
    assert first_category.leaders, "Category should have leaders"
    
    # Check first leader
    if first_category.leaders:
        first_leader = first_category.leaders[0]
        assert first_leader.display_value, "Leader should have display value"
        assert first_leader.value is not None, "Leader should have numeric value"
        assert first_leader.ranks, "Leader should have rank"
        assert first_leader.team, "Leader should have team"
        
        # Check team structure
        team = first_leader.team
        assert team.id, "Team should have ID"
        assert team.display_name, "Team should have display name"
        assert team.abbreviation, "Team should have abbreviation"
    
    # Save response for analysis
    with open(f"{ensure_json_output_dir}/nfl_teamleaders_test.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)


@pytest.mark.api
@pytest.mark.parametrize("sport,league", [
    ("basketball", "nba"),
    ("baseball", "mlb"),
    ("hockey", "nhl"),
    ("basketball", "wnba"),
    ("football", "college-football"),
    ("basketball", "mens-college-basketball"),
    ("basketball", "womens-college-basketball"),
])
def test_get_teamleaders_cross_sport(site_web_api_client, sport, league):
    """Test team leaders endpoint across different sports and leagues."""
    response = get_team_leaders.sync_detailed(
        client=site_web_api_client,
        sport=sport,
        league=league
    )

    skip_on_transient_gateway_error(response, f"{sport}/{league}")

    assert response.status_code == 200, f"Expected status code 200 for {sport}/{league}, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, TeamLeadersResponse), f"Response should parse to TeamLeadersResponse for {sport}/{league}"
    
    # Basic structure validation
    assert result.current_season, f"Should have current season for {sport}/{league}"
    assert result.team_leaders, f"Should have team leaders for {sport}/{league}"
    assert result.team_leaders.categories, f"Should have categories for {sport}/{league}"


@pytest.mark.api
def test_get_teamleaders_with_season(site_web_api_client):
    """Test team leaders endpoint with season parameter."""
    response = get_team_leaders.sync_detailed(
        client=site_web_api_client,
        sport="football",
        league="nfl",
        season=2023
    )

    skip_on_transient_gateway_error(response, "football/nfl season=2023")

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, TeamLeadersResponse), "Response should parse to TeamLeadersResponse"
    
    # Check that requested season matches
    assert result.requested_season.year == 2023, "Requested season should be 2023"