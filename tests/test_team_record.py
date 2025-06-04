import json
import pytest
from models.sports_core_api.espn_sports_core_api_client.api.default import get_team_record
from models.sports_core_api.espn_sports_core_api_client.models import TeamRecordResponse, TeamRecordItem, RecordStat


@pytest.mark.api
@pytest.mark.parametrize("sport,league,year,seasontype,team_id,expected_min_records", [
    ("football", "nfl", "2024", "2", "12", 4),  # Kansas City Chiefs
    ("basketball", "nba", "2024", "2", "13", 4),  # LA Lakers
    ("baseball", "mlb", "2024", "2", "15", 3),  # NY Mets
    ("hockey", "nhl", "2024", "2", "TOR", 4),  # Toronto Maple Leafs
])
def test_get_team_record(sports_core_api_client, sport, league, year, seasontype, team_id, expected_min_records, ensure_json_output_dir):
    """Test getting team record across different sports."""
    response = get_team_record.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=year,
        seasontype=seasontype,
        team_id=team_id
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, TeamRecordResponse), "Response should parse to TeamRecordResponse"
    
    # Validate response structure
    assert hasattr(result, 'count'), "Response should have count"
    assert hasattr(result, 'page_index'), "Response should have page_index"
    assert hasattr(result, 'page_size'), "Response should have page_size"
    assert hasattr(result, 'page_count'), "Response should have page_count"
    assert hasattr(result, 'items'), "Response should have items"
    
    # Validate pagination
    if result.count > 0:
        assert result.page_index >= 1, "Page index should be at least 1 when there are results"
        assert result.page_count >= 1, "Page count should be at least 1 when there are results"
    else:
        assert result.page_index >= 0, "Page index should be non-negative when there are no results"
        assert result.page_count >= 0, "Page count should be non-negative when there are no results"
    assert result.page_size > 0, "Page size should be positive"
    
    # Validate records
    assert result.count >= expected_min_records, f"Expected at least {expected_min_records} records, got {result.count}"
    assert len(result.items) == result.count, "Items length should match count"
    
    # Track record types found
    record_types = set()
    
    # Validate each record
    for record in result.items:
        assert isinstance(record, TeamRecordItem), "Each item should be a TeamRecordItem"
        assert record.id, "Record should have an ID"
        assert record.name, "Record should have a name"
        assert record.type, "Record should have a type"
        assert record.summary, "Record should have a summary"
        assert record.display_value, "Record should have a display_value"
        assert record.stats, "Record should have stats"
        
        record_types.add(record.name)
        
        # Validate stats
        assert isinstance(record.stats, list), "Stats should be a list"
        for stat in record.stats:
            assert isinstance(stat, RecordStat), "Each stat should be a RecordStat"
            assert stat.name, "Stat should have a name"
            assert stat.type, "Stat should have a type"
            assert hasattr(stat, 'value'), "Stat should have a value"
    
    # Check for expected record types
    print(f"✓ {sport.upper()} team {team_id} has records: {', '.join(record_types)}")
    
    # Most sports should have at least overall, home, and away records
    common_types = {'overall', 'Home', 'Road', 'Away'}
    found_common = record_types & common_types
    assert len(found_common) >= 2, f"Expected at least 2 common record types, found: {found_common}"
    
    # Save response for analysis
    with open(f"{ensure_json_output_dir}/team_record_{sport}_{team_id}_{year}_test.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)


@pytest.mark.api
def test_get_team_record_invalid_team(sports_core_api_client):
    """Test getting record for invalid team ID."""
    response = get_team_record.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        year="2024",
        seasontype="2",
        team_id="9999"  # Invalid team ID
    )
    
    # The API returns 200 with empty results for invalid teams
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, TeamRecordResponse), "Response should parse to TeamRecordResponse"
    assert result.count == 0, "Invalid team should have no records"
    assert len(result.items) == 0, "Invalid team should have empty items list"


@pytest.mark.api
def test_get_team_record_preseason(sports_core_api_client):
    """Test getting team record for preseason."""
    response = get_team_record.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        year="2024",
        seasontype="1",  # Preseason
        team_id="12"
    )
    
    # Preseason may not have records or may return different data
    assert response.status_code in [200, 404], f"Expected status code 200 or 404, got {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        assert isinstance(result, TeamRecordResponse), "Response should parse to TeamRecordResponse"
        # Preseason might have fewer record types
        print(f"Preseason records count: {result.count}")


@pytest.mark.api
@pytest.mark.parametrize("sport,league", [
    ("football", "college-football"),
    ("basketball", "mens-college-basketball"),
    ("basketball", "womens-college-basketball"),
])
def test_get_team_record_college_sports(sports_core_api_client, sport, league):
    """Test if team record endpoint works for college sports."""
    # Use a well-known college team
    team_ids = {
        "college-football": "333",  # Alabama
        "mens-college-basketball": "150",  # Duke
        "womens-college-basketball": "2",  # UConn
    }
    
    response = get_team_record.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year="2024",
        seasontype="2",
        team_id=team_ids[league]
    )
    
    # College sports may or may not support this endpoint
    if response.status_code == 200:
        result = response.parsed
        assert isinstance(result, TeamRecordResponse), "Response should parse to TeamRecordResponse"
        print(f"✓ {league} supports team records with {result.count} record types")
    else:
        print(f"✗ {league} does not support team records (status: {response.status_code})")