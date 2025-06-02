"""Test Partners API Events endpoint"""
import json
import logging
import pytest
from models.partners_api.espn_partners_api_client.api.default import get_events_list
from models.partners_api.espn_partners_api_client.models import EventsListResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize("sport,league", [
    ("football", "nfl"),
    ("basketball", "nba"),
    ("baseball", "mlb"),
    ("hockey", "nhl"),
])
def test_get_events_list_basic(partners_api_client, sport, league, ensure_json_output_dir):
    """Test getting events list from partners API for different sports."""
    response = get_events_list.sync_detailed(
        client=partners_api_client,
        sport=sport,
        league=league,
        limit=5
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, EventsListResponse), "Response should parse to EventsListResponse"
    
    # Validate response structure
    assert result.count >= 0, "Total count should be non-negative"
    assert result.page_index == 1, "Page index should be 1"
    assert result.page_size <= 5, "Page size should be at most 5"
    assert result.page_count >= 0, "Page count should be non-negative"
    
    # Log some info
    logger.info(f"{sport.upper()}/{league.upper()} Events: Found {result.count} total, showing {len(result.events)}")
    
    # Validate first few events if any exist
    for i, event in enumerate(result.events[:3]):
        assert event.id, "Event should have ID"
        assert event.name, "Event should have name"
        assert event.date, "Event should have date"
        
        logger.info(f"  {i+1}. {event.name} ({event.short_name}) - {event.date}")
        
        # Check competitions
        assert len(event.competitions) > 0, "Event should have at least one competition"
        competition = event.competitions[0]
        assert len(competition.competitors) == 2, "Competition should have 2 competitors"
        
        home_team = next((c for c in competition.competitors if c.home_away == "home"), None)
        away_team = next((c for c in competition.competitors if c.home_away == "away"), None)
        
        assert home_team and away_team, "Should have both home and away teams"
        
        if competition.status and competition.status.type:
            logger.info(f"     Status: {competition.status.type.description}")
    
    # Save response for analysis
    output_file = f"{ensure_json_output_dir}/partners_{sport}_{league}_events.json"
    with open(output_file, "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    logger.info(f"Saved response to {output_file}")


@pytest.mark.api
def test_get_events_with_date_range(partners_api_client, ensure_json_output_dir):
    """Test getting events with date range filter."""
    sport = "football"
    league = "nfl"
    dates = "20250901-20250907"  # First week of September 2025
    
    response = get_events_list.sync_detailed(
        client=partners_api_client,
        sport=sport,
        league=league,
        dates=dates,
        limit=10
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, EventsListResponse), "Response should parse to EventsListResponse"
    
    logger.info(f"Date range {dates}: Found {result.count} events, showing {len(result.events)}")
    
    # All events should be within the date range
    for event in result.events:
        event_date = event.date.strftime("%Y%m%d")
        assert "20250901" <= event_date <= "20250907", f"Event date {event_date} should be in range"


@pytest.mark.api
def test_get_events_with_single_date(partners_api_client):
    """Test getting events for a single date."""
    sport = "football"
    league = "nfl"
    dates = "20250907"  # September 7, 2025
    
    response = get_events_list.sync_detailed(
        client=partners_api_client,
        sport=sport,
        league=league,
        dates=dates,
        limit=20
    )
    
    # Note: This might return 0 events if no games on that date
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    logger.info(f"Date {dates}: Found {result.count} events")
    
    # Note: API might return events from nearby dates as well
    # Just log the dates we get
    event_dates = set()
    for event in result.events:
        event_date = event.date.strftime("%Y%m%d")
        event_dates.add(event_date)
    
    if event_dates:
        logger.info(f"Event dates returned: {sorted(event_dates)}")


@pytest.mark.api
def test_get_events_with_year(partners_api_client):
    """Test getting events for a full year."""
    sport = "football"
    league = "nfl"
    dates = "2024"  # Full 2024 season
    
    response = get_events_list.sync_detailed(
        client=partners_api_client,
        sport=sport,
        league=league,
        dates=dates,
        limit=5
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    logger.info(f"Year {dates}: Found {result.count} total events")
    
    # Should have many events for a full year
    assert result.count > 0, "Should have events for the year"
    
    # All events should be in 2024
    for event in result.events:
        assert event.date.year == 2024, f"Event date should be in 2024"


@pytest.mark.api
def test_get_events_with_large_limit(partners_api_client):
    """Test getting events with a large limit."""
    sport = "football"
    league = "nfl"
    limit = 100
    
    response = get_events_list.sync_detailed(
        client=partners_api_client,
        sport=sport,
        league=league,
        limit=limit
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    actual_count = len(result.events)
    logger.info(f"Requested {limit} events, got {actual_count} (total available: {result.count})")
    
    # Verify we got the requested number (or all available if less)
    if result.count >= limit:
        assert actual_count == limit, f"Should return exactly {limit} events when available"
    else:
        assert actual_count == result.count, "Should return all available events when less than limit"


@pytest.mark.api
@pytest.mark.parametrize("sport,league", [
    ("football", "college-football"),
    ("basketball", "wnba"),
    ("soccer", "eng.1"),
])
def test_get_events_other_leagues(partners_api_client, sport, league):
    """Test getting events for other leagues."""
    response = get_events_list.sync_detailed(
        client=partners_api_client,
        sport=sport,
        league=league,
        limit=5
    )
    
    # These might work or return 404/400 depending on what's supported
    if response.status_code == 200:
        result = response.parsed
        logger.info(f"{sport.upper()}/{league.upper()} Events: Found {result.count} total")
    else:
        logger.info(f"{sport.upper()}/{league.upper()} Events: Status {response.status_code} - might not be supported")