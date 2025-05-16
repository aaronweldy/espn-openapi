from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SearchV2ResultType")


@_attrs_define
class SearchV2ResultType:
    """
    Attributes:
        total_found (int):
        type (str):
        display_name (str):
    """

    total_found: int
    type: str
    display_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_found = self.total_found

        type = self.type

        display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalFound": total_found,
                "type": type,
                "displayName": display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_found = d.pop("totalFound")

        type = d.pop("type")

        display_name = d.pop("displayName")

        search_v2_result_type = cls(
            total_found=total_found,
            type=type,
            display_name=display_name,
        )

        search_v2_result_type.additional_properties = d
        return search_v2_result_type

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
