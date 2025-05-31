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
from .generic_scoreboard_response import GenericScoreboardResponse
from .generic_scoreboard_response_day import GenericScoreboardResponseDay
from .geo_broadcast import GeoBroadcast
from .geo_broadcast_market import GeoBroadcastMarket
from .geo_broadcast_media import GeoBroadcastMedia
from .geo_broadcast_type import GeoBroadcastType
from .get_mlb_team_details_team_id_or_abbrev import GetMLBTeamDetailsTeamIdOrAbbrev
from .get_mlb_team_roster_team_id_or_abbrev import GetMLBTeamRosterTeamIdOrAbbrev
from .get_scoreboard_seasontype import GetScoreboardSeasontype
from .get_scoreboard_sport import GetScoreboardSport
from .headline import Headline
from .headshot import Headshot
from .image import Image
from .injury import Injury
from .leader import Leader
from .leader_category import LeaderCategory
from .leader_entry import LeaderEntry
from .leader_performance import LeaderPerformance
from .league import League
from .league_enum import LeagueEnum
from .league_links import LeagueLinks
from .league_season import LeagueSeason
from .linescore import Linescore
from .link import Link
from .logo import Logo
from .mlb_against_the_spread import MlbAgainstTheSpread
from .mlb_article import MlbArticle
from .mlb_boxscore import MlbBoxscore
from .mlb_broadcast import MlbBroadcast
from .mlb_coach import MlbCoach
from .mlb_format import MlbFormat
from .mlb_game_info import MlbGameInfo
from .mlb_game_summary_response import MlbGameSummaryResponse
from .mlb_game_summary_response_at_bats import MlbGameSummaryResponseAtBats
from .mlb_game_summary_response_plays_map import MlbGameSummaryResponsePlaysMap
from .mlb_header import MlbHeader
from .mlb_injury import MlbInjury
from .mlb_meta import MlbMeta
from .mlb_news import MlbNews
from .mlb_pickcenter import MlbPickcenter
from .mlb_play import MlbPlay
from .mlb_plays_map import MlbPlaysMap
from .mlb_position_group import MlbPositionGroup
from .mlb_roster import MlbRoster
from .mlb_roster_athlete import MlbRosterAthlete
from .mlb_roster_athlete_alternate_ids import MlbRosterAthleteAlternateIds
from .mlb_roster_athlete_bats import MlbRosterAthleteBats
from .mlb_roster_athlete_bats_abbreviation import MlbRosterAthleteBatsAbbreviation
from .mlb_roster_athlete_bats_display_value import MlbRosterAthleteBatsDisplayValue
from .mlb_roster_athlete_bats_type import MlbRosterAthleteBatsType
from .mlb_roster_athlete_birth_place import MlbRosterAthleteBirthPlace
from .mlb_roster_athlete_college import MlbRosterAthleteCollege
from .mlb_roster_athlete_contracts_item import MlbRosterAthleteContractsItem
from .mlb_roster_athlete_contracts_item_season import MlbRosterAthleteContractsItemSeason
from .mlb_roster_athlete_experience import MlbRosterAthleteExperience
from .mlb_roster_athlete_headshot import MlbRosterAthleteHeadshot
from .mlb_roster_athlete_injuries_item import MlbRosterAthleteInjuriesItem
from .mlb_roster_athlete_position import MlbRosterAthletePosition
from .mlb_roster_athlete_position_parent import MlbRosterAthletePositionParent
from .mlb_roster_athlete_positions_item import MlbRosterAthletePositionsItem
from .mlb_roster_athlete_positions_item_parent import MlbRosterAthletePositionsItemParent
from .mlb_roster_athlete_status import MlbRosterAthleteStatus
from .mlb_roster_athlete_teams_item import MlbRosterAthleteTeamsItem
from .mlb_roster_athlete_throws import MlbRosterAthleteThrows
from .mlb_roster_athlete_throws_abbreviation import MlbRosterAthleteThrowsAbbreviation
from .mlb_roster_athlete_throws_display_value import MlbRosterAthleteThrowsDisplayValue
from .mlb_roster_athlete_throws_type import MlbRosterAthleteThrowsType
from .mlb_scoreboard_response import MlbScoreboardResponse
from .mlb_scoreboard_response_day import MlbScoreboardResponseDay
from .mlb_season_series import MlbSeasonSeries
from .mlb_standings import MlbStandings
from .mlb_statistic_name import MlbStatisticName
from .mlb_team_abbreviation import MLBTeamAbbreviation
from .mlb_team_roster_response import MlbTeamRosterResponse
from .mlb_team_roster_response_season import MlbTeamRosterResponseSeason
from .mlb_team_roster_response_team import MlbTeamRosterResponseTeam
from .mlb_win_probability import MlbWinProbability
from .monday_night_football_response import MondayNightFootballResponse
from .nba_game_summary_response import NbaGameSummaryResponse
from .nba_game_summary_response_against_the_spread_item import NbaGameSummaryResponseAgainstTheSpreadItem
from .nba_game_summary_response_article import NbaGameSummaryResponseArticle
from .nba_game_summary_response_boxscore import NbaGameSummaryResponseBoxscore
from .nba_game_summary_response_broadcasts_item import NbaGameSummaryResponseBroadcastsItem
from .nba_game_summary_response_format import NbaGameSummaryResponseFormat
from .nba_game_summary_response_game_info import NbaGameSummaryResponseGameInfo
from .nba_game_summary_response_header import NbaGameSummaryResponseHeader
from .nba_game_summary_response_injuries_item import NbaGameSummaryResponseInjuriesItem
from .nba_game_summary_response_last_five_games_item import NbaGameSummaryResponseLastFiveGamesItem
from .nba_game_summary_response_leaders_item import NbaGameSummaryResponseLeadersItem
from .nba_game_summary_response_news import NbaGameSummaryResponseNews
from .nba_game_summary_response_odds_item import NbaGameSummaryResponseOddsItem
from .nba_game_summary_response_pickcenter_item import NbaGameSummaryResponsePickcenterItem
from .nba_game_summary_response_predictor import NbaGameSummaryResponsePredictor
from .nba_game_summary_response_seasonseries import NbaGameSummaryResponseSeasonseries
from .nba_game_summary_response_standings import NbaGameSummaryResponseStandings
from .nba_game_summary_response_tickets_info import NbaGameSummaryResponseTicketsInfo
from .nba_game_summary_response_videos_item import NbaGameSummaryResponseVideosItem
from .nba_game_summary_response_win_probability_item import NbaGameSummaryResponseWinProbabilityItem
from .nba_scoreboard_response import NbaScoreboardResponse
from .nba_scoreboard_response_day import NbaScoreboardResponseDay
from .nba_statistic_name import NbaStatisticName
from .nba_team_abbreviation import NBATeamAbbreviation
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
from .nfl_statistic_name import NflStatisticName
from .nfl_team_abbreviation import NFLTeamAbbreviation
from .nfl_team_schedule_response import NFLTeamScheduleResponse
from .nhl_athlete import NhlAthlete
from .nhl_athlete_catches import NhlAthleteCatches
from .nhl_athlete_catches_abbreviation import NhlAthleteCatchesAbbreviation
from .nhl_athlete_catches_display_value import NhlAthleteCatchesDisplayValue
from .nhl_athlete_catches_type import NhlAthleteCatchesType
from .nhl_athlete_college import NhlAthleteCollege
from .nhl_athlete_contracts_item import NhlAthleteContractsItem
from .nhl_athlete_contracts_item_season import NhlAthleteContractsItemSeason
from .nhl_athlete_experience import NhlAthleteExperience
from .nhl_athlete_injuries_item import NhlAthleteInjuriesItem
from .nhl_athlete_position import NhlAthletePosition
from .nhl_athlete_position_parent import NhlAthletePositionParent
from .nhl_athlete_positions_item import NhlAthletePositionsItem
from .nhl_athlete_positions_item_parent import NhlAthletePositionsItemParent
from .nhl_athlete_shoots import NhlAthleteShoots
from .nhl_athlete_shoots_abbreviation import NhlAthleteShootsAbbreviation
from .nhl_athlete_shoots_display_value import NhlAthleteShootsDisplayValue
from .nhl_athlete_shoots_type import NhlAthleteShootsType
from .nhl_athlete_status import NhlAthleteStatus
from .nhl_athlete_teams_item import NhlAthleteTeamsItem
from .nhl_coach import NhlCoach
from .nhl_game_summary_response import NhlGameSummaryResponse
from .nhl_game_summary_response_boxscore import NhlGameSummaryResponseBoxscore
from .nhl_game_summary_response_game_info import NhlGameSummaryResponseGameInfo
from .nhl_game_summary_response_header import NhlGameSummaryResponseHeader
from .nhl_game_summary_response_plays_item import NhlGameSummaryResponsePlaysItem
from .nhl_game_summary_response_standings import NhlGameSummaryResponseStandings
from .nhl_game_summary_response_win_probability_item import NhlGameSummaryResponseWinProbabilityItem
from .nhl_position_group import NhlPositionGroup
from .nhl_position_group_position import NhlPositionGroupPosition
from .nhl_scoreboard_response import NhlScoreboardResponse
from .nhl_statistic_name import NhlStatisticName
from .nhl_team_abbreviation import NHLTeamAbbreviation
from .nhl_team_roster_response import NhlTeamRosterResponse
from .official import Official
from .play import Play
from .play_clock import PlayClock
from .play_period import PlayPeriod
from .play_type import PlayType
from .player_stats import PlayerStats
from .player_stats_stats import PlayerStatsStats
from .position import Position
from .position_group import PositionGroup
from .position_group_position import PositionGroupPosition
from .position_name import PositionName
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
from .sport_enum import SportEnum
from .sport_league import SportLeague
from .sport_league_season import SportLeagueSeason
from .sport_news_api_schema import SportNewsAPISchema
from .standing_entry import StandingEntry
from .standing_group import StandingGroup
from .statistic import Statistic
from .statistic_entry import StatisticEntry
from .statistic_entry_name import StatisticEntryName
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
from .wnba_team_abbreviation import WNBATeamAbbreviation

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
    "GenericScoreboardResponse",
    "GenericScoreboardResponseDay",
    "GeoBroadcast",
    "GeoBroadcastMarket",
    "GeoBroadcastMedia",
    "GeoBroadcastType",
    "GetMLBTeamDetailsTeamIdOrAbbrev",
    "GetMLBTeamRosterTeamIdOrAbbrev",
    "GetScoreboardSeasontype",
    "GetScoreboardSport",
    "Headline",
    "Headshot",
    "Image",
    "Injury",
    "Leader",
    "LeaderCategory",
    "LeaderEntry",
    "LeaderPerformance",
    "League",
    "LeagueEnum",
    "LeagueLinks",
    "LeagueSeason",
    "Linescore",
    "Link",
    "Logo",
    "MlbAgainstTheSpread",
    "MlbArticle",
    "MlbBoxscore",
    "MlbBroadcast",
    "MlbCoach",
    "MlbFormat",
    "MlbGameInfo",
    "MlbGameSummaryResponse",
    "MlbGameSummaryResponseAtBats",
    "MlbGameSummaryResponsePlaysMap",
    "MlbHeader",
    "MlbInjury",
    "MlbMeta",
    "MlbNews",
    "MlbPickcenter",
    "MlbPlay",
    "MlbPlaysMap",
    "MlbPositionGroup",
    "MlbRoster",
    "MlbRosterAthlete",
    "MlbRosterAthleteAlternateIds",
    "MlbRosterAthleteBats",
    "MlbRosterAthleteBatsAbbreviation",
    "MlbRosterAthleteBatsDisplayValue",
    "MlbRosterAthleteBatsType",
    "MlbRosterAthleteBirthPlace",
    "MlbRosterAthleteCollege",
    "MlbRosterAthleteContractsItem",
    "MlbRosterAthleteContractsItemSeason",
    "MlbRosterAthleteExperience",
    "MlbRosterAthleteHeadshot",
    "MlbRosterAthleteInjuriesItem",
    "MlbRosterAthletePosition",
    "MlbRosterAthletePositionParent",
    "MlbRosterAthletePositionsItem",
    "MlbRosterAthletePositionsItemParent",
    "MlbRosterAthleteStatus",
    "MlbRosterAthleteTeamsItem",
    "MlbRosterAthleteThrows",
    "MlbRosterAthleteThrowsAbbreviation",
    "MlbRosterAthleteThrowsDisplayValue",
    "MlbRosterAthleteThrowsType",
    "MlbScoreboardResponse",
    "MlbScoreboardResponseDay",
    "MlbSeasonSeries",
    "MlbStandings",
    "MlbStatisticName",
    "MLBTeamAbbreviation",
    "MlbTeamRosterResponse",
    "MlbTeamRosterResponseSeason",
    "MlbTeamRosterResponseTeam",
    "MlbWinProbability",
    "MondayNightFootballResponse",
    "NbaGameSummaryResponse",
    "NbaGameSummaryResponseAgainstTheSpreadItem",
    "NbaGameSummaryResponseArticle",
    "NbaGameSummaryResponseBoxscore",
    "NbaGameSummaryResponseBroadcastsItem",
    "NbaGameSummaryResponseFormat",
    "NbaGameSummaryResponseGameInfo",
    "NbaGameSummaryResponseHeader",
    "NbaGameSummaryResponseInjuriesItem",
    "NbaGameSummaryResponseLastFiveGamesItem",
    "NbaGameSummaryResponseLeadersItem",
    "NbaGameSummaryResponseNews",
    "NbaGameSummaryResponseOddsItem",
    "NbaGameSummaryResponsePickcenterItem",
    "NbaGameSummaryResponsePredictor",
    "NbaGameSummaryResponseSeasonseries",
    "NbaGameSummaryResponseStandings",
    "NbaGameSummaryResponseTicketsInfo",
    "NbaGameSummaryResponseVideosItem",
    "NbaGameSummaryResponseWinProbabilityItem",
    "NbaScoreboardResponse",
    "NbaScoreboardResponseDay",
    "NbaStatisticName",
    "NBATeamAbbreviation",
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
    "NflStatisticName",
    "NFLTeamAbbreviation",
    "NFLTeamScheduleResponse",
    "NhlAthlete",
    "NhlAthleteCatches",
    "NhlAthleteCatchesAbbreviation",
    "NhlAthleteCatchesDisplayValue",
    "NhlAthleteCatchesType",
    "NhlAthleteCollege",
    "NhlAthleteContractsItem",
    "NhlAthleteContractsItemSeason",
    "NhlAthleteExperience",
    "NhlAthleteInjuriesItem",
    "NhlAthletePosition",
    "NhlAthletePositionParent",
    "NhlAthletePositionsItem",
    "NhlAthletePositionsItemParent",
    "NhlAthleteShoots",
    "NhlAthleteShootsAbbreviation",
    "NhlAthleteShootsDisplayValue",
    "NhlAthleteShootsType",
    "NhlAthleteStatus",
    "NhlAthleteTeamsItem",
    "NhlCoach",
    "NhlGameSummaryResponse",
    "NhlGameSummaryResponseBoxscore",
    "NhlGameSummaryResponseGameInfo",
    "NhlGameSummaryResponseHeader",
    "NhlGameSummaryResponsePlaysItem",
    "NhlGameSummaryResponseStandings",
    "NhlGameSummaryResponseWinProbabilityItem",
    "NhlPositionGroup",
    "NhlPositionGroupPosition",
    "NhlScoreboardResponse",
    "NhlStatisticName",
    "NHLTeamAbbreviation",
    "NhlTeamRosterResponse",
    "Official",
    "Play",
    "PlayClock",
    "PlayerStats",
    "PlayerStatsStats",
    "PlayPeriod",
    "PlayType",
    "Position",
    "PositionGroup",
    "PositionGroupPosition",
    "PositionName",
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
    "SportEnum",
    "SportLeague",
    "SportLeagueSeason",
    "SportNewsAPISchema",
    "StandingEntry",
    "StandingGroup",
    "Statistic",
    "StatisticEntry",
    "StatisticEntryName",
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
    "WNBATeamAbbreviation",
)
