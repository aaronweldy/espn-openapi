#!/usr/bin/env python3
"""
Game Preview Generator Recipe

This recipe auto-generates comprehensive game previews by combining data from multiple
ESPN API endpoints including team stats, injury reports, recent performance, and
head-to-head history.
"""

import argparse
import json
from datetime import datetime
from typing import Dict, List, Optional

# Import API clients
from models.site_api.espn_nfl_api_client import Client as SiteApiClient
from models.sports_core_api.espn_sports_core_api_client import Client as SportsCoreApiClient
from models.site_web_api.espn_site_web_api_client import Client as SiteWebApiClient

# Import specific endpoints
from models.site_api.espn_nfl_api_client.api.default import (
    get_scoreboard,
    get_team_details,
    get_team_schedule,
    get_league_news
)
from models.sports_core_api.espn_sports_core_api_client.api.default import (
    get_team_injuries
)


class GamePreviewGenerator:
    """Generate comprehensive game previews."""
    
    def __init__(self):
        self.site_client = SiteApiClient(base_url="https://site.api.espn.com/apis/site/v2")
        self.core_client = SportsCoreApiClient(base_url="https://sports.core.api.espn.com/v2")
        self.web_client = SiteWebApiClient(base_url="https://site.web.api.espn.com")
        
        # Sport configurations
        self.sports_config = {
            "nfl": ("football", "nfl", "NFL"),
            "nba": ("basketball", "nba", "NBA"),
            "mlb": ("baseball", "mlb", "MLB"),
            "nhl": ("hockey", "nhl", "NHL"),
            "ncaaf": ("football", "college-football", "NCAAF"),
            "ncaab": ("basketball", "mens-college-basketball", "NCAAB")
        }
        
        # Cache for team data
        self.team_cache = {}
        
    def get_upcoming_games(self, sport: str, league: str, date: Optional[str] = None) -> List[Dict]:
        """Get upcoming games for a specific date."""
        if not date:
            date = datetime.now().strftime('%Y%m%d')
            
        try:
            response = get_scoreboard.sync_detailed(
                client=self.site_client,
                sport=sport,
                league=league,
                dates=date
            )
            
            if response.status_code != 200:
                print(f"Error fetching scoreboard: {response.status_code}")
                return []
                
            games = []
            if hasattr(response.parsed, 'events') and response.parsed.events:
                for event in response.parsed.events:
                    if hasattr(event, 'competitions') and event.competitions:
                        comp = event.competitions[0]
                        if hasattr(comp, 'competitors') and len(comp.competitors) >= 2:
                            # Extract game info
                            game_info = {
                                'id': event.id if hasattr(event, 'id') else None,
                                'name': event.name if hasattr(event, 'name') else "Unknown",
                                'short_name': event.short_name if hasattr(event, 'short_name') else "Unknown",
                                'date': event.date if hasattr(event, 'date') else None,
                                'status': comp.status.type.name if hasattr(comp, 'status') and hasattr(comp.status, 'type') else "scheduled",
                                'competitors': []
                            }
                            
                            # Extract competitor info
                            for competitor in comp.competitors:
                                team_data = {
                                    'id': competitor.id if hasattr(competitor, 'id') else None,
                                    'team': {}
                                }
                                
                                if hasattr(competitor, 'team'):
                                    team_data['team'] = {
                                        'id': competitor.team.id if hasattr(competitor.team, 'id') else None,
                                        'name': competitor.team.display_name if hasattr(competitor.team, 'display_name') else "Unknown",
                                        'abbreviation': competitor.team.abbreviation if hasattr(competitor.team, 'abbreviation') else "UNK",
                                        'logo': competitor.team.logo if hasattr(competitor.team, 'logo') else None
                                    }
                                    
                                if hasattr(competitor, 'home_away'):
                                    team_data['home_away'] = competitor.home_away
                                    
                                if hasattr(competitor, 'records') and competitor.records:
                                    for record in competitor.records:
                                        if hasattr(record, 'summary'):
                                            team_data['record'] = record.summary
                                            break
                                            
                                game_info['competitors'].append(team_data)
                                
                            games.append(game_info)
                            
            return games
            
        except Exception as e:
            print(f"Error getting upcoming games: {e}")
            return []
            
    async def fetch_team_details_async(self, sport: str, league: str, team_id: str) -> Optional[Dict]:
        """Fetch team details asynchronously."""
        cache_key = f"{sport}_{league}_{team_id}"
        if cache_key in self.team_cache:
            return self.team_cache[cache_key]
            
        try:
            # Get basic team info
            response = get_team_details.sync_detailed(
                client=self.site_client,
                sport=sport,
                league=league,
                team_id_or_abbrev=team_id
            )
            
            if response.status_code != 200:
                return None
                
            team_data = {
                'info': response.parsed.to_dict() if response.parsed else {},
                'injuries': [],
                'recent_games': [],
                'season_stats': {}
            }
            
            # Cache and return
            self.team_cache[cache_key] = team_data
            return team_data
            
        except Exception as e:
            print(f"Error fetching team details: {e}")
            return None
            
    def get_team_injuries(self, sport: str, league: str, team_id: str) -> List[Dict]:
        """Get injury report for a team."""
        try:
            response = get_team_injuries.sync_detailed(
                client=self.core_client,
                sport=sport,
                league=league,
                team_id=team_id
            )
            
            if response.status_code == 404:
                # No injuries is common
                return []
            elif response.status_code != 200:
                return []
                
            injuries = []
            if hasattr(response.parsed, 'items') and response.parsed.items:
                for item in response.parsed.items:
                    injury_data = {
                        'athlete': {},
                        'status': None,
                        'description': None
                    }
                    
                    # Extract athlete info
                    if hasattr(item, 'athlete') and item.athlete:
                        if hasattr(item.athlete, 'display_name'):
                            injury_data['athlete']['name'] = item.athlete.display_name
                        if hasattr(item.athlete, 'position') and item.athlete.position:
                            if hasattr(item.athlete.position, 'abbreviation'):
                                injury_data['athlete']['position'] = item.athlete.position.abbreviation
                                
                    # Extract injury details
                    if hasattr(item, 'status') and item.status:
                        if hasattr(item.status, 'type') and item.status.type:
                            if hasattr(item.status.type, 'abbreviation'):
                                injury_data['status'] = item.status.type.abbreviation
                                
                    if hasattr(item, 'details') and item.details:
                        if hasattr(item.details, 'type'):
                            injury_data['description'] = item.details.type
                            
                    injuries.append(injury_data)
                    
            return injuries
            
        except Exception:
            return []
            
    def get_recent_games(self, sport: str, league: str, team_id: str, limit: int = 5) -> List[Dict]:
        """Get recent game results for a team."""
        try:
            # Get team schedule
            current_year = datetime.now().year
            response = get_team_schedule.sync_detailed(
                client=self.site_client,
                sport=sport,
                league=league,
                team_id_or_abbrev=team_id,
                season=str(current_year)
            )
            
            if response.status_code != 200:
                return []
                
            games = []
            if hasattr(response.parsed, 'events') and response.parsed.events:
                # Filter completed games
                completed_games = []
                for event in response.parsed.events:
                    if hasattr(event, 'competitions') and event.competitions:
                        comp = event.competitions[0]
                        if hasattr(comp, 'status') and comp.status:
                            if hasattr(comp.status, 'type') and comp.status.type:
                                if hasattr(comp.status.type, 'completed') and comp.status.type.completed:
                                    completed_games.append(event)
                                    
                # Get last N completed games
                for event in completed_games[-limit:]:
                    game_data = {
                        'date': event.date if hasattr(event, 'date') else None,
                        'opponent': None,
                        'result': None,
                        'score': None
                    }
                    
                    if event.competitions:
                        comp = event.competitions[0]
                        if hasattr(comp, 'competitors') and len(comp.competitors) >= 2:
                            # Find team and opponent
                            team_score = None
                            opp_score = None
                            team_won = None
                            
                            for competitor in comp.competitors:
                                if hasattr(competitor, 'team') and competitor.team:
                                    # Get score value
                                    score_val = None
                                    if hasattr(competitor, 'score'):
                                        if isinstance(competitor.score, dict):
                                            score_val = competitor.score.get('displayValue', competitor.score.get('value', ''))
                                        else:
                                            score_val = str(competitor.score)
                                    
                                    if str(competitor.team.id) == str(team_id) or competitor.team.abbreviation == team_id:
                                        # This is our team
                                        team_score = score_val
                                        if hasattr(competitor, 'winner'):
                                            team_won = competitor.winner
                                    else:
                                        # This is the opponent
                                        game_data['opponent'] = competitor.team.display_name if hasattr(competitor.team, 'display_name') else "Unknown"
                                        opp_score = score_val
                            
                            # Set result and full score
                            if team_won is not None:
                                game_data['result'] = 'W' if team_won else 'L'
                            
                            if team_score and opp_score:
                                if team_won:
                                    game_data['score'] = f"{team_score}-{opp_score}"
                                else:
                                    game_data['score'] = f"{opp_score}-{team_score}"
                                        
                    games.append(game_data)
                    
            return games
            
        except Exception as e:
            print(f"Error getting recent games: {e}")
            return []
            
    def get_head_to_head(self, sport: str, league: str, team1_id: str, team2_id: str) -> Dict:
        """Get head-to-head history between two teams."""
        # For now, return a placeholder
        # In a full implementation, this would search historical games
        return {
            'all_time': {'team1_wins': 0, 'team2_wins': 0, 'ties': 0},
            'recent': {'team1_wins': 0, 'team2_wins': 0, 'ties': 0},
            'last_meeting': None
        }
        
    def get_relevant_news(self, sport: str, league: str, team_ids: List[str], team_names: List[str], limit: int = 20) -> List[Dict]:
        """Get news articles relevant to the teams playing."""
        try:
            # Get recent news
            response = get_league_news.sync_detailed(
                client=self.site_client,
                sport=sport,
                league=league,
                limit=limit
            )
            
            if response.status_code != 200:
                return []
                
            relevant_articles = []
            
            if hasattr(response.parsed, 'articles') and response.parsed.articles:
                for article in response.parsed.articles:
                    # Check if article is relevant to either team
                    is_relevant = False
                    
                    # Check headline
                    if hasattr(article, 'headline') and article.headline:
                        headline_lower = article.headline.lower()
                        for team_name in team_names:
                            if team_name.lower() in headline_lower:
                                is_relevant = True
                                break
                                
                    # Check description if not already relevant
                    if not is_relevant and hasattr(article, 'description') and article.description:
                        desc_lower = article.description.lower()
                        for team_name in team_names:
                            if team_name.lower() in desc_lower:
                                is_relevant = True
                                break
                                
                    # Check categories for team IDs
                    if not is_relevant and hasattr(article, 'categories') and article.categories:
                        for category in article.categories:
                            if hasattr(category, 'team_id') and str(category.team_id) in team_ids:
                                is_relevant = True
                                break
                                
                    if is_relevant:
                        article_data = {
                            'headline': article.headline if hasattr(article, 'headline') else '',
                            'description': article.description if hasattr(article, 'description') else '',
                            'published': article.published if hasattr(article, 'published') else None,
                            'type': article.type if hasattr(article, 'type') else 'article',
                            'premium': article.premium if hasattr(article, 'premium') else False
                        }
                        
                        # Add link if available
                        if hasattr(article, 'links') and article.links:
                            if hasattr(article.links, 'web') and article.links.web:
                                if hasattr(article.links.web, 'href'):
                                    article_data['link'] = article.links.web.href
                                    
                        relevant_articles.append(article_data)
                        
            return relevant_articles[:5]  # Return top 5 relevant articles
            
        except Exception as e:
            print(f"Error fetching news: {e}")
            return []
        
    def generate_preview(self, game: Dict, sport: str, league: str) -> Dict:
        """Generate a comprehensive preview for a single game."""
        preview = {
            'game_info': game,
            'teams': {},
            'injuries': {},
            'recent_form': {},
            'head_to_head': {},
            'relevant_news': [],
            'key_storylines': []
        }
        
        # Extract team IDs and names
        teams = []
        team_ids = []
        team_names = []
        
        for comp in game['competitors']:
            team_data = {
                'id': comp['team']['id'],
                'name': comp['team']['name'],
                'abbreviation': comp['team']['abbreviation'],
                'home_away': comp.get('home_away', 'away')
            }
            teams.append(team_data)
            team_ids.append(str(team_data['id']))
            team_names.append(team_data['name'])
            
        # Fetch data for each team
        for team in teams:
            team_id = team['id']
            team_key = team['home_away']
            
            # Get team injuries
            injuries = self.get_team_injuries(sport, league, team_id)
            preview['injuries'][team_key] = injuries
            
            # Get recent games
            recent_games = self.get_recent_games(sport, league, team_id, limit=5)
            preview['recent_form'][team_key] = recent_games
            
            # Store team info
            preview['teams'][team_key] = team
            
        # Get relevant news
        preview['relevant_news'] = self.get_relevant_news(sport, league, team_ids, team_names)
            
        # Get head-to-head if we have both teams
        if len(teams) == 2:
            preview['head_to_head'] = self.get_head_to_head(
                sport, league, teams[0]['id'], teams[1]['id']
            )
            
        # Generate key storylines
        preview['key_storylines'] = self.generate_storylines(preview)
        
        return preview
        
    def generate_storylines(self, preview: Dict) -> List[str]:
        """Generate key storylines based on preview data."""
        storylines = []
        
        # Check injury impact
        for team_type in ['home', 'away']:
            injuries = preview['injuries'].get(team_type, [])
            key_injuries = [inj for inj in injuries if inj.get('status') in ['OUT', 'QUESTIONABLE']]
            if key_injuries:
                team_name = preview['teams'][team_type]['name']
                storylines.append(f"{team_name} dealing with {len(key_injuries)} key injuries")
                
        # Check recent form
        for team_type in ['home', 'away']:
            recent = preview['recent_form'].get(team_type, [])
            if recent:
                # Count recent wins/losses
                recent_results = [g['result'] for g in recent[-3:] if g.get('result')]
                if recent_results:
                    wins = recent_results.count('W')
                    team_name = preview['teams'][team_type]['name']
                    if wins == 3:
                        storylines.append(f"{team_name} riding a 3-game winning streak")
                    elif wins == 0:
                        storylines.append(f"{team_name} looking to snap a 3-game losing streak")
                        
        return storylines
        
    def format_preview_console(self, preview: Dict, sport_name: str) -> str:
        """Format preview for console output."""
        lines = []
        
        # Header
        lines.append("=" * 80)
        lines.append(f"{sport_name} GAME PREVIEW")
        lines.append("=" * 80)
        lines.append("")
        
        # Game info
        game = preview['game_info']
        lines.append(f"{game['name']}")
        if game.get('date'):
            # Handle datetime object or string
            if isinstance(game['date'], str):
                game_date = datetime.fromisoformat(game['date'].replace('Z', '+00:00'))
            else:
                game_date = game['date']
            lines.append(f"Date: {game_date.strftime('%B %d, %Y at %I:%M %p')}")
        lines.append("")
        
        # Teams and records
        lines.append("MATCHUP")
        lines.append("-" * 40)
        for team_type in ['away', 'home']:
            team = preview['teams'].get(team_type, {})
            if team:
                record = ""
                for comp in game['competitors']:
                    if comp['team']['id'] == team['id'] and comp.get('record'):
                        record = f" ({comp['record']})"
                        break
                lines.append(f"{team_type.upper()}: {team['name']}{record}")
        lines.append("")
        
        # Injury Report
        lines.append("INJURY REPORT")
        lines.append("-" * 40)
        has_injuries = False
        for team_type in ['home', 'away']:
            team = preview['teams'].get(team_type, {})
            injuries = preview['injuries'].get(team_type, [])
            if injuries:
                has_injuries = True
                lines.append(f"\n{team['name']}:")
                for injury in injuries[:5]:  # Show top 5
                    athlete = injury.get('athlete', {})
                    name = athlete.get('name', 'Unknown')
                    pos = athlete.get('position', '')
                    status = injury.get('status', 'Unknown')
                    desc = injury.get('description', '')
                    lines.append(f"  - {name} {f'({pos})' if pos else ''}: {status} - {desc}")
                if len(injuries) > 5:
                    lines.append(f"  ... and {len(injuries) - 5} more")
        if not has_injuries:
            lines.append("No significant injuries reported")
        lines.append("")
        
        # Recent Form
        lines.append("RECENT FORM")
        lines.append("-" * 40)
        for team_type in ['home', 'away']:
            team = preview['teams'].get(team_type, {})
            recent = preview['recent_form'].get(team_type, [])
            if team and recent:
                lines.append(f"\n{team['name']} (Last 5 games):")
                for game in recent:
                    if game.get('date') and game.get('opponent'):
                        # Handle datetime object or string
                        if isinstance(game['date'], str):
                            game_date = datetime.fromisoformat(game['date'].replace('Z', '+00:00'))
                        else:
                            game_date = game['date']
                        result = game.get('result', '?')
                        score = game.get('score', '')
                        lines.append(f"  {game_date.strftime('%m/%d')}: {result} vs {game['opponent']} {score}")
        lines.append("")
        
        # Key Storylines
        if preview['key_storylines']:
            lines.append("KEY STORYLINES")
            lines.append("-" * 40)
            for storyline in preview['key_storylines']:
                lines.append(f"• {storyline}")
            lines.append("")
            
        # Recent News
        if preview.get('relevant_news'):
            lines.append("RECENT NEWS")
            lines.append("-" * 40)
            for article in preview['relevant_news'][:3]:  # Show top 3
                lines.append(f"\n{article['headline']}")
                if article.get('description'):
                    # Truncate long descriptions
                    desc = article['description']
                    if len(desc) > 150:
                        desc = desc[:147] + "..."
                    lines.append(f"  {desc}")
                if article.get('published'):
                    # Handle datetime object or string
                    if isinstance(article['published'], str):
                        pub_date = datetime.fromisoformat(article['published'].replace('Z', '+00:00'))
                    else:
                        pub_date = article['published']
                    lines.append(f"  - {pub_date.strftime('%B %d, %Y')}")
            lines.append("")
            
        return "\n".join(lines)
        
    def format_preview_json(self, preview: Dict) -> str:
        """Format preview as JSON."""
        return json.dumps(preview, indent=2, default=str)
        
    def format_preview_markdown(self, preview: Dict, sport_name: str) -> str:
        """Format preview as Markdown."""
        lines = []
        
        # Header
        game = preview['game_info']
        lines.append(f"# {sport_name} Game Preview: {game['name']}")
        lines.append("")
        
        if game.get('date'):
            # Handle datetime object or string
            if isinstance(game['date'], str):
                game_date = datetime.fromisoformat(game['date'].replace('Z', '+00:00'))
            else:
                game_date = game['date']
            lines.append(f"**Date:** {game_date.strftime('%B %d, %Y at %I:%M %p')}")
            lines.append("")
            
        # Teams
        lines.append("## Matchup")
        lines.append("")
        lines.append("| Team | Record |")
        lines.append("|------|--------|")
        for team_type in ['away', 'home']:
            team = preview['teams'].get(team_type, {})
            if team:
                record = ""
                for comp in game['competitors']:
                    if comp['team']['id'] == team['id'] and comp.get('record'):
                        record = comp['record']
                        break
                lines.append(f"| **{team_type.upper()}:** {team['name']} | {record} |")
        lines.append("")
        
        # Injuries
        lines.append("## Injury Report")
        lines.append("")
        for team_type in ['home', 'away']:
            team = preview['teams'].get(team_type, {})
            injuries = preview['injuries'].get(team_type, [])
            if injuries:
                lines.append(f"### {team['name']}")
                lines.append("")
                lines.append("| Player | Position | Status | Injury |")
                lines.append("|--------|----------|--------|--------|")
                for injury in injuries:
                    athlete = injury.get('athlete', {})
                    name = athlete.get('name', 'Unknown')
                    pos = athlete.get('position', '-')
                    status = injury.get('status', 'Unknown')
                    desc = injury.get('description', '-')
                    lines.append(f"| {name} | {pos} | {status} | {desc} |")
                lines.append("")
                
        # Recent Form
        lines.append("## Recent Form")
        lines.append("")
        for team_type in ['home', 'away']:
            team = preview['teams'].get(team_type, {})
            recent = preview['recent_form'].get(team_type, [])
            if team and recent:
                lines.append(f"### {team['name']} (Last 5 games)")
                lines.append("")
                lines.append("| Date | Result | Opponent | Score |")
                lines.append("|------|--------|----------|-------|")
                for game in recent:
                    if game.get('date'):
                        # Handle datetime object or string
                        if isinstance(game['date'], str):
                            game_date = datetime.fromisoformat(game['date'].replace('Z', '+00:00'))
                        else:
                            game_date = game['date']
                        date_str = game_date.strftime('%m/%d')
                        result = game.get('result', '?')
                        opponent = game.get('opponent', 'Unknown')
                        score = game.get('score', '-')
                        lines.append(f"| {date_str} | {result} | {opponent} | {score} |")
                lines.append("")
                
        # Storylines
        if preview['key_storylines']:
            lines.append("## Key Storylines")
            lines.append("")
            for storyline in preview['key_storylines']:
                lines.append(f"- {storyline}")
            lines.append("")
            
        # Recent News
        if preview.get('relevant_news'):
            lines.append("## Recent News")
            lines.append("")
            for article in preview['relevant_news'][:5]:  # Show top 5 in markdown
                lines.append(f"### {article['headline']}")
                lines.append("")
                if article.get('description'):
                    lines.append(f"{article['description']}")
                    lines.append("")
                if article.get('published'):
                    # Handle datetime object or string
                    if isinstance(article['published'], str):
                        pub_date = datetime.fromisoformat(article['published'].replace('Z', '+00:00'))
                    else:
                        pub_date = article['published']
                    lines.append(f"*Published: {pub_date.strftime('%B %d, %Y at %I:%M %p')}*")
                    lines.append("")
            
        return "\n".join(lines)
        
    def run(self, leagues: List[str], date: Optional[str] = None, 
            output_format: str = 'console', limit: Optional[int] = None) -> List[Dict]:
        """Run the preview generator for specified leagues."""
        all_previews = []
        
        for league in leagues:
            if league not in self.sports_config:
                print(f"Unknown league: {league}")
                continue
                
            sport, league_key, display_name = self.sports_config[league]
            print(f"\nFetching {display_name} games...")
            
            # Get upcoming games
            games = self.get_upcoming_games(sport, league_key, date)
            
            if not games:
                print(f"No games found for {display_name} on {date or 'today'}")
                continue
                
            # Apply limit if specified
            if limit:
                games = games[:limit]
                
            print(f"Generating previews for {len(games)} {display_name} games...")
            
            # Generate preview for each game
            for i, game in enumerate(games, 1):
                print(f"  Processing game {i}/{len(games)}: {game['short_name']}...")
                preview = self.generate_preview(game, sport, league_key)
                preview['sport'] = sport
                preview['league'] = league_key
                preview['display_name'] = display_name
                
                # Format based on output type
                if output_format == 'console':
                    print("\n" + self.format_preview_console(preview, display_name))
                elif output_format == 'json':
                    all_previews.append(preview)
                elif output_format == 'markdown':
                    print("\n" + self.format_preview_markdown(preview, display_name))
                    
        return all_previews


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Auto-generate comprehensive game previews"
    )
    
    parser.add_argument(
        "--leagues",
        nargs="+",
        choices=["nfl", "nba", "mlb", "nhl", "ncaaf", "ncaab"],
        default=["nfl"],
        help="Leagues to generate previews for"
    )
    
    parser.add_argument(
        "--date",
        help="Date for games (YYYYMMDD format, default: today)"
    )
    
    parser.add_argument(
        "--output",
        choices=["console", "json", "markdown"],
        default="console",
        help="Output format"
    )
    
    parser.add_argument(
        "--save",
        help="Save output to file"
    )
    
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit number of games per league"
    )
    
    args = parser.parse_args()
    
    # Create generator
    generator = GamePreviewGenerator()
    
    # Run preview generation
    previews = generator.run(
        leagues=args.leagues,
        date=args.date,
        output_format=args.output,
        limit=args.limit
    )
    
    # Save if requested
    if args.save:
        if args.output == 'json':
            with open(args.save, 'w') as f:
                json.dump(previews, f, indent=2, default=str)
            print(f"\nPreviews saved to: {args.save}")
        elif args.output == 'markdown':
            # For markdown, we need to regenerate with proper formatting
            with open(args.save, 'w') as f:
                for preview in previews:
                    f.write(generator.format_preview_markdown(preview, preview['display_name']))
                    f.write("\n\n---\n\n")
            print(f"\nPreviews saved to: {args.save}")


if __name__ == "__main__":
    main()