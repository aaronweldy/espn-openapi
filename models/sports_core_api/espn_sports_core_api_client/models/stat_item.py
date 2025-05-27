from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StatItem")


@_attrs_define
class StatItem:
    """An individual statistical item within a category.

    Attributes:
        name (str): The stat name Example: soloTackles.
        display_name (str): The display name for the stat Example: Solo Tackles.
        short_display_name (str): The short display name for the stat Example: SOLO.
        description (str): Description of what the stat represents Example: The number of times a tackle was made
            unassisted..
        abbreviation (str): The abbreviation for the stat Example: SOLO.
        value (float): The numeric value of the stat correction (can be negative) Example: -1.
        display_value (str): The display value of the stat correction Example: -1.
    """

    name: str
    display_name: str
    short_display_name: str
    description: str
    abbreviation: str
    value: float
    display_value: str
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
        field_dict.update(
            {
                "name": name,
                "displayName": display_name,
                "shortDisplayName": short_display_name,
                "description": description,
                "abbreviation": abbreviation,
                "value": value,
                "displayValue": display_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        display_name = d.pop("displayName")

        short_display_name = d.pop("shortDisplayName")

        description = d.pop("description")

        abbreviation = d.pop("abbreviation")

        value = d.pop("value")

        display_value = d.pop("displayValue")

        stat_item = cls(
            name=name,
            display_name=display_name,
            short_display_name=short_display_name,
            description=description,
            abbreviation=abbreviation,
            value=value,
            display_value=display_value,
        )

        stat_item.additional_properties = d
        return stat_item

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
