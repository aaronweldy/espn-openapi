from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AthleteFlag")


@_attrs_define
class AthleteFlag:
    """Country flag information

    Attributes:
        href (Union[Unset, str]): URL to the flag image
        alt (Union[Unset, str]): Country name
        rel (Union[Unset, List[str]]):
    """

    href: Union[Unset, str] = UNSET
    alt: Union[Unset, str] = UNSET
    rel: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        alt = self.alt

        rel: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rel, Unset):
            rel = self.rel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if alt is not UNSET:
            field_dict["alt"] = alt
        if rel is not UNSET:
            field_dict["rel"] = rel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        href = d.pop("href", UNSET)

        alt = d.pop("alt", UNSET)

        rel = cast(List[str], d.pop("rel", UNSET))

        athlete_flag = cls(
            href=href,
            alt=alt,
            rel=rel,
        )

        athlete_flag.additional_properties = d
        return athlete_flag

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
