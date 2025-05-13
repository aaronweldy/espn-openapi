from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatRule")


@_attrs_define
class StatRule:
    """
    Attributes:
        id (int): Stat ID Example: 42.
        points (float): Points awarded for this stat Example: 4.0.
        name (Union[Unset, str]): Stat name Example: Passing TD.
        is_active (Union[Unset, bool]):  Example: True.
    """

    id: int
    points: float
    name: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        points = self.points

        name = self.name

        is_active = self.is_active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "points": points,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if is_active is not UNSET:
            field_dict["isActive"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        points = d.pop("points")

        name = d.pop("name", UNSET)

        is_active = d.pop("isActive", UNSET)

        stat_rule = cls(
            id=id,
            points=points,
            name=name,
            is_active=is_active,
        )

        stat_rule.additional_properties = d
        return stat_rule

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
