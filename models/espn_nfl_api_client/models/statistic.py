from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Statistic")


@_attrs_define
class Statistic:
    """
    Attributes:
        name (Union[Unset, str]):  Example: firstDowns.
        display_name (Union[Unset, str]):  Example: First Downs.
        short_display_name (Union[Unset, str]):
        display_value (Union[Unset, str]):  Example: 27.
        value (Union[Unset, float]):  Example: 27.
    """

    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    short_display_name: Union[Unset, str] = UNSET
    display_value: Union[Unset, str] = UNSET
    value: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name = self.display_name

        short_display_name = self.short_display_name

        display_value = self.display_value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        short_display_name = d.pop("shortDisplayName", UNSET)

        display_value = d.pop("displayValue", UNSET)

        value = d.pop("value", UNSET)

        statistic = cls(
            name=name,
            display_name=display_name,
            short_display_name=short_display_name,
            display_value=display_value,
            value=value,
        )

        statistic.additional_properties = d
        return statistic

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
