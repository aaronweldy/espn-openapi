import pytest
import logging
from models.site_web_api.espn_site_web_api_client.api.default import get_league_leaders
from models.site_web_api.espn_site_web_api_client.models.leaders_response import LeadersResponse
from models.site_web_api.espn_site_web_api_client.types import UNSET

logging.basicConfig(level=logging.INFO)


@pytest.mark.api
@pytest.mark.flaky(retries=3, delay=2)
@pytest.mark.parametrize("sport,league", [
    ("football", "nfl"),
    ("hockey", "nhl"),
    ("basketball", "mens-college-basketball"),
    ("basketball", "nba"),
    ("baseball", "mlb"),
])
def test_get_league_leaders(site_web_api_client, ensure_json_output_dir, sport, league):
    """Test getting league leaders for different sports."""
    response = get_league_leaders.sync_detailed(
        client=site_web_api_client,
        sport=sport,
        league=league
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code} for {sport}/{league}"
    
    result = response.parsed
    assert isinstance(result, LeadersResponse), f"Response should be an LeagueLeadersResponse for {sport}/{league}"
    
    # Validate response structure
    assert result.current_season, "Response should have current season"
    assert result.requested_season, "Response should have requested season"
    assert result.leaders, "Response should have leaders"
    assert result.league, "Response should have league info"
    
    # Validate leaders structure
    assert result.leaders.categories, "Leaders should have categories"
    assert len(result.leaders.categories) > 0, "Should have at least one category"
    
    # Log some interesting info
    logging.info(f"\n{sport.upper()} {league.upper()} Leaders:")
    logging.info(f"  Current Season: {result.current_season.year}")
    logging.info(f"  Number of categories: {len(result.leaders.categories)}")
    
    # Check first category
    first_category = result.leaders.categories[0]
    logging.info(f"  First category: {first_category.display_name} ({first_category.abbreviation})")
    
    if first_category.leaders:
        leader = first_category.leaders[0]
        logging.info(f"  Leader: {leader.athlete.display_name} - {leader.display_value}")
        if leader.team:
            logging.info(f"  Team: {leader.team.display_name}")
    
    # Save response for analysis
    import json
    with open(f"{ensure_json_output_dir}/site_v3_{league}_leaders_test.json", "w") as f:
        assert response
        json.dump(response.parsed.to_dict(), f, indent=2)


@pytest.mark.api
def test_get_league_leaders_with_season(site_web_api_client):
    """Test getting league leaders with specific season parameter."""
    response = get_league_leaders.sync_detailed(
        client=site_web_api_client,
        sport="football",
        league="nfl",
        season=2023
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert isinstance(response.parsed, LeadersResponse), f"Response should be an LeagueLeadersResponse"
    
    result = response.parsed
    assert result, "Response should parse successfully"
    assert result.requested_season.year == 2023, "Requested season should be 2023"


