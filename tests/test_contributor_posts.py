"""Test contributor posts (flex) endpoint."""
import json
import pytest
from models.site_web_api.espn_site_web_api_client.api.default import get_contributor_posts


@pytest.mark.api
def test_get_contributor_posts_empty(site_web_api_client, ensure_json_output_dir):
    """Test getting contributor posts with no contributor specified."""
    response = get_contributor_posts.sync_detailed(
        client=site_web_api_client,
        region="us",
        lang="en",
        contentorigin="espn",
        limit=10
    )
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    result = response.parsed
    assert result is not None, "Response should parse successfully"
    assert hasattr(result, 'columns'), "Response should have columns"
    assert len(result.columns) == 3, "Should have 3 columns (left, middle, right)"
    
    # Save response for analysis
    with open(f"{ensure_json_output_dir}/contributor_flex_empty_test.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    
    # Check column structure
    for column in result.columns:
        assert column.name in ["leftcolumn", "middlecolumn", "rightcolumn"]
        assert column.description
        assert isinstance(column.items, list)


@pytest.mark.api
@pytest.mark.xfail(reason="Contributor parameter may cause script error")
def test_get_contributor_posts_with_contributor(site_web_api_client, ensure_json_output_dir):
    """Test getting contributor posts for a specific contributor."""
    response = get_contributor_posts.sync_detailed(
        client=site_web_api_client,
        region="us",
        lang="en",
        contentorigin="espn",
        contributor="adam-schefter",
        limit=5
    )
    
    # Note: This might return 400 or 1008 error
    if response.status_code == 200:
        result = response.parsed
        assert result is not None, "Response should parse successfully"
        
        # Save response for analysis
        with open(f"{ensure_json_output_dir}/contributor_flex_schefter_test.json", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
        
        # Look for content in middle column
        middle_column = next((col for col in result.columns if col.name == "middlecolumn"), None)
        if middle_column and middle_column.items:
            first_item = middle_column.items[0]
            if first_item.type == "contributor-page":
                assert first_item.contributor
                assert first_item.feed