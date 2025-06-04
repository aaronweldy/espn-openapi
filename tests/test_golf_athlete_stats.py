import pytest
import json
from models.site_web_api.espn_site_web_api_client.api.default import get_athlete_stats, get_golf_athlete_stats
from models.site_web_api.espn_site_web_api_client.models import SportEnum, LeagueEnum


@pytest.mark.api
def test_golf_athlete_stats(site_web_api_client, ensure_json_output_dir):
    """Test the golf-specific athlete stats endpoint."""
    
    # Tiger Woods ID: 388
    response = get_golf_athlete_stats.sync_detailed(
        client=site_web_api_client,
        athlete_id=388,
        season=2024
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, "Response should parse successfully"
    
    # Check the response has required fields
    assert hasattr(result, 'filters'), "Response should have filters"
    
    # Check optional fields
    if hasattr(result, 'statistics') and result.statistics:
        stats = result.statistics
        assert stats.display_name, "Statistics should have display name"
        assert stats.labels, "Statistics should have labels"
        assert stats.names, "Statistics should have names"
        assert stats.display_names, "Statistics should have display names"
        assert stats.splits, "Statistics should have splits"
        
        # Check splits
        if stats.splits:
            first_split = stats.splits[0]
            assert first_split.display_name, "Split should have display name"
            assert first_split.stats, "Split should have stats"
        
        # Save sample data
        sample_data = {
            'athlete_id': 388,
            'display_name': stats.display_name,
            'filters': len(result.filters) if result.filters else 0,
            'labels_count': len(stats.labels) if stats.labels else 0,
            'splits_count': len(stats.splits) if stats.splits else 0,
            'has_statistics': True
        }
        
        print(f"\n✓ Golf athlete stats endpoint successfully implemented")
        print(f"Display Name: {stats.display_name}")
        print(f"Number of splits: {len(stats.splits) if stats.splits else 0}")
    else:
        # No statistics available
        sample_data = {
            'athlete_id': 388,
            'filters': len(result.filters) if result.filters else 0,
            'has_statistics': False
        }
        
        print(f"\n✓ Golf athlete stats endpoint works but no statistics available")
    
    with open(f"{ensure_json_output_dir}/golf_athlete_stats_test.json", "w") as f:
        json.dump(sample_data, f, indent=2)


@pytest.mark.api
@pytest.mark.xfail(reason="Generic endpoint doesn't work for golf - it includes league in URL")
def test_golf_athlete_stats_generic_endpoint(site_web_api_client, ensure_json_output_dir):
    """Test that the generic endpoint doesn't work for golf."""
    
    # Tiger Woods ID: 388
    response = get_athlete_stats.sync_detailed(
        client=site_web_api_client,
        sport=SportEnum.GOLF,
        league=LeagueEnum.PGA,
        athlete_id=388,
        season=2024
    )
    
    # This will fail with 404 because golf doesn't use league in the URL
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"


@pytest.mark.api
@pytest.mark.parametrize("athlete_id,athlete_name", [
    (388, "Tiger Woods"),
    (780, "Scottie Scheffler"),
    (4686086, "Rory McIlroy"),
])
def test_multiple_golf_athletes(site_web_api_client, athlete_id, athlete_name):
    """Test golf stats for multiple athletes."""
    
    response = get_golf_athlete_stats.sync_detailed(
        client=site_web_api_client,
        athlete_id=athlete_id,
        season=2024
    )
    
    assert response.status_code == 200, f"Failed to get stats for {athlete_name} (ID: {athlete_id})"
    
    result = response.parsed
    assert result is not None, f"Response should parse successfully for {athlete_name}"
    
    # Check basic structure
    assert result.filters, f"Should have filters for {athlete_name}"
    
    print(f"\n✓ Successfully retrieved response for {athlete_name}")
    if hasattr(result, 'statistics') and result.statistics:
        print(f"  - Has statistics: Yes")
        if result.statistics.splits:
            print(f"  - Number of splits: {len(result.statistics.splits)}")
    else:
        print(f"  - Has statistics: No (only filters available)")