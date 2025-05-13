from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Position")


@_attrs_define
class Position:
    """
    Attributes:
        id (str):  Example: 8.
        abbreviation (str):  Example: QB.
        name (Union[Unset, str]):  Example: Quarterback.
        display_name (Union[Unset, str]):  Example: Quarterback.
    """

    id: str
    abbreviation: str
    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        abbreviation = self.abbreviation

        name = self.name

        display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "abbreviation": abbreviation,
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
        id = d.pop("id")

        abbreviation = d.pop("abbreviation")

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        position = cls(
            id=id,
            abbreviation=abbreviation,
            name=name,
            display_name=display_name,
        )

        position.additional_properties = d
        return position

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
