"""Contains all the data models used in inputs/outputs"""

from .alternate_ids import AlternateIds
from .athlete import Athlete
from .athletes_list_response import AthletesListResponse
from .draft import Draft
from .error_response import ErrorResponse
from .error_response_error import ErrorResponseError
from .injury import Injury
from .injury_details import InjuryDetails
from .injury_type import InjuryType
from .league_enum import LeagueEnum
from .position import Position
from .sport_enum import SportEnum
from .status import Status
from .team import Team

__all__ = (
    "AlternateIds",
    "Athlete",
    "AthletesListResponse",
    "Draft",
    "ErrorResponse",
    "ErrorResponseError",
    "Injury",
    "InjuryDetails",
    "InjuryType",
    "LeagueEnum",
    "Position",
    "SportEnum",
    "Status",
    "Team",
)
