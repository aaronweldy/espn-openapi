"""Contains all the data models used in inputs/outputs"""

from .athlete_details import AthleteDetails
from .athlete_details_alternate_ids import AthleteDetailsAlternateIds
from .athlete_details_college import AthleteDetailsCollege
from .athlete_game_log_response import AthleteGameLogResponse
from .athlete_game_log_response_events import AthleteGameLogResponseEvents
from .athlete_overview_response import AthleteOverviewResponse
from .athlete_profile_response import AthleteProfileResponse
from .athlete_profile_response_athlete import AthleteProfileResponseAthlete
from .athlete_profile_response_athlete_college import AthleteProfileResponseAthleteCollege
from .athlete_reference import AthleteReference
from .athlete_splits_category import AthleteSplitsCategory
from .athlete_splits_filter import AthleteSplitsFilter
from .athlete_splits_option import AthleteSplitsOption
from .athlete_splits_response import AthleteSplitsResponse
from .athlete_splits_split import AthleteSplitsSplit
from .athlete_splits_split_category import AthleteSplitsSplitCategory
from .athlete_status import AthleteStatus
from .author import Author
from .author_links_type_0 import AuthorLinksType0
from .birth_place import BirthPlace
from .career_statistics import CareerStatistics
from .career_statistics_categories_item import CareerStatisticsCategoriesItem
from .career_statistics_splits_item import CareerStatisticsSplitsItem
from .college import College
from .draft import Draft
from .error import Error
from .error_response import ErrorResponse
from .event_status import EventStatus
from .event_status_state import EventStatusState
from .experience import Experience
from .flag_type_0 import FlagType0
from .game_event import GameEvent
from .game_event_at_vs import GameEventAtVs
from .game_event_game_result import GameEventGameResult
from .game_event_team import GameEventTeam
from .game_log_season import GameLogSeason
from .get_general_search_mode import GetGeneralSearchMode
from .get_league_leaders_sport import GetLeagueLeadersSport
from .get_nfl_athlete_game_log_seasontype import GetNFLAthleteGameLogSeasontype
from .hand_type_0 import HandType0
from .headshot import Headshot
from .href_link import HrefLink
from .image import Image
from .image_link import ImageLink
from .image_link_with_size import ImageLinkWithSize
from .injury import Injury
from .injury_type import InjuryType
from .leader_athlete import LeaderAthlete
from .leader_category import LeaderCategory
from .leader_entry import LeaderEntry
from .leader_entry_statistics import LeaderEntryStatistics
from .leader_team import LeaderTeam
from .leaders_container import LeadersContainer
from .leaders_league import LeadersLeague
from .leaders_response import LeadersResponse
from .leaders_season import LeadersSeason
from .leaders_season_type import LeadersSeasonType
from .leaders_season_type_week import LeadersSeasonTypeWeek
from .league_enum import LeagueEnum
from .league_reference import LeagueReference
from .link import Link
from .logo import Logo
from .mlb_athlete_details_athlete import MLBAthleteDetailsAthlete
from .mlb_athlete_details_athlete_college import MLBAthleteDetailsAthleteCollege
from .mlb_athlete_details_athlete_headshot import MLBAthleteDetailsAthleteHeadshot
from .mlb_athlete_details_athlete_position import MLBAthleteDetailsAthletePosition
from .mlb_athlete_details_athlete_stats_summary import MLBAthleteDetailsAthleteStatsSummary
from .mlb_athlete_details_athlete_status import MLBAthleteDetailsAthleteStatus
from .mlb_athlete_details_athlete_team import MLBAthleteDetailsAthleteTeam
from .mlb_athlete_details_response import MLBAthleteDetailsResponse
from .mlb_athlete_details_response_league import MLBAthleteDetailsResponseLeague
from .mlb_athlete_details_response_player_switcher import MLBAthleteDetailsResponsePlayerSwitcher
from .mlb_athlete_details_response_quicklinks_item import MLBAthleteDetailsResponseQuicklinksItem
from .mlb_athlete_details_response_season import MLBAthleteDetailsResponseSeason
from .mlb_athlete_details_response_standings import MLBAthleteDetailsResponseStandings
from .mlb_athlete_details_response_tickets_info import MLBAthleteDetailsResponseTicketsInfo
from .mlb_statistic_name import MlbStatisticName
from .navigation_item import NavigationItem
from .news_category import NewsCategory
from .news_category_athlete import NewsCategoryAthlete
from .news_category_athlete_links import NewsCategoryAthleteLinks
from .news_category_league import NewsCategoryLeague
from .news_category_league_links import NewsCategoryLeagueLinks
from .news_category_team import NewsCategoryTeam
from .news_category_team_links import NewsCategoryTeamLinks
from .news_item_detailed import NewsItemDetailed
from .news_links import NewsLinks
from .note import Note
from .position import Position
from .reference import Reference
from .requested_season import RequestedSeason
from .scoreboard_event import ScoreboardEvent
from .scoreboard_header_response import ScoreboardHeaderResponse
from .scoreboard_header_response_sports_item import ScoreboardHeaderResponseSportsItem
from .scoreboard_header_response_sports_item_leagues_item import ScoreboardHeaderResponseSportsItemLeaguesItem
from .scoreboard_header_response_sports_item_leagues_item_events_item import (
    ScoreboardHeaderResponseSportsItemLeaguesItemEventsItem,
)
from .scoreboard_header_response_sports_item_leagues_item_events_item_app_links_item import (
    ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemAppLinksItem,
)
from .scoreboard_header_response_sports_item_leagues_item_events_item_broadcasts_item import (
    ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemBroadcastsItem,
)
from .scoreboard_header_response_sports_item_leagues_item_events_item_competitors_item import (
    ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemCompetitorsItem,
)
from .scoreboard_header_response_sports_item_leagues_item_events_item_full_status import (
    ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemFullStatus,
)
from .scoreboard_header_response_sports_item_leagues_item_events_item_group import (
    ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemGroup,
)
from .scoreboard_header_response_sports_item_leagues_item_events_item_links_item import (
    ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemLinksItem,
)
from .scoreboard_header_response_sports_item_leagues_item_events_item_odds import (
    ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemOdds,
)
from .scoreboard_header_response_sports_item_leagues_item_smartdates_item import (
    ScoreboardHeaderResponseSportsItemLeaguesItemSmartdatesItem,
)
from .search_metadata import SearchMetadata
from .search_response import SearchResponse
from .search_result import SearchResult
from .search_v2_content_item import SearchV2ContentItem
from .search_v2_content_item_categories_type_0_item import SearchV2ContentItemCategoriesType0Item
from .search_v2_content_item_image_type_0 import SearchV2ContentItemImageType0
from .search_v2_content_item_images_type_0_item import SearchV2ContentItemImagesType0Item
from .search_v2_content_item_link import SearchV2ContentItemLink
from .search_v2_response import SearchV2Response
from .search_v2_result_group import SearchV2ResultGroup
from .search_v2_result_type import SearchV2ResultType
from .season import Season
from .season_info_response import SeasonInfoResponse
from .season_type import SeasonType
from .season_type_info import SeasonTypeInfo
from .self_link import SelfLink
from .sport_enum import SportEnum
from .sport_reference import SportReference
from .stat_category import StatCategory
from .status import Status
from .team import Team
from .team_reference import TeamReference
from .video_ad_details import VideoAdDetails
from .video_device_restrictions import VideoDeviceRestrictions
from .video_geo_restrictions import VideoGeoRestrictions
from .video_item import VideoItem
from .video_links import VideoLinks
from .video_links_api import VideoLinksApi
from .video_links_mobile import VideoLinksMobile
from .video_links_source import VideoLinksSource
from .video_links_source_hls import VideoLinksSourceHLS
from .video_poster_images import VideoPosterImages
from .video_time_restrictions import VideoTimeRestrictions
from .video_tracking_details import VideoTrackingDetails

__all__ = (
    "AthleteDetails",
    "AthleteDetailsAlternateIds",
    "AthleteDetailsCollege",
    "AthleteGameLogResponse",
    "AthleteGameLogResponseEvents",
    "AthleteOverviewResponse",
    "AthleteProfileResponse",
    "AthleteProfileResponseAthlete",
    "AthleteProfileResponseAthleteCollege",
    "AthleteReference",
    "AthleteSplitsCategory",
    "AthleteSplitsFilter",
    "AthleteSplitsOption",
    "AthleteSplitsResponse",
    "AthleteSplitsSplit",
    "AthleteSplitsSplitCategory",
    "AthleteStatus",
    "Author",
    "AuthorLinksType0",
    "BirthPlace",
    "CareerStatistics",
    "CareerStatisticsCategoriesItem",
    "CareerStatisticsSplitsItem",
    "College",
    "Draft",
    "Error",
    "ErrorResponse",
    "EventStatus",
    "EventStatusState",
    "Experience",
    "FlagType0",
    "GameEvent",
    "GameEventAtVs",
    "GameEventGameResult",
    "GameEventTeam",
    "GameLogSeason",
    "GetGeneralSearchMode",
    "GetLeagueLeadersSport",
    "GetNFLAthleteGameLogSeasontype",
    "HandType0",
    "Headshot",
    "HrefLink",
    "Image",
    "ImageLink",
    "ImageLinkWithSize",
    "Injury",
    "InjuryType",
    "LeaderAthlete",
    "LeaderCategory",
    "LeaderEntry",
    "LeaderEntryStatistics",
    "LeadersContainer",
    "LeadersLeague",
    "LeadersResponse",
    "LeadersSeason",
    "LeadersSeasonType",
    "LeadersSeasonTypeWeek",
    "LeaderTeam",
    "LeagueEnum",
    "LeagueReference",
    "Link",
    "Logo",
    "MLBAthleteDetailsAthlete",
    "MLBAthleteDetailsAthleteCollege",
    "MLBAthleteDetailsAthleteHeadshot",
    "MLBAthleteDetailsAthletePosition",
    "MLBAthleteDetailsAthleteStatsSummary",
    "MLBAthleteDetailsAthleteStatus",
    "MLBAthleteDetailsAthleteTeam",
    "MLBAthleteDetailsResponse",
    "MLBAthleteDetailsResponseLeague",
    "MLBAthleteDetailsResponsePlayerSwitcher",
    "MLBAthleteDetailsResponseQuicklinksItem",
    "MLBAthleteDetailsResponseSeason",
    "MLBAthleteDetailsResponseStandings",
    "MLBAthleteDetailsResponseTicketsInfo",
    "MlbStatisticName",
    "NavigationItem",
    "NewsCategory",
    "NewsCategoryAthlete",
    "NewsCategoryAthleteLinks",
    "NewsCategoryLeague",
    "NewsCategoryLeagueLinks",
    "NewsCategoryTeam",
    "NewsCategoryTeamLinks",
    "NewsItemDetailed",
    "NewsLinks",
    "Note",
    "Position",
    "Reference",
    "RequestedSeason",
    "ScoreboardEvent",
    "ScoreboardHeaderResponse",
    "ScoreboardHeaderResponseSportsItem",
    "ScoreboardHeaderResponseSportsItemLeaguesItem",
    "ScoreboardHeaderResponseSportsItemLeaguesItemEventsItem",
    "ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemAppLinksItem",
    "ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemBroadcastsItem",
    "ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemCompetitorsItem",
    "ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemFullStatus",
    "ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemGroup",
    "ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemLinksItem",
    "ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemOdds",
    "ScoreboardHeaderResponseSportsItemLeaguesItemSmartdatesItem",
    "SearchMetadata",
    "SearchResponse",
    "SearchResult",
    "SearchV2ContentItem",
    "SearchV2ContentItemCategoriesType0Item",
    "SearchV2ContentItemImagesType0Item",
    "SearchV2ContentItemImageType0",
    "SearchV2ContentItemLink",
    "SearchV2Response",
    "SearchV2ResultGroup",
    "SearchV2ResultType",
    "Season",
    "SeasonInfoResponse",
    "SeasonType",
    "SeasonTypeInfo",
    "SelfLink",
    "SportEnum",
    "SportReference",
    "StatCategory",
    "Status",
    "Team",
    "TeamReference",
    "VideoAdDetails",
    "VideoDeviceRestrictions",
    "VideoGeoRestrictions",
    "VideoItem",
    "VideoLinks",
    "VideoLinksApi",
    "VideoLinksMobile",
    "VideoLinksSource",
    "VideoLinksSourceHLS",
    "VideoPosterImages",
    "VideoTimeRestrictions",
    "VideoTrackingDetails",
)
