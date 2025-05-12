from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArticleImage")


@_attrs_define
class ArticleImage:
    """
    Attributes:
        url (str): URL to the image
        name (Union[Unset, str]): Name of the image
        type (Union[Unset, str]): Type of image (e.g., "header", "Media")
        width (Union[Unset, int]): Width of the image in pixels
        height (Union[Unset, int]): Height of the image in pixels
        id (Union[Unset, int]): Unique identifier for the image
        data_source_identifier (Union[Unset, str]): Data source identifier
        caption (Union[Unset, str]): Caption text for the image
        credit (Union[Unset, str]): Photo credit/attribution
        alt (Union[Unset, str]): Alternative text
    """

    url: str
    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    data_source_identifier: Union[Unset, str] = UNSET
    caption: Union[Unset, str] = UNSET
    credit: Union[Unset, str] = UNSET
    alt: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        name = self.name

        type = self.type

        width = self.width

        height = self.height

        id = self.id

        data_source_identifier = self.data_source_identifier

        caption = self.caption

        credit = self.credit

        alt = self.alt

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if id is not UNSET:
            field_dict["id"] = id
        if data_source_identifier is not UNSET:
            field_dict["dataSourceIdentifier"] = data_source_identifier
        if caption is not UNSET:
            field_dict["caption"] = caption
        if credit is not UNSET:
            field_dict["credit"] = credit
        if alt is not UNSET:
            field_dict["alt"] = alt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        id = d.pop("id", UNSET)

        data_source_identifier = d.pop("dataSourceIdentifier", UNSET)

        caption = d.pop("caption", UNSET)

        credit = d.pop("credit", UNSET)

        alt = d.pop("alt", UNSET)

        article_image = cls(
            url=url,
            name=name,
            type=type,
            width=width,
            height=height,
            id=id,
            data_source_identifier=data_source_identifier,
            caption=caption,
            credit=credit,
            alt=alt,
        )

        article_image.additional_properties = d
        return article_image

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
