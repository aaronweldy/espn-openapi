from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NflStandingsStat")


@_attrs_define
class NflStandingsStat:
    """
    Attributes:
        short_display_name (Union[Unset, str]):
        display_value (Union[Unset, str]):
        display_name (Union[Unset, str]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        type (Union[Unset, str]):
        abbreviation (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    short_display_name: Union[Unset, str] = UNSET
    display_value: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        short_display_name = self.short_display_name

        display_value = self.display_value

        display_name = self.display_name

        name = self.name

        description = self.description

        type = self.type

        abbreviation = self.abbreviation

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if type is not UNSET:
            field_dict["type"] = type
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        short_display_name = d.pop("shortDisplayName", UNSET)

        display_value = d.pop("displayValue", UNSET)

        display_name = d.pop("displayName", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        type = d.pop("type", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        value = d.pop("value", UNSET)

        nfl_standings_stat = cls(
            short_display_name=short_display_name,
            display_value=display_value,
            display_name=display_name,
            name=name,
            description=description,
            type=type,
            abbreviation=abbreviation,
            value=value,
        )

        nfl_standings_stat.additional_properties = d
        return nfl_standings_stat

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
