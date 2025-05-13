from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchMetadata")


@_attrs_define
class SearchMetadata:
    """
    Attributes:
        count (int):  Example: 10.
        total_count (Union[Unset, int]):  Example: 125.
        offset (Union[Unset, int]):
    """

    count: int
    total_count: Union[Unset, int] = UNSET
    offset: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        total_count = self.total_count

        offset = self.offset

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
            }
        )
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count")

        total_count = d.pop("totalCount", UNSET)

        offset = d.pop("offset", UNSET)

        search_metadata = cls(
            count=count,
            total_count=total_count,
            offset=offset,
        )

        search_metadata.additional_properties = d
        return search_metadata

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
