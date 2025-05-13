import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.article_image import ArticleImage
    from ..models.article_links import ArticleLinks
    from ..models.category import Category


T = TypeVar("T", bound="Article")


@_attrs_define
class Article:
    """
    Attributes:
        id (int): Unique identifier for the article
        headline (str): Article headline/title
        description (str): Brief summary or description of the article
        published (datetime.datetime): When the article was first published
        now_id (Union[Unset, str]): Alternative identifier
        content_key (Union[Unset, str]): Content identifier key
        data_source_identifier (Union[Unset, str]): Data source identifier
        byline (Union[Unset, str]): Author of the article
        type (Union[Unset, str]): Type of content (e.g., "Story", "HeadlineNews", "Video")
        premium (Union[Unset, bool]): Whether the content is premium/subscription content
        last_modified (Union[Unset, datetime.datetime]): When the article was last modified
        images (Union[Unset, List['ArticleImage']]):
        links (Union[Unset, ArticleLinks]):
        categories (Union[Unset, List['Category']]):
    """

    id: int
    headline: str
    description: str
    published: datetime.datetime
    now_id: Union[Unset, str] = UNSET
    content_key: Union[Unset, str] = UNSET
    data_source_identifier: Union[Unset, str] = UNSET
    byline: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    premium: Union[Unset, bool] = UNSET
    last_modified: Union[Unset, datetime.datetime] = UNSET
    images: Union[Unset, List["ArticleImage"]] = UNSET
    links: Union[Unset, "ArticleLinks"] = UNSET
    categories: Union[Unset, List["Category"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        headline = self.headline

        description = self.description

        published = self.published.isoformat()

        now_id = self.now_id

        content_key = self.content_key

        data_source_identifier = self.data_source_identifier

        byline = self.byline

        type = self.type

        premium = self.premium

        last_modified: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

        images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        categories: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "headline": headline,
                "description": description,
                "published": published,
            }
        )
        if now_id is not UNSET:
            field_dict["nowId"] = now_id
        if content_key is not UNSET:
            field_dict["contentKey"] = content_key
        if data_source_identifier is not UNSET:
            field_dict["dataSourceIdentifier"] = data_source_identifier
        if byline is not UNSET:
            field_dict["byline"] = byline
        if type is not UNSET:
            field_dict["type"] = type
        if premium is not UNSET:
            field_dict["premium"] = premium
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if images is not UNSET:
            field_dict["images"] = images
        if links is not UNSET:
            field_dict["links"] = links
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.article_image import ArticleImage
        from ..models.article_links import ArticleLinks
        from ..models.category import Category

        d = src_dict.copy()
        id = d.pop("id")

        headline = d.pop("headline")

        description = d.pop("description")

        published = isoparse(d.pop("published"))

        now_id = d.pop("nowId", UNSET)

        content_key = d.pop("contentKey", UNSET)

        data_source_identifier = d.pop("dataSourceIdentifier", UNSET)

        byline = d.pop("byline", UNSET)

        type = d.pop("type", UNSET)

        premium = d.pop("premium", UNSET)

        _last_modified = d.pop("lastModified", UNSET)
        last_modified: Union[Unset, datetime.datetime]
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = isoparse(_last_modified)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = ArticleImage.from_dict(images_item_data)

            images.append(images_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ArticleLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ArticleLinks.from_dict(_links)

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = Category.from_dict(categories_item_data)

            categories.append(categories_item)

        article = cls(
            id=id,
            headline=headline,
            description=description,
            published=published,
            now_id=now_id,
            content_key=content_key,
            data_source_identifier=data_source_identifier,
            byline=byline,
            type=type,
            premium=premium,
            last_modified=last_modified,
            images=images,
            links=links,
            categories=categories,
        )

        article.additional_properties = d
        return article

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
