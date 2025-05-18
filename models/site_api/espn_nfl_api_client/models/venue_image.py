from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VenueImage")


@_attrs_define
class VenueImage:
    """
    Attributes:
        href (Union[Unset, str]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        alt (Union[Unset, str]):
        rel (Union[Unset, List[str]]):
    """

    href: Union[Unset, str] = UNSET
    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    alt: Union[Unset, str] = UNSET
    rel: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        width = self.width

        height = self.height

        alt = self.alt

        rel: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rel, Unset):
            rel = self.rel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if alt is not UNSET:
            field_dict["alt"] = alt
        if rel is not UNSET:
            field_dict["rel"] = rel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        href = d.pop("href", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        alt = d.pop("alt", UNSET)

        rel = cast(List[str], d.pop("rel", UNSET))

        venue_image = cls(
            href=href,
            width=width,
            height=height,
            alt=alt,
            rel=rel,
        )

        venue_image.additional_properties = d
        return venue_image

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
