from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScoreboardLink")


@_attrs_define
class ScoreboardLink:
    """
    Attributes:
        is_external (Union[Unset, bool]):
        short_text (Union[Unset, str]):
        rel (Union[Unset, List[str]]):
        language (Union[Unset, str]):
        href (Union[Unset, str]):
        text (Union[Unset, str]):
        is_premium (Union[Unset, bool]):
    """

    is_external: Union[Unset, bool] = UNSET
    short_text: Union[Unset, str] = UNSET
    rel: Union[Unset, List[str]] = UNSET
    language: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    is_premium: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_external = self.is_external

        short_text = self.short_text

        rel: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rel, Unset):
            rel = self.rel

        language = self.language

        href = self.href

        text = self.text

        is_premium = self.is_premium

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_external is not UNSET:
            field_dict["isExternal"] = is_external
        if short_text is not UNSET:
            field_dict["shortText"] = short_text
        if rel is not UNSET:
            field_dict["rel"] = rel
        if language is not UNSET:
            field_dict["language"] = language
        if href is not UNSET:
            field_dict["href"] = href
        if text is not UNSET:
            field_dict["text"] = text
        if is_premium is not UNSET:
            field_dict["isPremium"] = is_premium

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_external = d.pop("isExternal", UNSET)

        short_text = d.pop("shortText", UNSET)

        rel = cast(List[str], d.pop("rel", UNSET))

        language = d.pop("language", UNSET)

        href = d.pop("href", UNSET)

        text = d.pop("text", UNSET)

        is_premium = d.pop("isPremium", UNSET)

        scoreboard_link = cls(
            is_external=is_external,
            short_text=short_text,
            rel=rel,
            language=language,
            href=href,
            text=text,
            is_premium=is_premium,
        )

        scoreboard_link.additional_properties = d
        return scoreboard_link

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
