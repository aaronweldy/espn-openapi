from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Official")


@_attrs_define
class Official:
    """
    Attributes:
        full_name (Union[Unset, str]):  Example: Carl Cheffers.
        display_name (Union[Unset, str]):  Example: C. Cheffers.
        position (Union[Unset, str]):  Example: Referee.
        order (Union[Unset, int]):
    """

    full_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    position: Union[Unset, str] = UNSET
    order: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        full_name = self.full_name

        display_name = self.display_name

        position = self.position

        order = self.order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if position is not UNSET:
            field_dict["position"] = position
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        full_name = d.pop("fullName", UNSET)

        display_name = d.pop("displayName", UNSET)

        position = d.pop("position", UNSET)

        order = d.pop("order", UNSET)

        official = cls(
            full_name=full_name,
            display_name=display_name,
            position=position,
            order=order,
        )

        official.additional_properties = d
        return official

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
