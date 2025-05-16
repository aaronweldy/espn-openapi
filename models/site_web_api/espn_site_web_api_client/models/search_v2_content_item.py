import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_v2_content_item_categories_type_0_item import SearchV2ContentItemCategoriesType0Item
    from ..models.search_v2_content_item_image_type_0 import SearchV2ContentItemImageType0
    from ..models.search_v2_content_item_images_type_0_item import SearchV2ContentItemImagesType0Item
    from ..models.search_v2_content_item_link import SearchV2ContentItemLink


T = TypeVar("T", bound="SearchV2ContentItem")


@_attrs_define
class SearchV2ContentItem:
    """
    Attributes:
        id (str):
        type (str):
        display_name (str):
        link (SearchV2ContentItemLink):
        uid (Union[None, Unset, str]):
        guid (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        subtitle (Union[None, Unset, str]):
        image (Union['SearchV2ContentItemImageType0', None, Unset]):
        images (Union[List['SearchV2ContentItemImagesType0Item'], None, Unset]):
        default_league_slug (Union[None, Unset, str]):
        sport (Union[None, Unset, str]):
        byline (Union[None, Unset, str]):
        date (Union[None, Unset, datetime.datetime]):
        is_premium (Union[None, Unset, bool]):
        categories (Union[List['SearchV2ContentItemCategoriesType0Item'], None, Unset]):
        now_id (Union[None, Unset, str]):
        status (Union[None, Unset, str]):
    """

    id: str
    type: str
    display_name: str
    link: "SearchV2ContentItemLink"
    uid: Union[None, Unset, str] = UNSET
    guid: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    subtitle: Union[None, Unset, str] = UNSET
    image: Union["SearchV2ContentItemImageType0", None, Unset] = UNSET
    images: Union[List["SearchV2ContentItemImagesType0Item"], None, Unset] = UNSET
    default_league_slug: Union[None, Unset, str] = UNSET
    sport: Union[None, Unset, str] = UNSET
    byline: Union[None, Unset, str] = UNSET
    date: Union[None, Unset, datetime.datetime] = UNSET
    is_premium: Union[None, Unset, bool] = UNSET
    categories: Union[List["SearchV2ContentItemCategoriesType0Item"], None, Unset] = UNSET
    now_id: Union[None, Unset, str] = UNSET
    status: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.search_v2_content_item_image_type_0 import SearchV2ContentItemImageType0

        id = self.id

        type = self.type

        display_name = self.display_name

        link = self.link.to_dict()

        uid: Union[None, Unset, str]
        if isinstance(self.uid, Unset):
            uid = UNSET
        else:
            uid = self.uid

        guid: Union[None, Unset, str]
        if isinstance(self.guid, Unset):
            guid = UNSET
        else:
            guid = self.guid

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        subtitle: Union[None, Unset, str]
        if isinstance(self.subtitle, Unset):
            subtitle = UNSET
        else:
            subtitle = self.subtitle

        image: Union[Dict[str, Any], None, Unset]
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, SearchV2ContentItemImageType0):
            image = self.image.to_dict()
        else:
            image = self.image

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

        default_league_slug: Union[None, Unset, str]
        if isinstance(self.default_league_slug, Unset):
            default_league_slug = UNSET
        else:
            default_league_slug = self.default_league_slug

        sport: Union[None, Unset, str]
        if isinstance(self.sport, Unset):
            sport = UNSET
        else:
            sport = self.sport

        byline: Union[None, Unset, str]
        if isinstance(self.byline, Unset):
            byline = UNSET
        else:
            byline = self.byline

        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        is_premium: Union[None, Unset, bool]
        if isinstance(self.is_premium, Unset):
            is_premium = UNSET
        else:
            is_premium = self.is_premium

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

        now_id: Union[None, Unset, str]
        if isinstance(self.now_id, Unset):
            now_id = UNSET
        else:
            now_id = self.now_id

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "displayName": display_name,
                "link": link,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if guid is not UNSET:
            field_dict["guid"] = guid
        if description is not UNSET:
            field_dict["description"] = description
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if image is not UNSET:
            field_dict["image"] = image
        if images is not UNSET:
            field_dict["images"] = images
        if default_league_slug is not UNSET:
            field_dict["defaultLeagueSlug"] = default_league_slug
        if sport is not UNSET:
            field_dict["sport"] = sport
        if byline is not UNSET:
            field_dict["byline"] = byline
        if date is not UNSET:
            field_dict["date"] = date
        if is_premium is not UNSET:
            field_dict["isPremium"] = is_premium
        if categories is not UNSET:
            field_dict["categories"] = categories
        if now_id is not UNSET:
            field_dict["nowId"] = now_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_v2_content_item_categories_type_0_item import SearchV2ContentItemCategoriesType0Item
        from ..models.search_v2_content_item_image_type_0 import SearchV2ContentItemImageType0
        from ..models.search_v2_content_item_images_type_0_item import SearchV2ContentItemImagesType0Item
        from ..models.search_v2_content_item_link import SearchV2ContentItemLink

        d = src_dict.copy()
        id = d.pop("id")

        type = d.pop("type")

        display_name = d.pop("displayName")

        link = SearchV2ContentItemLink.from_dict(d.pop("link"))

        def _parse_uid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        uid = _parse_uid(d.pop("uid", UNSET))

        def _parse_guid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        guid = _parse_guid(d.pop("guid", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_subtitle(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subtitle = _parse_subtitle(d.pop("subtitle", UNSET))

        def _parse_image(data: object) -> Union["SearchV2ContentItemImageType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_type_0 = SearchV2ContentItemImageType0.from_dict(data)

                return image_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SearchV2ContentItemImageType0", None, Unset], data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_images(data: object) -> Union[List["SearchV2ContentItemImagesType0Item"], None, Unset]:
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
                    images_type_0_item = SearchV2ContentItemImagesType0Item.from_dict(images_type_0_item_data)

                    images_type_0.append(images_type_0_item)

                return images_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["SearchV2ContentItemImagesType0Item"], None, Unset], data)

        images = _parse_images(d.pop("images", UNSET))

        def _parse_default_league_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default_league_slug = _parse_default_league_slug(d.pop("defaultLeagueSlug", UNSET))

        def _parse_sport(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sport = _parse_sport(d.pop("sport", UNSET))

        def _parse_byline(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        byline = _parse_byline(d.pop("byline", UNSET))

        def _parse_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data)

                return date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_is_premium(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_premium = _parse_is_premium(d.pop("isPremium", UNSET))

        def _parse_categories(data: object) -> Union[List["SearchV2ContentItemCategoriesType0Item"], None, Unset]:
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
                    categories_type_0_item = SearchV2ContentItemCategoriesType0Item.from_dict(
                        categories_type_0_item_data
                    )

                    categories_type_0.append(categories_type_0_item)

                return categories_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["SearchV2ContentItemCategoriesType0Item"], None, Unset], data)

        categories = _parse_categories(d.pop("categories", UNSET))

        def _parse_now_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        now_id = _parse_now_id(d.pop("nowId", UNSET))

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

        search_v2_content_item = cls(
            id=id,
            type=type,
            display_name=display_name,
            link=link,
            uid=uid,
            guid=guid,
            description=description,
            subtitle=subtitle,
            image=image,
            images=images,
            default_league_slug=default_league_slug,
            sport=sport,
            byline=byline,
            date=date,
            is_premium=is_premium,
            categories=categories,
            now_id=now_id,
            status=status,
        )

        search_v2_content_item.additional_properties = d
        return search_v2_content_item

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
