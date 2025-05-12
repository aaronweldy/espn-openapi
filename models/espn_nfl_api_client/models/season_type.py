from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeasonType")


@_attrs_define
class SeasonType:
    """
    Attributes:
        id (str):  Example: 2.
        type_ (int):  Example: 2.
        name (str):  Example: Regular Season.
        abbreviation (Union[Unset, str]):  Example: reg.
    """

    id: str
    type_: int
    name: str
    abbreviation: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        name = self.name

        abbreviation = self.abbreviation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "name": name,
            }
        )
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        name = d.pop("name")

        abbreviation = d.pop("abbreviation", UNSET)

        season_type = cls(
            id=id,
            type_=type_,
            name=name,
            abbreviation=abbreviation,
        )

        season_type.additional_properties = d
        return season_type

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
