from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GlossaryEntry")


@_attrs_define
class GlossaryEntry:
    """
    Attributes:
        abbreviation (str): Statistical abbreviation
        display_name (str): Full description
    """

    abbreviation: str
    display_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        abbreviation = self.abbreviation

        display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "abbreviation": abbreviation,
                "displayName": display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        abbreviation = d.pop("abbreviation")

        display_name = d.pop("displayName")

        glossary_entry = cls(
            abbreviation=abbreviation,
            display_name=display_name,
        )

        glossary_entry.additional_properties = d
        return glossary_entry

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
