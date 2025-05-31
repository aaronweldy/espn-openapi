#!/usr/bin/env python3
"""
Test ESPN Generic API Endpoints (news, teams, scoreboard)
Tests the generic endpoints that work across multiple sports and leagues
"""

import json
import pytest
import logging

from models.site_api.espn_nfl_api_client.api.default import (
    get_teams_list,
    get_league_news,
    get_scoreboard,
)
from models.site_api.espn_nfl_api_client.models.sport_enum import SportEnum
from models.site_api.espn_nfl_api_client.models.league_enum import LeagueEnum
from models.site_api.espn_nfl_api_client.models.get_scoreboard_sport import GetScoreboardSport
from models.site_api.espn_nfl_api_client.models.get_scoreboard_seasontype import GetScoreboardSeasontype
from models.site_api.espn_nfl_api_client.models.teams_list_response import TeamsListResponse
from models.site_api.espn_nfl_api_client.models.sport_news_api_schema import SportNewsAPISchema
from models.site_api.espn_nfl_api_client.models.generic_scoreboard_response import GenericScoreboardResponse
from models.site_api.espn_nfl_api_client.models.error_response import ErrorResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Test data for different sport/league combinations
SPORT_LEAGUE_COMBINATIONS = [
    # Major Professional Sports
    (SportEnum.BASKETBALL, LeagueEnum.NBA, "National Basketball Association"),
    (SportEnum.BASKETBALL, LeagueEnum.WNBA, "Women's National Basketball Association"),
    (SportEnum.FOOTBALL, LeagueEnum.NFL, "National Football League"),
    (SportEnum.BASEBALL, LeagueEnum.MLB, "Major League Baseball"),
    (SportEnum.HOCKEY, LeagueEnum.NHL, "National Hockey League"),
    # College Sports
    (SportEnum.FOOTBALL, LeagueEnum.COLLEGE_FOOTBALL, "NCAA Football"),
    (SportEnum.BASKETBALL, LeagueEnum.MENS_COLLEGE_BASKETBALL, "NCAA Men's Basketball"),
    (SportEnum.BASKETBALL, LeagueEnum.WOMENS_COLLEGE_BASKETBALL, "NCAA Women's Basketball"),
    (SportEnum.BASEBALL, LeagueEnum.COLLEGE_BASEBALL, "NCAA Baseball"),
]


class TestGenericTeams:
    """Test the generic teams endpoint across different sports"""
    
    @pytest.mark.api
    @pytest.mark.parametrize("sport,league,expected_name", SPORT_LEAGUE_COMBINATIONS)
    def test_get_teams_list(self, site_api_client, ensure_json_output_dir, sport, league, expected_name):
        """Test fetching teams list for different sports leagues."""
        
        # Call the API
        response = get_teams_list.sync_detailed(
            client=site_api_client,
            sport=sport,
            league=league
        )
        
        # Validate response
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        
        result = response.parsed
        assert result is not None, "Response parsed to None"
        assert not isinstance(result, ErrorResponse), f"Got error response: {result}"
        assert isinstance(result, TeamsListResponse), f"Expected TeamsListResponse, got {type(result)}"
        
        # Validate structure
        assert result.sports, "Missing sports list"
        assert len(result.sports) > 0, "Empty sports list"
        
        sport_data = result.sports[0]
        assert sport_data.leagues, "Missing leagues list"
        assert len(sport_data.leagues) > 0, "Empty leagues list"
        
        league_data = sport_data.leagues[0]
        assert league_data.teams, "Missing teams list"
        assert len(league_data.teams) > 0, "Should have at least one team"
        
        # Check team structure (only if there are teams)
        team_entry = league_data.teams[0]
        assert team_entry.team, "TeamEntry missing team object"
        team = team_entry.team
        assert team.id, "Team missing id"
        assert team.display_name, "Team missing display_name"
        assert team.abbreviation, "Team missing abbreviation"
        
        # Save response for analysis
        filename = f"generic_{sport.value}_{league.value}_teams.json"
        with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
        
        logger.info(f"{sport.value.upper()} {league.value.upper()} Teams:")
        logger.info(f"  League: {league_data.name}")
        logger.info(f"  Total teams: {len(league_data.teams)}")
        logger.info(f"  Sample teams: {', '.join(t.team.display_name for t in league_data.teams[:3])}")


class TestGenericNews:
    """Test the generic news endpoint across different sports"""
    
    @pytest.mark.api
    @pytest.mark.parametrize("sport,league,expected_name", SPORT_LEAGUE_COMBINATIONS)
    def test_get_league_news(self, site_api_client, ensure_json_output_dir, sport, league, expected_name):
        """Test fetching news for different sports leagues."""
        
        # Call the API
        response = get_league_news.sync_detailed(
            client=site_api_client,
            sport=sport,
            league=league,
            limit=3  # Limit to 3 articles for testing
        )
        
        # Validate response
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        
        result = response.parsed
        assert result is not None, "Response parsed to None"
        assert not isinstance(result, ErrorResponse), f"Got error response: {result}"
        assert isinstance(result, SportNewsAPISchema), f"Expected SportNewsAPISchema, got {type(result)}"
        
        # Validate required fields
        assert result.header, "Missing required header field"
        assert result.articles, "Missing or empty articles list"
        
        # Check first article structure
        article = result.articles[0]
        assert article.headline, "Article missing headline"
        assert article.type, "Article missing type"
        
        # Save response for analysis
        filename = f"generic_{sport.value}_{league.value}_news.json"
        with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
        
        logger.info(f"{sport.value.upper()} {league.value.upper()} News:")
        logger.info(f"  Header: {result.header}")
        logger.info(f"  Articles count: {len(result.articles)}")
        logger.info(f"  First article: {result.articles[0].headline}")


class TestGenericScoreboard:
    """Test the generic scoreboard endpoint across different sports"""
    
    @pytest.mark.api
    @pytest.mark.parametrize("sport,league,expected_name", [
        # Test major sports only - college sports might have different date requirements
        (SportEnum.BASKETBALL, LeagueEnum.NBA, "National Basketball Association"),
        (SportEnum.BASKETBALL, LeagueEnum.WNBA, "Women's National Basketball Association"),
        (SportEnum.FOOTBALL, LeagueEnum.NFL, "National Football League"),
        (SportEnum.BASEBALL, LeagueEnum.MLB, "Major League Baseball"),
        (SportEnum.HOCKEY, LeagueEnum.NHL, "National Hockey League"),
    ])
    def test_get_scoreboard(self, site_api_client, ensure_json_output_dir, sport, league, expected_name):
        """Test fetching scoreboard for different sports leagues."""
        
        # Call the API
        response = get_scoreboard.sync_detailed(
            client=site_api_client,
            sport=GetScoreboardSport(sport.value),
            league=league
            # Not providing dates to get current/default scoreboard
        )
        
        # Validate response
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        
        result = response.parsed
        assert result is not None, "Response parsed to None"
        assert not isinstance(result, ErrorResponse), f"Got error response: {result}"
        assert isinstance(result, GenericScoreboardResponse), f"Expected GenericScoreboardResponse, got {type(result)}"
        
        # Validate structure
        assert result.leagues, "Missing leagues list"
        assert len(result.leagues) > 0, "Empty leagues list"
        
        league_data = result.leagues[0]
        # Events might be empty depending on the day/season
        
        # Save response for analysis
        filename = f"generic_{sport.value}_{league.value}_scoreboard.json"
        with open(f"{ensure_json_output_dir}/{filename}", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
        
        logger.info(f"{sport.value.upper()} {league.value.upper()} Scoreboard:")
        logger.info(f"  League: {league_data.name if league_data.name else 'N/A'}")
        logger.info(f"  Events count: {len(result.events) if result.events else 0}")
        if result.events:
            event = result.events[0]
            logger.info(f"  First event: {event.name if event.name else 'N/A'}")


class TestCrossSportValidation:
    """Validate that generic endpoints work consistently across sports"""
    
    @pytest.mark.api
    def test_all_endpoints_for_nba(self, site_api_client, ensure_json_output_dir):
        """Test all three generic endpoints work for NBA"""
        sport = SportEnum.BASKETBALL
        league = LeagueEnum.NBA
        
        # Test teams
        teams_response = get_teams_list.sync_detailed(
            client=site_api_client,
            sport=sport,
            league=league
        )
        assert teams_response.status_code == 200
        assert isinstance(teams_response.parsed, TeamsListResponse)
        assert len(teams_response.parsed.sports[0].leagues[0].teams) == 30  # NBA has 30 teams
        
        # Test news
        news_response = get_league_news.sync_detailed(
            client=site_api_client,
            sport=sport,
            league=league,
            limit=5
        )
        assert news_response.status_code == 200
        assert isinstance(news_response.parsed, SportNewsAPISchema)
        assert len(news_response.parsed.articles) > 0
        
        # Test scoreboard
        scoreboard_response = get_scoreboard.sync_detailed(
            client=site_api_client,
            sport=GetScoreboardSport(sport.value),
            league=league
        )
        assert scoreboard_response.status_code == 200
        assert isinstance(scoreboard_response.parsed, GenericScoreboardResponse)
        
        logger.info("✅ All generic endpoints work correctly for NBA")
    
    @pytest.mark.api
    def test_all_endpoints_for_wnba(self, site_api_client, ensure_json_output_dir):
        """Test all three generic endpoints work for WNBA"""
        sport = SportEnum.BASKETBALL
        league = LeagueEnum.WNBA
        
        # Test teams
        teams_response = get_teams_list.sync_detailed(
            client=site_api_client,
            sport=sport,
            league=league
        )
        assert teams_response.status_code == 200
        assert isinstance(teams_response.parsed, TeamsListResponse)
        assert len(teams_response.parsed.sports[0].leagues[0].teams) == 14  # WNBA has 14 teams
        
        # Test news
        news_response = get_league_news.sync_detailed(
            client=site_api_client,
            sport=sport,
            league=league,
            limit=5
        )
        assert news_response.status_code == 200
        assert isinstance(news_response.parsed, SportNewsAPISchema)
        
        # Test scoreboard
        scoreboard_response = get_scoreboard.sync_detailed(
            client=site_api_client,
            sport=GetScoreboardSport(sport.value),
            league=league
        )
        assert scoreboard_response.status_code == 200
        assert isinstance(scoreboard_response.parsed, GenericScoreboardResponse)
        
        logger.info("✅ All generic endpoints work correctly for WNBA")