#!/usr/bin/env python3
"""
Test ESPN NFL API - News Endpoint
Requires Python 3.10+
"""

import json
import pytest
import requests

from models.site_api.espn_nfl_api_client import Client
from models.site_api.espn_nfl_api_client.api.default import get_league_news
from models.site_api.espn_nfl_api_client.models.error_response import ErrorResponse
from models.site_api.espn_nfl_api_client.types import UNSET
from models.site_api.espn_nfl_api_client.models.sport_news_api_schema import (
    SportNewsAPISchema,
)


def validate_schema_response(data):
    """Validate if response matches expected schema structure."""
    required_attrs = ["header", "articles"]
    for attr in required_attrs:
        if getattr(data, attr, UNSET) is UNSET:
            print(f"Missing required attribute: {attr}")
            return False

    # Check articles
    articles = data.articles
    if not articles:
        print("No articles found or articles list is empty")
        return False

    # Check first article
    article = articles[0]
    if (
        getattr(article, "id", UNSET) is UNSET
        or getattr(article, "headline", UNSET) is UNSET
        or getattr(article, "description", UNSET) is UNSET
    ):
        print("Invalid article structure: missing required keys")
        return False

    return True


def format_news_response(data):
    """Format news data for display."""
    if not data.header or not data.articles:
        return "Invalid data format: missing header or articles"

    output = []
    output.append(f"=== {data.header} ===")
    output.append(f"Total Articles: {len(data.articles)}")

    output.append("\n--- Recent Articles ---")
    for idx, article in enumerate(data.articles[:5], 1):  # Show top 5 articles
        output.append(f"{idx}. {article.headline}")
        output.append(f"   Type: {article.type}")
        output.append(f"   Published: {article.published}")
        output.append(f"   By: {article.byline}")
        output.append(f"   Description: {article.description}")

        if hasattr(article, "links") and article.links is not UNSET:
            if hasattr(article.links, "web") and article.links.web is not UNSET:
                output.append(f"   Link: {article.links.web.href}")

        output.append("")

    return "\n".join(output)


def fetch_direct_news():
    """Fetch the news data directly using requests to bypass model issues."""
    url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/news"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


@pytest.mark.api
def test_fetch_direct_news(ensure_json_output_dir):
    """Test fetching news data directly using requests."""
    news_json = fetch_direct_news()

    assert news_json is not None, "Failed to fetch news data directly"
    assert "header" in news_json and "articles" in news_json, (
        "Response does not match expected structure"
    )
    articles = news_json.get("articles", [])
    assert len(articles) > 0, "No articles found in direct response"

    # Save the raw JSON for analysis
    with open(f"{ensure_json_output_dir}/nfl_news_response.json", "w") as f:
        json.dump(news_json, f, indent=2)
    print(
        f"\nFull news response saved to {ensure_json_output_dir}/nfl_news_response.json"
    )


@pytest.mark.api
def test_fetch_news_with_client(site_api_client, ensure_json_output_dir):
    """Test fetching news data using the generated client."""
    try:
        # The URL path in the API client is '/sports/football/nfl/news',
        # so we need to ensure the base URL is correct and includes '/apis/site/v2'
        # The site_api_client fixture sets its base_url to "https://site.api.espn.com"
        # Let's recreate the client with the correct full base URL
        client = Client(base_url="https://site.api.espn.com/apis/site/v2")
        news_data = get_league_news.sync(client=client, sport="football", league="nfl")

        assert news_data is not None, "API returned None response"
        assert not isinstance(news_data, ErrorResponse), (
            f"API returned an error response: {news_data.error.message if hasattr(news_data, 'error') and news_data.error and hasattr(news_data.error, 'message') else str(news_data)}"
        )
        assert isinstance(news_data, SportNewsAPISchema), (
            "Failed to fetch news data using client or unexpected response type"
        )

        # Validate schema
        assert validate_schema_response(news_data), (
            "Response does not match expected schema structure"
        )

        # Display formatted summary
        print("\n" + format_news_response(news_data))

        # Save full response for analysis
        with open(
            f"{ensure_json_output_dir}/nfl_news_response_processed.json", "w"
        ) as f:
            json.dump(news_data.to_dict(), f, indent=2)
        print(
            f"\nFull processed response saved to {ensure_json_output_dir}/nfl_news_response_processed.json"
        )

    except Exception as e:
        pytest.fail(f"Exception during news API test: {str(e)}")
