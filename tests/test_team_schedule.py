import pytest
import json
import logging
from models.site_api.espn_nfl_api_client.api.default import get_team_schedule
from models.site_api.espn_nfl_api_client.models.team_schedule_response import TeamScheduleResponse
from models.site_api.espn_nfl_api_client.models.sport_enum import SportEnum
from models.site_api.espn_nfl_api_client.models.league_enum import LeagueEnum
from models.site_api.espn_nfl_api_client.types import UNSET

logging.basicConfig(level=logging.INFO)


@pytest.mark.api
@pytest.mark.parametrize("sport,league,team_id", [
    (SportEnum.BASKETBALL, LeagueEnum.NBA, "LAL"),
    (SportEnum.FOOTBALL, LeagueEnum.NFL, "KC"),
    (SportEnum.BASEBALL, LeagueEnum.MLB, "NYY"),
    (SportEnum.HOCKEY, LeagueEnum.NHL, "TOR"),
    (SportEnum.BASKETBALL, LeagueEnum.WNBA, "LA"),
    (SportEnum.FOOTBALL, LeagueEnum.COLLEGE_FOOTBALL, "MICH"),
    (SportEnum.BASKETBALL, LeagueEnum.MENS_COLLEGE_BASKETBALL, "DUKE"),
    (SportEnum.BASKETBALL, LeagueEnum.WOMENS_COLLEGE_BASKETBALL, "2"),  # Use numeric ID for Auburn
])
def test_get_team_schedule(site_api_client, ensure_json_output_dir, sport, league, team_id):
    """Test fetching team schedules across different sports."""
    response = get_team_schedule.sync_detailed(
        client=site_api_client,
        sport=sport,
        league=league,
        team_id_or_abbrev=team_id
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code} for {sport.value}/{league.value}/{team_id}"
    
    result = response.parsed
    assert isinstance(result, TeamScheduleResponse), f"Response should parse to TeamScheduleResponse for {sport.value}/{league.value}"
    
    # Common fields present in all sports
    assert result.timestamp, "timestamp field should be present"
    assert result.status == "success", f"status should be 'success', got {result.status}"
    assert result.season, "season field should be present"
    assert result.team, "team field should be present"
    assert result.events is not None, "events field should be present (can be empty array)"
    
    # Team verification (only check if team_id is not numeric)
    if not team_id.isdigit():
        assert result.team.abbreviation == team_id, f"Team abbreviation should match requested team {team_id}"
    
    # Log some interesting info
    logging.info(f"{sport.value.upper()} - {result.team.display_name} Schedule:")
    if result.season:
        season_info = result.season.display_name if result.season.display_name else f"{result.season.year}"
    else:
        season_info = 'N/A'
    logging.info(f"  Season: {season_info}")
    logging.info(f"  Number of events: {len(result.events)}")
    if result.bye_week is not UNSET and sport == SportEnum.FOOTBALL:
        logging.info(f"  Bye week: {result.bye_week}")
    
    # Sport-specific assertions
    if sport == SportEnum.FOOTBALL and league == LeagueEnum.NFL:
        # NFL teams have bye week info, but only on regular season schedules —
        # the endpoint defaults to the preseason schedule during the summer,
        # and that response omits byeWeek entirely.
        requested_season_type = (
            result.requested_season.type if result.requested_season else None
        )
        if requested_season_type == 2:
            assert result.bye_week is not UNSET, (
                "NFL regular season schedule should have bye week information"
            )
        else:
            logging.info(
                f"  Skipping bye week check: schedule is for season type {requested_season_type}"
            )
    else:
        # Other sports typically don't have bye weeks
        if result.bye_week is not UNSET:
            logging.info(f"  Note: {sport.value} has bye_week field set to {result.bye_week}")
    
    # Save response for analysis
    output_file = f"{ensure_json_output_dir}/team_schedule_{sport.value}_{league.value}_{team_id}.json"
    with open(output_file, "w") as f:
        json.dump(result.to_dict(), f, indent=2, default=str)
    
    logging.info(f"  Response saved to {output_file}")


@pytest.mark.api
def test_get_team_schedule_with_season(site_api_client, ensure_json_output_dir):
    """Test fetching team schedule for a specific season."""
    response = get_team_schedule.sync_detailed(
        client=site_api_client,
        sport=SportEnum.BASKETBALL,
        league=LeagueEnum.NBA,
        team_id_or_abbrev="LAL",
        season=2023
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, TeamScheduleResponse), "Response should parse to TeamScheduleResponse"
    
    # Verify we got the requested season
    if result.requested_season:
        assert result.requested_season.year == 2023, f"Requested season should be 2023, got {result.requested_season.year}"
    
    logging.info("NBA Lakers 2023 Schedule:")
    logging.info(f"  Number of events: {len(result.events)}")
    
    # Save response
    output_file = f"{ensure_json_output_dir}/team_schedule_nba_LAL_2023.json"
    with open(output_file, "w") as f:
        json.dump(result.to_dict(), f, indent=2, default=str)


@pytest.mark.api
def test_get_nfl_team_schedule_has_bye_week(site_api_client):
    """Test that an NFL regular season schedule reports the team's bye week.

    Uses a completed season so the schedule is always the regular season one —
    the unparameterized endpoint returns the preseason schedule (which has no
    byeWeek) during the summer.
    """
    response = get_team_schedule.sync_detailed(
        client=site_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        team_id_or_abbrev="KC",
        season=2024,
    )

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    result = response.parsed
    assert isinstance(result, TeamScheduleResponse), "Response should parse to TeamScheduleResponse"
    assert result.requested_season, "requestedSeason should be present"
    assert result.requested_season.type == 2, (
        f"Expected regular season schedule, got season type {result.requested_season.type}"
    )
    assert result.bye_week is not UNSET, "NFL regular season schedule should have bye week information"

    logging.info(f"NFL KC 2024 bye week: {result.bye_week}")


@pytest.mark.api
def test_get_team_schedule_invalid_team(site_api_client):
    """Test fetching schedule for an invalid team."""
    response = get_team_schedule.sync_detailed(
        client=site_api_client,
        sport=SportEnum.BASKETBALL,
        league=LeagueEnum.NBA,
        team_id_or_abbrev="INVALID"
    )
    
    # ESPN typically returns 400 for invalid teams
    assert response.status_code in [400, 404], f"Expected error status code, got {response.status_code}"