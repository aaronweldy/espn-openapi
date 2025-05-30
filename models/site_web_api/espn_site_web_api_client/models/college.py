from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="College")


@_attrs_define
class College:
    """
    Attributes:
        id (Union[Unset, str]):
        mascot (Union[Unset, str]):
        name (Union[Unset, str]):
        short_name (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    mascot: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        mascot = self.mascot

        name = self.name

        short_name = self.short_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if mascot is not UNSET:
            field_dict["mascot"] = mascot
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        mascot = d.pop("mascot", UNSET)

        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        college = cls(
            id=id,
            mascot=mascot,
            name=name,
            short_name=short_name,
        )

        college.additional_properties = d
        return college

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
