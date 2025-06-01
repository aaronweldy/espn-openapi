from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BettingProvider")


@_attrs_define
class BettingProvider:
    """
    Attributes:
        id (str): Provider identifier Example: 58.
        name (str): Provider name Example: ESPN BET.
        active (Union[Unset, int]): Active status (1 = active) Example: 1.
        priority (Union[Unset, int]): Display priority Example: 1.
    """

    id: str
    name: str
    active: Union[Unset, int] = UNSET
    priority: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        active = self.active

        priority = self.priority

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        active = d.pop("active", UNSET)

        priority = d.pop("priority", UNSET)

        betting_provider = cls(
            id=id,
            name=name,
            active=active,
            priority=priority,
        )

        betting_provider.additional_properties = d
        return betting_provider

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
