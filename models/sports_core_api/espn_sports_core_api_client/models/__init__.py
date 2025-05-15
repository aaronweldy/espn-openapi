"""Contains all the data models used in inputs/outputs"""

from .athlete_details_response import AthleteDetailsResponse
from .athlete_details_response_alternate_ids import AthleteDetailsResponseAlternateIds
from .athlete_details_response_experience import AthleteDetailsResponseExperience
from .athlete_reference import AthleteReference
from .athlete_statistics_log_response import AthleteStatisticsLogResponse
from .athlete_statistics_response import AthleteStatisticsResponse
from .athlete_statistics_response_splits import AthleteStatisticsResponseSplits
from .athlete_status import AthleteStatus
from .calendar_list_response import CalendarListResponse
from .error_response import ErrorResponse
from .error_response_error import ErrorResponseError
from .event_detail import EventDetail
from .event_detail_competitions_item_type_1 import EventDetailCompetitionsItemType1
from .event_detail_league_type_1 import EventDetailLeagueType1
from .event_detail_season_type_1 import EventDetailSeasonType1
from .event_detail_season_type_type_1 import EventDetailSeasonTypeType1
from .event_detail_venues_item_type_1 import EventDetailVenuesItemType1
from .event_detail_week_type_1 import EventDetailWeekType1
from .event_reference import EventReference
from .get_league_season_weeks_season_type import GetLeagueSeasonWeeksSeasonType
from .link import Link
from .paginated_reference_list_response import PaginatedReferenceListResponse
from .position import Position
from .reference import Reference
from .season import Season
from .statistic import Statistic
from .statistic_category import StatisticCategory
from .statistics_log_entry import StatisticsLogEntry
from .statistics_reference import StatisticsReference
from .statistics_type_entry import StatisticsTypeEntry
from .team import Team
from .team_reference import TeamReference

__all__ = (
    "AthleteDetailsResponse",
    "AthleteDetailsResponseAlternateIds",
    "AthleteDetailsResponseExperience",
    "AthleteReference",
    "AthleteStatisticsLogResponse",
    "AthleteStatisticsResponse",
    "AthleteStatisticsResponseSplits",
    "AthleteStatus",
    "CalendarListResponse",
    "ErrorResponse",
    "ErrorResponseError",
    "EventDetail",
    "EventDetailCompetitionsItemType1",
    "EventDetailLeagueType1",
    "EventDetailSeasonType1",
    "EventDetailSeasonTypeType1",
    "EventDetailVenuesItemType1",
    "EventDetailWeekType1",
    "EventReference",
    "GetLeagueSeasonWeeksSeasonType",
    "Link",
    "PaginatedReferenceListResponse",
    "Position",
    "Reference",
    "Season",
    "Statistic",
    "StatisticCategory",
    "StatisticsLogEntry",
    "StatisticsReference",
    "StatisticsTypeEntry",
    "Team",
    "TeamReference",
)
