#!/usr/bin/env python3

import pytest
import json
import logging
from datetime import datetime

from models.site_api.espn_nfl_api_client.api.default import get_league_news
from models.site_api.espn_nfl_api_client.types import UNSET
from models.site_api.espn_nfl_api_client.models.sport_news_api_schema import (
    SportNewsAPISchema,
)
from models.site_api.espn_nfl_api_client.models.error_response import ErrorResponse
from models.site_api.espn_nfl_api_client.models.news_article import NewsArticle
from models.site_api.espn_nfl_api_client.models.news_article_type import (
    NewsArticleType,
)
from models.site_api.espn_nfl_api_client.models.news_category_type import (
    NewsCategoryType,
)
from models.site_api.espn_nfl_api_client.models.league_enum import (
    LeagueEnum,
)
from models.site_api.espn_nfl_api_client.models.sport_enum import (
    SportEnum,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
def test_nfl_news(site_api_client, ensure_json_output_dir):
    """Test retrieving NFL news from the specific endpoint"""
    limit = 5
    response = get_league_news.sync_detailed(client=site_api_client, sport="football", league="nfl", limit=limit)
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
    assert isinstance(article.type, NewsArticleType), (
        f"Article type should be a known NewsArticleType, got {article.type!r}"
    )
    assert isinstance(article.headline, str), "Article headline should be a string"
    # `description` is optional -- some articles (e.g. Media items) omit it.
    assert article.description is UNSET or isinstance(article.description, str), (
        "Article description should be a string when present"
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
    for img in article.images:
        assert hasattr(img, "url"), "Image should have URL attribute"
        assert isinstance(img.url, str) or img.url is UNSET, (
            "Image URL should be a string or UNSET"
        )
    for cat in article.categories:
        assert hasattr(cat, "type"), "Category should have type attribute"
        assert hasattr(cat, "guid"), "Category should have guid attribute"
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
    with open(f"{ensure_json_output_dir}/nfl_news_response.json", "w") as f:
        json.dump(news.to_dict(), f, indent=2)
    logger.info("First article summary:")
    logger.info(f"  Headline: {article.headline}")
    logger.info(f"  Description: {article.description}")
    logger.info(f"  Published: {article.published}")
    logger.info(f"  Images: {len(article.images)}")
    logger.info(f"  Categories: {len(article.categories)}")
    logger.info(f"  Links: web={getattr(links.web, 'href', None)}")


@pytest.mark.api
def test_nfl_news_team_specific(site_api_client, ensure_json_output_dir):
    """Test retrieving NFL news filtered by team (Kansas City Chiefs, team=12)"""
    limit = 5
    team_id = 12
    response = get_league_news.sync_detailed(client=site_api_client, sport="football", league="nfl", limit=limit, team=team_id)
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
    with open(
        f"{ensure_json_output_dir}/nfl_news_team_{team_id}_response.json", "w"
    ) as f:
        json.dump(news.to_dict(), f, indent=2)
    article = news.articles[0]
    logger.info("First article summary (team-specific):")
    logger.info(f"  Headline: {article.headline}")
    logger.info(f"  Description: {article.description}")
    logger.info(f"  Published: {article.published}")
    logger.info(f"  Images: {len(article.images)}")
    logger.info(f"  Categories: {len(article.categories)}")
    logger.info(f"  Links: web={getattr(article.links.web, 'href', None)}")


@pytest.mark.api
def test_mlb_news(site_api_client, ensure_json_output_dir):
    """Test retrieving MLB news from the specific endpoint"""
    limit = 5
    from models.site_api.espn_nfl_api_client.api.default.get_league_news import (
        sync_detailed as get_news,
    )

    response = get_news(
        client=site_api_client,
        limit=limit,
        sport=SportEnum("baseball"),
        league=LeagueEnum("mlb"),
    )
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
    assert isinstance(article.type, NewsArticleType), (
        f"Article type should be a known NewsArticleType, got {article.type!r}"
    )
    assert isinstance(article.headline, str), "Article headline should be a string"
    # `description` is optional -- some articles (e.g. Media items) omit it.
    assert article.description is UNSET or isinstance(article.description, str), (
        "Article description should be a string when present"
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
    with open(f"{ensure_json_output_dir}/mlb_news_response.json", "w") as f:
        json.dump(news.to_dict(), f, indent=2)
    logger.info("First MLB article summary:")
    logger.info(f"  Headline: {article.headline}")
    logger.info(f"  Description: {article.description}")
    logger.info(f"  Published: {article.published}")
    logger.info(f"  Images: {len(article.images)}")
    logger.info(f"  Categories: {len(article.categories)}")
    logger.info(f"  Links: web={getattr(article.links.web, 'href', None)}")


@pytest.mark.api
@pytest.mark.parametrize(
    "sport,league",
    [
        # These leagues surface article types beyond the common
        # HeadlineNews/Media/Story trio -- Preview and Recap for game-driven
        # feeds, Eticket for long-form features, Columnist for opinion pieces.
        ("baseball", "mlb"),
        ("basketball", "wnba"),
        ("basketball", "mens-college-basketball"),
        ("golf", "pga"),
        ("mma", "ufc"),
    ],
)
def test_news_article_types_parse(site_api_client, sport, league):
    """All article types the news feed emits should parse into NewsArticleType.

    ESPN keeps adding content types (Preview, Eticket, Columnist ...), and an
    unknown value makes the generated client raise while deserializing rather
    than fail an assertion. Pull a wide page so rarer types are included.
    """
    response = get_league_news.sync_detailed(
        client=site_api_client, sport=sport, league=league, limit=50
    )
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )
    news = response.parsed
    assert isinstance(news, SportNewsAPISchema), (
        "Response should parse to SportNewsAPISchema"
    )
    for article in news.articles:
        assert isinstance(article.type, NewsArticleType), (
            f"Unknown article type {article.type!r} for {sport}/{league}"
        )
        for category in article.categories:
            assert isinstance(category.type, NewsCategoryType), (
                f"Unknown category type {category.type!r} for {sport}/{league}"
            )
    logger.info(
        f"{sport}/{league}: {len(news.articles)} articles, types="
        f"{sorted({a.type.value for a in news.articles})}"
    )
