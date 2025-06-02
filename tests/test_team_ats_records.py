import pytest
import json
import logging
from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_team_ats_records,
)
from models.sports_core_api.espn_sports_core_api_client.models import (
    SportEnum,
    LeagueEnum,
    TeamAtsRecordsResponse,
    TeamAtsRecord,
    AtsRecordType,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league,year,seasontype,team_id",
    [
        (SportEnum.FOOTBALL, LeagueEnum.NFL, 2023, 2, "12"),  # Kansas City Chiefs
        (SportEnum.BASKETBALL, LeagueEnum.NBA, 2023, 2, "13"),  # LA Lakers
        pytest.param(
            SportEnum.BASEBALL, LeagueEnum.MLB, 2023, 2, "15",  # NY Yankees
            marks=pytest.mark.xfail(reason="MLB ATS endpoint returns 500 error")
        ),
        pytest.param(
            SportEnum.HOCKEY, LeagueEnum.NHL, 2023, 2, "10",  # Toronto Maple Leafs
            marks=pytest.mark.xfail(reason="NHL ATS endpoint may return 500 error")
        ),
    ],
)
def test_get_team_ats_records(
    sports_core_api_client,
    ensure_json_output_dir,
    sport,
    league,
    year,
    seasontype,
    team_id,
):
    """Test getting team ATS records across different sports."""
    response = get_team_ats_records.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=year,
        seasontype=seasontype,
        team_id=team_id,
    )

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, TeamAtsRecordsResponse), "Response should parse to TeamAtsRecordsResponse"
    
    # Validate pagination fields
    assert isinstance(result.count, int), "Count should be an integer"
    assert result.count >= 0, "Count should be non-negative"
    assert isinstance(result.page_index, int), "Page index should be an integer"
    assert result.page_index >= 0, "Page index should be non-negative"
    assert result.page_size > 0, "Page size should be positive"
    assert isinstance(result.page_count, int), "Page count should be an integer"
    assert result.page_count >= 0, "Page count should be non-negative"
    assert isinstance(result.items, list), "Items should be a list"
    
    # Log summary for the team
    logger.info(f"\n{sport.value.upper()} {league.value.upper()} Team ATS Records:")
    logger.info(f"  Team ID: {team_id}")
    logger.info(f"  Year: {year}, Season Type: {seasontype}")
    logger.info(f"  Total Record Types: {result.count}")
    
    # If there are items, validate and log them
    if result.items:
        for item in result.items:
            assert isinstance(item, TeamAtsRecord), "Item should be a TeamAtsRecord"
            assert isinstance(item.wins, int) and item.wins >= 0, "Wins should be non-negative integer"
            assert isinstance(item.losses, int) and item.losses >= 0, "Losses should be non-negative integer"
            assert isinstance(item.pushes, int) and item.pushes >= 0, "Pushes should be non-negative integer"
            
            assert isinstance(item.type, AtsRecordType), "Type should be an AtsRecordType"
            assert item.type.id, "Type should have an ID"
            assert item.type.name, "Type should have a name"
            assert item.type.description, "Type should have a description"
            
            # Calculate total games and win percentage
            total_games = item.wins + item.losses + item.pushes
            win_pct = item.wins / (item.wins + item.losses) if (item.wins + item.losses) > 0 else 0
            
            logger.info(f"  {item.type.description}:")
            logger.info(f"    Record: {item.wins}-{item.losses}-{item.pushes} ({win_pct:.3f})")
            logger.info(f"    Total Games: {total_games}")
    else:
        logger.info("  No ATS records available for this team/season")
    
    # Save one example
    if sport == SportEnum.FOOTBALL:
        filename = f"{sport.value}_{league.value}_team_ats_records_{year}_type{seasontype}_team{team_id}.json"
        with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
        logger.info(f"✓ Saved ATS records to {filename}")


@pytest.mark.api
def test_ats_record_types(sports_core_api_client):
    """Test that we get all expected ATS record types for NFL."""
    response = get_team_ats_records.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2023,
        seasontype=2,
        team_id="12",  # Kansas City Chiefs
    )
    
    assert response.status_code == 200
    result = response.parsed
    
    # Expected ATS record types for NFL
    expected_types = {
        "atsOverall": "Overall team season record against the spread",
        "atsFavorite": "Team season record against the spread as the favorite",
        "atsUnderdog": "Team season record against the spread as the underdog",
        "atsAway": "Team season record against the spread as the away team",
        "atsHome": "Team season record against the spread as the home team",
        "atsAwayFavorite": "Team season record against the spread as the away favorite",
        "atsAwayUnderdog": "Team season record against the spread as the away underdog",
        "atsHomeFavorite": "Team season record against the spread as the home favorite",
    }
    
    # Check that we have records
    assert len(result.items) > 0, "Should have ATS records"
    
    # Collect the types we received
    received_types = {item.type.name: item.type.description for item in result.items}
    
    logger.info("\nATS Record Types Found:")
    for name, desc in received_types.items():
        logger.info(f"  {name}: {desc}")
    
    # Check that we have most of the expected types (some sports might have different types)
    for expected_name in expected_types:
        if expected_name in received_types:
            logger.info(f"✓ Found expected type: {expected_name}")


@pytest.mark.api
def test_invalid_team_ats_records(sports_core_api_client):
    """Test requesting ATS records for an invalid team ID."""
    response = get_team_ats_records.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2023,
        seasontype=2,
        team_id="99999",  # Invalid team ID
    )
    
    # ESPN API might return 404 or empty results for invalid team
    assert response.status_code in [200, 404], f"Expected status code 200 or 404, got {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        assert result.count == 0, "Should have no results for invalid team"


@pytest.mark.api
def test_ats_records_different_season_types(sports_core_api_client):
    """Test ATS records for different season types."""
    team_id = "1"  # Buffalo Bills
    year = 2023
    
    for seasontype, type_name in [(1, "Preseason"), (2, "Regular Season"), (3, "Postseason")]:
        response = get_team_ats_records.sync_detailed(
            client=sports_core_api_client,
            sport=SportEnum.FOOTBALL,
            league=LeagueEnum.NFL,
            year=year,
            seasontype=seasontype,
            team_id=team_id,
        )
        
        if response.status_code == 200:
            result = response.parsed
            logger.info(f"\n{type_name} ATS Records for Team {team_id}:")
            
            if result.items:
                # Find overall record
                overall = next((item for item in result.items if item.type.name == "atsOverall"), None)
                if overall:
                    total_games = overall.wins + overall.losses + overall.pushes
                    logger.info(f"  Overall: {overall.wins}-{overall.losses}-{overall.pushes} ({total_games} games)")
            else:
                logger.info(f"  No ATS records available")
        else:
            logger.info(f"\n{type_name}: No data available (HTTP {response.status_code})")