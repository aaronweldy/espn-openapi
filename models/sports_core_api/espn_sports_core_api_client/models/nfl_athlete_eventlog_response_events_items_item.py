from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference import Reference


T = TypeVar("T", bound="NflAthleteEventlogResponseEventsItemsItem")


@_attrs_define
class NflAthleteEventlogResponseEventsItemsItem:
    """
    Attributes:
        event (Reference):
        competition (Reference):
        team_id (str):
        played (bool):
        statistics (Union[Unset, Reference]):
    """

    event: "Reference"
    competition: "Reference"
    team_id: str
    played: bool
    statistics: Union[Unset, "Reference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event = self.event.to_dict()

        competition = self.competition.to_dict()

        team_id = self.team_id

        played = self.played

        statistics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
                "competition": competition,
                "teamId": team_id,
                "played": played,
            }
        )
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference

        d = src_dict.copy()
        event = Reference.from_dict(d.pop("event"))

        competition = Reference.from_dict(d.pop("competition"))

        team_id = d.pop("teamId")

        played = d.pop("played")

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, Reference]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = Reference.from_dict(_statistics)

        nfl_athlete_eventlog_response_events_items_item = cls(
            event=event,
            competition=competition,
            team_id=team_id,
            played=played,
            statistics=statistics,
        )

        nfl_athlete_eventlog_response_events_items_item.additional_properties = d
        return nfl_athlete_eventlog_response_events_items_item

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
