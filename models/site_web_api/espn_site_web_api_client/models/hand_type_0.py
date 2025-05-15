from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HandType0")


@_attrs_define
class HandType0:
    """
    Attributes:
        type (Union[Unset, str]):
        abbreviation (Union[Unset, str]):
        display_value (Union[Unset, str]):
    """

    type: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    display_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        abbreviation = self.abbreviation

        display_value = self.display_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        display_value = d.pop("displayValue", UNSET)

        hand_type_0 = cls(
            type=type,
            abbreviation=abbreviation,
            display_value=display_value,
        )

        hand_type_0.additional_properties = d
        return hand_type_0

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
