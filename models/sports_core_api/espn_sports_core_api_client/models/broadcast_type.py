from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BroadcastType")


@_attrs_define
class BroadcastType:
    """
    Attributes:
        id (str):
        short_name (str):
        long_name (str):
        slug (str):
    """

    id: str
    short_name: str
    long_name: str
    slug: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        short_name = self.short_name

        long_name = self.long_name

        slug = self.slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "shortName": short_name,
                "longName": long_name,
                "slug": slug,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        short_name = d.pop("shortName")

        long_name = d.pop("longName")

        slug = d.pop("slug")

        broadcast_type = cls(
            id=id,
            short_name=short_name,
            long_name=long_name,
            slug=slug,
        )

        broadcast_type.additional_properties = d
        return broadcast_type

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
