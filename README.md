# ESPN API Client

A Python client for the ESPN API, focusing on NFL data.

## Overview

This project provides a Python client for accessing ESPN's public APIs, with a focus on NFL data. It includes:

- Generated OpenAPI client based on the ESPN API schema
- Type definitions for API responses
- Utility functions for fetching and processing data

## Usage

```python
from models.espn_nfl_api_client import Client
from models.espn_nfl_api_client.api.default.get_nfl_teams_list import sync as get_teams

client = Client(base_url="https://site.api.espn.com/apis/site/v2")
teams = get_teams(client=client)
```

## Development

This project uses openapi-python-client to generate Python clients from the OpenAPI specification.

```bash
# Generate client from OpenAPI spec
openapi-python-client generate --path spec.yaml --output-path models/ --overwrite
```