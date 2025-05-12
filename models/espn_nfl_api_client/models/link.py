from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Link")


@_attrs_define
class Link:
    """
    Attributes:
        href (Union[Unset, str]):
        text (Union[Unset, str]):
        rel (Union[Unset, List[str]]):
        is_external (Union[Unset, bool]):
        is_premium (Union[Unset, bool]):
    """

    href: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    rel: Union[Unset, List[str]] = UNSET
    is_external: Union[Unset, bool] = UNSET
    is_premium: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        text = self.text

        rel: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rel, Unset):
            rel = self.rel

        is_external = self.is_external

        is_premium = self.is_premium

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if text is not UNSET:
            field_dict["text"] = text
        if rel is not UNSET:
            field_dict["rel"] = rel
        if is_external is not UNSET:
            field_dict["isExternal"] = is_external
        if is_premium is not UNSET:
            field_dict["isPremium"] = is_premium

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        href = d.pop("href", UNSET)

        text = d.pop("text", UNSET)

        rel = cast(List[str], d.pop("rel", UNSET))

        is_external = d.pop("isExternal", UNSET)

        is_premium = d.pop("isPremium", UNSET)

        link = cls(
            href=href,
            text=text,
            rel=rel,
            is_external=is_external,
            is_premium=is_premium,
        )

        link.additional_properties = d
        return link

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
