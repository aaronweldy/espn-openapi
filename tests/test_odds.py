import pytest
import json
import logging
from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_competition_odds,
    get_competition_odds_provider,
)
from models.sports_core_api.espn_sports_core_api_client.models import (
    SportEnum,
    LeagueEnum,
    OddsResponse,
    OddsItem,
    OddsProvider,
    TeamOdds,
    OddsItemCurrent,
    OddsValue,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league,event_id,competition_id",
    [
        (SportEnum.FOOTBALL, LeagueEnum.NFL, "401547417", "401547417"),
        (SportEnum.BASKETBALL, LeagueEnum.NBA, "401584793", "401584793"),
    ],
)
def test_get_competition_odds(
    sports_core_api_client, ensure_json_output_dir, sport, league, event_id, competition_id
):
    """Test getting odds for competitions across different sports."""
    response = get_competition_odds.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
    )

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, OddsResponse), "Response should parse to OddsResponse"
    assert result.count > 0, "Should have at least one odds provider"
    assert result.items, "Should have odds items"
    
    # Check first odds item
    first_item = result.items[0]
    assert isinstance(first_item, OddsItem), "Item should be OddsItem"
    assert first_item.ref, "Odds item should have a reference URL"
    assert isinstance(first_item.provider, OddsProvider), "Should have provider info"
    assert first_item.provider.id, "Provider should have ID"
    assert first_item.provider.name, "Provider should have name"
    
    # Check team odds if available
    if first_item.away_team_odds:
        assert isinstance(first_item.away_team_odds, TeamOdds), "Away team odds should be TeamOdds"
        assert isinstance(first_item.away_team_odds.favorite, bool), "Should have favorite flag"
        assert isinstance(first_item.away_team_odds.underdog, bool), "Should have underdog flag"
    
    if first_item.home_team_odds:
        assert isinstance(first_item.home_team_odds, TeamOdds), "Home team odds should be TeamOdds"
    
    # Check current odds if available
    if first_item.current:
        assert isinstance(first_item.current, OddsItemCurrent), "Current should be OddsItemCurrent"
    
    logger.info(f"Found {result.count} odds providers for {sport.value} {league.value} event {event_id}")
    logger.info(f"Providers: {[item.provider.name for item in result.items[:5]]}")
    
    # Save response
    if result:
        with open(f"{ensure_json_output_dir}/{sport.value}_{league.value}_odds_{event_id}.json", "w") as f:
            json.dump(result.to_dict() if hasattr(result, 'to_dict') else result.__dict__, f, indent=2)


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league,event_id,competition_id,provider_id,provider_name",
    [
        (SportEnum.FOOTBALL, LeagueEnum.NFL, "401547417", "401547417", "58", "ESPN BET"),
        (SportEnum.BASKETBALL, LeagueEnum.NBA, "401584793", "401584793", "58", "ESPN BET"),
        (SportEnum.FOOTBALL, LeagueEnum.NFL, "401547417", "401547417", "40", "DraftKings"),
    ],
)
def test_get_competition_odds_provider(
    sports_core_api_client,
    ensure_json_output_dir,
    sport,
    league,
    event_id,
    competition_id,
    provider_id,
    provider_name,
):
    """Test getting odds from a specific provider."""
    response = get_competition_odds_provider.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=competition_id,
        provider_id=provider_id,
    )

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, OddsItem), "Response should parse to OddsItem"
    assert result.ref, "Odds item should have a reference URL"
    assert isinstance(result.provider, OddsProvider), "Should have provider info"
    assert result.provider.id == provider_id, f"Provider ID should be {provider_id}"
    assert result.provider.name == provider_name, f"Provider name should be {provider_name}"
    
    # Check betting details
    assert result.details, "Should have betting details string"
    assert isinstance(result.moneyline_winner, bool), "Should have moneyline winner flag"
    assert isinstance(result.spread_winner, bool), "Should have spread winner flag"
    
    # Check over/under if available
    if result.over_under is not None:
        assert isinstance(result.over_under, (int, float)), "Over/under should be numeric"
    
    # Check spread if available
    if result.spread is not None:
        assert isinstance(result.spread, (int, float)), "Spread should be numeric"
    
    # Check team odds
    if result.away_team_odds:
        assert isinstance(result.away_team_odds, TeamOdds), "Away team odds should be TeamOdds"
        if result.away_team_odds.money_line is not None:
            assert isinstance(result.away_team_odds.money_line, int), "Money line should be integer"
        if result.away_team_odds.current:
            assert result.away_team_odds.current.point_spread, "Should have point spread"
    
    if result.home_team_odds:
        assert isinstance(result.home_team_odds, TeamOdds), "Home team odds should be TeamOdds"
    
    # Check current/open/close odds
    if result.current:
        assert isinstance(result.current, OddsItemCurrent), "Current should be OddsItemCurrent"
        if result.current.over:
            assert result.current.over.alternate_display_value, "Over should have display value"
        if result.current.total:
            assert result.current.total.alternate_display_value, "Total should have display value"
    
    logger.info(f"Got odds from {provider_name} for {sport.value} {league.value}: {result.details}")
    if result.over_under:
        logger.info(f"Over/Under: {result.over_under}")
    if result.spread:
        logger.info(f"Spread: {result.spread}")
    
    # Save response
    if result:
        filename = f"{sport.value}_{league.value}_odds_{event_id}_provider_{provider_id}.json"
        with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
            json.dump(result.to_dict() if hasattr(result, 'to_dict') else result.__dict__, f, indent=2)


@pytest.mark.api
def test_invalid_provider_id(sports_core_api_client):
    """Test requesting odds from an invalid provider ID."""
    response = get_competition_odds_provider.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        event_id="401547417",
        competition_id="401547417",
        provider_id="99999",  # Invalid provider ID
    )
    
    # ESPN API returns 404 for invalid provider
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"