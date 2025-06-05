from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference import Reference


T = TypeVar("T", bound="AthleteEventlogResponseEventsItemsItem")


@_attrs_define
class AthleteEventlogResponseEventsItemsItem:
    """
    Attributes:
        played (bool):
        event (Union[Unset, Reference]):
        competition (Union[Unset, Reference]):
        competitor (Union[Unset, Reference]):
        statistics (Union[Unset, Reference]):
        team_id (Union[Unset, str]):
        league (Union[Unset, str]): League identifier (e.g., 'pga', 'eur' for golf)
    """

    played: bool
    event: Union[Unset, "Reference"] = UNSET
    competition: Union[Unset, "Reference"] = UNSET
    competitor: Union[Unset, "Reference"] = UNSET
    statistics: Union[Unset, "Reference"] = UNSET
    team_id: Union[Unset, str] = UNSET
    league: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        played = self.played

        event: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()

        competition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.competition, Unset):
            competition = self.competition.to_dict()

        competitor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.competitor, Unset):
            competitor = self.competitor.to_dict()

        statistics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        team_id = self.team_id

        league = self.league

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "played": played,
            }
        )
        if event is not UNSET:
            field_dict["event"] = event
        if competition is not UNSET:
            field_dict["competition"] = competition
        if competitor is not UNSET:
            field_dict["competitor"] = competitor
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if league is not UNSET:
            field_dict["league"] = league

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference

        d = src_dict.copy()
        played = d.pop("played")

        _event = d.pop("event", UNSET)
        event: Union[Unset, Reference]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = Reference.from_dict(_event)

        _competition = d.pop("competition", UNSET)
        competition: Union[Unset, Reference]
        if isinstance(_competition, Unset):
            competition = UNSET
        else:
            competition = Reference.from_dict(_competition)

        _competitor = d.pop("competitor", UNSET)
        competitor: Union[Unset, Reference]
        if isinstance(_competitor, Unset):
            competitor = UNSET
        else:
            competitor = Reference.from_dict(_competitor)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, Reference]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = Reference.from_dict(_statistics)

        team_id = d.pop("teamId", UNSET)

        league = d.pop("league", UNSET)

        athlete_eventlog_response_events_items_item = cls(
            played=played,
            event=event,
            competition=competition,
            competitor=competitor,
            statistics=statistics,
            team_id=team_id,
            league=league,
        )

        athlete_eventlog_response_events_items_item.additional_properties = d
        return athlete_eventlog_response_events_items_item

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
