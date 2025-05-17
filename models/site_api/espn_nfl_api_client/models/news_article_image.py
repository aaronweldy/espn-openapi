from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewsArticleImage")


@_attrs_define
class NewsArticleImage:
    """
    Attributes:
        data_source_identifier (Union[Unset, str]): Data source identifier for the image Example: 3b206fdd0ebb6.
        id (Union[Unset, int]): Image identifier Example: 45184155.
        type (Union[Unset, str]): Type of image Example: header.
        name (Union[Unset, str]): Image name Example: John Jenkins [600x400].
        credit (Union[Unset, str]): Credit for the image Example: Abbie Parr/AP.
        height (Union[Unset, int]): Image height in pixels Example: 400.
        width (Union[Unset, int]): Image width in pixels Example: 600.
        url (Union[Unset, str]): URL of the image Example:
            https://a.espncdn.com/photo/2025/0517/r1494212_600x400_3-2.jpg.
        caption (Union[Unset, str]): Caption for the image
        alt (Union[Unset, str]): Alt text for the image
    """

    data_source_identifier: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    credit: Union[Unset, str] = UNSET
    height: Union[Unset, int] = UNSET
    width: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    caption: Union[Unset, str] = UNSET
    alt: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_source_identifier = self.data_source_identifier

        id = self.id

        type = self.type

        name = self.name

        credit = self.credit

        height = self.height

        width = self.width

        url = self.url

        caption = self.caption

        alt = self.alt

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_source_identifier is not UNSET:
            field_dict["dataSourceIdentifier"] = data_source_identifier
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if credit is not UNSET:
            field_dict["credit"] = credit
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width
        if url is not UNSET:
            field_dict["url"] = url
        if caption is not UNSET:
            field_dict["caption"] = caption
        if alt is not UNSET:
            field_dict["alt"] = alt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data_source_identifier = d.pop("dataSourceIdentifier", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        credit = d.pop("credit", UNSET)

        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        url = d.pop("url", UNSET)

        caption = d.pop("caption", UNSET)

        alt = d.pop("alt", UNSET)

        news_article_image = cls(
            data_source_identifier=data_source_identifier,
            id=id,
            type=type,
            name=name,
            credit=credit,
            height=height,
            width=width,
            url=url,
            caption=caption,
            alt=alt,
        )

        news_article_image.additional_properties = d
        return news_article_image

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
