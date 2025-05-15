import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image import Image
    from ..models.news_category import NewsCategory
    from ..models.video_ad_details import VideoAdDetails
    from ..models.video_device_restrictions import VideoDeviceRestrictions
    from ..models.video_geo_restrictions import VideoGeoRestrictions
    from ..models.video_links import VideoLinks
    from ..models.video_poster_images import VideoPosterImages
    from ..models.video_time_restrictions import VideoTimeRestrictions
    from ..models.video_tracking_details import VideoTrackingDetails


T = TypeVar("T", bound="VideoItem")


@_attrs_define
class VideoItem:
    """Detailed information about a video.

    Attributes:
        source (Union[None, Unset, str]):  Example: espn.
        id (Union[Unset, int]):  Example: 45014514.
        headline (Union[None, Unset, str]):
        title (Union[None, Unset, str]):
        caption (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        premium (Union[None, Unset, bool]):
        ad (Union[Unset, VideoAdDetails]):
        tracking (Union[Unset, VideoTrackingDetails]):
        cerebro_id (Union[None, Unset, str]):
        last_modified (Union[None, Unset, datetime.datetime]):
        original_publish_date (Union[None, Unset, datetime.datetime]):
        time_restrictions (Union[Unset, VideoTimeRestrictions]):
        device_restrictions (Union[Unset, VideoDeviceRestrictions]):
        geo_restrictions (Union[Unset, VideoGeoRestrictions]):
        syndicatable (Union[None, Unset, bool]):
        duration (Union[None, Unset, int]):
        categories (Union[List['NewsCategory'], None, Unset]):
        poster_images (Union[Unset, VideoPosterImages]):
        images (Union[List['Image'], None, Unset]):
        thumbnail (Union[None, Unset, str]):
        links (Union[Unset, VideoLinks]):
    """

    source: Union[None, Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    headline: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    caption: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    premium: Union[None, Unset, bool] = UNSET
    ad: Union[Unset, "VideoAdDetails"] = UNSET
    tracking: Union[Unset, "VideoTrackingDetails"] = UNSET
    cerebro_id: Union[None, Unset, str] = UNSET
    last_modified: Union[None, Unset, datetime.datetime] = UNSET
    original_publish_date: Union[None, Unset, datetime.datetime] = UNSET
    time_restrictions: Union[Unset, "VideoTimeRestrictions"] = UNSET
    device_restrictions: Union[Unset, "VideoDeviceRestrictions"] = UNSET
    geo_restrictions: Union[Unset, "VideoGeoRestrictions"] = UNSET
    syndicatable: Union[None, Unset, bool] = UNSET
    duration: Union[None, Unset, int] = UNSET
    categories: Union[List["NewsCategory"], None, Unset] = UNSET
    poster_images: Union[Unset, "VideoPosterImages"] = UNSET
    images: Union[List["Image"], None, Unset] = UNSET
    thumbnail: Union[None, Unset, str] = UNSET
    links: Union[Unset, "VideoLinks"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source: Union[None, Unset, str]
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        id = self.id

        headline: Union[None, Unset, str]
        if isinstance(self.headline, Unset):
            headline = UNSET
        else:
            headline = self.headline

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        caption: Union[None, Unset, str]
        if isinstance(self.caption, Unset):
            caption = UNSET
        else:
            caption = self.caption

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        premium: Union[None, Unset, bool]
        if isinstance(self.premium, Unset):
            premium = UNSET
        else:
            premium = self.premium

        ad: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ad, Unset):
            ad = self.ad.to_dict()

        tracking: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tracking, Unset):
            tracking = self.tracking.to_dict()

        cerebro_id: Union[None, Unset, str]
        if isinstance(self.cerebro_id, Unset):
            cerebro_id = UNSET
        else:
            cerebro_id = self.cerebro_id

        last_modified: Union[None, Unset, str]
        if isinstance(self.last_modified, Unset):
            last_modified = UNSET
        elif isinstance(self.last_modified, datetime.datetime):
            last_modified = self.last_modified.isoformat()
        else:
            last_modified = self.last_modified

        original_publish_date: Union[None, Unset, str]
        if isinstance(self.original_publish_date, Unset):
            original_publish_date = UNSET
        elif isinstance(self.original_publish_date, datetime.datetime):
            original_publish_date = self.original_publish_date.isoformat()
        else:
            original_publish_date = self.original_publish_date

        time_restrictions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_restrictions, Unset):
            time_restrictions = self.time_restrictions.to_dict()

        device_restrictions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.device_restrictions, Unset):
            device_restrictions = self.device_restrictions.to_dict()

        geo_restrictions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.geo_restrictions, Unset):
            geo_restrictions = self.geo_restrictions.to_dict()

        syndicatable: Union[None, Unset, bool]
        if isinstance(self.syndicatable, Unset):
            syndicatable = UNSET
        else:
            syndicatable = self.syndicatable

        duration: Union[None, Unset, int]
        if isinstance(self.duration, Unset):
            duration = UNSET
        else:
            duration = self.duration

        categories: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.categories, Unset):
            categories = UNSET
        elif isinstance(self.categories, list):
            categories = []
            for categories_type_0_item_data in self.categories:
                categories_type_0_item = categories_type_0_item_data.to_dict()
                categories.append(categories_type_0_item)

        else:
            categories = self.categories

        poster_images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.poster_images, Unset):
            poster_images = self.poster_images.to_dict()

        images: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.images, Unset):
            images = UNSET
        elif isinstance(self.images, list):
            images = []
            for images_type_0_item_data in self.images:
                images_type_0_item = images_type_0_item_data.to_dict()
                images.append(images_type_0_item)

        else:
            images = self.images

        thumbnail: Union[None, Unset, str]
        if isinstance(self.thumbnail, Unset):
            thumbnail = UNSET
        else:
            thumbnail = self.thumbnail

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if id is not UNSET:
            field_dict["id"] = id
        if headline is not UNSET:
            field_dict["headline"] = headline
        if title is not UNSET:
            field_dict["title"] = title
        if caption is not UNSET:
            field_dict["caption"] = caption
        if description is not UNSET:
            field_dict["description"] = description
        if premium is not UNSET:
            field_dict["premium"] = premium
        if ad is not UNSET:
            field_dict["ad"] = ad
        if tracking is not UNSET:
            field_dict["tracking"] = tracking
        if cerebro_id is not UNSET:
            field_dict["cerebroId"] = cerebro_id
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if original_publish_date is not UNSET:
            field_dict["originalPublishDate"] = original_publish_date
        if time_restrictions is not UNSET:
            field_dict["timeRestrictions"] = time_restrictions
        if device_restrictions is not UNSET:
            field_dict["deviceRestrictions"] = device_restrictions
        if geo_restrictions is not UNSET:
            field_dict["geoRestrictions"] = geo_restrictions
        if syndicatable is not UNSET:
            field_dict["syndicatable"] = syndicatable
        if duration is not UNSET:
            field_dict["duration"] = duration
        if categories is not UNSET:
            field_dict["categories"] = categories
        if poster_images is not UNSET:
            field_dict["posterImages"] = poster_images
        if images is not UNSET:
            field_dict["images"] = images
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image import Image
        from ..models.news_category import NewsCategory
        from ..models.video_ad_details import VideoAdDetails
        from ..models.video_device_restrictions import VideoDeviceRestrictions
        from ..models.video_geo_restrictions import VideoGeoRestrictions
        from ..models.video_links import VideoLinks
        from ..models.video_poster_images import VideoPosterImages
        from ..models.video_time_restrictions import VideoTimeRestrictions
        from ..models.video_tracking_details import VideoTrackingDetails

        d = src_dict.copy()

        def _parse_source(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source = _parse_source(d.pop("source", UNSET))

        id = d.pop("id", UNSET)

        def _parse_headline(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        headline = _parse_headline(d.pop("headline", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_caption(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        caption = _parse_caption(d.pop("caption", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_premium(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        premium = _parse_premium(d.pop("premium", UNSET))

        _ad = d.pop("ad", UNSET)
        ad: Union[Unset, VideoAdDetails]
        if isinstance(_ad, Unset):
            ad = UNSET
        else:
            ad = VideoAdDetails.from_dict(_ad)

        _tracking = d.pop("tracking", UNSET)
        tracking: Union[Unset, VideoTrackingDetails]
        if isinstance(_tracking, Unset):
            tracking = UNSET
        else:
            tracking = VideoTrackingDetails.from_dict(_tracking)

        def _parse_cerebro_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cerebro_id = _parse_cerebro_id(d.pop("cerebroId", UNSET))

        def _parse_last_modified(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_modified_type_0 = isoparse(data)

                return last_modified_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_modified = _parse_last_modified(d.pop("lastModified", UNSET))

        def _parse_original_publish_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                original_publish_date_type_0 = isoparse(data)

                return original_publish_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        original_publish_date = _parse_original_publish_date(d.pop("originalPublishDate", UNSET))

        _time_restrictions = d.pop("timeRestrictions", UNSET)
        time_restrictions: Union[Unset, VideoTimeRestrictions]
        if isinstance(_time_restrictions, Unset):
            time_restrictions = UNSET
        else:
            time_restrictions = VideoTimeRestrictions.from_dict(_time_restrictions)

        _device_restrictions = d.pop("deviceRestrictions", UNSET)
        device_restrictions: Union[Unset, VideoDeviceRestrictions]
        if isinstance(_device_restrictions, Unset):
            device_restrictions = UNSET
        else:
            device_restrictions = VideoDeviceRestrictions.from_dict(_device_restrictions)

        _geo_restrictions = d.pop("geoRestrictions", UNSET)
        geo_restrictions: Union[Unset, VideoGeoRestrictions]
        if isinstance(_geo_restrictions, Unset):
            geo_restrictions = UNSET
        else:
            geo_restrictions = VideoGeoRestrictions.from_dict(_geo_restrictions)

        def _parse_syndicatable(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        syndicatable = _parse_syndicatable(d.pop("syndicatable", UNSET))

        def _parse_duration(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        duration = _parse_duration(d.pop("duration", UNSET))

        def _parse_categories(data: object) -> Union[List["NewsCategory"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = []
                _categories_type_0 = data
                for categories_type_0_item_data in _categories_type_0:
                    categories_type_0_item = NewsCategory.from_dict(categories_type_0_item_data)

                    categories_type_0.append(categories_type_0_item)

                return categories_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["NewsCategory"], None, Unset], data)

        categories = _parse_categories(d.pop("categories", UNSET))

        _poster_images = d.pop("posterImages", UNSET)
        poster_images: Union[Unset, VideoPosterImages]
        if isinstance(_poster_images, Unset):
            poster_images = UNSET
        else:
            poster_images = VideoPosterImages.from_dict(_poster_images)

        def _parse_images(data: object) -> Union[List["Image"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                images_type_0 = []
                _images_type_0 = data
                for images_type_0_item_data in _images_type_0:
                    images_type_0_item = Image.from_dict(images_type_0_item_data)

                    images_type_0.append(images_type_0_item)

                return images_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["Image"], None, Unset], data)

        images = _parse_images(d.pop("images", UNSET))

        def _parse_thumbnail(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        thumbnail = _parse_thumbnail(d.pop("thumbnail", UNSET))

        _links = d.pop("links", UNSET)
        links: Union[Unset, VideoLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = VideoLinks.from_dict(_links)

        video_item = cls(
            source=source,
            id=id,
            headline=headline,
            title=title,
            caption=caption,
            description=description,
            premium=premium,
            ad=ad,
            tracking=tracking,
            cerebro_id=cerebro_id,
            last_modified=last_modified,
            original_publish_date=original_publish_date,
            time_restrictions=time_restrictions,
            device_restrictions=device_restrictions,
            geo_restrictions=geo_restrictions,
            syndicatable=syndicatable,
            duration=duration,
            categories=categories,
            poster_images=poster_images,
            images=images,
            thumbnail=thumbnail,
            links=links,
        )

        video_item.additional_properties = d
        return video_item

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
