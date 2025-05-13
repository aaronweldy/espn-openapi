from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Statistic")


@_attrs_define
class Statistic:
    """
    Attributes:
        name (str):  Example: completions.
        value (float):  Example: 401.0.
        display_name (Union[Unset, str]):  Example: Completions.
        short_display_name (Union[Unset, str]):  Example: COMP.
        description (Union[Unset, str]):  Example: The number of passes completed.
        abbreviation (Union[Unset, str]):  Example: COMP.
        display_value (Union[Unset, str]):  Example: 401.
    """

    name: str
    value: float
    display_name: Union[Unset, str] = UNSET
    short_display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    display_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        value = self.value

        display_name = self.display_name

        short_display_name = self.short_display_name

        description = self.description

        abbreviation = self.abbreviation

        display_value = self.display_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if description is not UNSET:
            field_dict["description"] = description
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        value = d.pop("value")

        display_name = d.pop("displayName", UNSET)

        short_display_name = d.pop("shortDisplayName", UNSET)

        description = d.pop("description", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        display_value = d.pop("displayValue", UNSET)

        statistic = cls(
            name=name,
            value=value,
            display_name=display_name,
            short_display_name=short_display_name,
            description=description,
            abbreviation=abbreviation,
            display_value=display_value,
        )

        statistic.additional_properties = d
        return statistic

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
