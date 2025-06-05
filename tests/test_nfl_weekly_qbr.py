"""Test NFL Weekly QBR endpoint."""
import pytest
import json
from models.sports_core_api.espn_sports_core_api_client.api.default import get_nfl_weekly_qbr
from models.sports_core_api.espn_sports_core_api_client.types import UNSET


@pytest.mark.api
def test_get_nfl_weekly_qbr(sports_core_api_client, ensure_json_output_dir):
    """Test getting NFL weekly QBR data."""
    # Test with 2024 season, week 1
    response = get_nfl_weekly_qbr.sync_detailed(
        client=sports_core_api_client,
        year=2024,
        seasontype=2,  # Regular season
        week=1,
        page=UNSET,
        limit=UNSET
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, "Response should parse successfully"
    
    # Check pagination structure
    assert hasattr(result, 'count')
    assert hasattr(result, 'page_index')
    assert hasattr(result, 'page_size')
    assert hasattr(result, 'page_count')
    assert hasattr(result, 'items')
    
    # Should have QBR data for quarterbacks
    assert len(result.items) > 0, "Should have at least one quarterback"
    
    # Check first item structure
    first_item = result.items[0]
    assert hasattr(first_item, 'athlete')
    assert hasattr(first_item, 'splits')
    
    # Save response for analysis first (so we can inspect on failure)
    with open(f"{ensure_json_output_dir}/nfl_weekly_qbr_test.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    # Check splits structure
    if first_item.splits:
        assert hasattr(first_item.splits, 'categories')
        if first_item.splits.categories:
            first_category = first_item.splits.categories[0]
            assert hasattr(first_category, 'stats')
            
            # Print available stats for debugging
            if first_category.stats:
                stat_names = [stat.name for stat in first_category.stats if hasattr(stat, 'name')]
                print(f"Available stats: {stat_names}")
                
                # Look for QBR stat
                qbr_stats = [stat for stat in first_category.stats 
                           if hasattr(stat, 'name') and 'qbr' in stat.name.lower()]
                assert len(qbr_stats) > 0, f"Should have QBR rating stat. Available stats: {stat_names}"
    
    print(f"Retrieved QBR data for {result.count} quarterbacks")
    print(f"Page {result.page_index} of {result.page_count}")


@pytest.mark.api
def test_get_nfl_weekly_qbr_pagination(sports_core_api_client):
    """Test pagination for NFL weekly QBR."""
    # Get first page with a small limit
    response = get_nfl_weekly_qbr.sync_detailed(
        client=sports_core_api_client,
        year=2024,
        seasontype=2,
        week=1,
        page=1,
        limit=5
    )
    
    assert response.status_code == 200
    result = response.parsed
    
    # Should respect the limit
    assert len(result.items) <= 5
    assert result.page_size == 5
    
    # If there are more pages, test second page
    if result.page_count > 1:
        response2 = get_nfl_weekly_qbr.sync_detailed(
            client=sports_core_api_client,
            year=2024,
            seasontype=2,
            week=1,
            page=2,
            limit=5
        )
        
        assert response2.status_code == 200
        result2 = response2.parsed
        assert result2.page_index == 2


@pytest.mark.api
def test_get_nfl_weekly_qbr_invalid_week(sports_core_api_client):
    """Test NFL weekly QBR with invalid week."""
    # Test with future week that doesn't exist yet
    response = get_nfl_weekly_qbr.sync_detailed(
        client=sports_core_api_client,
        year=2025,
        seasontype=2,
        week=10,
        page=UNSET,
        limit=UNSET
    )
    
    # Should return 200 with empty items or 404
    assert response.status_code in [200, 404]
    
    if response.status_code == 200:
        result = response.parsed
        assert result.count == 0 or len(result.items) == 0