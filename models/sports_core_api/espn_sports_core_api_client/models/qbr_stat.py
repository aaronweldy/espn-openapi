from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QBRStat")


@_attrs_define
class QBRStat:
    """
    Attributes:
        name (Union[Unset, str]):  Example: qbr.
        display_name (Union[Unset, str]):  Example: RAW QBR.
        short_display_name (Union[Unset, str]):  Example: RAW QBR.
        description (Union[Unset, str]):  Example: Raw Total Quarterback Rating, which values quarterback on all play
            types on a 0-100 scale (not adjusted for opposing defenses faced).
        abbreviation (Union[Unset, str]):  Example: QBR.
        value (Union[Unset, float]):  Example: 45.96.
        display_value (Union[Unset, str]):  Example: 46.0.
    """

    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    short_display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    value: Union[Unset, float] = UNSET
    display_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        short_display_name = self.short_display_name

        description = self.description

        abbreviation = self.abbreviation

        value = self.value

        display_value = self.display_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if description is not UNSET:
            field_dict["description"] = description
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if value is not UNSET:
            field_dict["value"] = value
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        short_display_name = d.pop("shortDisplayName", UNSET)

        description = d.pop("description", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        value = d.pop("value", UNSET)

        display_value = d.pop("displayValue", UNSET)

        qbr_stat = cls(
            name=name,
            display_name=display_name,
            short_display_name=short_display_name,
            description=description,
            abbreviation=abbreviation,
            value=value,
            display_value=display_value,
        )

        qbr_stat.additional_properties = d
        return qbr_stat

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
