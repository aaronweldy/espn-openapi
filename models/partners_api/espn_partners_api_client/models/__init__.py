"""Contains all the data models used in inputs/outputs"""

from .alternate_ids import AlternateIds
from .athlete import Athlete
from .athletes_list_response import AthletesListResponse
from .competition import Competition
from .competitor import Competitor
from .competitor_home_away import CompetitorHomeAway
from .draft import Draft
from .error_response import ErrorResponse
from .error_response_error import ErrorResponseError
from .event import Event
from .event_format import EventFormat
from .event_note import EventNote
from .event_status import EventStatus
from .event_status_type import EventStatusType
from .event_status_type_state import EventStatusTypeState
from .event_team import EventTeam
from .event_time import EventTime
from .events_list_response import EventsListResponse
from .injury import Injury
from .injury_details import InjuryDetails
from .injury_type import InjuryType
from .league_enum import LeagueEnum
from .period_format import PeriodFormat
from .position import Position
from .record import Record
from .score import Score
from .sport_enum import SportEnum
from .status import Status
from .team import Team

__all__ = (
    "AlternateIds",
    "Athlete",
    "AthletesListResponse",
    "Competition",
    "Competitor",
    "CompetitorHomeAway",
    "Draft",
    "ErrorResponse",
    "ErrorResponseError",
    "Event",
    "EventFormat",
    "EventNote",
    "EventsListResponse",
    "EventStatus",
    "EventStatusType",
    "EventStatusTypeState",
    "EventTeam",
    "EventTime",
    "Injury",
    "InjuryDetails",
    "InjuryType",
    "LeagueEnum",
    "PeriodFormat",
    "Position",
    "Record",
    "Score",
    "SportEnum",
    "Status",
    "Team",
)
