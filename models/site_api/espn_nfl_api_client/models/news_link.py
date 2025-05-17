from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewsLink")


@_attrs_define
class NewsLink:
    """
    Attributes:
        href (str): URL for the link Example: https://www.espn.com/nfl/.
        language (Union[Unset, str]): Language of the content Example: en.
        rel (Union[Unset, List[str]]): Relationship types Example: ['index', 'desktop', 'league'].
        text (Union[Unset, str]): Display text for the link Example: All NFL News.
        short_text (Union[Unset, str]): Short display text for the link Example: All News.
        is_external (Union[Unset, bool]): Whether the link is external
        is_premium (Union[Unset, bool]): Whether the linked content is premium
    """

    href: str
    language: Union[Unset, str] = UNSET
    rel: Union[Unset, List[str]] = UNSET
    text: Union[Unset, str] = UNSET
    short_text: Union[Unset, str] = UNSET
    is_external: Union[Unset, bool] = UNSET
    is_premium: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        language = self.language

        rel: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rel, Unset):
            rel = self.rel

        text = self.text

        short_text = self.short_text

        is_external = self.is_external

        is_premium = self.is_premium

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "href": href,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if rel is not UNSET:
            field_dict["rel"] = rel
        if text is not UNSET:
            field_dict["text"] = text
        if short_text is not UNSET:
            field_dict["shortText"] = short_text
        if is_external is not UNSET:
            field_dict["isExternal"] = is_external
        if is_premium is not UNSET:
            field_dict["isPremium"] = is_premium

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        href = d.pop("href")

        language = d.pop("language", UNSET)

        rel = cast(List[str], d.pop("rel", UNSET))

        text = d.pop("text", UNSET)

        short_text = d.pop("shortText", UNSET)

        is_external = d.pop("isExternal", UNSET)

        is_premium = d.pop("isPremium", UNSET)

        news_link = cls(
            href=href,
            language=language,
            rel=rel,
            text=text,
            short_text=short_text,
            is_external=is_external,
            is_premium=is_premium,
        )

        news_link.additional_properties = d
        return news_link

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
