import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_status import EventStatus
    from ..models.team_reference import TeamReference


T = TypeVar("T", bound="ScoreboardEvent")


@_attrs_define
class ScoreboardEvent:
    """
    Attributes:
        id (str):  Example: 401547417.
        name (str):  Example: Kansas City Chiefs vs. Philadelphia Eagles.
        date (datetime.datetime):  Example: 2023-02-12T23:30:00Z.
        short_name (Union[Unset, str]):  Example: KC vs PHI.
        home_team (Union[Unset, TeamReference]):
        away_team (Union[Unset, TeamReference]):
        status (Union[Unset, EventStatus]):
    """

    id: str
    name: str
    date: datetime.datetime
    short_name: Union[Unset, str] = UNSET
    home_team: Union[Unset, "TeamReference"] = UNSET
    away_team: Union[Unset, "TeamReference"] = UNSET
    status: Union[Unset, "EventStatus"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        date = self.date.isoformat()

        short_name = self.short_name

        home_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.home_team, Unset):
            home_team = self.home_team.to_dict()

        away_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.away_team, Unset):
            away_team = self.away_team.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "date": date,
            }
        )
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if home_team is not UNSET:
            field_dict["homeTeam"] = home_team
        if away_team is not UNSET:
            field_dict["awayTeam"] = away_team
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_status import EventStatus
        from ..models.team_reference import TeamReference

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        date = isoparse(d.pop("date"))

        short_name = d.pop("shortName", UNSET)

        _home_team = d.pop("homeTeam", UNSET)
        home_team: Union[Unset, TeamReference]
        if isinstance(_home_team, Unset):
            home_team = UNSET
        else:
            home_team = TeamReference.from_dict(_home_team)

        _away_team = d.pop("awayTeam", UNSET)
        away_team: Union[Unset, TeamReference]
        if isinstance(_away_team, Unset):
            away_team = UNSET
        else:
            away_team = TeamReference.from_dict(_away_team)

        _status = d.pop("status", UNSET)
        status: Union[Unset, EventStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EventStatus.from_dict(_status)

        scoreboard_event = cls(
            id=id,
            name=name,
            date=date,
            short_name=short_name,
            home_team=home_team,
            away_team=away_team,
            status=status,
        )

        scoreboard_event.additional_properties = d
        return scoreboard_event

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
