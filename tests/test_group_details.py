import pytest
from models.sports_core_api.espn_sports_core_api_client.models.group_details_response import (
    GroupDetailsResponse,
)
from models.sports_core_api.espn_sports_core_api_client.models.reference import (
    Reference,
)
from models.sports_core_api.espn_sports_core_api_client.models.sport_enum import (
    SportEnum,
)
from models.sports_core_api.espn_sports_core_api_client.models.league_enum import (
    LeagueEnum,
)
from models.sports_core_api.espn_sports_core_api_client.models.get_league_season_group_details_season_type import (
    GetLeagueSeasonGroupDetailsSeasonType,
)
from models.sports_core_api.espn_sports_core_api_client.api.default.get_league_season_group_details import (
    sync_detailed as get_league_season_group_details,
)


@pytest.mark.api
def test_get_nfc_group_details(sports_core_api_client, ensure_json_output_dir):
    """Test the group details endpoint for NFL NFC (group 7)."""
    response = get_league_season_group_details(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2024,
        season_type=GetLeagueSeasonGroupDetailsSeasonType.VALUE_2,  # regular season
        group_id="7",  # NFC
    )

    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, GroupDetailsResponse), (
        "Response should parse to GroupDetailsResponse"
    )

    # Verify basic group information
    assert result.id == "7", f"Expected group ID 7, got {result.id}"
    assert result.abbreviation == "NFC", (
        f"Expected abbreviation NFC, got {result.abbreviation}"
    )
    assert result.name == "National Football Conference", (
        f"Expected name 'National Football Conference', got {result.name}"
    )
    assert result.is_conference is True, "NFC should be marked as a conference"
    assert result.slug == "national-football-conference", (
        f"Expected slug 'national-football-conference', got {result.slug}"
    )

    # Verify reference fields
    assert isinstance(result.season, Reference), "Season should be a Reference"
    assert result.season.ref, "Season reference should have a $ref URL"
    assert "seasons/2024" in result.season.ref, "Season reference should point to 2024"

    assert isinstance(result.children, Reference), "Children should be a Reference"
    assert result.children.ref, "Children reference should have a $ref URL"
    assert "children" in result.children.ref, (
        "Children reference should contain 'children'"
    )

    assert isinstance(result.parent, Reference), "Parent should be a Reference"
    assert result.parent.ref, "Parent reference should have a $ref URL"

    assert isinstance(result.standings, Reference), "Standings should be a Reference"
    assert result.standings.ref, "Standings reference should have a $ref URL"
    assert "standings" in result.standings.ref, (
        "Standings reference should contain 'standings'"
    )

    assert isinstance(result.teams, Reference), "Teams should be a Reference"
    assert result.teams.ref, "Teams reference should have a $ref URL"
    assert "teams" in result.teams.ref, "Teams reference should contain 'teams'"


@pytest.mark.api
def test_get_afc_group_details(sports_core_api_client, ensure_json_output_dir):
    """Test the group details endpoint for NFL AFC (group 8)."""
    response = get_league_season_group_details(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2024,
        season_type=GetLeagueSeasonGroupDetailsSeasonType.VALUE_2,  # regular season
        group_id="8",  # AFC
    )

    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, GroupDetailsResponse), (
        "Response should parse to GroupDetailsResponse"
    )

    # Verify basic group information
    assert result.id == "8", f"Expected group ID 8, got {result.id}"
    assert result.abbreviation == "AFC", (
        f"Expected abbreviation AFC, got {result.abbreviation}"
    )
    assert result.name == "American Football Conference", (
        f"Expected name 'American Football Conference', got {result.name}"
    )
    assert result.is_conference is True, "AFC should be marked as a conference"
    assert result.slug == "american-football-conference", (
        f"Expected slug 'american-football-conference', got {result.slug}"
    )


@pytest.mark.api
@pytest.mark.parametrize(
    "group_id,expected_abbreviation",
    [
        ("7", "NFC"),
        ("8", "AFC"),
    ],
)
def test_get_group_details_parametrized(
    sports_core_api_client, group_id, expected_abbreviation
):
    """Test the group details endpoint for both NFL conferences."""
    response = get_league_season_group_details(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2024,
        season_type=GetLeagueSeasonGroupDetailsSeasonType.VALUE_2,  # regular season
        group_id=group_id,
    )

    assert response.status_code == 200, (
        f"Expected status code 200 for group {group_id}, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, GroupDetailsResponse), (
        f"Response should parse to GroupDetailsResponse for group {group_id}"
    )

    assert result.id == group_id, f"Expected group ID {group_id}, got {result.id}"
    assert result.abbreviation == expected_abbreviation, (
        f"Expected abbreviation {expected_abbreviation}, got {result.abbreviation}"
    )
    assert result.is_conference is True, (
        f"Group {group_id} should be marked as a conference"
    )


@pytest.mark.api
def test_get_group_details_invalid_group(sports_core_api_client):
    """Test the group details endpoint with an invalid group ID."""
    response = get_league_season_group_details(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        year=2024,
        season_type=GetLeagueSeasonGroupDetailsSeasonType.VALUE_2,  # regular season
        group_id="999",  # Invalid group ID
    )

    # Should return 404 for invalid group
    assert response.status_code == 404, (
        f"Expected status code 404 for invalid group, got {response.status_code}"
    )
