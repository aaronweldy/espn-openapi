from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contributor_info import ContributorInfo
    from ..models.feed_category import FeedCategory
    from ..models.feed_item_attributes import FeedItemAttributes
    from ..models.feed_item_dates import FeedItemDates
    from ..models.feed_item_descriptions import FeedItemDescriptions
    from ..models.feed_item_ids import FeedItemIds
    from ..models.flex_image import FlexImage
    from ..models.flex_link import FlexLink


T = TypeVar("T", bound="FeedItem")


@_attrs_define
class FeedItem:
    """
    Attributes:
        id (str):
        type (str): Content type (e.g., shortstop)
        ids (Union[Unset, FeedItemIds]):
        dates (Union[Unset, FeedItemDates]):
        descriptions (Union[Unset, FeedItemDescriptions]):
        payload (Union[Unset, str]):
        images (Union[Unset, List['FlexImage']]):
        contributors (Union[Unset, List['ContributorInfo']]):
        categories (Union[Unset, List['FeedCategory']]):
        attributes (Union[Unset, FeedItemAttributes]):
        locales (Union[Unset, List[str]]):
        links (Union[Unset, List['FlexLink']]):
    """

    id: str
    type: str
    ids: Union[Unset, "FeedItemIds"] = UNSET
    dates: Union[Unset, "FeedItemDates"] = UNSET
    descriptions: Union[Unset, "FeedItemDescriptions"] = UNSET
    payload: Union[Unset, str] = UNSET
    images: Union[Unset, List["FlexImage"]] = UNSET
    contributors: Union[Unset, List["ContributorInfo"]] = UNSET
    categories: Union[Unset, List["FeedCategory"]] = UNSET
    attributes: Union[Unset, "FeedItemAttributes"] = UNSET
    locales: Union[Unset, List[str]] = UNSET
    links: Union[Unset, List["FlexLink"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type

        ids: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids.to_dict()

        dates: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dates, Unset):
            dates = self.dates.to_dict()

        descriptions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.descriptions, Unset):
            descriptions = self.descriptions.to_dict()

        payload = self.payload

        images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        contributors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contributors, Unset):
            contributors = []
            for contributors_item_data in self.contributors:
                contributors_item = contributors_item_data.to_dict()
                contributors.append(contributors_item)

        categories: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        locales: Union[Unset, List[str]] = UNSET
        if not isinstance(self.locales, Unset):
            locales = self.locales

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
            }
        )
        if ids is not UNSET:
            field_dict["ids"] = ids
        if dates is not UNSET:
            field_dict["dates"] = dates
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if payload is not UNSET:
            field_dict["payload"] = payload
        if images is not UNSET:
            field_dict["images"] = images
        if contributors is not UNSET:
            field_dict["contributors"] = contributors
        if categories is not UNSET:
            field_dict["categories"] = categories
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if locales is not UNSET:
            field_dict["locales"] = locales
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contributor_info import ContributorInfo
        from ..models.feed_category import FeedCategory
        from ..models.feed_item_attributes import FeedItemAttributes
        from ..models.feed_item_dates import FeedItemDates
        from ..models.feed_item_descriptions import FeedItemDescriptions
        from ..models.feed_item_ids import FeedItemIds
        from ..models.flex_image import FlexImage
        from ..models.flex_link import FlexLink

        d = src_dict.copy()
        id = d.pop("id")

        type = d.pop("type")

        _ids = d.pop("ids", UNSET)
        ids: Union[Unset, FeedItemIds]
        if isinstance(_ids, Unset):
            ids = UNSET
        else:
            ids = FeedItemIds.from_dict(_ids)

        _dates = d.pop("dates", UNSET)
        dates: Union[Unset, FeedItemDates]
        if isinstance(_dates, Unset):
            dates = UNSET
        else:
            dates = FeedItemDates.from_dict(_dates)

        _descriptions = d.pop("descriptions", UNSET)
        descriptions: Union[Unset, FeedItemDescriptions]
        if isinstance(_descriptions, Unset):
            descriptions = UNSET
        else:
            descriptions = FeedItemDescriptions.from_dict(_descriptions)

        payload = d.pop("payload", UNSET)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = FlexImage.from_dict(images_item_data)

            images.append(images_item)

        contributors = []
        _contributors = d.pop("contributors", UNSET)
        for contributors_item_data in _contributors or []:
            contributors_item = ContributorInfo.from_dict(contributors_item_data)

            contributors.append(contributors_item)

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = FeedCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, FeedItemAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = FeedItemAttributes.from_dict(_attributes)

        locales = cast(List[str], d.pop("locales", UNSET))

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = FlexLink.from_dict(links_item_data)

            links.append(links_item)

        feed_item = cls(
            id=id,
            type=type,
            ids=ids,
            dates=dates,
            descriptions=descriptions,
            payload=payload,
            images=images,
            contributors=contributors,
            categories=categories,
            attributes=attributes,
            locales=locales,
            links=links,
        )

        feed_item.additional_properties = d
        return feed_item

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
