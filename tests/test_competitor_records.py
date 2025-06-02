import pytest
import json
from models.sports_core_api.espn_sports_core_api_client.api.default import get_competitor_records
from models.sports_core_api.espn_sports_core_api_client.models.competitor_records_response import CompetitorRecordsResponse
from models.sports_core_api.espn_sports_core_api_client.models.team_record import TeamRecord


@pytest.mark.api
def test_get_competitor_records_nfl(sports_core_api_client, ensure_json_output_dir):
    """Test getting competitor records for NFL event."""
    # Using a known NFL game with available records
    event_id = "401547417"
    competition_id = "401547417"
    competitor_id = "1"  # Atlanta Falcons (home team)
    
    response = get_competitor_records.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        event_id=event_id,
        competition_id=competition_id,
        competitor_id=competitor_id
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.parsed is not None, "Response should have parsed content"
    
    result = response.parsed
    assert isinstance(result, CompetitorRecordsResponse), "Response should parse to CompetitorRecordsResponse"
    
    # Validate structure
    assert result.count > 0, "Should have record count"
    assert result.items, "Response should have record items"
    assert len(result.items) > 0, "Should have at least one record"
    
    # Check record structure
    first_record = result.items[0]
    assert isinstance(first_record, TeamRecord), "Items should be TeamRecord instances"
    assert first_record.id, "Record should have ID"
    assert first_record.name, "Record should have name"
    assert first_record.display_name, "Record should have display_name"
    assert first_record.type, "Record should have type"
    
    # Check for expected record types
    record_types = [record.type for record in result.items]
    assert "total" in record_types, "Should have overall record"
    assert "home" in record_types, "Should have home record" 
    assert "road" in record_types, "Should have away/road record"
    
    # Save response
    with open(f"{ensure_json_output_dir}/competitor_records_nfl_{event_id}_competitor{competitor_id}_test.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    print(f"Successfully retrieved {len(result.items)} records for NFL competitor {competitor_id}")
    print(f"Record types: {', '.join(record_types)}")


@pytest.mark.api
def test_get_competitor_records_both_teams(sports_core_api_client, ensure_json_output_dir):
    """Test competitor records for both teams in an NFL game."""
    event_id = "401547417"
    competition_id = "401547417"
    
    # Test both competitors (home and away teams)
    competitors = [
        {"id": "1", "team": "home"},
        {"id": "9", "team": "away"}
    ]
    
    for competitor in competitors:
        competitor_id = competitor["id"]
        team_type = competitor["team"]
        
        response = get_competitor_records.sync_detailed(
            client=sports_core_api_client,
            sport="football",
            league="nfl",
            event_id=event_id,
            competition_id=competition_id,
            competitor_id=competitor_id
        )
        
        assert response.status_code == 200, f"Expected 200 for competitor {competitor_id}, got {response.status_code}"
        result = response.parsed
        assert isinstance(result, CompetitorRecordsResponse), f"Should parse for competitor {competitor_id}"
        assert result.items, f"Should have records for competitor {competitor_id}"
        
        # Validate we get expected record types
        record_types = [record.type for record in result.items]
        assert "total" in record_types, f"Competitor {competitor_id} should have overall record"
        
        # Save response
        with open(f"{ensure_json_output_dir}/competitor_records_nfl_{event_id}_competitor{competitor_id}_{team_type}_test.json", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
            
        print(f"✓ Competitor {competitor_id} ({team_type}): {len(result.items)} records")


@pytest.mark.api
def test_get_competitor_records_cross_sport(sports_core_api_client, ensure_json_output_dir):
    """Test competitor records across different sports."""
    test_cases = [
        # NFL - Known to work
        {
            "sport": "football",
            "league": "nfl", 
            "event_id": "401547417",
            "competition_id": "401547417",
            "competitor_id": "1",
            "should_work": True
        },
        # Basketball - May or may not work
        {
            "sport": "basketball",
            "league": "nba",
            "event_id": "401584793", 
            "competition_id": "401584793",
            "competitor_id": "1",
            "should_work": False
        },
        # Baseball - May or may not work
        {
            "sport": "baseball",
            "league": "mlb",
            "event_id": "401472463",
            "competition_id": "401472463", 
            "competitor_id": "1",
            "should_work": False
        }
    ]
    
    for test_case in test_cases:
        sport = test_case["sport"]
        league = test_case["league"]
        event_id = test_case["event_id"]
        competition_id = test_case["competition_id"]
        competitor_id = test_case["competitor_id"]
        should_work = test_case["should_work"]
        
        response = get_competitor_records.sync_detailed(
            client=sports_core_api_client,
            sport=sport,
            league=league,
            event_id=event_id,
            competition_id=competition_id,
            competitor_id=competitor_id
        )
        
        if should_work:
            assert response.status_code == 200, f"Expected {sport}/{league} to work, got {response.status_code}"
            result = response.parsed
            assert isinstance(result, CompetitorRecordsResponse), f"Response should parse for {sport}/{league}"
            
            with open(f"{ensure_json_output_dir}/competitor_records_{sport}_{league}_{event_id}_test.json", "w") as f:
                json.dump(result.to_dict(), f, indent=2)
                
            print(f"✓ {sport.upper()}/{league.upper()}: {len(result.items)} records")
        else:
            # These might return 404 or other errors - that's expected
            if response.status_code == 200:
                result = response.parsed
                if isinstance(result, CompetitorRecordsResponse) and result.items:
                    with open(f"{ensure_json_output_dir}/competitor_records_{sport}_{league}_{event_id}_test.json", "w") as f:
                        json.dump(result.to_dict(), f, indent=2)
                    print(f"✓ {sport.upper()}/{league.upper()}: {len(result.items)} records (unexpected success)")
                else:
                    print(f"? {sport.upper()}/{league.upper()}: Got 200 but no valid record data")
            else:
                print(f"✗ {sport.upper()}/{league.upper()}: {response.status_code} (expected)")


@pytest.mark.api
def test_get_competitor_records_invalid_params(sports_core_api_client):
    """Test competitor records with invalid parameters."""
    # Test with invalid event ID
    response = get_competitor_records.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        event_id="999999999",
        competition_id="999999999",
        competitor_id="1"
    )
    
    # Should return 404 for invalid event
    assert response.status_code in [400, 404], f"Expected 400 or 404 for invalid event, got {response.status_code}"
    
    # Test with invalid competitor ID
    response = get_competitor_records.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl",
        event_id="401547417",
        competition_id="401547417",
        competitor_id="99999"  # Invalid competitor ID
    )
    
    # Should return 404 for invalid competitor
    assert response.status_code in [400, 404], f"Expected 400 or 404 for invalid competitor, got {response.status_code}"


@pytest.mark.api 
def test_competitor_records_data_validation(sports_core_api_client):
    """Test that competitor records data contains expected fields and types."""
    response = get_competitor_records.sync_detailed(
        client=sports_core_api_client,
        sport="football",
        league="nfl", 
        event_id="401547417",
        competition_id="401547417",
        competitor_id="1"
    )
    
    assert response.status_code == 200
    result = response.parsed
    assert isinstance(result, CompetitorRecordsResponse)
    
    # Validate response structure
    assert result.count > 0, "Should have record count"
    assert result.page_index >= 1, "Should have valid page index"
    assert result.page_size > 0, "Should have valid page size"
    assert result.page_count >= 1, "Should have valid page count"
    assert len(result.items) <= result.page_size, "Items should not exceed page size"
    
    # Check record items
    assert len(result.items) > 0, "Should have record items"
    
    for record in result.items:
        # Required fields
        assert isinstance(record, TeamRecord), "Should be TeamRecord instance"
        assert record.ref, "Record should have $ref"
        assert record.id, "Record should have id"
        assert record.name, "Record should have name"
        assert record.display_name, "Record should have displayName"
        assert record.type, "Record should have type"
        
        # Optional fields validation
        if record.stats:
            assert len(record.stats) > 0, "Stats array should not be empty if present"
            
            # Check first few stats
            for stat in record.stats[:3]:
                assert stat.name, "Stat should have name"
                assert stat.display_name, "Stat should have displayName"
                assert stat.type, "Stat should have type"
                assert stat.value is not None, "Stat should have value"
                assert stat.display_value, "Stat should have displayValue"
        
        print(f"Record: {record.display_name} ({record.type}) - {record.summary if record.summary else 'No summary'}")


@pytest.mark.api
def test_get_competitor_records_multiple_events(sports_core_api_client, ensure_json_output_dir):
    """Test competitor records with different NFL events."""
    # Test multiple NFL events to verify the endpoint works broadly
    test_events = [
        {"event_id": "401547417", "season": "2023", "competitor_id": "1"},
        {"event_id": "401547675", "season": "2023", "competitor_id": "1"},  # Different event
    ]
    
    for event_data in test_events:
        event_id = event_data["event_id"]
        season = event_data["season"]
        competitor_id = event_data["competitor_id"]
        
        response = get_competitor_records.sync_detailed(
            client=sports_core_api_client,
            sport="football",
            league="nfl",
            event_id=event_id,
            competition_id=event_id,
            competitor_id=competitor_id
        )
        
        if response.status_code == 200:
            result = response.parsed
            assert isinstance(result, CompetitorRecordsResponse), f"Should parse for event {event_id}"
            assert result.items, f"Should have records for event {event_id}"
            
            # Save response
            with open(f"{ensure_json_output_dir}/competitor_records_nfl_{event_id}_competitor{competitor_id}_multi_events_test.json", "w") as f:
                json.dump(result.to_dict(), f, indent=2)
                
            print(f"✓ NFL Event {event_id} ({season}): {len(result.items)} records")
        else:
            print(f"✗ NFL Event {event_id} ({season}): {response.status_code} (may not have records)")