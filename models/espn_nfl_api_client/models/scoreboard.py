from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.event import Event
    from ..models.league import League
    from ..models.season_info import SeasonInfo
    from ..models.week_info import WeekInfo


T = TypeVar("T", bound="Scoreboard")


@_attrs_define
class Scoreboard:
    """
    Attributes:
        leagues (list['League']):
        season (SeasonInfo):
        week (WeekInfo):
        events (list['Event']):
    """

    leagues: list["League"]
    season: "SeasonInfo"
    week: "WeekInfo"
    events: list["Event"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        leagues = []
        for leagues_item_data in self.leagues:
            leagues_item = leagues_item_data.to_dict()
            leagues.append(leagues_item)

        season = self.season.to_dict()

        week = self.week.to_dict()

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "leagues": leagues,
                "season": season,
                "week": week,
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event import Event
        from ..models.league import League
        from ..models.season_info import SeasonInfo
        from ..models.week_info import WeekInfo

        d = dict(src_dict)
        leagues = []
        _leagues = d.pop("leagues")
        for leagues_item_data in _leagues:
            leagues_item = League.from_dict(leagues_item_data)

            leagues.append(leagues_item)

        season = SeasonInfo.from_dict(d.pop("season"))

        week = WeekInfo.from_dict(d.pop("week"))

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = Event.from_dict(events_item_data)

            events.append(events_item)

        scoreboard = cls(
            leagues=leagues,
            season=season,
            week=week,
            events=events,
        )

        scoreboard.additional_properties = d
        return scoreboard

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
