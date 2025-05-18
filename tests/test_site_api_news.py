#!/usr/bin/env python3

import pytest
from datetime import datetime

from models.site_api.espn_nfl_api_client.api.default.get_nfl_news import (
    sync_detailed as get_nfl_news,
)
from models.site_api.espn_nfl_api_client.types import UNSET
from models.site_api.espn_nfl_api_client.models.sport_news_api_schema import (
    SportNewsAPISchema,
)
from models.site_api.espn_nfl_api_client.models.error_response import ErrorResponse
from models.site_api.espn_nfl_api_client.models.news_article import NewsArticle


@pytest.mark.api
def test_nfl_news(site_api_client, ensure_json_output_dir):
    """Test retrieving NFL news from the specific endpoint"""
    limit = 5

    response = get_nfl_news(client=site_api_client, limit=limit)
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    assert not isinstance(response.parsed, ErrorResponse), (
        f"API returned an error: {response.parsed}"
    )
    assert isinstance(response.parsed, SportNewsAPISchema), (
        "Response should parse to SportNewsAPISchema"
    )

    news: SportNewsAPISchema = response.parsed

    # Check top-level fields
    assert isinstance(news.header, str), "Header should be a string"
    assert isinstance(news.articles, list), "Articles should be a list"
    assert len(news.articles) > 0, "Articles list should not be empty"
    assert news.link, "Link should be present"
    assert news.link.href, "Link should have href attribute"

    # Check the first article in detail
    article = news.articles[0]
    assert isinstance(article, NewsArticle), "Article should be a NewsArticle instance"
    assert isinstance(article.id, int), "Article ID should be an integer"
    assert isinstance(article.now_id, str), "Article now_id should be a string"
    assert isinstance(article.content_key, str), (
        "Article content_key should be a string"
    )
    assert isinstance(article.data_source_identifier, str), (
        "Article data_source_identifier should be a string"
    )
    assert article.type.value in ["HeadlineNews", "Media", "Story"], (
        "Article type should be valid"
    )
    assert isinstance(article.headline, str), "Article headline should be a string"
    assert isinstance(article.description, str), (
        "Article description should be a string"
    )
    assert isinstance(article.last_modified, (str, datetime)) or hasattr(
        article.last_modified, "isoformat"
    ), "Last modified should be a valid date format"
    assert isinstance(article.published, (str, datetime)) or hasattr(
        article.published, "isoformat"
    ), "Published date should be a valid date format"
    assert isinstance(article.images, list), "Images should be a list"
    assert isinstance(article.categories, list), "Categories should be a list"
    assert isinstance(article.premium, bool), "Premium flag should be a boolean"
    assert article.links, "Links should be present"

    # Check images
    for img in article.images:
        assert hasattr(img, "url"), "Image should have URL attribute"
        assert isinstance(img.url, str) or img.url is UNSET, (
            "Image URL should be a string or UNSET"
        )

    # Check categories
    for cat in article.categories:
        assert hasattr(cat, "type"), "Category should have type attribute"
        assert hasattr(cat, "guid"), "Category should have guid attribute"
        # Optional nested objects
        if cat.athlete and cat.athlete is not UNSET:
            assert hasattr(cat.athlete, "id"), "Athlete should have id attribute"
            assert hasattr(cat.athlete, "description"), (
                "Athlete should have description attribute"
            )
        if cat.team and cat.team is not UNSET:
            assert hasattr(cat.team, "id"), "Team should have id attribute"
            assert hasattr(cat.team, "description"), (
                "Team should have description attribute"
            )
        if cat.league and cat.league is not UNSET:
            assert hasattr(cat.league, "id"), "League should have id attribute"
            assert hasattr(cat.league, "description"), (
                "League should have description attribute"
            )

    # Check links
    links = article.links
    assert hasattr(links, "web"), "Links should have web attribute"
    if links.web and links.web is not UNSET:
        assert hasattr(links.web, "href"), "Web link should have href attribute"
    if links.mobile and links.mobile is not UNSET:
        assert hasattr(links.mobile, "href"), "Mobile link should have href attribute"
    if links.api and links.api is not UNSET:
        if links.api.self_ and links.api.self_ is not UNSET:
            assert hasattr(links.api.self_, "href"), (
                "API self link should have href attribute"
            )
    if links.app and links.app is not UNSET:
        if links.app.sportscenter and links.app.sportscenter is not UNSET:
            assert hasattr(links.app.sportscenter, "href"), (
                "Sportscenter app link should have href attribute"
            )

    # Save response for analysis
    import json

    with open(f"{ensure_json_output_dir}/nfl_news_response.json", "w") as f:
        json.dump(news.to_dict(), f, indent=2)

    # Print a summary of the first article for debugging
    print("First article summary:")
    print(f"  Headline: {article.headline}")
    print(f"  Description: {article.description}")
    print(f"  Published: {article.published}")
    print(f"  Images: {len(article.images)}")
    print(f"  Categories: {len(article.categories)}")
    print(f"  Links: web={getattr(links.web, 'href', None)}")


@pytest.mark.api
def test_nfl_news_team_specific(site_api_client, ensure_json_output_dir):
    """Test retrieving NFL news filtered by team (Kansas City Chiefs, team=12)"""
    limit = 5
    team_id = 12

    response = get_nfl_news(client=site_api_client, limit=limit, team=team_id)
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    assert not isinstance(response.parsed, ErrorResponse), (
        f"API returned an error: {response.parsed}"
    )
    assert isinstance(response.parsed, SportNewsAPISchema), (
        "Response should parse to SportNewsAPISchema"
    )

    news: SportNewsAPISchema = response.parsed

    assert isinstance(news.header, str), "Header should be a string"
    assert isinstance(news.articles, list), "Articles should be a list"
    assert len(news.articles) > 0, "Articles list should not be empty"
    assert news.link, "Link should be present"
    assert news.link.href, "Link should have href attribute"

    # Check that at least one article has a category with team id 12
    found_team = False
    for article in news.articles:
        for cat in article.categories:
            if cat.team and cat.team is not UNSET:
                if hasattr(cat.team, "id") and cat.team.id == team_id:
                    found_team = True
                    break
        if found_team:
            break
    assert found_team, (
        "No article found with category for team id 12 (Kansas City Chiefs)"
    )

    # Save response for analysis
    import json

    with open(
        f"{ensure_json_output_dir}/nfl_news_team_{team_id}_response.json", "w"
    ) as f:
        json.dump(news.to_dict(), f, indent=2)

    # Print a summary of the first article for debugging
    article = news.articles[0]
    print("First article summary (team-specific):")
    print(f"  Headline: {article.headline}")
    print(f"  Description: {article.description}")
    print(f"  Published: {article.published}")
    print(f"  Images: {len(article.images)}")
    print(f"  Categories: {len(article.categories)}")
    print(f"  Links: web={getattr(article.links.web, 'href', None)}")


@pytest.mark.api
@pytest.mark.skip(reason="Test functionality not yet implemented")
def test_generic_news_endpoint(site_api_client):
    """Test retrieving news from the generic sport/league endpoint"""
    pass


@pytest.mark.api
def test_mlb_news(site_api_client, ensure_json_output_dir):
    """Test retrieving MLB news from the specific endpoint"""
    limit = 5

    from models.site_api.espn_nfl_api_client.api.default.get_mlb_news import (
        sync_detailed as get_mlb_news,
    )

    response = get_mlb_news(client=site_api_client, limit=limit)
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    assert not isinstance(response.parsed, ErrorResponse), (
        f"API returned an error: {response.parsed}"
    )
    assert isinstance(response.parsed, SportNewsAPISchema), (
        "Response should parse to SportNewsAPISchema"
    )

    news: SportNewsAPISchema = response.parsed

    # Check top-level fields
    assert isinstance(news.header, str), "Header should be a string"
    assert isinstance(news.articles, list), "Articles should be a list"
    assert len(news.articles) > 0, "Articles list should not be empty"
    assert news.link, "Link should be present"
    assert news.link.href, "Link should have href attribute"

    # Check the first article in detail
    article = news.articles[0]
    assert isinstance(article, NewsArticle), "Article should be a NewsArticle instance"
    assert isinstance(article.id, int), "Article ID should be an integer"
    assert isinstance(article.now_id, str), "Article now_id should be a string"
    assert isinstance(article.content_key, str), (
        "Article content_key should be a string"
    )
    assert isinstance(article.data_source_identifier, str), (
        "Article data_source_identifier should be a string"
    )
    assert article.type.value in ["HeadlineNews", "Media", "Story", "Recap"], (
        "Article type should be valid"
    )
    assert isinstance(article.headline, str), "Article headline should be a string"
    assert isinstance(article.description, str), (
        "Article description should be a string"
    )
    assert isinstance(article.last_modified, (str, datetime)) or hasattr(
        article.last_modified, "isoformat"
    ), "Last modified should be a valid date format"
    assert isinstance(article.published, (str, datetime)) or hasattr(
        article.published, "isoformat"
    ), "Published date should be a valid date format"
    assert isinstance(article.images, list), "Images should be a list"
    assert isinstance(article.categories, list), "Categories should be a list"
    assert isinstance(article.premium, bool), "Premium flag should be a boolean"
    assert article.links, "Links should be present"

    # Save response for analysis
    import json

    with open(f"{ensure_json_output_dir}/mlb_news_response.json", "w") as f:
        json.dump(news.to_dict(), f, indent=2)

    # Print a summary of the first article for debugging
    print("First MLB article summary:")
    print(f"  Headline: {article.headline}")
    print(f"  Description: {article.description}")
    print(f"  Published: {article.published}")
    print(f"  Images: {len(article.images)}")
    print(f"  Categories: {len(article.categories)}")
    print(f"  Links: web={getattr(article.links.web, 'href', None)}")
