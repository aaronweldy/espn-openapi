import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewsItem")


@_attrs_define
class NewsItem:
    """
    Attributes:
        headline (str):  Example: Mahomes throws 3 TDs in comeback win.
        published (datetime.datetime):  Example: 2023-02-13T04:30:00Z.
        description (Union[Unset, str]):  Example: Patrick Mahomes led the Chiefs to a comeback victory....
        image (Union[Unset, str]):  Example: https://a.espncdn.com/photo/2023/0213/r1129633_1296x729_16-9.jpg.
        url (Union[Unset, str]):  Example: https://www.espn.com/nfl/story/_/id/35642589/patrick-mahomes-comeback-win.
    """

    headline: str
    published: datetime.datetime
    description: Union[Unset, str] = UNSET
    image: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        headline = self.headline

        published = self.published.isoformat()

        description = self.description

        image = self.image

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "headline": headline,
                "published": published,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if image is not UNSET:
            field_dict["image"] = image
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        headline = d.pop("headline")

        published = isoparse(d.pop("published"))

        description = d.pop("description", UNSET)

        image = d.pop("image", UNSET)

        url = d.pop("url", UNSET)

        news_item = cls(
            headline=headline,
            published=published,
            description=description,
            image=image,
            url=url,
        )

        news_item.additional_properties = d
        return news_item

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
