from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_event import ScoreboardEvent
    from ..models.scoreboard_league_data import ScoreboardLeagueData
    from ..models.scoreboard_season import ScoreboardSeason
    from ..models.scoreboard_week import ScoreboardWeek


T = TypeVar("T", bound="ScoreboardSbData")


@_attrs_define
class ScoreboardSbData:
    """
    Attributes:
        week (Union[Unset, ScoreboardWeek]):
        leagues (Union[Unset, List['ScoreboardLeagueData']]):
        season (Union[Unset, ScoreboardSeason]):
        events (Union[Unset, List['ScoreboardEvent']]):
    """

    week: Union[Unset, "ScoreboardWeek"] = UNSET
    leagues: Union[Unset, List["ScoreboardLeagueData"]] = UNSET
    season: Union[Unset, "ScoreboardSeason"] = UNSET
    events: Union[Unset, List["ScoreboardEvent"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        week: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.week, Unset):
            week = self.week.to_dict()

        leagues: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.leagues, Unset):
            leagues = []
            for leagues_item_data in self.leagues:
                leagues_item = leagues_item_data.to_dict()
                leagues.append(leagues_item)

        season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if week is not UNSET:
            field_dict["week"] = week
        if leagues is not UNSET:
            field_dict["leagues"] = leagues
        if season is not UNSET:
            field_dict["season"] = season
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_event import ScoreboardEvent
        from ..models.scoreboard_league_data import ScoreboardLeagueData
        from ..models.scoreboard_season import ScoreboardSeason
        from ..models.scoreboard_week import ScoreboardWeek

        d = src_dict.copy()
        _week = d.pop("week", UNSET)
        week: Union[Unset, ScoreboardWeek]
        if isinstance(_week, Unset):
            week = UNSET
        else:
            week = ScoreboardWeek.from_dict(_week)

        leagues = []
        _leagues = d.pop("leagues", UNSET)
        for leagues_item_data in _leagues or []:
            leagues_item = ScoreboardLeagueData.from_dict(leagues_item_data)

            leagues.append(leagues_item)

        _season = d.pop("season", UNSET)
        season: Union[Unset, ScoreboardSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = ScoreboardSeason.from_dict(_season)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = ScoreboardEvent.from_dict(events_item_data)

            events.append(events_item)

        scoreboard_sb_data = cls(
            week=week,
            leagues=leagues,
            season=season,
            events=events,
        )

        scoreboard_sb_data.additional_properties = d
        return scoreboard_sb_data

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
