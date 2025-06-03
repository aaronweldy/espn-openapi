"""
Shared test fixtures and configuration for pytest.
"""

import os
import pytest

from models.site_web_api.espn_site_web_api_client import Client as SiteWebApiClient
from models.cdn_api.espn_cdn_nfl_api_client import Client as CdnApiClient
from models.site_api.espn_nfl_api_client import Client as SiteApiClient
from models.sports_core_api.espn_sports_core_api_client import (
    Client as SportsCoreApiClient,
)
from models.fantasy_api.espn_fantasy_api_client import Client as FantasyApiClient
from models.partners_api.espn_partners_api_client import Client as PartnersApiClient


@pytest.fixture(scope="session")
def site_web_api_client():
    """Fixture for ESPN site web API client."""
    return SiteWebApiClient(base_url="https://site.web.api.espn.com")


@pytest.fixture(scope="session")
def cdn_api_client():
    """Fixture for ESPN CDN API client."""
    return CdnApiClient(base_url="https://cdn.espn.com")


@pytest.fixture(scope="session")
def site_api_client():
    """Fixture for ESPN site API client."""
    return SiteApiClient(base_url="https://site.api.espn.com/apis/site/v2")


@pytest.fixture(scope="session")
def sports_core_api_client():
    """Fixture for ESPN sports core API client."""
    return SportsCoreApiClient(base_url="https://sports.core.api.espn.com")


@pytest.fixture(scope="session")
def fantasy_api_client():
    """Fixture for ESPN fantasy API client."""
    return FantasyApiClient(base_url="https://lm-api-reads.fantasy.espn.com")


@pytest.fixture(scope="session")
def partners_api_client():
    """Fixture for ESPN partners API client."""
    return PartnersApiClient(base_url="https://partners.api.espn.com")


@pytest.fixture(scope="session")
def site_api_fantasy_client():
    """Fixture for ESPN site API client with fantasy base URL.
    
    This is used for fantasy endpoints that are under site.api.espn.com/apis/fantasy/
    instead of the regular site.api.espn.com/apis/site/v2/
    """
    return SiteApiClient(base_url="https://site.api.espn.com/apis")


@pytest.fixture(scope="session")
def site_api_v2_client():
    """Fixture for ESPN site API client with v2 base URL.
    
    This is used for endpoints that are under site.api.espn.com/apis/v2/
    instead of the regular site.api.espn.com/apis/site/v2/
    This includes soccer standings and potentially other standings endpoints.
    """
    return SiteApiClient(base_url="https://site.api.espn.com/apis/v2")


@pytest.fixture(scope="session")
def ensure_json_output_dir():
    """Ensure the json_output directory exists."""
    os.makedirs("json_output", exist_ok=True)
    return "json_output"


@pytest.fixture(autouse=True)
def setup_test(request):
    """Setup for each test - prints test name for easier log reading."""
    print(f"\n----- Running test: {request.node.name} -----")
    yield
    # Any teardown actions would go here
