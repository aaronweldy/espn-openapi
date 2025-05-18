# ESPN API Testing Guide

This guide provides instructions for testing the ESPN API using pytest.

## Setup

1. Make sure you have pytest installed:
```bash
pip install pytest
```

2. Make sure your environment is activated and all dependencies are installed:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running Tests

### Basic Test Commands

Run all tests:
```bash
pytest
```

Run tests with verbose output:
```bash
pytest -v
```

Run a specific test file:
```bash
pytest tests/test_site_web_api.py
```

Run a specific test within a file:
```bash
pytest tests/test_site_web_api.py::test_get_athlete_overview
```

Run tests by markers:
```bash
pytest -m api  # Run all tests marked with @pytest.mark.api
```

### Available Markers

- `api`: Tests that make actual API calls
- `slow`: Tests that might take longer to run

## Writing Tests

### Test Structure

1. All test files should be in the `tests/` directory with filenames matching `test_*.py` pattern.
2. Test functions should start with `test_`.
3. Use the fixtures from `conftest.py` for clients and common resources.

### Example Test

```python
import pytest
from models.site_web_api.espn_site_web_api_client.api.default import get_scoreboard_header

@pytest.mark.api
def test_my_endpoint(site_web_api_client, ensure_json_output_dir):
    """Test description."""
    # Call the API
    response = get_scoreboard_header.sync_detailed(
        client=site_web_api_client,
        # ... parameters
    )
    
    # Validate response
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Additional assertions
    result = response.parsed
    assert result.some_field, "Response field validation"
    
    # Save response for analysis
    with open(f"{ensure_json_output_dir}/my_response.json", "w") as f:
        json.dump(result.to_dict(), f, indent=2)
```

### Test Workflow for New Endpoints

1. Find an endpoint that is not yet documented in the OpenAPI spec.
2. Fetch an example JSON response with curl or another HTTP client.
3. Use quicktype to generate a JSON schema object:
   ```bash
   npx quicktype --src json_output/endpoint_response.json --src-lang json --lang schema --out json_schemas/endpoint_schema.json
   ```
4. Convert the JSON schema to OpenAPI format in the relevant spec file.
5. Generate the API client models with:
   ```bash
   make openapi
   ```
6. Write a pytest test case to validate the model parsing:
   ```bash
   touch tests/test_new_endpoint.py
   ```
7. Run the test to verify the schema and generated models:
   ```bash
   pytest -v tests/test_new_endpoint.py
   ```
8. If the test passes, update CHECKLIST.md to mark the endpoint as implemented.

## Debugging Tests

For more detailed test output:
```bash
pytest -vv --showlocals
```

To stop at the first failure:
```bash
pytest -x
```

To enter the debugger on failures:
```bash
pytest --pdb
```

## Logging

Use the `logging` library to log messages.

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
```

For each endpoint, log some interesting information about the response.

## Handling API Rate Limits

To avoid hitting rate limits during testing, you can:

1. Use the `slow` marker for tests that should be run less frequently:
   ```python
   @pytest.mark.slow
   def test_rate_limited_endpoint():
       # Test code
   ```

2. Run tests excluding those with the `slow` marker:
   ```bash
   pytest -m "not slow"
   ```

## Continuous Integration

If running in CI environments, you may want to generate test reports:
```bash
pytest --junitxml=test-results.xml
``` 