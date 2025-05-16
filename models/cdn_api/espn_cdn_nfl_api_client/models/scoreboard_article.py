from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_article_links import ScoreboardArticleLinks
    from ..models.scoreboard_category import ScoreboardCategory
    from ..models.scoreboard_image import ScoreboardImage


T = TypeVar("T", bound="ScoreboardArticle")


@_attrs_define
class ScoreboardArticle:
    """
    Attributes:
        content_key (Union[Unset, str]):
        images (Union[Unset, List['ScoreboardImage']]):
        data_source_identifier (Union[Unset, str]):
        description (Union[Unset, str]):
        published (Union[Unset, str]):
        type (Union[Unset, str]):
        now_id (Union[Unset, str]):
        premium (Union[Unset, bool]):
        links (Union[Unset, ScoreboardArticleLinks]):
        id (Union[Unset, int]):
        last_modified (Union[Unset, str]):
        categories (Union[Unset, List['ScoreboardCategory']]):
        headline (Union[Unset, str]):
        byline (Union[Unset, str]):
    """

    content_key: Union[Unset, str] = UNSET
    images: Union[Unset, List["ScoreboardImage"]] = UNSET
    data_source_identifier: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    published: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    now_id: Union[Unset, str] = UNSET
    premium: Union[Unset, bool] = UNSET
    links: Union[Unset, "ScoreboardArticleLinks"] = UNSET
    id: Union[Unset, int] = UNSET
    last_modified: Union[Unset, str] = UNSET
    categories: Union[Unset, List["ScoreboardCategory"]] = UNSET
    headline: Union[Unset, str] = UNSET
    byline: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_key = self.content_key

        images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        data_source_identifier = self.data_source_identifier

        description = self.description

        published = self.published

        type = self.type

        now_id = self.now_id

        premium = self.premium

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        id = self.id

        last_modified = self.last_modified

        categories: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        headline = self.headline

        byline = self.byline

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_key is not UNSET:
            field_dict["contentKey"] = content_key
        if images is not UNSET:
            field_dict["images"] = images
        if data_source_identifier is not UNSET:
            field_dict["dataSourceIdentifier"] = data_source_identifier
        if description is not UNSET:
            field_dict["description"] = description
        if published is not UNSET:
            field_dict["published"] = published
        if type is not UNSET:
            field_dict["type"] = type
        if now_id is not UNSET:
            field_dict["nowId"] = now_id
        if premium is not UNSET:
            field_dict["premium"] = premium
        if links is not UNSET:
            field_dict["links"] = links
        if id is not UNSET:
            field_dict["id"] = id
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if categories is not UNSET:
            field_dict["categories"] = categories
        if headline is not UNSET:
            field_dict["headline"] = headline
        if byline is not UNSET:
            field_dict["byline"] = byline

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_article_links import ScoreboardArticleLinks
        from ..models.scoreboard_category import ScoreboardCategory
        from ..models.scoreboard_image import ScoreboardImage

        d = src_dict.copy()
        content_key = d.pop("contentKey", UNSET)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = ScoreboardImage.from_dict(images_item_data)

            images.append(images_item)

        data_source_identifier = d.pop("dataSourceIdentifier", UNSET)

        description = d.pop("description", UNSET)

        published = d.pop("published", UNSET)

        type = d.pop("type", UNSET)

        now_id = d.pop("nowId", UNSET)

        premium = d.pop("premium", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ScoreboardArticleLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ScoreboardArticleLinks.from_dict(_links)

        id = d.pop("id", UNSET)

        last_modified = d.pop("lastModified", UNSET)

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = ScoreboardCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        headline = d.pop("headline", UNSET)

        byline = d.pop("byline", UNSET)

        scoreboard_article = cls(
            content_key=content_key,
            images=images,
            data_source_identifier=data_source_identifier,
            description=description,
            published=published,
            type=type,
            now_id=now_id,
            premium=premium,
            links=links,
            id=id,
            last_modified=last_modified,
            categories=categories,
            headline=headline,
            byline=byline,
        )

        scoreboard_article.additional_properties = d
        return scoreboard_article

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
