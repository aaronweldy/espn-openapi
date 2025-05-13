from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatCategory")


@_attrs_define
class StatCategory:
    """
    Attributes:
        name (str):  Example: passingYards.
        value (float):  Example: 4183.
        display_name (Union[Unset, str]):  Example: Passing Yards.
        display_value (Union[Unset, str]):  Example: 4,183.
        rank_display_value (Union[Unset, str]):  Example: 6th in NFL.
    """

    name: str
    value: float
    display_name: Union[Unset, str] = UNSET
    display_value: Union[Unset, str] = UNSET
    rank_display_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        value = self.value

        display_name = self.display_name

        display_value = self.display_value

        rank_display_value = self.rank_display_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value
        if rank_display_value is not UNSET:
            field_dict["rankDisplayValue"] = rank_display_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        value = d.pop("value")

        display_name = d.pop("displayName", UNSET)

        display_value = d.pop("displayValue", UNSET)

        rank_display_value = d.pop("rankDisplayValue", UNSET)

        stat_category = cls(
            name=name,
            value=value,
            display_name=display_name,
            display_value=display_value,
            rank_display_value=rank_display_value,
        )

        stat_category.additional_properties = d
        return stat_category

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
