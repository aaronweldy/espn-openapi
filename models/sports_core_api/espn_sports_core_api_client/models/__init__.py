"""Contains all the data models used in inputs/outputs"""

from .athlete_details_response import AthleteDetailsResponse
from .athlete_details_response_alternate_ids import AthleteDetailsResponseAlternateIds
from .athlete_details_response_experience import AthleteDetailsResponseExperience
from .athlete_reference import AthleteReference
from .athlete_statistics_log_response import AthleteStatisticsLogResponse
from .athlete_statistics_response import AthleteStatisticsResponse
from .athlete_statistics_response_splits import AthleteStatisticsResponseSplits
from .athlete_status import AthleteStatus
from .error_response import ErrorResponse
from .error_response_error import ErrorResponseError
from .event_reference import EventReference
from .link import Link
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
    "ErrorResponse",
    "ErrorResponseError",
    "EventReference",
    "Link",
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
