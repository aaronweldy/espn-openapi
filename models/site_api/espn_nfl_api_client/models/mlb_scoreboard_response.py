from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event import Event
    from ..models.league import League
    from ..models.mlb_scoreboard_response_day import MlbScoreboardResponseDay
    from ..models.season_info import SeasonInfo


T = TypeVar("T", bound="MlbScoreboardResponse")


@_attrs_define
class MlbScoreboardResponse:
    """MLB scoreboard response, including all games for the specified date(s).

    Attributes:
        leagues (List['League']):
        events (List['Event']):
        season (Union[Unset, SeasonInfo]):
        day (Union[Unset, MlbScoreboardResponseDay]):
    """

    leagues: List["League"]
    events: List["Event"]
    season: Union[Unset, "SeasonInfo"] = UNSET
    day: Union[Unset, "MlbScoreboardResponseDay"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        leagues = []
        for leagues_item_data in self.leagues:
            leagues_item = leagues_item_data.to_dict()
            leagues.append(leagues_item)

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        day: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.day, Unset):
            day = self.day.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "leagues": leagues,
                "events": events,
            }
        )
        if season is not UNSET:
            field_dict["season"] = season
        if day is not UNSET:
            field_dict["day"] = day

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event import Event
        from ..models.league import League
        from ..models.mlb_scoreboard_response_day import MlbScoreboardResponseDay
        from ..models.season_info import SeasonInfo

        d = src_dict.copy()
        leagues = []
        _leagues = d.pop("leagues")
        for leagues_item_data in _leagues:
            leagues_item = League.from_dict(leagues_item_data)

            leagues.append(leagues_item)

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = Event.from_dict(events_item_data)

            events.append(events_item)

        _season = d.pop("season", UNSET)
        season: Union[Unset, SeasonInfo]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = SeasonInfo.from_dict(_season)

        _day = d.pop("day", UNSET)
        day: Union[Unset, MlbScoreboardResponseDay]
        if isinstance(_day, Unset):
            day = UNSET
        else:
            day = MlbScoreboardResponseDay.from_dict(_day)

        mlb_scoreboard_response = cls(
            leagues=leagues,
            events=events,
            season=season,
            day=day,
        )

        mlb_scoreboard_response.additional_properties = d
        return mlb_scoreboard_response

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
