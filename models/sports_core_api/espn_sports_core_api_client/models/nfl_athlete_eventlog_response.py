from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.nfl_athlete_eventlog_events import NflAthleteEventlogEvents
    from ..models.nfl_athlete_eventlog_response_teams import NflAthleteEventlogResponseTeams


T = TypeVar("T", bound="NflAthleteEventlogResponse")


@_attrs_define
class NflAthleteEventlogResponse:
    """
    Attributes:
        ref (str):
        teams (NflAthleteEventlogResponseTeams):
        events (NflAthleteEventlogEvents):
    """

    ref: str
    teams: "NflAthleteEventlogResponseTeams"
    events: "NflAthleteEventlogEvents"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        teams = self.teams.to_dict()

        events = self.events.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "teams": teams,
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_athlete_eventlog_events import NflAthleteEventlogEvents
        from ..models.nfl_athlete_eventlog_response_teams import NflAthleteEventlogResponseTeams

        d = src_dict.copy()
        ref = d.pop("$ref")

        teams = NflAthleteEventlogResponseTeams.from_dict(d.pop("teams"))

        events = NflAthleteEventlogEvents.from_dict(d.pop("events"))

        nfl_athlete_eventlog_response = cls(
            ref=ref,
            teams=teams,
            events=events,
        )

        nfl_athlete_eventlog_response.additional_properties = d
        return nfl_athlete_eventlog_response

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
