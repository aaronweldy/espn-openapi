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
        name (str):  Example: Quarterback.
        abbreviation (str):  Example: QB.
        display_name (Union[Unset, str]):  Example: Quarterback.
        leaf (Union[Unset, bool]):  Example: True.
    """

    id: str
    name: str
    abbreviation: str
    display_name: Union[Unset, str] = UNSET
    leaf: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        abbreviation = self.abbreviation

        display_name = self.display_name

        leaf = self.leaf

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "abbreviation": abbreviation,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if leaf is not UNSET:
            field_dict["leaf"] = leaf

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        abbreviation = d.pop("abbreviation")

        display_name = d.pop("displayName", UNSET)

        leaf = d.pop("leaf", UNSET)

        position = cls(
            id=id,
            name=name,
            abbreviation=abbreviation,
            display_name=display_name,
            leaf=leaf,
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
