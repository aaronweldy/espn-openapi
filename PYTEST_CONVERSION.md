# Guide to Converting Existing Tests to pytest Format

Based on the analysis of the existing test files, here's a comprehensive guide on how to convert them to pytest format.

## Common Changes Needed for All Test Files

1. **Add pytest Import**
   ```python
   import pytest
   ```

2. **Add Markers to Test Functions**
   ```python
   @pytest.mark.api
   def test_your_function_name():
       # Test code
   ```

3. **Replace Client Creation with Fixtures**
   - Replace custom client creation with the fixtures from conftest.py:
     ```python
     # Old way:
     client = EspnSiteWebApiClient(base_url="https://site.web.api.espn.com")
     
     # New way:
     def test_function(site_web_api_client):
         # Use site_web_api_client instead of client
     ```

4. **Replace Boolean Returns with Assertions**
   - Instead of returning True/False, use pytest assertions:
     ```python
     # Old way:
     if not condition:
         return False
     return True
     
     # New way:
     assert condition, "Error message explaining the condition"
     ```

5. **Replace Conditional Checks with Assertions**
   - Convert conditional checks to assertions:
     ```python
     # Old way:
     if not isinstance(result, ExpectedType):
         return False
     
     # New way:
     assert isinstance(result, ExpectedType), "Result should be of type ExpectedType"
     ```

6. **Convert Main Function and Name-Main Check**
   - Remove or repurpose the main function
   - Remove the `if __name__ == "__main__":` block
   - Move the functionality to test functions

7. **Use JSON Output Directory Fixture**
   - Replace direct creation of output directories with the fixture:
     ```python
     # Old way:
     os.makedirs("json_output", exist_ok=True)
     with open("json_output/output.json", "w") as f:
         json.dump(data, f, indent=2)
     
     # New way:
     def test_function(ensure_json_output_dir):
         with open(f"{ensure_json_output_dir}/output.json", "w") as f:
             json.dump(data, f, indent=2)
     ```

## Example Conversion for a Test Function

### Before

```python
def test_get_athlete_overview(athlete_id: int = TEST_ATHLETE_ID_NFL):
    """Tests fetching and parsing the athlete overview."""
    client = EspnSiteWebApiClient(base_url="https://site.web.api.espn.com")

    try:
        api_func = get_athlete_overview_nfl
        response = api_func.sync_detailed(
            athlete_id=athlete_id,
            client=client,
        )

        if response.status_code == 200:
            result = response.parsed
            if not isinstance(result, AthleteOverviewResponse):
                return False

            print("\n" + format_athlete_overview(result))
            os.makedirs("json_output", exist_ok=True)
            with open(f"json_output/athlete_{athlete_id}_overview_processed.json", "w") as f:
                json.dump(result.to_dict(), f, indent=2)
            return True
        else:
            return False
    except Exception as e:
        print(f"✗ Error during test: {e}")
        return False
```

### After

```python
@pytest.mark.api
def test_get_athlete_overview(site_web_api_client, ensure_json_output_dir, athlete_id: int = TEST_ATHLETE_ID_NFL):
    """Tests fetching and parsing the athlete overview."""
    try:
        api_func = get_athlete_overview_nfl
        response = api_func.sync_detailed(
            athlete_id=athlete_id,
            client=site_web_api_client,
        )

        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        result = response.parsed
        assert isinstance(result, AthleteOverviewResponse), "Response should parse to AthleteOverviewResponse"

        print("\n" + format_athlete_overview(result))
        with open(f"{ensure_json_output_dir}/athlete_{athlete_id}_overview_processed.json", "w") as f:
            json.dump(result.to_dict(), f, indent=2)
    except Exception as e:
        print(f"✗ Error during test: {e}")
        pytest.fail(f"Exception during test: {str(e)}")
```

## Converting Main Function Tests

For files with a `main()` function, you'll need to convert the core functionality into test functions:

### Before

```python
def main():
    client = Client(base_url="https://site.api.espn.com/apis/site/v2")
    
    # Get team details
    team_data = sync(client=client, team_id=team_id)
    
    if isinstance(team_data, ErrorResponse):
        print("Error")
    elif isinstance(team_data, TeamDetailsResponse):
        if validate_schema_response(team_data):
            print("Valid schema")
        print(format_team_details(team_data))
        with open("nfl_team_details_response_processed.json", "w") as f:
            json.dump(team_data.to_dict(), f, indent=2)
    else:
        print("Failed")

if __name__ == "__main__":
    main()
```

### After

```python
@pytest.mark.api
def test_get_team_details(site_api_client, ensure_json_output_dir):
    team_id = "12"  # Kansas City Chiefs
    
    # Get team details
    team_data = sync(client=site_api_client, team_id=team_id)
    
    assert not isinstance(team_data, ErrorResponse), f"API returned an error: {team_data.error.message if team_data.error else 'Unknown error'}"
    assert isinstance(team_data, TeamDetailsResponse), "Response should be a TeamDetailsResponse"
    assert validate_schema_response(team_data), "Response should match the expected schema structure"
    
    print(format_team_details(team_data))
    with open(f"{ensure_json_output_dir}/nfl_team_details_response_processed.json", "w") as f:
        json.dump(team_data.to_dict(), f, indent=2)
```

## Next Steps

1. Start by converting one test file at a time
2. Run pytest after each conversion to ensure it works:
   ```bash
   pytest -v tests/test_your_file.py
   ```
3. Use the script `convert_tests_to_pytest.py` to identify specific needed changes
4. Update the conftest.py file if needed with additional fixtures
5. Consider updating file names from `test-name.py` to `test_name.py` for consistency

Remember that pytest automatically discovers tests in files matching the pattern `test_*.py` or `*_test.py` and functions named `test_*`. 