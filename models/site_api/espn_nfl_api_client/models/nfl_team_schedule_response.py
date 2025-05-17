import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.event import Event
    from ..models.season import Season
    from ..models.team_details_full import TeamDetailsFull


T = TypeVar("T", bound="NFLTeamScheduleResponse")


@_attrs_define
class NFLTeamScheduleResponse:
    """NFL team schedule response, including all games for the team in the specified season.

    Attributes:
        timestamp (datetime.datetime):
        status (str):
        season (Season):
        team (TeamDetailsFull):
        events (List['Event']):
        requested_season (Season):
        bye_week (int):
    """

    timestamp: datetime.datetime
    status: str
    season: "Season"
    team: "TeamDetailsFull"
    events: List["Event"]
    requested_season: "Season"
    bye_week: int
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
                "requestedSeason": requested_season,
                "byeWeek": bye_week,
            }
        )

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

        requested_season = Season.from_dict(d.pop("requestedSeason"))

        bye_week = d.pop("byeWeek")

        nfl_team_schedule_response = cls(
            timestamp=timestamp,
            status=status,
            season=season,
            team=team,
            events=events,
            requested_season=requested_season,
            bye_week=bye_week,
        )

        nfl_team_schedule_response.additional_properties = d
        return nfl_team_schedule_response

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
