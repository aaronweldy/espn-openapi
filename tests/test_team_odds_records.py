"""Test Team Odds Records endpoint"""
import json
import logging
import pytest
from models.sports_core_api.espn_sports_core_api_client.api.default import get_team_odds_records
from models.sports_core_api.espn_sports_core_api_client.models import TeamOddsRecordsResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize("sport,league,year,seasontype,team_id", [
    ("football", "nfl", 2024, 0, "12"),  # Kansas City Chiefs
    pytest.param("basketball", "nba", 2024, 0, "13", marks=pytest.mark.xfail(reason="NBA might not have odds records for this season")),  # Los Angeles Lakers
])
def test_get_team_odds_records(sports_core_api_client, sport, league, year, seasontype, team_id, ensure_json_output_dir):
    """Test getting team odds records for different sports."""
    response = get_team_odds_records.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=year,
        seasontype=seasontype,
        team_id=team_id
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
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


@pytest.mark.api
@pytest.mark.parametrize("sport,league,year,seasontype,team_id", [
    pytest.param("baseball", "mlb", 2024, 0, "15", marks=pytest.mark.xfail(reason="MLB might not support odds records")),
    pytest.param("hockey", "nhl", 2024, 0, "10", marks=pytest.mark.xfail(reason="NHL might not support odds records")),
])
def test_get_team_odds_records_unsupported_sports(sports_core_api_client, sport, league, year, seasontype, team_id):
    """Test getting team odds records for sports that might not support them."""
    response = get_team_odds_records.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=year,
        seasontype=seasontype,
        team_id=team_id
    )
    
    # These might return 400/404/500 for unsupported sports
    assert response.status_code in [400, 404, 500], f"Expected error status code, got {response.status_code}"
    logger.info(f"{sport.upper()}/{league.upper()} odds records returned status code {response.status_code}")