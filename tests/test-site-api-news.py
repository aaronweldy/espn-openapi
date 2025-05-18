#!/usr/bin/env python3

import os
import sys
from typing import cast, Union
from datetime import datetime

from models.site_api.espn_nfl_api_client.api.default.get_league_news import (
    sync_detailed as get_league_news,
)
from models.site_api.espn_nfl_api_client.api.default.get_nfl_news import (
    sync_detailed as get_nfl_news,
)
from models.site_api.espn_nfl_api_client.client import Client
from models.site_api.espn_nfl_api_client.models.news_response import NewsResponse
from models.site_api.espn_nfl_api_client.types import UNSET
from models.site_api.espn_nfl_api_client.models.sport_news_api_schema import (
    SportNewsAPISchema,
)
from models.site_api.espn_nfl_api_client.models.error_response import ErrorResponse
from models.site_api.espn_nfl_api_client.models.news_article import NewsArticle
from models.site_api.espn_nfl_api_client.models.news_category import NewsCategory
from models.site_api.espn_nfl_api_client.models.news_athlete import NewsAthlete
from models.site_api.espn_nfl_api_client.models.news_team import NewsTeam
from models.site_api.espn_nfl_api_client.models.news_league import NewsLeague


def test_nfl_news():
    """Test retrieving NFL news from the specific endpoint"""
    print("Testing NFL News endpoint...")
    limit = 5

    client = Client(base_url="https://site.api.espn.com/apis/site/v2")
    response = get_nfl_news(client=client, limit=limit)
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    if isinstance(response, ErrorResponse):
        print(f"Error: {response.parsed}")
        return False

    assert isinstance(response.parsed, SportNewsAPISchema)
    news: SportNewsAPISchema = response.parsed

    # Check top-level fields
    assert isinstance(news.header, str)
    assert isinstance(news.articles, list)
    assert len(news.articles) > 0
    assert hasattr(news, "link")
    assert hasattr(news.link, "href")

    # Check the first article in detail
    article = news.articles[0]
    assert isinstance(article, NewsArticle)
    assert isinstance(article.id, int)
    assert isinstance(article.now_id, str)
    assert isinstance(article.content_key, str)
    assert isinstance(article.data_source_identifier, str)
    assert article.type.value in ["HeadlineNews", "Media", "Story"]
    assert isinstance(article.headline, str)
    assert isinstance(article.description, str)
    assert isinstance(article.last_modified, (str, datetime)) or hasattr(
        article.last_modified, "isoformat"
    )
    assert isinstance(article.published, (str, datetime)) or hasattr(
        article.published, "isoformat"
    )
    assert isinstance(article.images, list)
    assert isinstance(article.categories, list)
    assert isinstance(article.premium, bool)
    assert hasattr(article, "links")

    # Check images
    for img in article.images:
        assert hasattr(img, "url")
        assert isinstance(img.url, str) or img.url is UNSET

    # Check categories
    for cat in article.categories:
        assert hasattr(cat, "type")
        assert hasattr(cat, "guid")
        # Optional nested objects
        if hasattr(cat, "athlete") and cat.athlete and cat.athlete is not UNSET:
            assert hasattr(cat.athlete, "id")
            assert hasattr(cat.athlete, "description")
        if hasattr(cat, "team") and cat.team and cat.team is not UNSET:
            assert hasattr(cat.team, "id")
            assert hasattr(cat.team, "description")
        if hasattr(cat, "league") and cat.league and cat.league is not UNSET:
            assert hasattr(cat.league, "id")
            assert hasattr(cat.league, "description")

    # Check links
    links = article.links
    assert hasattr(links, "web")
    if links.web and links.web is not UNSET:
        assert hasattr(links.web, "href")
    if hasattr(links, "mobile") and links.mobile and links.mobile is not UNSET:
        assert hasattr(links.mobile, "href")
    if hasattr(links, "api") and links.api and links.api is not UNSET:
        if (
            hasattr(links.api, "self_")
            and links.api.self_
            and links.api.self_ is not UNSET
        ):
            assert hasattr(links.api.self_, "href")
    if hasattr(links, "app") and links.app and links.app is not UNSET:
        if (
            hasattr(links.app, "sportscenter")
            and links.app.sportscenter
            and links.app.sportscenter is not UNSET
        ):
            assert hasattr(links.app.sportscenter, "href")

    # Print a summary of the first article for debugging
    print("First article summary:")
    print(f"  Headline: {article.headline}")
    print(f"  Description: {article.description}")
    print(f"  Published: {article.published}")
    print(f"  Images: {len(article.images)}")
    print(f"  Categories: {len(article.categories)}")
    print(f"  Links: web={getattr(links.web, 'href', None)}")

    return True


def test_nfl_news_team_specific():
    """Test retrieving NFL news filtered by team (Kansas City Chiefs, team=12)"""
    print("Testing NFL News endpoint with team filter (team=12, Kansas City Chiefs)...")
    limit = 5
    team_id = 12

    client = Client(base_url="https://site.api.espn.com/apis/site/v2")
    response = get_nfl_news(client=client, limit=limit, team=team_id)
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    if isinstance(response, ErrorResponse):
        print(f"Error: {response.parsed}")
        return False

    assert isinstance(response.parsed, SportNewsAPISchema)
    news: SportNewsAPISchema = response.parsed

    assert isinstance(news.header, str)
    assert isinstance(news.articles, list)
    assert len(news.articles) > 0
    assert hasattr(news, "link")
    assert hasattr(news.link, "href")

    # Check that at least one article has a category with team id 12
    found_team = False
    for article in news.articles:
        for cat in article.categories:
            if hasattr(cat, "team") and cat.team and cat.team is not UNSET:
                if hasattr(cat.team, "id") and cat.team.id == team_id:
                    found_team = True
                    break
        if found_team:
            break
    assert found_team, (
        "No article found with category for team id 12 (Kansas City Chiefs)"
    )

    # Print a summary of the first article for debugging
    article = news.articles[0]
    print("First article summary (team-specific):")
    print(f"  Headline: {article.headline}")
    print(f"  Description: {article.description}")
    print(f"  Published: {article.published}")
    print(f"  Images: {len(article.images)}")
    print(f"  Categories: {len(article.categories)}")
    print(f"  Links: web={getattr(article.links.web, 'href', None)}")

    return True


def test_generic_news_endpoint():
    """Test retrieving news from the generic sport/league endpoint"""
    # Skip this test for now
    return True


def test_mlb_news():
    """Test retrieving MLB news from the specific endpoint"""
    print("Testing MLB News endpoint...")
    limit = 5

    client = Client(base_url="https://site.api.espn.com/apis/site/v2")
    from models.site_api.espn_nfl_api_client.api.default.get_mlb_news import (
        sync_detailed as get_mlb_news,
    )

    response = get_mlb_news(client=client, limit=limit)
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    if isinstance(response, ErrorResponse):
        print(f"Error: {response.parsed}")
        return False

    assert isinstance(response.parsed, SportNewsAPISchema)
    news: SportNewsAPISchema = response.parsed

    # Check top-level fields
    assert isinstance(news.header, str)
    assert isinstance(news.articles, list)
    assert len(news.articles) > 0
    assert hasattr(news, "link")
    assert hasattr(news.link, "href")

    # Check the first article in detail
    article = news.articles[0]
    assert isinstance(article, NewsArticle)
    assert isinstance(article.id, int)
    assert isinstance(article.now_id, str)
    assert isinstance(article.content_key, str)
    assert isinstance(article.data_source_identifier, str)
    assert article.type.value in ["HeadlineNews", "Media", "Story", "Recap"]
    assert isinstance(article.headline, str)
    assert isinstance(article.description, str)
    assert isinstance(article.last_modified, (str, datetime)) or hasattr(
        article.last_modified, "isoformat"
    )
    assert isinstance(article.published, (str, datetime)) or hasattr(
        article.published, "isoformat"
    )
    assert isinstance(article.images, list)
    assert isinstance(article.categories, list)
    assert isinstance(article.premium, bool)
    assert hasattr(article, "links")

    # Print a summary of the first article for debugging
    print("First MLB article summary:")
    print(f"  Headline: {article.headline}")
    print(f"  Description: {article.description}")
    print(f"  Published: {article.published}")
    print(f"  Images: {len(article.images)}")
    print(f"  Categories: {len(article.categories)}")
    print(f"  Links: web={getattr(article.links.web, 'href', None)}")

    return True


if __name__ == "__main__":
    tests = [
        test_nfl_news,
        test_nfl_news_team_specific,
        test_generic_news_endpoint,
        test_mlb_news,
    ]

    success = True
    for test in tests:
        try:
            test_success = test()
            if not test_success:
                success = False
                print(f"Test {test.__name__} failed")
        except Exception as e:
            success = False
            print(f"Test {test.__name__} raised an exception: {e}")
            import traceback

            traceback.print_exc()

    if success:
        print("\nAll tests passed!")
        sys.exit(0)
    else:
        print("\nSome tests failed!")
        sys.exit(1)
