import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event import Event
    from ..models.season import Season
    from ..models.team_details_full import TeamDetailsFull


T = TypeVar("T", bound="TeamScheduleResponse")


@_attrs_define
class TeamScheduleResponse:
    """Generic team schedule response, including all games for the team in the specified season. The byeWeek field is only
    present for NFL teams.

        Attributes:
            timestamp (datetime.datetime):
            status (str):
            season (Season):
            team (TeamDetailsFull):
            events (List['Event']):
            requested_season (Union[Unset, Season]):
            bye_week (Union[Unset, int]): Week number of the team's bye week (NFL only)
    """

    timestamp: datetime.datetime
    status: str
    season: "Season"
    team: "TeamDetailsFull"
    events: List["Event"]
    requested_season: Union[Unset, "Season"] = UNSET
    bye_week: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        status = self.status

        season = self.season.to_dict()

        team = self.team.to_dict()

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        requested_season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.requested_season, Unset):
            requested_season = self.requested_season.to_dict()

        bye_week = self.bye_week

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "status": status,
                "season": season,
                "team": team,
                "events": events,
            }
        )
        if requested_season is not UNSET:
            field_dict["requestedSeason"] = requested_season
        if bye_week is not UNSET:
            field_dict["byeWeek"] = bye_week

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event import Event
        from ..models.season import Season
        from ..models.team_details_full import TeamDetailsFull

        d = src_dict.copy()
        timestamp = isoparse(d.pop("timestamp"))

        status = d.pop("status")

        season = Season.from_dict(d.pop("season"))

        team = TeamDetailsFull.from_dict(d.pop("team"))

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = Event.from_dict(events_item_data)

            events.append(events_item)

        _requested_season = d.pop("requestedSeason", UNSET)
        requested_season: Union[Unset, Season]
        if isinstance(_requested_season, Unset):
            requested_season = UNSET
        else:
            requested_season = Season.from_dict(_requested_season)

        bye_week = d.pop("byeWeek", UNSET)

        team_schedule_response = cls(
            timestamp=timestamp,
            status=status,
            season=season,
            team=team,
            events=events,
            requested_season=requested_season,
            bye_week=bye_week,
        )

        team_schedule_response.additional_properties = d
        return team_schedule_response

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
