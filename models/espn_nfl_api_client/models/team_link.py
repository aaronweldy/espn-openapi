from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamLink")


@_attrs_define
class TeamLink:
    """
    Attributes:
        rel (List[str]):
        href (str):  Example: https://www.espn.com/nfl/team/_/name/ari/arizona-cardinals.
        language (Union[Unset, str]):  Example: en-US.
        text (Union[Unset, str]):  Example: Clubhouse.
        short_text (Union[Unset, str]):  Example: Clubhouse.
        is_external (Union[Unset, bool]):
        is_premium (Union[Unset, bool]):
        is_hidden (Union[Unset, bool]):
    """

    rel: List[str]
    href: str
    language: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    short_text: Union[Unset, str] = UNSET
    is_external: Union[Unset, bool] = UNSET
    is_premium: Union[Unset, bool] = UNSET
    is_hidden: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rel = self.rel

        href = self.href

        language = self.language

        text = self.text

        short_text = self.short_text

        is_external = self.is_external

        is_premium = self.is_premium

        is_hidden = self.is_hidden

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rel": rel,
                "href": href,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rel = cast(List[str], d.pop("rel"))

        href = d.pop("href")

        language = d.pop("language", UNSET)

        text = d.pop("text", UNSET)

        short_text = d.pop("shortText", UNSET)

        is_external = d.pop("isExternal", UNSET)

        is_premium = d.pop("isPremium", UNSET)

        is_hidden = d.pop("isHidden", UNSET)

        team_link = cls(
            rel=rel,
            href=href,
            language=language,
            text=text,
            short_text=short_text,
            is_external=is_external,
            is_premium=is_premium,
            is_hidden=is_hidden,
        )

        team_link.additional_properties = d
        return team_link

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
