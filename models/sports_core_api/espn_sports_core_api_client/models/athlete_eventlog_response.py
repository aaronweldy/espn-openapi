from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.athlete_eventlog_response_events import AthleteEventlogResponseEvents
    from ..models.athlete_eventlog_response_leagues import AthleteEventlogResponseLeagues
    from ..models.athlete_eventlog_response_teams import AthleteEventlogResponseTeams


T = TypeVar("T", bound="AthleteEventlogResponse")


@_attrs_define
class AthleteEventlogResponse:
    """
    Attributes:
        ref (Union[Unset, str]):
        leagues (Union[Unset, AthleteEventlogResponseLeagues]):
        teams (Union[Unset, AthleteEventlogResponseTeams]):
        events (Union[Unset, AthleteEventlogResponseEvents]):
    """

    ref: Union[Unset, str] = UNSET
    leagues: Union[Unset, "AthleteEventlogResponseLeagues"] = UNSET
    teams: Union[Unset, "AthleteEventlogResponseTeams"] = UNSET
    events: Union[Unset, "AthleteEventlogResponseEvents"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        leagues: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.leagues, Unset):
            leagues = self.leagues.to_dict()

        teams: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = self.teams.to_dict()

        events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ref is not UNSET:
            field_dict["$ref"] = ref
        if leagues is not UNSET:
            field_dict["leagues"] = leagues
        if teams is not UNSET:
            field_dict["teams"] = teams
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_eventlog_response_events import AthleteEventlogResponseEvents
        from ..models.athlete_eventlog_response_leagues import AthleteEventlogResponseLeagues
        from ..models.athlete_eventlog_response_teams import AthleteEventlogResponseTeams

        d = src_dict.copy()
        ref = d.pop("$ref", UNSET)

        _leagues = d.pop("leagues", UNSET)
        leagues: Union[Unset, AthleteEventlogResponseLeagues]
        if isinstance(_leagues, Unset):
            leagues = UNSET
        else:
            leagues = AthleteEventlogResponseLeagues.from_dict(_leagues)

        _teams = d.pop("teams", UNSET)
        teams: Union[Unset, AthleteEventlogResponseTeams]
        if isinstance(_teams, Unset):
            teams = UNSET
        else:
            teams = AthleteEventlogResponseTeams.from_dict(_teams)

        _events = d.pop("events", UNSET)
        events: Union[Unset, AthleteEventlogResponseEvents]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = AthleteEventlogResponseEvents.from_dict(_events)

        athlete_eventlog_response = cls(
            ref=ref,
            leagues=leagues,
            teams=teams,
            events=events,
        )

        athlete_eventlog_response.additional_properties = d
        return athlete_eventlog_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
