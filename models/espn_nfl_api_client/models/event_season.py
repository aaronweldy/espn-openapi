from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventSeason")


@_attrs_define
class EventSeason:
    """
    Attributes:
        year (int):  Example: 2024.
        type_ (int):  Example: 3.
        slug (Union[Unset, str]):  Example: post-season.
    """

    year: int
    type_: int
    slug: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        year = self.year

        type_ = self.type_

        slug = self.slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "year": year,
                "type": type_,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        year = d.pop("year")

        type_ = d.pop("type")

        slug = d.pop("slug", UNSET)

        event_season = cls(
            year=year,
            type_=type_,
            slug=slug,
        )

        event_season.additional_properties = d
        return event_season

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
