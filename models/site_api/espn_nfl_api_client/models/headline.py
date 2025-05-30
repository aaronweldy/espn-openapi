from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Headline")


@_attrs_define
class Headline:
    """
    Attributes:
        type (str):  Example: Recap.
        description (Union[Unset, str]):
        short_link_text (Union[Unset, str]):
    """

    type: str
    description: Union[Unset, str] = UNSET
    short_link_text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        description = self.description

        short_link_text = self.short_link_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if short_link_text is not UNSET:
            field_dict["shortLinkText"] = short_link_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        description = d.pop("description", UNSET)

        short_link_text = d.pop("shortLinkText", UNSET)

        headline = cls(
            type=type,
            description=description,
            short_link_text=short_link_text,
        )

        headline.additional_properties = d
        return headline

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
