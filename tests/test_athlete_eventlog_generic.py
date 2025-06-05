"""Test generic athlete eventlog endpoint."""
import pytest
import json
from models.sports_core_api.espn_sports_core_api_client.api.default import get_athlete_eventlog
from models.sports_core_api.espn_sports_core_api_client.models.athlete_eventlog_response import AthleteEventlogResponse
from models.sports_core_api.espn_sports_core_api_client.types import UNSET


@pytest.mark.api
@pytest.mark.parametrize("sport,league,year,athlete_id,athlete_name", [
    ("golf", "pga", 2024, "388", "Tiger Woods"),
    ("football", "nfl", 2024, "3139477", "Patrick Mahomes"),
    ("basketball", "nba", 2024, "1966", "LeBron James"),
    ("baseball", "mlb", 2024, "33912", "Mike Trout"),
    ("hockey", "nhl", 2024, "3024816", "Connor McDavid"),
])
def test_get_athlete_eventlog(sports_core_api_client, ensure_json_output_dir, sport, league, year, athlete_id, athlete_name):
    """Test getting athlete event log for various sports."""
    response = get_athlete_eventlog.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=year,
        athlete_id=athlete_id,
        page=UNSET,
        limit=UNSET
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, AthleteEventlogResponse), "Response should parse to AthleteEventlogResponse"
    
    # Check basic structure
    assert hasattr(result, 'events'), "Response should have events"
    if result.events:
        assert hasattr(result.events, 'count'), "Events should have count"
        assert hasattr(result.events, 'items'), "Events should have items"
        
        print(f"\n{athlete_name} ({sport.upper()}) - Found {result.events.count} events in {year}")
        
        # For golf, check for league field in items
        if sport == "golf" and result.events.items:
            for item in result.events.items[:3]:  # Check first 3 items
                if hasattr(item, 'league'):
                    print(f"  - Event league: {item.league}")
    
    # Save response for analysis
    filename = f"{sport}_{league}_athlete_{athlete_id}_eventlog_{year}.json"
    with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
        json.dump(result.to_dict(), f, indent=2)


@pytest.mark.api
def test_get_athlete_eventlog_pagination(sports_core_api_client):
    """Test pagination for athlete event log."""
    # Use golf as example with limited results
    response = get_athlete_eventlog.sync_detailed(
        client=sports_core_api_client,
        sport="golf",
        league="pga",
        year=2024,
        athlete_id="388",
        page=1,
        limit=10
    )
    
    assert response.status_code == 200
    result = response.parsed
    
    # Check pagination
    if result.events:
        assert result.events.page_size <= 10, "Should respect limit parameter"
        assert result.events.page_index == 1, "Should be on first page"
        
        # If there are more pages, test second page
        if result.events.page_count and result.events.page_count > 1:
            response2 = get_athlete_eventlog.sync_detailed(
                client=sports_core_api_client,
                sport="golf",
                league="pga",
                year=2024,
                athlete_id="388",
                page=2,
                limit=10
            )
            
            assert response2.status_code == 200
            result2 = response2.parsed
            assert result2.events.page_index == 2, "Should be on second page"


@pytest.mark.api
def test_get_athlete_eventlog_invalid_athlete(sports_core_api_client):
    """Test athlete event log with invalid athlete ID."""
    response = get_athlete_eventlog.sync_detailed(
        client=sports_core_api_client,
        sport="golf",
        league="pga",
        year=2024,
        athlete_id="99999999",  # Invalid ID
        page=UNSET,
        limit=UNSET
    )
    
    # ESPN often returns 200 with minimal data for invalid IDs
    assert response.status_code in [200, 400, 404], f"Unexpected status code: {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        # For invalid athlete, should have minimal data (just $ref, no events)
        assert not result.events or result.events.count == 0, "Invalid athlete should have no events"