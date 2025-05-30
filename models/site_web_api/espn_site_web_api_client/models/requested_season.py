from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestedSeason")


@_attrs_define
class RequestedSeason:
    """
    Attributes:
        year (int):  Example: 2024.
        type (int):  Example: 2.
        name (Union[Unset, str]):  Example: Regular Season.
        display_name (Union[Unset, str]):  Example: 2024 Regular Season.
    """

    year: int
    type: int
    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        year = self.year

        type = self.type

        name = self.name

        display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "year": year,
                "type": type,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        year = d.pop("year")

        type = d.pop("type")

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        requested_season = cls(
            year=year,
            type=type,
            name=name,
            display_name=display_name,
        )

        requested_season.additional_properties = d
        return requested_season

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
