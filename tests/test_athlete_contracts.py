import pytest
import json
from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_athlete_contracts,
    get_athlete_contract_by_year
)
from models.sports_core_api.espn_sports_core_api_client.models.athlete_contracts_response import AthleteContractsResponse
from models.sports_core_api.espn_sports_core_api_client.models.athlete_contract import AthleteContract
from models.sports_core_api.espn_sports_core_api_client.models.sport_enum import SportEnum
from models.sports_core_api.espn_sports_core_api_client.models.league_enum import LeagueEnum


@pytest.mark.api
def test_get_athlete_contracts_nba(sports_core_api_client, ensure_json_output_dir):
    """Test getting athlete contracts for LeBron James (NBA)."""
    response = get_athlete_contracts.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.BASKETBALL,
        league=LeagueEnum.NBA,
        athlete_id="1966"  # LeBron James
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, AthleteContractsResponse), "Response should parse to AthleteContractsResponse"
    
    # Verify response structure
    assert result.count > 0, "LeBron should have contracts"
    assert result.page_index == 1
    assert result.page_size == 25
    assert len(result.items) > 0, "Should have contract items"
    
    # Save response for analysis
    with open(f"{ensure_json_output_dir}/athlete_contracts_nba_lebron.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)


@pytest.mark.api
def test_get_athlete_contract_by_year_nba(sports_core_api_client, ensure_json_output_dir):
    """Test getting specific year contract for LeBron James."""
    response = get_athlete_contract_by_year.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.BASKETBALL,
        league=LeagueEnum.NBA,
        athlete_id="1966",  # LeBron James
        year="2024"
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, AthleteContract), "Response should parse to AthleteContract"
    
    # Verify contract details
    assert result.ref is not None
    assert result.salary > 0, "Should have a salary"
    assert result.active == True, "2024 contract should be active"
    assert result.season is not None
    assert result.team is not None
    
    # Save response for analysis
    with open(f"{ensure_json_output_dir}/athlete_contract_nba_lebron_2024.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)


@pytest.mark.api
def test_get_athlete_contracts_nfl(sports_core_api_client, ensure_json_output_dir):
    """Test getting athlete contracts for Patrick Mahomes (NFL)."""
    response = get_athlete_contracts.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.FOOTBALL,
        league=LeagueEnum.NFL,
        athlete_id="3139477"  # Patrick Mahomes
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, AthleteContractsResponse), "Response should parse to AthleteContractsResponse"
    
    # NFL might have empty contracts
    assert result.count >= 0
    assert result.page_index == 0 or result.page_index == 1
    
    # Save response for analysis
    with open(f"{ensure_json_output_dir}/athlete_contracts_nfl_mahomes.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)


@pytest.mark.api
@pytest.mark.parametrize("sport,league,athlete_id,athlete_name", [
    (SportEnum.BASKETBALL, LeagueEnum.NBA, "5104157", "Wembanyama"),
    (SportEnum.BASEBALL, LeagueEnum.MLB, "592450", "Mookie Betts"),
])
def test_get_athlete_contracts_cross_sport(sports_core_api_client, ensure_json_output_dir, sport, league, athlete_id, athlete_name):
    """Test getting athlete contracts across different sports."""
    response = get_athlete_contracts.sync_detailed(
        client=sports_core_api_client,
        sport=sport,
        league=league,
        athlete_id=athlete_id
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code} for {athlete_name}"
    
    result = response.parsed
    assert isinstance(result, AthleteContractsResponse), f"Response should parse to AthleteContractsResponse for {athlete_name}"
    
    # Save response for analysis
    with open(f"{ensure_json_output_dir}/athlete_contracts_{league.value}_{athlete_name.lower()}.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)


@pytest.mark.api
def test_get_athlete_contracts_invalid_athlete(sports_core_api_client):
    """Test getting contracts for invalid athlete ID."""
    response = get_athlete_contracts.sync_detailed(
        client=sports_core_api_client,
        sport=SportEnum.BASKETBALL,
        league=LeagueEnum.NBA,
        athlete_id="99999999"  # Invalid ID
    )
    
    # ESPN might return 200 with empty results or 404
    assert response.status_code in [200, 404], f"Expected status code 200 or 404, got {response.status_code}"
    
    if response.status_code == 200:
        result = response.parsed
        assert result.count == 0, "Invalid athlete should have no contracts"