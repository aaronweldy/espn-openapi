from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.event import Event
    from ..models.league import League
    from ..models.season_info import SeasonInfo


T = TypeVar("T", bound="SundayNightFootballResponse")


@_attrs_define
class SundayNightFootballResponse:
    """
    Attributes:
        leagues (List['League']):
        season (SeasonInfo):
        events (List['Event']):
    """

    leagues: List["League"]
    season: "SeasonInfo"
    events: List["Event"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        leagues = []
        for leagues_item_data in self.leagues:
            leagues_item = leagues_item_data.to_dict()
            leagues.append(leagues_item)

        season = self.season.to_dict()

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "leagues": leagues,
                "season": season,
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event import Event
        from ..models.league import League
        from ..models.season_info import SeasonInfo

        d = src_dict.copy()
        leagues = []
        _leagues = d.pop("leagues")
        for leagues_item_data in _leagues:
            leagues_item = League.from_dict(leagues_item_data)

            leagues.append(leagues_item)

        season = SeasonInfo.from_dict(d.pop("season"))

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = Event.from_dict(events_item_data)

            events.append(events_item)

        sunday_night_football_response = cls(
            leagues=leagues,
            season=season,
            events=events,
        )

        sunday_night_football_response.additional_properties = d
        return sunday_night_football_response

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
