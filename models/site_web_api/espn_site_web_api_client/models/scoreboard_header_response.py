from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.league_reference import LeagueReference
    from ..models.navigation_item import NavigationItem
    from ..models.scoreboard_event import ScoreboardEvent
    from ..models.season import Season


T = TypeVar("T", bound="ScoreboardHeaderResponse")


@_attrs_define
class ScoreboardHeaderResponse:
    """
    Attributes:
        league (LeagueReference):
        season (Season):
        navigation (Union[Unset, List['NavigationItem']]):
        events (Union[Unset, List['ScoreboardEvent']]):
    """

    league: "LeagueReference"
    season: "Season"
    navigation: Union[Unset, List["NavigationItem"]] = UNSET
    events: Union[Unset, List["ScoreboardEvent"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        league = self.league.to_dict()

        season = self.season.to_dict()

        navigation: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.navigation, Unset):
            navigation = []
            for navigation_item_data in self.navigation:
                navigation_item = navigation_item_data.to_dict()
                navigation.append(navigation_item)

        events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "league": league,
                "season": season,
            }
        )
        if navigation is not UNSET:
            field_dict["navigation"] = navigation
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.league_reference import LeagueReference
        from ..models.navigation_item import NavigationItem
        from ..models.scoreboard_event import ScoreboardEvent
        from ..models.season import Season

        d = src_dict.copy()
        league = LeagueReference.from_dict(d.pop("league"))

        season = Season.from_dict(d.pop("season"))

        navigation = []
        _navigation = d.pop("navigation", UNSET)
        for navigation_item_data in _navigation or []:
            navigation_item = NavigationItem.from_dict(navigation_item_data)

            navigation.append(navigation_item)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = ScoreboardEvent.from_dict(events_item_data)

            events.append(events_item)

        scoreboard_header_response = cls(
            league=league,
            season=season,
            navigation=navigation,
            events=events,
        )

        scoreboard_header_response.additional_properties = d
        return scoreboard_header_response

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
