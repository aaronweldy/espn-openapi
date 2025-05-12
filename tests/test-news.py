#!/usr/bin/env python3
"""
Test ESPN NFL API - News Endpoint
Requires Python 3.10+
"""

import json
import requests

from models.espn_nfl_api_client import Client
from models.espn_nfl_api_client.api.default.get_nfl_news import sync
from models.espn_nfl_api_client.models.error_response import ErrorResponse
from models.espn_nfl_api_client.models.news_response import NewsResponse
from models.espn_nfl_api_client.types import UNSET


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


def main():
    """Main function to test the ESPN NFL News API."""
    print("ESPN NFL News API Test Script")
    print("=" * 50)

    client = Client(base_url="https://site.api.espn.com/apis/site/v2")

    print("\nFetching NFL news data")
    print("-" * 50)
    
    # First try the direct approach
    news_json = fetch_direct_news()
    
    if not news_json:
        print("✗ Failed to fetch news data directly")
        return
        
    # Save the raw JSON for analysis
    with open("json_output/nfl_news_response.json", "w") as f:
        json.dump(news_json, f, indent=2)
    
    print("✓ Successfully fetched news data")
        
    # Basic validation and display from the direct JSON
    if "header" not in news_json or "articles" not in news_json:
        print("✗ Response does not match expected structure")
        return
    
    articles = news_json.get("articles", [])
    print(f"\n=== {news_json.get('header', 'NFL News')} ===")
    print(f"Total Articles: {len(articles)}")
    
    print("\n--- Recent Articles ---")
    for idx, article in enumerate(articles[:5], 1):  # Show top 5 articles
        print(f"{idx}. {article.get('headline', 'No headline')}")
        print(f"   Type: {article.get('type', 'Unknown')}")
        print(f"   Published: {article.get('published', 'Unknown')}")
        print(f"   By: {article.get('byline', 'Unknown')}")
        print("")
    
    print("\n✓ Full news response saved to json_output/nfl_news_response.json")
    
    # Now try using the generated client
    try:
        print("\nUsing the generated client to fetch news:")
        news_data: NewsResponse | ErrorResponse | None = sync(client=client)

        if isinstance(news_data, ErrorResponse):
            print("✗ API returned an error response:")
            print(
                news_data.error.message
                if hasattr(news_data, "error") 
                and news_data.error
                and hasattr(news_data.error, "message")
                else str(news_data)
            )
        elif isinstance(news_data, NewsResponse):
            # Validate schema
            if validate_schema_response(news_data):
                print("✓ Response matches expected schema structure")
            else:
                print("✗ Response does not match expected schema structure")

            # Display formatted summary
            print("\n" + format_news_response(news_data))

            # Save full response for analysis
            with open("json_output/nfl_news_response_processed.json", "w") as f:
                json.dump(news_data.to_dict(), f, indent=2)
            print("\n✓ Full processed response saved to json_output/nfl_news_response_processed.json")
        else:
            print("✗ Failed to fetch news data using client")
    except Exception as e:
        print(f"✗ Error using generated client: {str(e)}")


if __name__ == "__main__":
    main()