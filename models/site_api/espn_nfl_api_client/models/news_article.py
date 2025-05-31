import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.news_article_type import NewsArticleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.news_article_image import NewsArticleImage
    from ..models.news_article_links import NewsArticleLinks
    from ..models.news_category import NewsCategory


T = TypeVar("T", bound="NewsArticle")


@_attrs_define
class NewsArticle:
    """
    Attributes:
        id (int): Unique identifier for the article Example: 45184227.
        now_id (str): ID used for the 'now' platform Example: 1-45184227.
        content_key (str): Content identification key Example: 45184227-1-5-1.
        data_source_identifier (str): Data source identifier Example: 7be1db4ba2243.
        type (NewsArticleType): Type of article content Example: HeadlineNews.
        headline (str): Article headline Example: Ravens sign veteran nose tackle John Jenkins.
        last_modified (datetime.datetime): Last time the article was modified Example: 2025-05-17T01:27:10Z.
        published (datetime.datetime): When the article was published Example: 2025-05-17T01:03:00Z.
        images (List['NewsArticleImage']): Images associated with the article
        categories (List['NewsCategory']): Categories the article belongs to
        premium (bool): Whether the article is premium content
        links (NewsArticleLinks):
        description (Union[Unset, str]): Brief summary of the article Example: The Ravens on Friday signed journeyman
            nose tackle John Jenkins, who most recently played two seasons for the Raiders..
        byline (Union[Unset, str]): Author of the article Example: Jamison Hensley.
    """

    id: int
    now_id: str
    content_key: str
    data_source_identifier: str
    type: NewsArticleType
    headline: str
    last_modified: datetime.datetime
    published: datetime.datetime
    images: List["NewsArticleImage"]
    categories: List["NewsCategory"]
    premium: bool
    links: "NewsArticleLinks"
    description: Union[Unset, str] = UNSET
    byline: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        now_id = self.now_id

        content_key = self.content_key

        data_source_identifier = self.data_source_identifier

        type = self.type.value

        headline = self.headline

        last_modified = self.last_modified.isoformat()

        published = self.published.isoformat()

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        premium = self.premium

        links = self.links.to_dict()

        description = self.description

        byline = self.byline

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "nowId": now_id,
                "contentKey": content_key,
                "dataSourceIdentifier": data_source_identifier,
                "type": type,
                "headline": headline,
                "lastModified": last_modified,
                "published": published,
                "images": images,
                "categories": categories,
                "premium": premium,
                "links": links,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if byline is not UNSET:
            field_dict["byline"] = byline

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.news_article_image import NewsArticleImage
        from ..models.news_article_links import NewsArticleLinks
        from ..models.news_category import NewsCategory

        d = src_dict.copy()
        id = d.pop("id")

        now_id = d.pop("nowId")

        content_key = d.pop("contentKey")

        data_source_identifier = d.pop("dataSourceIdentifier")

        type = NewsArticleType(d.pop("type"))

        headline = d.pop("headline")

        last_modified = isoparse(d.pop("lastModified"))

        published = isoparse(d.pop("published"))

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = NewsArticleImage.from_dict(images_item_data)

            images.append(images_item)

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = NewsCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        premium = d.pop("premium")

        links = NewsArticleLinks.from_dict(d.pop("links"))

        description = d.pop("description", UNSET)

        byline = d.pop("byline", UNSET)

        news_article = cls(
            id=id,
            now_id=now_id,
            content_key=content_key,
            data_source_identifier=data_source_identifier,
            type=type,
            headline=headline,
            last_modified=last_modified,
            published=published,
            images=images,
            categories=categories,
            premium=premium,
            links=links,
            description=description,
            byline=byline,
        )

        news_article.additional_properties = d
        return news_article

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
