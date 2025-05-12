"""Contains all the data models used in inputs/outputs"""

from .address import Address
from .article import Article
from .article_image import ArticleImage
from .article_links import ArticleLinks
from .article_links_app import ArticleLinksApp
from .athlete import Athlete
from .boxscore import Boxscore
from .boxscore_player import BoxscorePlayer
from .boxscore_team import BoxscoreTeam
from .broadcast import Broadcast
from .calendar_entry import CalendarEntry
from .calendar_item import CalendarItem
from .category import Category
from .category_athlete import CategoryAthlete
from .category_athlete_links import CategoryAthleteLinks
from .category_athlete_links_mobile import CategoryAthleteLinksMobile
from .category_athlete_links_web import CategoryAthleteLinksWeb
from .category_contributor import CategoryContributor
from .category_contributor_links import CategoryContributorLinks
from .category_contributor_links_mobile import CategoryContributorLinksMobile
from .category_contributor_links_web import CategoryContributorLinksWeb
from .category_league import CategoryLeague
from .category_league_links import CategoryLeagueLinks
from .category_league_links_mobile import CategoryLeagueLinksMobile
from .category_league_links_web import CategoryLeagueLinksWeb
from .category_team import CategoryTeam
from .category_team_links import CategoryTeamLinks
from .category_team_links_mobile import CategoryTeamLinksMobile
from .category_team_links_web import CategoryTeamLinksWeb
from .college import College
from .competition import Competition
from .competition_leader import CompetitionLeader
from .competition_type import CompetitionType
from .competitor import Competitor
from .competitor_home_away import CompetitorHomeAway
from .conference import Conference
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
from .league_season import LeagueSeason
from .linescore import Linescore
from .link import Link
from .logo import Logo
from .news_response import NewsResponse
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
from .standing_entry import StandingEntry
from .standing_group import StandingGroup
from .standings_response import StandingsResponse
from .statistic import Statistic
from .statistic_entry import StatisticEntry
from .status_type import StatusType
from .status_type_state import StatusTypeState
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
from .venue import Venue
from .venue_image import VenueImage
from .weather import Weather
from .week_info import WeekInfo

__all__ = (
    "Address",
    "Article",
    "ArticleImage",
    "ArticleLinks",
    "ArticleLinksApp",
    "Athlete",
    "Boxscore",
    "BoxscorePlayer",
    "BoxscoreTeam",
    "Broadcast",
    "CalendarEntry",
    "CalendarItem",
    "Category",
    "CategoryAthlete",
    "CategoryAthleteLinks",
    "CategoryAthleteLinksMobile",
    "CategoryAthleteLinksWeb",
    "CategoryContributor",
    "CategoryContributorLinks",
    "CategoryContributorLinksMobile",
    "CategoryContributorLinksWeb",
    "CategoryLeague",
    "CategoryLeagueLinks",
    "CategoryLeagueLinksMobile",
    "CategoryLeagueLinksWeb",
    "CategoryTeam",
    "CategoryTeamLinks",
    "CategoryTeamLinksMobile",
    "CategoryTeamLinksWeb",
    "College",
    "Competition",
    "CompetitionLeader",
    "CompetitionType",
    "Competitor",
    "CompetitorHomeAway",
    "Conference",
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
    "LeagueSeason",
    "Linescore",
    "Link",
    "Logo",
    "NewsResponse",
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
    "StandingEntry",
    "StandingGroup",
    "StandingsResponse",
    "Statistic",
    "StatisticEntry",
    "StatusType",
    "StatusTypeState",
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
    "Venue",
    "VenueImage",
    "Weather",
    "WeekInfo",
)
