import json
import logging
import pytest

logging.basicConfig(level=logging.INFO)


@pytest.mark.api
@pytest.mark.parametrize("sport,league,athlete_id,athlete_name", [
    ("football", "nfl", 3139477, "Patrick Mahomes"),
    ("basketball", "nba", 1966, "LeBron James"),
    ("baseball", "mlb", 33192, "Mookie Betts"),
    ("hockey", "nhl", 3024816, "Sidney Crosby"),
])
def test_get_athlete_bio(site_web_api_client, ensure_json_output_dir, sport, league, athlete_id, athlete_name):
    """Test the generic athlete bio endpoint across different sports."""
    from models.site_web_api.espn_site_web_api_client.api.default import get_athlete_bio
    
    response = get_athlete_bio.sync_detailed(
        client=site_web_api_client,
        sport=sport,
        league=league,
        athlete_id=athlete_id
    )
    
    assert response.status_code == 200, f"Expected status code 200 for {athlete_name}, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, "Response should parse successfully"
    
    # Verify team history exists
    assert hasattr(result, 'team_history'), "Response should have team_history"
    assert result.team_history is not None, "team_history should not be None"
    assert len(result.team_history) > 0, f"{athlete_name} should have team history"
    
    # Verify team history entries
    for team in result.team_history:
        assert team.id, "Team should have ID"
        assert team.display_name, "Team should have display name"
        assert team.seasons, "Team should have seasons"
        
        logging.info(f"{athlete_name} played for {team.display_name} ({team.seasons})")
    
    # Awards are optional - some athletes may not have any
    if hasattr(result, 'awards') and result.awards is not None:
        logging.info(f"{athlete_name} has {len(result.awards)} awards")
        for award in result.awards:
            assert award.id, "Award should have ID"
            assert award.name, "Award should have name"
            if award.seasons:
                logging.info(f"  - {award.name}: {award.seasons}")
    
    # Save response for analysis
    response_dict = result.to_dict() if hasattr(result, 'to_dict') else {}
    output_file = f"{ensure_json_output_dir}/{sport}_{league}_athlete_{athlete_id}_bio.json"
    with open(output_file, "w") as f:
        json.dump(response_dict, f, indent=2)
    logging.info(f"Saved bio response to {output_file}")


@pytest.mark.api
@pytest.mark.parametrize("sport,league,athlete_id,athlete_name", [
    ("football", "nfl", 3139477, "Patrick Mahomes"),
    ("basketball", "nba", 1966, "LeBron James"),
    ("baseball", "mlb", 33192, "Mookie Betts"),
    ("hockey", "nhl", 3024816, "Sidney Crosby"),
])
def test_get_athlete_stats(site_web_api_client, ensure_json_output_dir, sport, league, athlete_id, athlete_name):
    """Test the generic athlete stats endpoint across different sports."""
    from models.site_web_api.espn_site_web_api_client.api.default import get_athlete_stats
    
    response = get_athlete_stats.sync_detailed(
        client=site_web_api_client,
        sport=sport,
        league=league,
        athlete_id=athlete_id
    )
    
    assert response.status_code == 200, f"Expected status code 200 for {athlete_name}, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, "Response should parse successfully"
    
    # Verify filters
    assert hasattr(result, 'filters'), "Response should have filters"
    assert result.filters is not None, "filters should not be None"
    assert len(result.filters) > 0, "Should have at least one filter"
    
    # Verify teams
    assert hasattr(result, 'teams'), "Response should have teams"
    assert result.teams is not None, "teams should not be None"
    
    # Teams is an object with team properties, not a dict
    # Count teams by checking available attributes
    team_count = 0
    teams_dict = result.teams.to_dict() if hasattr(result.teams, 'to_dict') else {}
    
    # Log teams
    logging.info(f"{athlete_name} teams data:")
    for team_key, team_data in teams_dict.items():
        if isinstance(team_data, dict) and team_data.get('id'):
            team_count += 1
            team_name = team_data.get('display_name', team_data.get('displayName', 'Unknown'))
            team_abbr = team_data.get('abbreviation', 'N/A')
            logging.info(f"  - {team_name} ({team_abbr})")
    
    assert team_count > 0, f"{athlete_name} should have played for at least one team"
    
    # Verify categories
    assert hasattr(result, 'categories'), "Response should have categories"
    assert result.categories is not None, "categories should not be None"
    assert len(result.categories) > 0, "Should have statistical categories"
    
    # Log categories
    logging.info(f"{athlete_name} has {len(result.categories)} statistical categories:")
    for category in result.categories:
        assert category.name, "Category should have name"
        assert category.display_name, "Category should have display name"
        assert category.statistics is not None, "Category should have statistics"
        logging.info(f"  - {category.display_name} ({len(category.statistics)} seasons)")
    
    # Verify glossary
    assert hasattr(result, 'glossary'), "Response should have glossary"
    assert result.glossary is not None, "glossary should not be None"
    assert len(result.glossary) > 0, "Should have glossary entries"
    
    logging.info(f"Glossary has {len(result.glossary)} entries")
    
    # Save response for analysis
    response_dict = result.to_dict() if hasattr(result, 'to_dict') else {}
    output_file = f"{ensure_json_output_dir}/{sport}_{league}_athlete_{athlete_id}_stats.json"
    with open(output_file, "w") as f:
        json.dump(response_dict, f, indent=2)
    logging.info(f"Saved stats response to {output_file}")


@pytest.mark.api
def test_get_athlete_stats_with_season(site_web_api_client):
    """Test the athlete stats endpoint with optional season parameter."""
    from models.site_web_api.espn_site_web_api_client.api.default import get_athlete_stats
    
    response = get_athlete_stats.sync_detailed(
        client=site_web_api_client,
        sport="basketball",
        league="nba",
        athlete_id=1966,  # LeBron James
        season=2023
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, "Response should parse successfully"
    
    # When season is specified, should still return data
    assert hasattr(result, 'categories'), "Response should have categories"
    assert len(result.categories) > 0, "Should have statistical categories"
    
    logging.info("Successfully retrieved stats with season parameter")