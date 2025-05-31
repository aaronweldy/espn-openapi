"""Test rankings endpoints."""
import pytest
import json
import logging
from models.site_api.espn_nfl_api_client.api.default import get_rankings
from models.site_api.espn_nfl_api_client.models.rankings_response import RankingsResponse
from models.site_api.espn_nfl_api_client.types import UNSET

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize("sport,league,expected_rankings", [
    ("football", "college-football", ["AP Top 25", "AFCA Coaches Poll"]),
    ("basketball", "mens-college-basketball", ["AP Top 25"]),
    ("basketball", "womens-college-basketball", ["AP Top 25"]),
])
def test_get_rankings(site_api_client, ensure_json_output_dir, sport, league, expected_rankings):
    """Test getting rankings for college sports."""
    response = get_rankings.sync_detailed(
        client=site_api_client,
        sport=sport,
        league=league
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, RankingsResponse), "Response should parse to RankingsResponse"
    
    # Check that we have rankings
    assert result.rankings, f"Should have rankings for {sport}/{league}"
    
    # Check available rankings
    if result.available_rankings:
        available_names = [r.name for r in result.available_rankings if r.name]
        logger.info(f"Available rankings for {sport}/{league}: {available_names}")
    
    # Check that expected rankings are present
    ranking_names = [r.name for r in result.rankings if r.name]
    for expected in expected_rankings:
        assert any(expected in name for name in ranking_names), f"Expected to find '{expected}' in rankings"
    
    # Check first ranking details
    first_ranking = result.rankings[0]
    assert first_ranking.name, "First ranking should have a name"
    assert first_ranking.ranks, "First ranking should have ranks"
    
    # Check first ranked team
    if first_ranking.ranks:
        first_team = first_ranking.ranks[0]
        assert first_team.current, "First team should have current ranking"
        assert first_team.team, "First team should have team info"
        assert first_team.team.name, "Team should have a name"
        assert first_team.record_summary, "Team should have record summary"
        
        logger.info(f"{sport}/{league} - {first_ranking.name} #1: {first_team.team.name} ({first_team.record_summary})")
    
    # Check for teams receiving votes
    if first_ranking.others:
        logger.info(f"Teams receiving votes: {len(first_ranking.others)}")
    
    # Save response for analysis
    filename = f"{ensure_json_output_dir}/rankings_{sport}_{league.replace('-', '_')}.json"
    with open(filename, "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    logger.info(f"Saved rankings to {filename}")


@pytest.mark.api
@pytest.mark.parametrize("sport,league", [
    ("football", "nfl"),
    ("basketball", "nba"),
    ("baseball", "mlb"),
    ("hockey", "nhl"),
])
def test_rankings_not_available_for_pro_sports(site_api_client, sport, league):
    """Test that rankings endpoint returns 404 for professional sports."""
    response = get_rankings.sync_detailed(
        client=site_api_client,
        sport=sport,
        league=league
    )
    
    assert response.status_code == 404, f"Expected 404 for {sport}/{league} rankings, got {response.status_code}"
    logger.info(f"Confirmed: Rankings not available for {sport}/{league} (professional league)")


@pytest.mark.api
def test_rankings_with_season_and_week(site_api_client, ensure_json_output_dir):
    """Test getting rankings with specific season and week parameters."""
    response = get_rankings.sync_detailed(
        client=site_api_client,
        sport="football",
        league="college-football",
        season=2024,
        week=1
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, RankingsResponse), "Response should parse to RankingsResponse"
    
    # Check requested season
    if result.requested_season and result.requested_season.year:
        assert result.requested_season.year == 2024, "Requested season should be 2024"
    
    # Save response
    filename = f"{ensure_json_output_dir}/rankings_college_football_2024_week1.json"
    with open(filename, "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    logger.info(f"Saved 2024 week 1 rankings to {filename}")