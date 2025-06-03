import pytest
import json
from models.fantasy_api.espn_fantasy_api_client.api.default import get_fantasy_football_season
from models.fantasy_api.espn_fantasy_api_client.models import GetFantasyFootballSeasonView


@pytest.mark.api
def test_get_fantasy_pro_team_schedules(fantasy_api_client, ensure_json_output_dir):
    """Test the fantasy pro team schedules endpoint."""
    
    response = get_fantasy_football_season.sync_detailed(
        client=fantasy_api_client,
        year=2024,
        view=GetFantasyFootballSeasonView.PROTEAMSCHEDULES_WL
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, "Response should parse successfully"
    
    # Verify structure
    assert hasattr(result, 'display'), "Response should have display field"
    assert hasattr(result, 'settings'), "Response should have settings field"
    
    # Check settings structure
    settings = result.settings
    assert settings, "Settings should not be None"
    
    # Check pro teams
    assert hasattr(settings, 'pro_teams'), "Settings should have pro_teams"
    assert settings.pro_teams, "Pro teams list should not be empty"
    assert len(settings.pro_teams) > 30, f"Expected at least 30 teams, got {len(settings.pro_teams)}"
    
    # Analyze first team
    first_team = settings.pro_teams[0]
    assert hasattr(first_team, 'id'), "Team should have ID"
    assert hasattr(first_team, 'abbrev'), "Team should have abbreviation"
    assert hasattr(first_team, 'location'), "Team should have location"
    assert hasattr(first_team, 'name'), "Team should have name"
    assert hasattr(first_team, 'bye_week'), "Team should have bye week"
    
    # Check games schedule
    assert hasattr(first_team, 'pro_games_by_scoring_period'), "Team should have games by scoring period"
    assert first_team.pro_games_by_scoring_period, "Games schedule should not be empty"
    
    # Count total games
    total_games = 0
    bye_week = first_team.bye_week if first_team.bye_week else 0
    
    for period, games in first_team.pro_games_by_scoring_period.additional_properties.items():
        total_games += len(games)
        
        # Check game structure
        if games:
            game = games[0]
            assert hasattr(game, 'id'), "Game should have ID"
            assert hasattr(game, 'home_pro_team_id'), "Game should have home team ID"
            assert hasattr(game, 'away_pro_team_id'), "Game should have away team ID"
            assert hasattr(game, 'date'), "Game should have date"
            assert hasattr(game, 'scoring_period_id'), "Game should have scoring period ID"
    
    print(f"\nFirst team: {first_team.location} {first_team.name} ({first_team.abbrev})")
    print(f"Team ID: {first_team.id}")
    print(f"Bye week: {bye_week}")
    print(f"Total games scheduled: {total_games}")
    
    # Verify all teams have schedules
    teams_with_schedules = 0
    teams_with_bye_weeks = 0
    
    for team in settings.pro_teams:
        if team.pro_games_by_scoring_period and team.pro_games_by_scoring_period.additional_properties:
            teams_with_schedules += 1
        if team.bye_week and team.bye_week > 0:
            teams_with_bye_weeks += 1
    
    print(f"\nTeams with schedules: {teams_with_schedules}/{len(settings.pro_teams)}")
    print(f"Teams with bye weeks: {teams_with_bye_weeks}/{len(settings.pro_teams)}")
    
    # Save sample data for reference
    sample_data = {
        'total_teams': len(settings.pro_teams),
        'teams_with_schedules': teams_with_schedules,
        'teams_with_bye_weeks': teams_with_bye_weeks,
        'sample_team': {
            'id': first_team.id,
            'name': f"{first_team.location} {first_team.name}",
            'abbrev': first_team.abbrev,
            'bye_week': first_team.bye_week if first_team.bye_week else None,
            'total_games': total_games
        }
    }
    
    with open(f"{ensure_json_output_dir}/fantasy_pro_team_schedules_summary.json", "w") as f:
        json.dump(sample_data, f, indent=2)
    
    # All teams should have schedules
    assert teams_with_schedules == len(settings.pro_teams), "All teams should have schedules"
    
    # Most teams should have bye weeks (not all if there are 33 teams - one might be "FA")
    assert teams_with_bye_weeks >= 30, "At least 30 teams should have bye weeks"


@pytest.mark.api
def test_fantasy_pro_team_schedules_specific_checks(fantasy_api_client):
    """Test specific aspects of the pro team schedules."""
    
    response = get_fantasy_football_season.sync_detailed(
        client=fantasy_api_client,
        year=2024,
        view=GetFantasyFootballSeasonView.PROTEAMSCHEDULES_WL
    )
    
    assert response.status_code == 200
    result = response.parsed
    
    # Find a specific team (e.g., Kansas City Chiefs)
    kc_team = None
    for team in result.settings.pro_teams:
        if team.abbrev == "KC":
            kc_team = team
            break
    
    assert kc_team is not None, "Should find Kansas City Chiefs"
    
    # Check that games are properly organized by week
    weeks_with_games = []
    for week_str, games in kc_team.pro_games_by_scoring_period.additional_properties.items():
        if games:
            weeks_with_games.append(int(week_str))
            
            # Each week should have exactly one game
            assert len(games) == 1, f"Week {week_str} should have exactly 1 game, got {len(games)}"
            
            game = games[0]
            # Team should be either home or away
            assert game.home_pro_team_id == kc_team.id or game.away_pro_team_id == kc_team.id, \
                f"Team {kc_team.id} should be in game as home or away"
    
    print(f"\nKC Chiefs schedule:")
    print(f"Weeks with games: {sorted(weeks_with_games)}")
    print(f"Bye week: {kc_team.bye_week}")
    
    # Verify bye week is not in weeks with games
    if kc_team.bye_week and kc_team.bye_week > 0:
        assert kc_team.bye_week not in weeks_with_games, "Bye week should not have a game scheduled"
    
    # Check season settings
    settings = result.settings
    assert hasattr(settings, 'read_only'), "Settings should have read_only flag"
    assert hasattr(settings, 'team_activity_enabled'), "Settings should have team_activity_enabled"
    
    print(f"\nSeason settings:")
    print(f"Read only: {settings.read_only}")
    print(f"Team activity enabled: {settings.team_activity_enabled}")