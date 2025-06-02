from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderDetails")


@_attrs_define
class ProviderDetails:
    """
    Attributes:
        ref (str): Reference URL for this provider
        id (str): Provider ID Example: 58.
        name (str): Provider name Example: ESPN BET.
        priority (Union[Unset, int]): Provider priority/ranking Example: 1.
    """

    ref: str
    id: str
    name: str
    priority: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        id = self.id

        name = self.name

        priority = self.priority

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "id": id,
                "name": name,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ref = d.pop("$ref")

        id = d.pop("id")

        name = d.pop("name")

        priority = d.pop("priority", UNSET)

        provider_details = cls(
            ref=ref,
            id=id,
            name=name,
            priority=priority,
        )

        provider_details.additional_properties = d
        return provider_details

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
