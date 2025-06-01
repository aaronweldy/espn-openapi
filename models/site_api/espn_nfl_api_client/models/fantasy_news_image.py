from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FantasyNewsImage")


@_attrs_define
class FantasyNewsImage:
    """Fantasy news image

    Attributes:
        url (Union[Unset, str]): Image URL
        alt (Union[Unset, str]): Alt text for image
        caption (Union[Unset, str]): Image caption
        credit (Union[Unset, str]): Image credit
        height (Union[Unset, int]): Image height
        width (Union[Unset, int]): Image width
    """

    url: Union[Unset, str] = UNSET
    alt: Union[Unset, str] = UNSET
    caption: Union[Unset, str] = UNSET
    credit: Union[Unset, str] = UNSET
    height: Union[Unset, int] = UNSET
    width: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        alt = self.alt

        caption = self.caption

        credit = self.credit

        height = self.height

        width = self.width

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if alt is not UNSET:
            field_dict["alt"] = alt
        if caption is not UNSET:
            field_dict["caption"] = caption
        if credit is not UNSET:
            field_dict["credit"] = credit
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        alt = d.pop("alt", UNSET)

        caption = d.pop("caption", UNSET)

        credit = d.pop("credit", UNSET)

        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        fantasy_news_image = cls(
            url=url,
            alt=alt,
            caption=caption,
            credit=credit,
            height=height,
            width=width,
        )

        fantasy_news_image.additional_properties = d
        return fantasy_news_image

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
