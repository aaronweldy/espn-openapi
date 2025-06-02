import pytest
import json
import logging
from models.sports_core_api.espn_sports_core_api_client.api.default import get_team_leaders
from models.sports_core_api.espn_sports_core_api_client.models import (
    SportEnum,
    LeagueEnum,
    TeamLeadersResponse,
    LeaderCategory,
    TeamLeader,
    Reference,
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
        (SportEnum.HOCKEY, LeagueEnum.NHL, 2024, 2, "10", "Toronto Maple Leafs"),
    ],
)
def test_get_team_leaders(
    sports_core_api_client,
    ensure_json_output_dir,
    sport,
    league,
    year,
    seasontype,
    team_id,
    team_name,
):
    """Test getting team leaders across different sports."""
    response = get_team_leaders.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=year,
        seasontype=seasontype,
        team_id=team_id,
    )

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, TeamLeadersResponse), "Response should parse to TeamLeadersResponse"
    
    # Validate basic fields
    assert result.ref, "Should have a reference URL"
    assert result.id is not None, "Should have an ID"
    assert result.name, "Should have a name"
    assert result.categories, "Should have categories"
    
    # Validate categories
    assert len(result.categories) > 0, "Should have at least one category"
    
    # Log category names for this sport
    category_names = [cat.name for cat in result.categories[:5]]
    logger.info(f"{team_name} leader categories: {category_names}")
    
    # Check specific categories based on sport
    found_categories = set()
    for category in result.categories:
        assert isinstance(category, LeaderCategory), "Category should be LeaderCategory"
        assert category.name, "Category should have a name"
        assert category.display_name, "Category should have a display name"
        assert category.leaders, "Category should have leaders"
        
        found_categories.add(category.name)
        
        # Validate leaders in each category
        for leader in category.leaders[:2]:  # Check first 2 leaders
            assert isinstance(leader, TeamLeader), "Leader should be TeamLeader"
            assert leader.display_value, "Leader should have a display value"
            assert leader.value is not None, "Leader should have a numeric value"
            
            # Check references
            if leader.athlete:
                assert isinstance(leader.athlete, Reference), "Athlete should be a Reference"
                assert leader.athlete.ref, "Athlete reference should have a URL"
            
            if leader.statistics:
                assert isinstance(leader.statistics, Reference), "Statistics should be a Reference"
                assert leader.statistics.ref, "Statistics reference should have a URL"
        
        # Log some interesting leaders
        if category.leaders and category.name in ["passingLeader", "pointsPerGame", "battingAverage", "goals"]:
            leader = category.leaders[0]
            logger.info(f"{team_name} {category.display_name}: {leader.display_value}")
    
    # Verify sport-specific categories exist
    if sport == SportEnum.FOOTBALL:
        assert any(cat in found_categories for cat in ["passingLeader", "rushingLeader", "receivingLeader"]), \
            "Football should have passing/rushing/receiving leaders"
    elif sport == SportEnum.BASKETBALL:
        assert any(cat in found_categories for cat in ["pointsPerGame", "assistsPerGame", "reboundsPerGame"]), \
            "Basketball should have points/assists/rebounds leaders"
    
    # Save response for first sport
    if sport == SportEnum.FOOTBALL:
        filename = f"{sport.value}_{league.value}_team_leaders_{year}.json"
        with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
        logger.info(f"✓ Saved team leaders data to {filename}")


@pytest.mark.api
def test_team_leaders_with_limit(sports_core_api_client):
    """Test team leaders endpoint with limit parameter."""
    response = get_team_leaders.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2024,
        seasontype=2,
        team_id="12",
        limit=5,
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, TeamLeadersResponse), "Response should parse to TeamLeadersResponse"
    
    # Check that limit affects the response
    logger.info(f"Number of categories returned with limit=5: {len(result.categories)}")


@pytest.mark.api
def test_team_leaders_invalid_team(sports_core_api_client):
    """Test requesting leaders for an invalid team ID."""
    response = get_team_leaders.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2024,
        seasontype=2,
        team_id="99999",  # Invalid team ID
    )
    
    # ESPN API returns 404 for invalid team
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"