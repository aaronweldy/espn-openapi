import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_reference import TeamReference


T = TypeVar("T", bound="EventReference")


@_attrs_define
class EventReference:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 401547417.
        date (Union[Unset, datetime.datetime]):  Example: 2023-02-12T23:30:00Z.
        home_team (Union[Unset, TeamReference]):
        away_team (Union[Unset, TeamReference]):
    """

    id: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    home_team: Union[Unset, "TeamReference"] = UNSET
    away_team: Union[Unset, "TeamReference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        home_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.home_team, Unset):
            home_team = self.home_team.to_dict()

        away_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.away_team, Unset):
            away_team = self.away_team.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if date is not UNSET:
            field_dict["date"] = date
        if home_team is not UNSET:
            field_dict["homeTeam"] = home_team
        if away_team is not UNSET:
            field_dict["awayTeam"] = away_team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_reference import TeamReference

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

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

        event_reference = cls(
            id=id,
            date=date,
            home_team=home_team,
            away_team=away_team,
        )

        event_reference.additional_properties = d
        return event_reference

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
