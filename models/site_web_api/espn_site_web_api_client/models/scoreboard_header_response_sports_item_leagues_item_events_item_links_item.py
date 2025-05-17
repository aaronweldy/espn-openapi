from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemLinksItem")


@_attrs_define
class ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemLinksItem:
    """
    Attributes:
        rel (Union[Unset, List[str]]):
        href (Union[Unset, str]):
        text (Union[Unset, str]):
        short_text (Union[Unset, str]):
        is_external (Union[Unset, bool]):
        is_premium (Union[Unset, bool]):
        is_hidden (Union[Unset, bool]):
        language (Union[Unset, str]):
    """

    rel: Union[Unset, List[str]] = UNSET
    href: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    short_text: Union[Unset, str] = UNSET
    is_external: Union[Unset, bool] = UNSET
    is_premium: Union[Unset, bool] = UNSET
    is_hidden: Union[Unset, bool] = UNSET
    language: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rel: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rel, Unset):
            rel = self.rel

        href = self.href

        text = self.text

        short_text = self.short_text

        is_external = self.is_external

        is_premium = self.is_premium

        is_hidden = self.is_hidden

        language = self.language

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rel is not UNSET:
            field_dict["rel"] = rel
        if href is not UNSET:
            field_dict["href"] = href
        if text is not UNSET:
            field_dict["text"] = text
        if short_text is not UNSET:
            field_dict["shortText"] = short_text
        if is_external is not UNSET:
            field_dict["isExternal"] = is_external
        if is_premium is not UNSET:
            field_dict["isPremium"] = is_premium
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rel = cast(List[str], d.pop("rel", UNSET))

        href = d.pop("href", UNSET)

        text = d.pop("text", UNSET)

        short_text = d.pop("shortText", UNSET)

        is_external = d.pop("isExternal", UNSET)

        is_premium = d.pop("isPremium", UNSET)

        is_hidden = d.pop("isHidden", UNSET)

        language = d.pop("language", UNSET)

        scoreboard_header_response_sports_item_leagues_item_events_item_links_item = cls(
            rel=rel,
            href=href,
            text=text,
            short_text=short_text,
            is_external=is_external,
            is_premium=is_premium,
            is_hidden=is_hidden,
            language=language,
        )

        scoreboard_header_response_sports_item_leagues_item_events_item_links_item.additional_properties = d
        return scoreboard_header_response_sports_item_leagues_item_events_item_links_item

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
