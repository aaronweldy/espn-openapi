from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScoreboardImage")


@_attrs_define
class ScoreboardImage:
    """
    Attributes:
        data_source_identifier (Union[Unset, str]):
        name (Union[Unset, str]):
        width (Union[Unset, int]):
        id (Union[Unset, int]):
        type (Union[Unset, str]):
        credit (Union[Unset, str]):
        url (Union[Unset, str]):
        height (Union[Unset, int]):
        caption (Union[Unset, str]):
        alt (Union[Unset, str]):
    """

    data_source_identifier: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    width: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    credit: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    height: Union[Unset, int] = UNSET
    caption: Union[Unset, str] = UNSET
    alt: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_source_identifier = self.data_source_identifier

        name = self.name

        width = self.width

        id = self.id

        type = self.type

        credit = self.credit

        url = self.url

        height = self.height

        caption = self.caption

        alt = self.alt

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_source_identifier is not UNSET:
            field_dict["dataSourceIdentifier"] = data_source_identifier
        if name is not UNSET:
            field_dict["name"] = name
        if width is not UNSET:
            field_dict["width"] = width
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if credit is not UNSET:
            field_dict["credit"] = credit
        if url is not UNSET:
            field_dict["url"] = url
        if height is not UNSET:
            field_dict["height"] = height
        if caption is not UNSET:
            field_dict["caption"] = caption
        if alt is not UNSET:
            field_dict["alt"] = alt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data_source_identifier = d.pop("dataSourceIdentifier", UNSET)

        name = d.pop("name", UNSET)

        width = d.pop("width", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("type", UNSET)

        credit = d.pop("credit", UNSET)

        url = d.pop("url", UNSET)

        height = d.pop("height", UNSET)

        caption = d.pop("caption", UNSET)

        alt = d.pop("alt", UNSET)

        scoreboard_image = cls(
            data_source_identifier=data_source_identifier,
            name=name,
            width=width,
            id=id,
            type=type,
            credit=credit,
            url=url,
            height=height,
            caption=caption,
            alt=alt,
        )

        scoreboard_image.additional_properties = d
        return scoreboard_image

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
