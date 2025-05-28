import pytest
from models.site_api.espn_nfl_api_client.models.teams_list_response import (
    TeamsListResponse,
)
from models.site_api.espn_nfl_api_client.models.team_details_response import (
    TeamDetailsResponse,
)
from models.site_api.espn_nfl_api_client.api.default.get_nhl_teams_list import (
    sync_detailed as get_nhl_teams_list,
)
from models.site_api.espn_nfl_api_client.api.default.get_nhl_team_details import (
    sync_detailed as get_nhl_team_details,
)


@pytest.mark.api
def test_get_nhl_teams_list(site_api_client, ensure_json_output_dir):
    """Test the NHL teams list endpoint."""
    response = get_nhl_teams_list(client=site_api_client)

    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, TeamsListResponse), (
        "Response should parse to TeamsListResponse"
    )

    # Verify we have sports data
    assert result.sports, "Response should contain sports data"
    assert len(result.sports) > 0, "Should have at least one sport"

    # Find the hockey sport
    hockey_sport = None
    for sport in result.sports:
        if sport.slug == "hockey":
            hockey_sport = sport
            break

    assert hockey_sport is not None, "Should find hockey sport"
    assert hockey_sport.name == "Ice Hockey", (
        f"Expected 'Ice Hockey', got {hockey_sport.name}"
    )

    # Verify NHL league
    assert hockey_sport.leagues, "Hockey sport should have leagues"
    nhl_league = None
    for league in hockey_sport.leagues:
        if league.slug == "nhl":
            nhl_league = league
            break

    assert nhl_league is not None, "Should find NHL league"
    assert nhl_league.name == "National Hockey League", (
        f"Expected 'National Hockey League', got {nhl_league.name}"
    )
    assert nhl_league.abbreviation == "NHL", (
        f"Expected abbreviation 'NHL', got {nhl_league.abbreviation}"
    )

    # Verify teams
    assert nhl_league.teams, "NHL league should have teams"
    assert len(nhl_league.teams) == 32, (
        f"Expected 32 NHL teams, got {len(nhl_league.teams)}"
    )

    # Check a few specific teams
    team_abbreviations = {team.team.abbreviation for team in nhl_league.teams}
    expected_teams = {"BOS", "NYR", "TOR", "MTL", "CHI", "DET", "EDM", "CGY"}
    for team_abbrev in expected_teams:
        assert team_abbrev in team_abbreviations, (
            f"Expected to find team {team_abbrev} in NHL teams"
        )

    # Verify team structure for first team
    first_team = nhl_league.teams[0].team
    assert first_team.id, "Team should have an ID"
    assert first_team.uid, "Team should have a UID"
    assert first_team.slug, "Team should have a slug"
    assert first_team.abbreviation, "Team should have an abbreviation"
    assert first_team.display_name, "Team should have a display name"
    assert first_team.name, "Team should have a name"
    assert first_team.location, "Team should have a location"
    assert first_team.color, "Team should have a primary color"
    assert first_team.alternate_color, "Team should have an alternate color"
    assert first_team.logos, "Team should have logos"
    assert len(first_team.logos) > 0, "Team should have at least one logo"
    assert first_team.links, "Team should have links"
    assert len(first_team.links) > 0, "Team should have at least one link"

    # Save response for inspection
    import json

    with open(f"{ensure_json_output_dir}/nhl_teams_response_processed.json", "w") as f:
        if response.parsed:
            json.dump(response.parsed.to_dict(), f, indent=2)

    print(f"\n=== NHL Teams List ===")
    print(f"Total Teams: {len(nhl_league.teams)}")
    print(f"League Year: {nhl_league.year if nhl_league.year else 'N/A'}")
    print(f"\n--- Teams ---")
    for team_entry in sorted(nhl_league.teams, key=lambda x: x.team.display_name):
        team = team_entry.team
        print(f"{team.display_name} ({team.abbreviation})")
        print(f"  Location: {team.location}")
        print(f"  Colors: Primary={team.color}, Alt={team.alternate_color}")
        if team.logos:
            print(f"  Logo: {team.logos[0].href}")
        print()


@pytest.mark.api
def test_get_nhl_team_details_bruins(site_api_client, ensure_json_output_dir):
    """Test the NHL team details endpoint for Boston Bruins."""
    response = get_nhl_team_details(client=site_api_client, team_id_or_abbrev="1")

    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, TeamDetailsResponse), (
        "Response should parse to TeamDetailsResponse"
    )

    # The response contains the team directly
    bruins_team = result.team

    assert bruins_team.id == "1", f"Expected team ID 1, got {bruins_team.id}"
    assert bruins_team.abbreviation == "BOS", (
        f"Expected abbreviation BOS, got {bruins_team.abbreviation}"
    )
    assert "Bruins" in bruins_team.display_name, (
        f"Expected 'Bruins' in display name, got {bruins_team.display_name}"
    )
    assert bruins_team.location == "Boston", (
        f"Expected location 'Boston', got {bruins_team.location}"
    )


@pytest.mark.api
def test_get_nhl_team_details_by_abbreviation(site_api_client, ensure_json_output_dir):
    """Test the NHL team details endpoint using team abbreviation."""
    response = get_nhl_team_details(client=site_api_client, team_id_or_abbrev="TOR")

    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, TeamDetailsResponse), (
        "Response should parse to TeamDetailsResponse"
    )

    # The response contains the team directly
    leafs_team = result.team

    assert leafs_team.abbreviation == "TOR", (
        f"Expected abbreviation TOR, got {leafs_team.abbreviation}"
    )
    assert "Maple Leafs" in leafs_team.display_name, (
        f"Expected 'Maple Leafs' in display name, got {leafs_team.display_name}"
    )
    assert leafs_team.location == "Toronto", (
        f"Expected location 'Toronto', got {leafs_team.location}"
    )


@pytest.mark.api
@pytest.mark.parametrize(
    "team_identifier,expected_abbreviation",
    [
        ("1", "BOS"),  # Boston Bruins by ID
        ("BOS", "BOS"),  # Boston Bruins by abbreviation
        ("TOR", "TOR"),  # Toronto Maple Leafs by abbreviation
        ("NYR", "NYR"),  # New York Rangers by abbreviation
    ],
)
def test_get_nhl_team_details_parametrized(
    site_api_client, team_identifier, expected_abbreviation
):
    """Test the NHL team details endpoint with various team identifiers."""
    response = get_nhl_team_details(
        client=site_api_client, team_id_or_abbrev=team_identifier
    )

    assert response.status_code == 200, (
        f"Expected status code 200 for team {team_identifier}, got {response.status_code}"
    )

    result = response.parsed
    assert isinstance(result, TeamDetailsResponse), (
        f"Response should parse to TeamDetailsResponse for team {team_identifier}"
    )

    # The response contains the team directly
    team = result.team

    assert team.abbreviation == expected_abbreviation, (
        f"Expected abbreviation {expected_abbreviation}, got {team.abbreviation}"
    )


@pytest.mark.api
def test_get_nhl_team_details_invalid_team(site_api_client):
    """Test the NHL team details endpoint with an invalid team identifier."""
    response = get_nhl_team_details(client=site_api_client, team_id_or_abbrev="INVALID")

    # Should return 400 for invalid team
    assert response.status_code == 400, (
        f"Expected status code 400 for invalid team, got {response.status_code}"
    )
