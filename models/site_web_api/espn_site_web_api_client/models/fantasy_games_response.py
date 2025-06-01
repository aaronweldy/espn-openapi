from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.fantasy_game_event import FantasyGameEvent
    from ..models.fantasy_statistic import FantasyStatistic


T = TypeVar("T", bound="FantasyGamesResponse")


@_attrs_define
class FantasyGamesResponse:
    """
    Attributes:
        events (List['FantasyGameEvent']):
        statistics (List['FantasyStatistic']):
    """

    events: List["FantasyGameEvent"]
    statistics: List["FantasyStatistic"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        statistics = []
        for statistics_item_data in self.statistics:
            statistics_item = statistics_item_data.to_dict()
            statistics.append(statistics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
                "statistics": statistics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_game_event import FantasyGameEvent
        from ..models.fantasy_statistic import FantasyStatistic

        d = src_dict.copy()
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = FantasyGameEvent.from_dict(events_item_data)

            events.append(events_item)

        statistics = []
        _statistics = d.pop("statistics")
        for statistics_item_data in _statistics:
            statistics_item = FantasyStatistic.from_dict(statistics_item_data)

            statistics.append(statistics_item)

        fantasy_games_response = cls(
            events=events,
            statistics=statistics,
        )

        fantasy_games_response.additional_properties = d
        return fantasy_games_response

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
