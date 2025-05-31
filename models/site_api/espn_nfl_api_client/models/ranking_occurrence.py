from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RankingOccurrence")


@_attrs_define
class RankingOccurrence:
    """When this ranking occurred

    Attributes:
        type (Union[Unset, str]): Type of occurrence (e.g., "weekly")
        week_number (Union[Unset, int]): Week number
    """

    type: Union[Unset, str] = UNSET
    week_number: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        week_number = self.week_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if week_number is not UNSET:
            field_dict["weekNumber"] = week_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        week_number = d.pop("weekNumber", UNSET)

        ranking_occurrence = cls(
            type=type,
            week_number=week_number,
        )

        ranking_occurrence.additional_properties = d
        return ranking_occurrence

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
