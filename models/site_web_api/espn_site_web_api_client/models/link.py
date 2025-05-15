from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Link")


@_attrs_define
class Link:
    """
    Attributes:
        language (Union[Unset, str]):  Example: en-US.
        rel (Union[Unset, List[str]]):  Example: ['desktop', 'athlete'].
        href (Union[Unset, str]):
        text (Union[Unset, str]):
        short_text (Union[None, Unset, str]):
        is_external (Union[Unset, bool]):
        is_premium (Union[Unset, bool]):
        attributes (Union[List[str], None, Unset]):
    """

    language: Union[Unset, str] = UNSET
    rel: Union[Unset, List[str]] = UNSET
    href: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    short_text: Union[None, Unset, str] = UNSET
    is_external: Union[Unset, bool] = UNSET
    is_premium: Union[Unset, bool] = UNSET
    attributes: Union[List[str], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language = self.language

        rel: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rel, Unset):
            rel = self.rel

        href = self.href

        text = self.text

        short_text: Union[None, Unset, str]
        if isinstance(self.short_text, Unset):
            short_text = UNSET
        else:
            short_text = self.short_text

        is_external = self.is_external

        is_premium = self.is_premium

        attributes: Union[List[str], None, Unset]
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        elif isinstance(self.attributes, list):
            attributes = self.attributes

        else:
            attributes = self.attributes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if language is not UNSET:
            field_dict["language"] = language
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
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language = d.pop("language", UNSET)

        rel = cast(List[str], d.pop("rel", UNSET))

        href = d.pop("href", UNSET)

        text = d.pop("text", UNSET)

        def _parse_short_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        short_text = _parse_short_text(d.pop("shortText", UNSET))

        is_external = d.pop("isExternal", UNSET)

        is_premium = d.pop("isPremium", UNSET)

        def _parse_attributes(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attributes_type_0 = cast(List[str], data)

                return attributes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        attributes = _parse_attributes(d.pop("attributes", UNSET))

        link = cls(
            language=language,
            rel=rel,
            href=href,
            text=text,
            short_text=short_text,
            is_external=is_external,
            is_premium=is_premium,
            attributes=attributes,
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
