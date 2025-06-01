from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttendanceStat")


@_attrs_define
class AttendanceStat:
    """
    Attributes:
        name (str): Stat name Example: games.
        display_name (str): Display name for the stat Example: Home Games.
        abbreviation (str): Stat abbreviation Example: GMS.
        value (float): Numeric value of the stat Example: 6.0.
        display_value (str): Display-formatted value Example: 6.
        short_display_name (Union[Unset, str]): Short display name Example: GMS.
        description (Union[Unset, str]): Description of the stat Example: The total amount of games played as home..
    """

    name: str
    display_name: str
    abbreviation: str
    value: float
    display_value: str
    short_display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        abbreviation = self.abbreviation

        value = self.value

        display_value = self.display_value

        short_display_name = self.short_display_name

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "displayName": display_name,
                "abbreviation": abbreviation,
                "value": value,
                "displayValue": display_value,
            }
        )
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        display_name = d.pop("displayName")

        abbreviation = d.pop("abbreviation")

        value = d.pop("value")

        display_value = d.pop("displayValue")

        short_display_name = d.pop("shortDisplayName", UNSET)

        description = d.pop("description", UNSET)

        attendance_stat = cls(
            name=name,
            display_name=display_name,
            abbreviation=abbreviation,
            value=value,
            display_value=display_value,
            short_display_name=short_display_name,
            description=description,
        )

        attendance_stat.additional_properties = d
        return attendance_stat

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
