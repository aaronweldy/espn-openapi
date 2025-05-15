"""Contains all the data models used in inputs/outputs"""

from .athlete_details import AthleteDetails
from .athlete_details_alternate_ids import AthleteDetailsAlternateIds
from .athlete_details_college import AthleteDetailsCollege
from .athlete_game_log_response import AthleteGameLogResponse
from .athlete_overview_response import AthleteOverviewResponse
from .athlete_reference import AthleteReference
from .athlete_status import AthleteStatus
from .author import Author
from .author_links_type_0 import AuthorLinksType0
from .birth_place import BirthPlace
from .career_statistics import CareerStatistics
from .career_statistics_categories_item import CareerStatisticsCategoriesItem
from .career_statistics_splits_item import CareerStatisticsSplitsItem
from .category_label import CategoryLabel
from .college import College
from .draft import Draft
from .error import Error
from .error_response import ErrorResponse
from .event_status import EventStatus
from .event_status_state import EventStatusState
from .experience import Experience
from .flag_type_0 import FlagType0
from .game_log_category import GameLogCategory
from .game_log_event import GameLogEvent
from .game_log_event_home_away import GameLogEventHomeAway
from .get_general_search_mode import GetGeneralSearchMode
from .get_nfl_athlete_game_log_seasontype import GetNFLAthleteGameLogSeasontype
from .hand_type_0 import HandType0
from .headshot import Headshot
from .href_link import HrefLink
from .image import Image
from .image_link import ImageLink
from .image_link_with_size import ImageLinkWithSize
from .injury import Injury
from .injury_type import InjuryType
from .league_reference import LeagueReference
from .link import Link
from .logo import Logo
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
from .scoreboard_event import ScoreboardEvent
from .scoreboard_header_response import ScoreboardHeaderResponse
from .search_metadata import SearchMetadata
from .search_response import SearchResponse
from .search_result import SearchResult
from .season import Season
from .self_link import SelfLink
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
    "AthleteOverviewResponse",
    "AthleteReference",
    "AthleteStatus",
    "Author",
    "AuthorLinksType0",
    "BirthPlace",
    "CareerStatistics",
    "CareerStatisticsCategoriesItem",
    "CareerStatisticsSplitsItem",
    "CategoryLabel",
    "College",
    "Draft",
    "Error",
    "ErrorResponse",
    "EventStatus",
    "EventStatusState",
    "Experience",
    "FlagType0",
    "GameLogCategory",
    "GameLogEvent",
    "GameLogEventHomeAway",
    "GetGeneralSearchMode",
    "GetNFLAthleteGameLogSeasontype",
    "HandType0",
    "Headshot",
    "HrefLink",
    "Image",
    "ImageLink",
    "ImageLinkWithSize",
    "Injury",
    "InjuryType",
    "LeagueReference",
    "Link",
    "Logo",
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
    "ScoreboardEvent",
    "ScoreboardHeaderResponse",
    "SearchMetadata",
    "SearchResponse",
    "SearchResult",
    "Season",
    "SelfLink",
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
