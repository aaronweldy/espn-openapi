from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NflDraftAthleteAttribute")


@_attrs_define
class NflDraftAthleteAttribute:
    """
    Attributes:
        type (int):
        name (str):
        display_name (str):
        abbreviation (str):
        value (float):
        display_value (str):
    """

    type: int
    name: str
    display_name: str
    abbreviation: str
    value: float
    display_value: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        name = self.name

        display_name = self.display_name

        abbreviation = self.abbreviation

        value = self.value

        display_value = self.display_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "name": name,
                "displayName": display_name,
                "abbreviation": abbreviation,
                "value": value,
                "displayValue": display_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        name = d.pop("name")

        display_name = d.pop("displayName")

        abbreviation = d.pop("abbreviation")

        value = d.pop("value")

        display_value = d.pop("displayValue")

        nfl_draft_athlete_attribute = cls(
            type=type,
            name=name,
            display_name=display_name,
            abbreviation=abbreviation,
            value=value,
            display_value=display_value,
        )

        nfl_draft_athlete_attribute.additional_properties = d
        return nfl_draft_athlete_attribute

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
