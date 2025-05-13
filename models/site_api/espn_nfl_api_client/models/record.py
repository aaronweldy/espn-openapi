from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        name (Union[Unset, str]):  Example: overall.
        abbreviation (Union[Unset, str]):  Example: Total.
        type (Union[Unset, str]):  Example: total.
        summary (Union[Unset, str]):  Example: 14-3.
    """

    name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        abbreviation = self.abbreviation

        type = self.type

        summary = self.summary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if type is not UNSET:
            field_dict["type"] = type
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        type = d.pop("type", UNSET)

        summary = d.pop("summary", UNSET)

        record = cls(
            name=name,
            abbreviation=abbreviation,
            type=type,
            summary=summary,
        )

        record.additional_properties = d
        return record

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
