#!/usr/bin/env python3
"""
Test Soccer News using generic news endpoint
"""

import pytest
import logging
from models.site_api.espn_nfl_api_client.api.default import get_league_news
from models.site_api.espn_nfl_api_client.models.sport_news_api_schema import SportNewsAPISchema

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.parametrize("league_slug,league_name", [
    ("eng.1", "English Premier League"),
    ("usa.1", "MLS"),
    ("uefa.champions", "UEFA Champions League"),
])
def test_soccer_news_generic(site_api_client, league_slug, league_name):
    """Test that soccer news works with the generic news endpoint."""
    response = get_league_news.sync_detailed(
        client=site_api_client,
        sport="soccer",
        league=league_slug,
        limit=5
    )
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    result = response.parsed
    assert isinstance(result, SportNewsAPISchema), "Response should parse to SportNewsAPISchema"
    
    # Check structure
    assert hasattr(result, 'articles'), "Response should have articles"
    assert isinstance(result.articles, list), "Articles should be a list"
    
    if result.header:
        logger.info(f"News header: {result.header}")
    
    logger.info(f"{league_name} news: {len(result.articles)} articles")
    
    # Log first few articles
    for i, article in enumerate(result.articles[:3]):
        if hasattr(article, 'headline') and article.headline:
            logger.info(f"  Article {i+1}: {article.headline}")
            if hasattr(article, 'description') and article.description:
                # Truncate long descriptions
                desc = article.description[:100] + "..." if len(article.description) > 100 else article.description
                logger.info(f"    {desc}")