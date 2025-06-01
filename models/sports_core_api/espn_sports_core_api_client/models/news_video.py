from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.news_video_ad import NewsVideoAd
    from ..models.news_video_links import NewsVideoLinks


T = TypeVar("T", bound="NewsVideo")


@_attrs_define
class NewsVideo:
    """
    Attributes:
        id (Union[Unset, int]):
        source (Union[Unset, str]):
        headline (Union[Unset, str]):
        caption (Union[Unset, str]):
        description (Union[Unset, str]):
        premium (Union[Unset, bool]):
        ad (Union[Unset, NewsVideoAd]):
        duration (Union[Unset, int]):
        thumbnail (Union[Unset, str]):
        links (Union[Unset, NewsVideoLinks]):
    """

    id: Union[Unset, int] = UNSET
    source: Union[Unset, str] = UNSET
    headline: Union[Unset, str] = UNSET
    caption: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    premium: Union[Unset, bool] = UNSET
    ad: Union[Unset, "NewsVideoAd"] = UNSET
    duration: Union[Unset, int] = UNSET
    thumbnail: Union[Unset, str] = UNSET
    links: Union[Unset, "NewsVideoLinks"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        source = self.source

        headline = self.headline

        caption = self.caption

        description = self.description

        premium = self.premium

        ad: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ad, Unset):
            ad = self.ad.to_dict()

        duration = self.duration

        thumbnail = self.thumbnail

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if source is not UNSET:
            field_dict["source"] = source
        if headline is not UNSET:
            field_dict["headline"] = headline
        if caption is not UNSET:
            field_dict["caption"] = caption
        if description is not UNSET:
            field_dict["description"] = description
        if premium is not UNSET:
            field_dict["premium"] = premium
        if ad is not UNSET:
            field_dict["ad"] = ad
        if duration is not UNSET:
            field_dict["duration"] = duration
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.news_video_ad import NewsVideoAd
        from ..models.news_video_links import NewsVideoLinks

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        source = d.pop("source", UNSET)

        headline = d.pop("headline", UNSET)

        caption = d.pop("caption", UNSET)

        description = d.pop("description", UNSET)

        premium = d.pop("premium", UNSET)

        _ad = d.pop("ad", UNSET)
        ad: Union[Unset, NewsVideoAd]
        if isinstance(_ad, Unset):
            ad = UNSET
        else:
            ad = NewsVideoAd.from_dict(_ad)

        duration = d.pop("duration", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, NewsVideoLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = NewsVideoLinks.from_dict(_links)

        news_video = cls(
            id=id,
            source=source,
            headline=headline,
            caption=caption,
            description=description,
            premium=premium,
            ad=ad,
            duration=duration,
            thumbnail=thumbnail,
            links=links,
        )

        news_video.additional_properties = d
        return news_video

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
