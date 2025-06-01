"""Tests for game predictor endpoints."""

import json
import logging
import pytest
from models.sports_core_api.espn_sports_core_api_client.api.default import get_game_predictor
from models.sports_core_api.espn_sports_core_api_client.models import (
    PredictorResponse,
    PredictorTeam,
    PredictorStatistic,
    Reference,
    LeagueEnum,
    SportEnum,
)
from models.sports_core_api.espn_sports_core_api_client.types import UNSET

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league,event_id,expected_stats",
    [
        (SportEnum.FOOTBALL, LeagueEnum.NFL, "401547602", ["gameProjection", "matchupQuality", "teamDefEff", "teamOffEff"]),
        (SportEnum.BASKETBALL, LeagueEnum.NBA, "401584793", ["gameProjection", "matchupQuality", "teamPredPtDiff"]),
        pytest.param(SportEnum.BASEBALL, LeagueEnum.MLB, "401472463", ["gameProjection"], marks=pytest.mark.xfail(reason="MLB predictor might not be available")),
        pytest.param(SportEnum.HOCKEY, LeagueEnum.NHL, "401559593", ["gameProjection"], marks=pytest.mark.xfail(reason="NHL predictor not supported")),
        pytest.param(SportEnum.FOOTBALL, LeagueEnum.COLLEGE_FOOTBALL, "401628444", ["gameProjection"], marks=pytest.mark.xfail(reason="College football predictor not supported")),
    ],
)
def test_get_game_predictor(sports_core_api_client, ensure_json_output_dir, sport, league, event_id, expected_stats):
    """Test fetching game predictor data for different sports."""
    response = get_game_predictor.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=event_id,  # Usually the same as event_id
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, PredictorResponse), "Response should parse to PredictorResponse"
    
    # Validate response structure
    assert result.name, "Predictor should have a game name"
    assert result.short_name, "Predictor should have a short name"
    assert isinstance(result.home_team, PredictorTeam), "Home team should be PredictorTeam"
    assert isinstance(result.away_team, PredictorTeam), "Away team should be PredictorTeam"
    
    # Validate teams have references
    assert result.home_team.team, "Home team should have team reference"
    assert isinstance(result.home_team.team, Reference), "Home team reference should be Reference"
    assert result.away_team.team, "Away team should have team reference"
    assert isinstance(result.away_team.team, Reference), "Away team reference should be Reference"
    
    # Log predictor summary
    logger.info(f"\n{'='*60}")
    logger.info(f"{sport.value.upper()} {league.value.upper()} PREDICTOR - {event_id}")
    logger.info(f"{'='*60}")
    logger.info(f"Game: {result.name}")
    logger.info(f"Short: {result.short_name}")
    if result.last_modified:
        logger.info(f"Last Modified: {result.last_modified}")
    logger.info(f"{'-'*60}")
    
    # Check which team has statistics (varies by sport)
    home_stats = result.home_team.statistics if result.home_team.statistics else []
    away_stats = result.away_team.statistics if result.away_team.statistics else []
    
    # At least one team should have statistics
    assert home_stats or away_stats, "At least one team should have statistics"
    
    # Log statistics for both teams
    if home_stats:
        logger.info("\nHOME TEAM STATISTICS:")
        logger.info("-" * 40)
        for stat in home_stats:
            assert isinstance(stat, PredictorStatistic), "Should be PredictorStatistic"
            logger.info(f"{stat.display_name}: {stat.display_value}")
            if stat.description:
                logger.info(f"  Description: {stat.description}")
    
    if away_stats:
        logger.info("\nAWAY TEAM STATISTICS:")
        logger.info("-" * 40)
        for stat in away_stats:
            assert isinstance(stat, PredictorStatistic), "Should be PredictorStatistic"
            logger.info(f"{stat.display_name}: {stat.display_value}")
            if stat.description:
                logger.info(f"  Description: {stat.description}")
    
    # Verify expected statistics are present
    all_stats = home_stats + away_stats
    stat_names = {stat.name for stat in all_stats}
    
    # Some expected stats should be present (but not all sports have all stats)
    found_stats = [stat for stat in expected_stats if stat in stat_names]
    assert len(found_stats) > 0, f"Should have at least one of the expected stats: {expected_stats}"
    
    logger.info(f"\nFound statistics: {', '.join(stat_names)}")
    logger.info(f"Expected stats found: {', '.join(found_stats)}")
    
    # Save example response
    output_file = f"{ensure_json_output_dir}/{sport.value}_{league.value}_predictor_{event_id}_test.json"
    with open(output_file, "w") as f:
        json.dump(result.to_dict() if hasattr(result, 'to_dict') else result.__dict__, f, indent=2)
    
    print(f"Saved predictor response to {output_file}")


@pytest.mark.api
def test_predictor_win_probability_analysis(sports_core_api_client):
    """Test analyzing win probabilities from predictor data."""
    # Get NFL game predictor
    response = get_game_predictor.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        event_id="401547602",
        competition_id="401547602",
    )
    
    assert response.status_code == 200
    result = response.parsed
    
    logger.info(f"\n{'='*60}")
    logger.info("WIN PROBABILITY ANALYSIS")
    logger.info(f"{'='*60}")
    logger.info(f"Game: {result.short_name}")
    
    # Find game projection stats
    home_win_prob = None
    away_win_prob = None
    
    # Check home team stats
    if result.home_team.statistics:
        for stat in result.home_team.statistics:
            if stat.name == "gameProjection":
                home_win_prob = stat.value
                logger.info(f"Home Team Win Probability: {stat.display_value}%")
    
    # Check away team stats
    if result.away_team.statistics:
        for stat in result.away_team.statistics:
            if stat.name == "gameProjection":
                away_win_prob = stat.value
                logger.info(f"Away Team Win Probability: {stat.display_value}%")
    
    # Verify probabilities add up to ~100 (allowing for ties)
    if home_win_prob and away_win_prob:
        total_prob = home_win_prob + away_win_prob
        logger.info(f"Total Probability: {total_prob:.1f}%")
        assert 98.0 <= total_prob <= 102.0, "Win probabilities should sum to approximately 100%"
        
        # Determine favorite
        if home_win_prob > away_win_prob:
            logger.info(f"Favorite: HOME team with {home_win_prob:.1f}% chance")
        else:
            logger.info(f"Favorite: AWAY team with {away_win_prob:.1f}% chance")


@pytest.mark.api
def test_predictor_efficiency_ratings(sports_core_api_client):
    """Test efficiency ratings in NFL predictor data."""
    response = get_game_predictor.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        event_id="401547602",
        competition_id="401547602",
    )
    
    assert response.status_code == 200
    result = response.parsed
    
    logger.info(f"\n{'='*60}")
    logger.info("TEAM EFFICIENCY ANALYSIS")
    logger.info(f"{'='*60}")
    logger.info(f"Game: {result.short_name}")
    
    # Collect efficiency stats
    efficiencies = {"home": {}, "away": {}}
    
    if result.home_team.statistics:
        for stat in result.home_team.statistics:
            if "Eff" in stat.name:
                efficiencies["home"][stat.name] = {
                    "value": stat.value,
                    "display": stat.display_value,
                    "name": stat.display_name
                }
    
    if result.away_team.statistics:
        for stat in result.away_team.statistics:
            if "Eff" in stat.name:
                efficiencies["away"][stat.name] = {
                    "value": stat.value,
                    "display": stat.display_value,
                    "name": stat.display_name
                }
    
    # Log efficiency comparisons
    logger.info("\nEFFICIENCY RATINGS:")
    logger.info("-" * 40)
    
    for eff_type in ["teamOffEff", "teamDefEff", "teamSTEff", "teamTotEff"]:
        home_eff = efficiencies["home"].get(eff_type)
        away_eff = efficiencies["away"].get(eff_type)
        
        if home_eff and away_eff:
            logger.info(f"\n{home_eff['name']}:")
            logger.info(f"  Home: {home_eff['display']}")
            logger.info(f"  Away: {away_eff['display']}")
            
            # Determine which team is better
            if home_eff['value'] > away_eff['value']:
                advantage = home_eff['value'] - away_eff['value']
                logger.info(f"  Advantage: HOME (+{advantage:.1f})")
            else:
                advantage = away_eff['value'] - home_eff['value']
                logger.info(f"  Advantage: AWAY (+{advantage:.1f})")


@pytest.mark.api
def test_predictor_invalid_event(sports_core_api_client):
    """Test predictor with invalid event ID."""
    response = get_game_predictor.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        event_id="999999999",
        competition_id="999999999",
    )
    
    # API might return 404 or 400 for invalid event
    assert response.status_code in [400, 404], f"Expected status code 400 or 404, got {response.status_code}"


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league",
    [
        (SportEnum.FOOTBALL, LeagueEnum.NFL),
        (SportEnum.BASKETBALL, LeagueEnum.NBA),
    ],
)
def test_predictor_matchup_quality(sports_core_api_client, sport, league):
    """Test matchup quality metric in predictor data."""
    # Use recent game IDs based on sport
    event_ids = {
        (SportEnum.FOOTBALL, LeagueEnum.NFL): "401547602",
        (SportEnum.BASKETBALL, LeagueEnum.NBA): "401584793",
    }
    
    event_id = event_ids.get((sport, league))
    if not event_id:
        pytest.skip(f"No test event ID for {sport.value} {league.value}")
    
    response = get_game_predictor.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        event_id=event_id,
        competition_id=event_id,
    )
    
    assert response.status_code == 200
    result = response.parsed
    
    logger.info(f"\n{'='*60}")
    logger.info(f"MATCHUP QUALITY - {sport.value.upper()} {league.value.upper()}")
    logger.info(f"{'='*60}")
    logger.info(f"Game: {result.short_name}")
    
    # Find matchup quality stat
    matchup_quality = None
    game_quality = None
    
    all_stats = []
    if result.home_team.statistics:
        all_stats.extend(result.home_team.statistics)
    if result.away_team.statistics:
        all_stats.extend(result.away_team.statistics)
    
    for stat in all_stats:
        if stat.name == "matchupQuality":
            matchup_quality = stat.value
            logger.info(f"Matchup Quality: {stat.display_value}/100")
            if stat.description:
                logger.info(f"Description: {stat.description}")
        elif stat.name == "gameQuality":
            game_quality = stat.value
            logger.info(f"Game Quality: {stat.display_value}/100")
    
    # Matchup quality should be between 0 and 100
    if matchup_quality is not None:
        assert 0 <= matchup_quality <= 100, "Matchup quality should be between 0 and 100"
        
        # Interpret matchup quality
        if matchup_quality >= 80:
            logger.info("Rating: EXCELLENT matchup")
        elif matchup_quality >= 60:
            logger.info("Rating: GOOD matchup")
        elif matchup_quality >= 40:
            logger.info("Rating: AVERAGE matchup")
        else:
            logger.info("Rating: BELOW AVERAGE matchup")


@pytest.mark.api
def test_predictor_point_differential(sports_core_api_client):
    """Test predicted point differential in predictor data."""
    # Test with multiple games
    games = [
        (SportEnum.FOOTBALL, LeagueEnum.NFL, "401547602"),
        (SportEnum.BASKETBALL, LeagueEnum.NBA, "401584793"),
    ]
    
    logger.info(f"\n{'='*80}")
    logger.info("PREDICTED POINT DIFFERENTIAL ANALYSIS")
    logger.info(f"{'='*80}")
    
    for sport, league, event_id in games:
        response = get_game_predictor.sync_detailed(
            client=sports_core_api_client,
            sport=sport,
            league=league,
            event_id=event_id,
            competition_id=event_id,
        )
        
        if response.status_code != 200:
            continue
        
        result = response.parsed
        logger.info(f"\n{sport.value.upper()} - {result.short_name}")
        logger.info("-" * 40)
        
        # Find predicted point differential
        point_diffs = {}
        
        if result.home_team.statistics:
            for stat in result.home_team.statistics:
                if stat.name == "teamPredPtDiff":
                    point_diffs["home"] = stat.value
                    logger.info(f"Home Team Predicted Differential: {stat.display_value}")
        
        if result.away_team.statistics:
            for stat in result.away_team.statistics:
                if stat.name == "teamPredPtDiff":
                    point_diffs["away"] = stat.value
                    logger.info(f"Away Team Predicted Differential: {stat.display_value}")
        
        # Analyze the differential
        if "home" in point_diffs and "away" in point_diffs:
            # They should be opposites
            assert abs(point_diffs["home"] + point_diffs["away"]) < 0.1, "Point differentials should be opposites"
            
            # Determine predicted winner and margin
            if point_diffs["away"] > 0:
                logger.info(f"Predicted Winner: AWAY by {point_diffs['away']:.1f} points")
            else:
                logger.info(f"Predicted Winner: HOME by {abs(point_diffs['home']):.1f} points")
        
        # Check for expected points (NBA specific)
        if sport == SportEnum.BASKETBALL:
            expected_pts = {}
            
            for team, team_data in [("home", result.home_team), ("away", result.away_team)]:
                if team_data.statistics:
                    for stat in team_data.statistics:
                        if stat.name == "teamExpectedPts":
                            expected_pts[team] = stat.value
                            logger.info(f"{team.title()} Team Expected Points: {stat.display_value}")
                        elif stat.name == "oppExpectedPts":
                            expected_pts[f"{team}_opp"] = stat.value
            
            if expected_pts:
                logger.info("Expected Score Analysis available")