"""Contains all the data models used in inputs/outputs"""

from .address import Address
from .article import Article
from .article_image import ArticleImage
from .article_link import ArticleLink
from .article_links import ArticleLinks
from .article_links_api import ArticleLinksApi
from .article_links_app import ArticleLinksApp
from .article_type import ArticleType
from .athlete import Athlete
from .athlete_links import AthleteLinks
from .boxscore import Boxscore
from .boxscore_player import BoxscorePlayer
from .boxscore_team import BoxscoreTeam
from .broadcast import Broadcast
from .calendar_entry import CalendarEntry
from .calendar_item import CalendarItem
from .category import Category
from .category_type import CategoryType
from .college import College
from .competition import Competition
from .competition_leader import CompetitionLeader
from .competition_type import CompetitionType
from .competitor import Competitor
from .competitor_home_away import CompetitorHomeAway
from .conference import Conference
from .contributor import Contributor
from .contributor_links import ContributorLinks
from .contributor_links_mobile import ContributorLinksMobile
from .contributor_links_web import ContributorLinksWeb
from .detailed_venue import DetailedVenue
from .drive import Drive
from .drive_time_of_possession import DriveTimeOfPossession
from .error_response import ErrorResponse
from .error_response_error import ErrorResponseError
from .event import Event
from .event_competition import EventCompetition
from .event_competition_highlights_item import EventCompetitionHighlightsItem
from .event_competition_notes_item import EventCompetitionNotesItem
from .event_season import EventSeason
from .event_week import EventWeek
from .game_format import GameFormat
from .game_format_overtime import GameFormatOvertime
from .game_format_regulation import GameFormatRegulation
from .game_header import GameHeader
from .game_info import GameInfo
from .game_status import GameStatus
from .game_summary import GameSummary
from .game_summary_standings import GameSummaryStandings
from .geo_broadcast import GeoBroadcast
from .geo_broadcast_market import GeoBroadcastMarket
from .geo_broadcast_media import GeoBroadcastMedia
from .geo_broadcast_type import GeoBroadcastType
from .get_nfl_scoreboard_seasontype import GetNFLScoreboardSeasontype
from .get_nfl_standings_seasontype import GetNFLStandingsSeasontype
from .headline import Headline
from .headshot import Headshot
from .image import Image
from .injury import Injury
from .leader import Leader
from .leader_category import LeaderCategory
from .leader_entry import LeaderEntry
from .leader_performance import LeaderPerformance
from .league import League
from .league_links import LeagueLinks
from .league_season import LeagueSeason
from .linescore import Linescore
from .link import Link
from .logo import Logo
from .monday_night_football_response import MondayNightFootballResponse
from .news_article import NewsArticle
from .news_article_image import NewsArticleImage
from .news_article_link import NewsArticleLink
from .news_article_links import NewsArticleLinks
from .news_article_links_api import NewsArticleLinksApi
from .news_article_links_app import NewsArticleLinksApp
from .news_article_type import NewsArticleType
from .news_athlete import NewsAthlete
from .news_athlete_links import NewsAthleteLinks
from .news_category import NewsCategory
from .news_category_type import NewsCategoryType
from .news_contributor import NewsContributor
from .news_contributor_links import NewsContributorLinks
from .news_contributor_links_mobile import NewsContributorLinksMobile
from .news_contributor_links_web import NewsContributorLinksWeb
from .news_league import NewsLeague
from .news_league_links import NewsLeagueLinks
from .news_link import NewsLink
from .news_link_item import NewsLinkItem
from .news_response import NewsResponse
from .news_team import NewsTeam
from .news_team_links import NewsTeamLinks
from .news_web_mobile_links import NewsWebMobileLinks
from .nfl_team_schedule_response import NFLTeamScheduleResponse
from .official import Official
from .play import Play
from .play_clock import PlayClock
from .play_period import PlayPeriod
from .play_type import PlayType
from .player_stats import PlayerStats
from .player_stats_stats import PlayerStatsStats
from .position import Position
from .position_group import PositionGroup
from .record import Record
from .roster_athlete import RosterAthlete
from .roster_athlete_alternate_ids import RosterAthleteAlternateIds
from .roster_athlete_birth_place import RosterAthleteBirthPlace
from .roster_athlete_contracts_item import RosterAthleteContractsItem
from .roster_athlete_experience import RosterAthleteExperience
from .roster_athlete_headshot import RosterAthleteHeadshot
from .roster_athlete_status import RosterAthleteStatus
from .roster_athlete_teams_item import RosterAthleteTeamsItem
from .scoreboard import Scoreboard
from .season import Season
from .season_info import SeasonInfo
from .season_type import SeasonType
from .sport import Sport
from .sport_league import SportLeague
from .sport_league_season import SportLeagueSeason
from .sport_news_api_schema import SportNewsAPISchema
from .standing_entry import StandingEntry
from .standing_group import StandingGroup
from .standings_response import StandingsResponse
from .statistic import Statistic
from .statistic_entry import StatisticEntry
from .status_type import StatusType
from .status_type_state import StatusTypeState
from .sunday_night_football_response import SundayNightFootballResponse
from .team import Team
from .team_detail import TeamDetail
from .team_details_full import TeamDetailsFull
from .team_details_full_next_event_item import TeamDetailsFullNextEventItem
from .team_details_response import TeamDetailsResponse
from .team_entry import TeamEntry
from .team_franchise import TeamFranchise
from .team_franchise_team import TeamFranchiseTeam
from .team_groups import TeamGroups
from .team_groups_parent import TeamGroupsParent
from .team_link import TeamLink
from .team_logo import TeamLogo
from .team_record import TeamRecord
from .team_record_item import TeamRecordItem
from .team_record_stat import TeamRecordStat
from .team_roster_response import TeamRosterResponse
from .team_venue import TeamVenue
from .teams_list_response import TeamsListResponse
from .thursday_night_football_response import ThursdayNightFootballResponse
from .venue import Venue
from .venue_image import VenueImage
from .weather import Weather
from .web_mobile_links import WebMobileLinks
from .week_info import WeekInfo

__all__ = (
    "Address",
    "Article",
    "ArticleImage",
    "ArticleLink",
    "ArticleLinks",
    "ArticleLinksApi",
    "ArticleLinksApp",
    "ArticleType",
    "Athlete",
    "AthleteLinks",
    "Boxscore",
    "BoxscorePlayer",
    "BoxscoreTeam",
    "Broadcast",
    "CalendarEntry",
    "CalendarItem",
    "Category",
    "CategoryType",
    "College",
    "Competition",
    "CompetitionLeader",
    "CompetitionType",
    "Competitor",
    "CompetitorHomeAway",
    "Conference",
    "Contributor",
    "ContributorLinks",
    "ContributorLinksMobile",
    "ContributorLinksWeb",
    "DetailedVenue",
    "Drive",
    "DriveTimeOfPossession",
    "ErrorResponse",
    "ErrorResponseError",
    "Event",
    "EventCompetition",
    "EventCompetitionHighlightsItem",
    "EventCompetitionNotesItem",
    "EventSeason",
    "EventWeek",
    "GameFormat",
    "GameFormatOvertime",
    "GameFormatRegulation",
    "GameHeader",
    "GameInfo",
    "GameStatus",
    "GameSummary",
    "GameSummaryStandings",
    "GeoBroadcast",
    "GeoBroadcastMarket",
    "GeoBroadcastMedia",
    "GeoBroadcastType",
    "GetNFLScoreboardSeasontype",
    "GetNFLStandingsSeasontype",
    "Headline",
    "Headshot",
    "Image",
    "Injury",
    "Leader",
    "LeaderCategory",
    "LeaderEntry",
    "LeaderPerformance",
    "League",
    "LeagueLinks",
    "LeagueSeason",
    "Linescore",
    "Link",
    "Logo",
    "MondayNightFootballResponse",
    "NewsArticle",
    "NewsArticleImage",
    "NewsArticleLink",
    "NewsArticleLinks",
    "NewsArticleLinksApi",
    "NewsArticleLinksApp",
    "NewsArticleType",
    "NewsAthlete",
    "NewsAthleteLinks",
    "NewsCategory",
    "NewsCategoryType",
    "NewsContributor",
    "NewsContributorLinks",
    "NewsContributorLinksMobile",
    "NewsContributorLinksWeb",
    "NewsLeague",
    "NewsLeagueLinks",
    "NewsLink",
    "NewsLinkItem",
    "NewsResponse",
    "NewsTeam",
    "NewsTeamLinks",
    "NewsWebMobileLinks",
    "NFLTeamScheduleResponse",
    "Official",
    "Play",
    "PlayClock",
    "PlayerStats",
    "PlayerStatsStats",
    "PlayPeriod",
    "PlayType",
    "Position",
    "PositionGroup",
    "Record",
    "RosterAthlete",
    "RosterAthleteAlternateIds",
    "RosterAthleteBirthPlace",
    "RosterAthleteContractsItem",
    "RosterAthleteExperience",
    "RosterAthleteHeadshot",
    "RosterAthleteStatus",
    "RosterAthleteTeamsItem",
    "Scoreboard",
    "Season",
    "SeasonInfo",
    "SeasonType",
    "Sport",
    "SportLeague",
    "SportLeagueSeason",
    "SportNewsAPISchema",
    "StandingEntry",
    "StandingGroup",
    "StandingsResponse",
    "Statistic",
    "StatisticEntry",
    "StatusType",
    "StatusTypeState",
    "SundayNightFootballResponse",
    "Team",
    "TeamDetail",
    "TeamDetailsFull",
    "TeamDetailsFullNextEventItem",
    "TeamDetailsResponse",
    "TeamEntry",
    "TeamFranchise",
    "TeamFranchiseTeam",
    "TeamGroups",
    "TeamGroupsParent",
    "TeamLink",
    "TeamLogo",
    "TeamRecord",
    "TeamRecordItem",
    "TeamRecordStat",
    "TeamRosterResponse",
    "TeamsListResponse",
    "TeamVenue",
    "ThursdayNightFootballResponse",
    "Venue",
    "VenueImage",
    "Weather",
    "WebMobileLinks",
    "WeekInfo",
)
