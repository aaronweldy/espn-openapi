from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NBATeamRosterResponseSeason")


@_attrs_define
class NBATeamRosterResponseSeason:
    """
    Attributes:
        year (Union[Unset, int]):
        display_name (Union[Unset, str]):
        type (Union[Unset, int]):
        name (Union[Unset, str]):
    """

    year: Union[Unset, int] = UNSET
    display_name: Union[Unset, str] = UNSET
    type: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        year = self.year

        display_name = self.display_name

        type = self.type

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if year is not UNSET:
            field_dict["year"] = year
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        year = d.pop("year", UNSET)

        display_name = d.pop("displayName", UNSET)

        type = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        nba_team_roster_response_season = cls(
            year=year,
            display_name=display_name,
            type=type,
            name=name,
        )

        nba_team_roster_response_season.additional_properties = d
        return nba_team_roster_response_season

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
