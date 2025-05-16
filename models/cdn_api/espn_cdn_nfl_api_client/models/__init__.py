"""Contains all the data models used in inputs/outputs"""

from .nfl_boxscore_response import NflBoxscoreResponse
from .nfl_play_by_play_response import NflPlayByPlayResponse
from .nfl_schedule_content import NflScheduleContent
from .nfl_schedule_content_defaults import NflScheduleContentDefaults
from .nfl_schedule_content_parameters import NflScheduleContentParameters
from .nfl_schedule_content_schedule import NflScheduleContentSchedule
from .nfl_schedule_content_week_map import NflScheduleContentWeekMap
from .nfl_schedule_date_games import NflScheduleDateGames
from .nfl_schedule_game import NflScheduleGame
from .nfl_schedule_game_season import NflScheduleGameSeason
from .nfl_schedule_game_week import NflScheduleGameWeek
from .nfl_schedule_response import NflScheduleResponse
from .nfl_schedule_response_ads import NflScheduleResponseAds
from .nfl_schedule_response_analytics import NflScheduleResponseAnalytics
from .nfl_schedule_response_calendar_entry import NflScheduleResponseCalendarEntry
from .nfl_schedule_response_calendar_item import NflScheduleResponseCalendarItem
from .nfl_schedule_response_meta import NflScheduleResponseMeta
from .nfl_schedule_response_tier_2_nav import NflScheduleResponseTier2Nav
from .nfl_scoreboard_response import NflScoreboardResponse
from .nfl_standings import NflStandings
from .nfl_standings_content import NflStandingsContent
from .nfl_standings_content_config import NflStandingsContentConfig
from .nfl_standings_content_params import NflStandingsContentParams
from .nfl_standings_entry import NflStandingsEntry
from .nfl_standings_group import NflStandingsGroup
from .nfl_standings_group_division import NflStandingsGroupDivision
from .nfl_standings_group_standings import NflStandingsGroupStandings
from .nfl_standings_response import NflStandingsResponse
from .nfl_standings_response_ads import NflStandingsResponseAds
from .nfl_standings_response_analytics import NflStandingsResponseAnalytics
from .nfl_standings_response_meta import NflStandingsResponseMeta
from .nfl_standings_response_tier_2_nav import NflStandingsResponseTier2Nav
from .nfl_standings_stat import NflStandingsStat
from .nfl_standings_team import NflStandingsTeam
from .nfl_standings_team_logos_item import NflStandingsTeamLogosItem
from .scoreboard_article import ScoreboardArticle
from .scoreboard_article_links import ScoreboardArticleLinks
from .scoreboard_article_links_api import ScoreboardArticleLinksApi
from .scoreboard_article_links_app import ScoreboardArticleLinksApp
from .scoreboard_article_links_mobile_type_1 import ScoreboardArticleLinksMobileType1
from .scoreboard_article_links_web_type_1 import ScoreboardArticleLinksWebType1
from .scoreboard_broadcast import ScoreboardBroadcast
from .scoreboard_calendar import ScoreboardCalendar
from .scoreboard_calendar_entry import ScoreboardCalendarEntry
from .scoreboard_category import ScoreboardCategory
from .scoreboard_competition import ScoreboardCompetition
from .scoreboard_competition_type import ScoreboardCompetitionType
from .scoreboard_competitor import ScoreboardCompetitor
from .scoreboard_competitor_statistics_item import ScoreboardCompetitorStatisticsItem
from .scoreboard_content import ScoreboardContent
from .scoreboard_content_date_params import ScoreboardContentDateParams
from .scoreboard_content_defaults import ScoreboardContentDefaults
from .scoreboard_contributor import ScoreboardContributor
from .scoreboard_contributor_links import ScoreboardContributorLinks
from .scoreboard_event import ScoreboardEvent
from .scoreboard_format import ScoreboardFormat
from .scoreboard_geo_broadcast import ScoreboardGeoBroadcast
from .scoreboard_geo_broadcast_type import ScoreboardGeoBroadcastType
from .scoreboard_image import ScoreboardImage
from .scoreboard_league import ScoreboardLeague
from .scoreboard_league_data import ScoreboardLeagueData
from .scoreboard_league_links import ScoreboardLeagueLinks
from .scoreboard_link import ScoreboardLink
from .scoreboard_market import ScoreboardMarket
from .scoreboard_media import ScoreboardMedia
from .scoreboard_news import ScoreboardNews
from .scoreboard_note import ScoreboardNote
from .scoreboard_regulation import ScoreboardRegulation
from .scoreboard_sb_data import ScoreboardSbData
from .scoreboard_sb_group import ScoreboardSbGroup
from .scoreboard_season import ScoreboardSeason
from .scoreboard_season_type import ScoreboardSeasonType
from .scoreboard_status import ScoreboardStatus
from .scoreboard_status_type import ScoreboardStatusType
from .scoreboard_team import ScoreboardTeam
from .scoreboard_team_data import ScoreboardTeamData
from .scoreboard_team_links import ScoreboardTeamLinks
from .scoreboard_ticket import ScoreboardTicket
from .scoreboard_venue import ScoreboardVenue
from .scoreboard_venue_address import ScoreboardVenueAddress
from .scoreboard_week import ScoreboardWeek

__all__ = (
    "NflBoxscoreResponse",
    "NflPlayByPlayResponse",
    "NflScheduleContent",
    "NflScheduleContentDefaults",
    "NflScheduleContentParameters",
    "NflScheduleContentSchedule",
    "NflScheduleContentWeekMap",
    "NflScheduleDateGames",
    "NflScheduleGame",
    "NflScheduleGameSeason",
    "NflScheduleGameWeek",
    "NflScheduleResponse",
    "NflScheduleResponseAds",
    "NflScheduleResponseAnalytics",
    "NflScheduleResponseCalendarEntry",
    "NflScheduleResponseCalendarItem",
    "NflScheduleResponseMeta",
    "NflScheduleResponseTier2Nav",
    "NflScoreboardResponse",
    "NflStandings",
    "NflStandingsContent",
    "NflStandingsContentConfig",
    "NflStandingsContentParams",
    "NflStandingsEntry",
    "NflStandingsGroup",
    "NflStandingsGroupDivision",
    "NflStandingsGroupStandings",
    "NflStandingsResponse",
    "NflStandingsResponseAds",
    "NflStandingsResponseAnalytics",
    "NflStandingsResponseMeta",
    "NflStandingsResponseTier2Nav",
    "NflStandingsStat",
    "NflStandingsTeam",
    "NflStandingsTeamLogosItem",
    "ScoreboardArticle",
    "ScoreboardArticleLinks",
    "ScoreboardArticleLinksApi",
    "ScoreboardArticleLinksApp",
    "ScoreboardArticleLinksMobileType1",
    "ScoreboardArticleLinksWebType1",
    "ScoreboardBroadcast",
    "ScoreboardCalendar",
    "ScoreboardCalendarEntry",
    "ScoreboardCategory",
    "ScoreboardCompetition",
    "ScoreboardCompetitionType",
    "ScoreboardCompetitor",
    "ScoreboardCompetitorStatisticsItem",
    "ScoreboardContent",
    "ScoreboardContentDateParams",
    "ScoreboardContentDefaults",
    "ScoreboardContributor",
    "ScoreboardContributorLinks",
    "ScoreboardEvent",
    "ScoreboardFormat",
    "ScoreboardGeoBroadcast",
    "ScoreboardGeoBroadcastType",
    "ScoreboardImage",
    "ScoreboardLeague",
    "ScoreboardLeagueData",
    "ScoreboardLeagueLinks",
    "ScoreboardLink",
    "ScoreboardMarket",
    "ScoreboardMedia",
    "ScoreboardNews",
    "ScoreboardNote",
    "ScoreboardRegulation",
    "ScoreboardSbData",
    "ScoreboardSbGroup",
    "ScoreboardSeason",
    "ScoreboardSeasonType",
    "ScoreboardStatus",
    "ScoreboardStatusType",
    "ScoreboardTeam",
    "ScoreboardTeamData",
    "ScoreboardTeamLinks",
    "ScoreboardTicket",
    "ScoreboardVenue",
    "ScoreboardVenueAddress",
    "ScoreboardWeek",
)
