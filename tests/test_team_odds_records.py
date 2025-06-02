"""Test Team Odds Records endpoint"""
import json
import logging
import pytest
from models.sports_core_api.espn_sports_core_api_client.api.default import get_team_odds_records
from models.sports_core_api.espn_sports_core_api_client.models import TeamOddsRecordsResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize("sport,league,year,seasontype,team_id,team_name", [
    ("football", "nfl", 2024, 0, "12", "Kansas City Chiefs"),
    ("basketball", "nba", 2025, 0, "13", "Los Angeles Lakers"),
    ("baseball", "mlb", 2025, 0, "15", "Colorado Rockies"),
    ("hockey", "nhl", 2025, 0, "10", "Toronto Maple Leafs"),
    ("football", "college-football", 2025, 0, "333", "Alabama"),
    ("basketball", "mens-college-basketball", 2025, 0, "150", "Duke"),
    ("basketball", "wnba", 2025, 0, "5", "Dallas Wings"),
])
def test_get_team_odds_records(sports_core_api_client, sport, league, year, seasontype, team_id, team_name, ensure_json_output_dir):
    """Test getting team odds records for different sports."""
    response = get_team_odds_records.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=year,
        seasontype=seasontype,
        team_id=team_id
    )
    
    # Log the test being run
    logger.info(f"Testing {sport}/{league} - {team_name} ({year})")
    
    if response.status_code != 200:
        logger.warning(f"{sport}/{league} odds records returned status code {response.status_code}")
        # Some sports/leagues might not support odds records
        assert response.status_code in [400, 404, 500], f"Unexpected status code {response.status_code}"
        return
    
    result = response.parsed
    assert isinstance(result, TeamOddsRecordsResponse), "Response should parse to TeamOddsRecordsResponse"
    
    # Validate response structure
    assert result.count > 0, "Should have at least one odds record type"
    assert result.page_index == 1, "Page index should be 1"
    assert result.page_size > 0, "Page size should be positive"
    assert result.page_count > 0, "Page count should be positive"
    assert len(result.items) > 0, "Should have odds record items"
    
    # Validate each odds record
    for record in result.items:
        assert record.abbreviation, "Record should have abbreviation"
        assert record.display_name, "Record should have display name"
        assert record.short_display_name, "Record should have short display name"
        assert record.type, "Record should have type"
        assert len(record.stats) > 0, "Record should have stats"
        
        # Log some interesting info
        logger.info(f"{sport.upper()}/{league.upper()} Team {team_id} - {record.display_name}")
        
        # Validate stats
        for stat in record.stats:
            assert stat.display_name, "Stat should have display name"
            assert stat.abbreviation, "Stat should have abbreviation"
            assert stat.type, "Stat should have type"
            assert stat.value is not None, "Stat should have value"
            assert stat.display_value, "Stat should have display value"
            
            if stat.abbreviation == "W":
                logger.info(f"  Wins: {stat.display_value}")
            elif stat.abbreviation == "L":
                logger.info(f"  Losses: {stat.display_value}")
            elif stat.abbreviation == "Margin":
                logger.info(f"  Margin: {stat.display_value}")
    
    # Save response for analysis
    output_file = f"{ensure_json_output_dir}/{sport}_{league}_team_{team_id}_odds_records_{year}.json"
    with open(output_file, "w") as f:
        # Convert to dict for JSON serialization
        json.dump(result.to_dict(), f, indent=2)
    logger.info(f"Saved response to {output_file}")


