"""Tests for season futures endpoints."""

import json
import logging
import pytest
from models.sports_core_api.espn_sports_core_api_client.api.default import get_season_futures
from models.sports_core_api.espn_sports_core_api_client.models import (
    FuturesResponse,
    FutureItem,
    FutureProvider,
    FutureBook,
    BettingProvider,
    LeagueEnum,
    SportEnum,
)
from models.sports_core_api.espn_sports_core_api_client.types import UNSET

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league,year,expected_min_items",
    [
        (SportEnum.FOOTBALL, LeagueEnum.NFL, 2024, 10),  # NFL futures
        (SportEnum.BASKETBALL, LeagueEnum.NBA, 2024, 5),  # NBA futures
        (SportEnum.BASEBALL, LeagueEnum.MLB, 2024, 3),  # MLB futures
        (SportEnum.HOCKEY, LeagueEnum.NHL, 2024, 3),  # NHL futures
        (SportEnum.FOOTBALL, LeagueEnum.COLLEGE_FOOTBALL, 2024, 5),  # College Football futures
        (SportEnum.BASKETBALL, LeagueEnum.MENS_COLLEGE_BASKETBALL, 2024, 3),  # Men's College Basketball
        (SportEnum.BASKETBALL, LeagueEnum.WNBA, 2024, 2),  # WNBA futures
        pytest.param(SportEnum.SOCCER, LeagueEnum.ENG_1, 2024, 1, marks=pytest.mark.xfail(reason="Soccer futures might not be available")),  # Premier League
    ],
)
def test_get_season_futures(sports_core_api_client, ensure_json_output_dir, sport, league, year, expected_min_items):
    """Test fetching season futures for different sports."""
    response = get_season_futures.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=year,
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, FuturesResponse), "Response should parse to FuturesResponse"
    
    # Validate response structure
    assert result.count >= 0, "Count should be non-negative"
    assert result.page_index >= 1, "Page index should be at least 1"
    assert result.page_size > 0, "Page size should be positive"
    assert result.page_count >= 0, "Page count should be non-negative"
    assert len(result.items) >= expected_min_items, f"Expected at least {expected_min_items} future items"
    
    # Log futures summary
    logger.info(f"\n{'='*60}")
    logger.info(f"{sport.value.upper()} {league.value.upper()} FUTURES - {year}")
    logger.info(f"{'='*60}")
    logger.info(f"Total futures: {result.count}")
    logger.info(f"Page {result.page_index} of {result.page_count} (size: {result.page_size})")
    logger.info(f"Futures on this page: {len(result.items)}")
    logger.info(f"{'-'*60}")
    
    # Validate future items
    for i, future_item in enumerate(result.items):
        assert isinstance(future_item, FutureItem), "Each item should be a FutureItem"
        assert future_item.id, "Future item should have an ID"
        assert future_item.name, "Future item should have a name"
        assert len(future_item.futures) > 0, "Future item should have at least one provider"
        
        # Log future details
        logger.info(f"\n{i+1}. {future_item.name}")
        if future_item.display_name and future_item.display_name != future_item.name:
            logger.info(f"   Display: {future_item.display_name}")
        if future_item.type:
            logger.info(f"   Type: {future_item.type}")
        logger.info(f"   ID: {future_item.id}")
        logger.info(f"   Providers: {len(future_item.futures)}")
        
        # Check if type is set (not all futures have a type)
        if future_item.type:
            assert future_item.type in ["winLeague", "winDivision", "winConference", "playerProp", "teamProp"]
        
        # Validate providers and books
        for j, provider_future in enumerate(future_item.futures):
            assert isinstance(provider_future, FutureProvider), "Should be FutureProvider"
            assert isinstance(provider_future.provider, BettingProvider), "Should have BettingProvider"
            assert provider_future.provider.id, "Provider should have ID"
            assert provider_future.provider.name, "Provider should have name"
            
            assert len(provider_future.books) > 0, "Provider should have at least one book"
            
            # Log provider info
            if j == 0:  # Only log first provider to avoid too much output
                logger.info(f"   Provider: {provider_future.provider.name} (ID: {provider_future.provider.id})")
                logger.info(f"   Books: {len(provider_future.books)}")
                
                # Log sample books (first 3)
                for k, book in enumerate(provider_future.books[:3]):
                    if book.athlete is not UNSET:
                        logger.info(f"     - Athlete: {book.value}")
                    elif book.team is not UNSET:
                        logger.info(f"     - Team: {book.value}")
                
                if len(provider_future.books) > 3:
                    logger.info(f"     ... and {len(provider_future.books) - 3} more")
            
            # Validate all books
            for book in provider_future.books:
                assert isinstance(book, FutureBook), "Should be FutureBook"
                assert book.value, "Book should have a value"
                
                # Check that either athlete or team is present (not both)
                has_athlete = book.athlete is not UNSET
                has_team = book.team is not UNSET
                assert has_athlete or has_team, "Book should have either athlete or team"
    
    # Save example response
    output_file = f"{ensure_json_output_dir}/{sport.value}_{league.value}_futures_{year}_test.json"
    with open(output_file, "w") as f:
        json.dump(result.to_dict() if hasattr(result, 'to_dict') else result.__dict__, f, indent=2)
    
    print(f"Saved futures response to {output_file}")


@pytest.mark.api
def test_get_season_futures_with_limit(sports_core_api_client):
    """Test fetching futures with a limit parameter."""
    response = get_season_futures.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2024,
        limit=10,
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, FuturesResponse), "Response should parse to FuturesResponse"
    assert result.page_size == 10, "Page size should match the limit parameter"


@pytest.mark.api
def test_get_season_futures_invalid_year(sports_core_api_client):
    """Test fetching futures with an invalid year."""
    response = get_season_futures.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=1950,  # Too far in the past
    )
    
    # API might return 200 with empty results or 404/400
    assert response.status_code in [200, 404, 400], f"Expected status code 200, 404, or 400, got {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        assert isinstance(result, FuturesResponse), "Response should parse to FuturesResponse"
        assert result.count == 0, "Should have no futures for invalid year"


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league,year",
    [
        (SportEnum.FOOTBALL, LeagueEnum.NFL, 2024),
        (SportEnum.BASKETBALL, LeagueEnum.NBA, 2024),
    ],
)
def test_get_season_futures_future_types(sports_core_api_client, sport, league, year):
    """Test that futures contain different types (player props, team props, etc)."""
    response = get_season_futures.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        year=year,
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, FuturesResponse), "Response should parse to FuturesResponse"
    
    # Collect future types
    future_types = set()
    has_player_futures = False
    has_team_futures = False
    
    for future_item in result.items:
        if future_item.type:
            future_types.add(future_item.type)
        
        # Check if this is a player or team future based on the books
        for provider_future in future_item.futures:
            for book in provider_future.books:
                if book.athlete is not UNSET:
                    has_player_futures = True
                if book.team is not UNSET:
                    has_team_futures = True
    
    logger.info(f"\n{'='*60}")
    logger.info(f"FUTURE TYPES ANALYSIS - {sport.value.upper()} {league.value.upper()}")
    logger.info(f"{'='*60}")
    logger.info(f"Future types found: {future_types}")
    logger.info(f"Has player futures: {has_player_futures}")
    logger.info(f"Has team futures: {has_team_futures}")
    
    # Log some example futures
    logger.info(f"\nExample futures:")
    for i, future_item in enumerate(result.items[:5]):
        logger.info(f"{i+1}. {future_item.name} (Type: {future_item.type or 'None'})")
    
    # Verify we have at least one type of future (player or team)
    assert has_player_futures or has_team_futures, f"{sport.value} {league.value} should have either player or team futures"
    
    # NFL typically has both, NBA might only show team futures on first page
    if sport == SportEnum.FOOTBALL and league == LeagueEnum.NFL:
        assert has_player_futures and has_team_futures, "NFL should have both player and team futures"
    
    # Verify we have different types
    assert len(future_types) >= 1, f"{sport.value} {league.value} should have at least one typed future"


@pytest.mark.api
def test_get_season_futures_pagination(sports_core_api_client):
    """Test pagination for futures endpoint."""
    # First request
    response1 = get_season_futures.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2024,
        limit=5,
    )
    
    assert response1.status_code == 200
    result1 = response1.parsed
    
    # Check if there are more pages
    if result1.page_count > 1:
        assert result1.count > 5, "Should have more items than page size"
        assert len(result1.items) == 5, "Should return exactly 5 items"
        
        # Note: The API doesn't seem to support page parameter in the URL
        # so we can't test actual pagination navigation
        logger.info(f"\nPAGINATION INFO:")
        logger.info(f"Total futures: {result1.count}")
        logger.info(f"Page count: {result1.page_count}")
        logger.info(f"Items on first page: {len(result1.items)}")


@pytest.mark.api
def test_get_season_futures_sport_specific(sports_core_api_client):
    """Test sport-specific futures content."""
    # Test NFL specific futures
    response = get_season_futures.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2024,
        limit=50,  # Get more to ensure we see various types
    )
    
    assert response.status_code == 200
    result = response.parsed
    
    # Look for NFL-specific future names
    future_names = [item.name for item in result.items]
    
    # Log NFL futures
    logger.info(f"\n{'='*60}")
    logger.info("NFL FUTURES FOUND:")
    logger.info(f"{'='*60}")
    for i, name in enumerate(future_names[:10]):
        logger.info(f"{i+1}. {name}")
    if len(future_names) > 10:
        logger.info(f"... and {len(future_names) - 10} more")
    
    # NFL should have Super Bowl winner
    assert any("super bowl" in name.lower() for name in future_names), "NFL should have Super Bowl futures"
    
    # NFL should have division winners
    assert any("division" in name.lower() for name in future_names), "NFL should have division winner futures"
    
    # Test NBA specific futures  
    response = get_season_futures.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.BASKETBALL,
        league=LeagueEnum.NBA,
        year=2024,
        limit=50,
    )
    
    if response.status_code == 200:
        result = response.parsed
        future_names = [item.name for item in result.items]
        
        # Log NBA futures
        logger.info(f"\n{'='*60}")
        logger.info("NBA FUTURES FOUND:")
        logger.info(f"{'='*60}")
        for i, name in enumerate(future_names[:10]):
            logger.info(f"{i+1}. {name}")
        if len(future_names) > 10:
            logger.info(f"... and {len(future_names) - 10} more")
        
        # NBA should have championship/finals winner
        assert any("winner" in name.lower() or "champion" in name.lower() for name in future_names), "NBA should have championship futures"