import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.news_category import NewsCategory
    from ..models.news_image import NewsImage
    from ..models.news_links import NewsLinks
    from ..models.news_metric import NewsMetric
    from ..models.news_related import NewsRelated
    from ..models.news_video import NewsVideo


T = TypeVar("T", bound="NewsHeadline")


@_attrs_define
class NewsHeadline:
    """
    Attributes:
        id (int): Unique identifier for the headline
        headline (str): The headline text
        type (str): Type of content Example: story.
        title (Union[Unset, str]): The article title
        description (Union[Unset, str]): Brief description of the article
        published (Union[Unset, datetime.datetime]): Publication date
        last_modified (Union[Unset, datetime.datetime]): Last modification date
        originally_posted (Union[Unset, datetime.datetime]): Original posting date
        premium (Union[Unset, bool]): Whether this is premium content
        links (Union[Unset, NewsLinks]):
        images (Union[Unset, List['NewsImage']]):
        video (Union[Unset, List['NewsVideo']]):
        categories (Union[Unset, List['NewsCategory']]):
        related (Union[Unset, List['NewsRelated']]):
        keywords (Union[Unset, List[str]]):
        allow_search (Union[Unset, bool]):
        allow_amp (Union[Unset, bool]):
        allow_ads (Union[Unset, bool]):
        allow_comments (Union[Unset, bool]):
        allow_commerce (Union[Unset, bool]):
        allow_content_reactions (Union[Unset, bool]):
        link_text (Union[Unset, str]):
        source (Union[Unset, str]):
        now_id (Union[Unset, str]):
        data_source_identifier (Union[Unset, str]):
        metrics (Union[Unset, List['NewsMetric']]):
        story (Union[Unset, str]): Full story text
    """

    id: int
    headline: str
    type: str
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    published: Union[Unset, datetime.datetime] = UNSET
    last_modified: Union[Unset, datetime.datetime] = UNSET
    originally_posted: Union[Unset, datetime.datetime] = UNSET
    premium: Union[Unset, bool] = UNSET
    links: Union[Unset, "NewsLinks"] = UNSET
    images: Union[Unset, List["NewsImage"]] = UNSET
    video: Union[Unset, List["NewsVideo"]] = UNSET
    categories: Union[Unset, List["NewsCategory"]] = UNSET
    related: Union[Unset, List["NewsRelated"]] = UNSET
    keywords: Union[Unset, List[str]] = UNSET
    allow_search: Union[Unset, bool] = UNSET
    allow_amp: Union[Unset, bool] = UNSET
    allow_ads: Union[Unset, bool] = UNSET
    allow_comments: Union[Unset, bool] = UNSET
    allow_commerce: Union[Unset, bool] = UNSET
    allow_content_reactions: Union[Unset, bool] = UNSET
    link_text: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    now_id: Union[Unset, str] = UNSET
    data_source_identifier: Union[Unset, str] = UNSET
    metrics: Union[Unset, List["NewsMetric"]] = UNSET
    story: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        headline = self.headline

        type = self.type

        title = self.title

        description = self.description

        published: Union[Unset, str] = UNSET
        if not isinstance(self.published, Unset):
            published = self.published.isoformat()

        last_modified: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

        originally_posted: Union[Unset, str] = UNSET
        if not isinstance(self.originally_posted, Unset):
            originally_posted = self.originally_posted.isoformat()

        premium = self.premium

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        video: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.video, Unset):
            video = []
            for video_item_data in self.video:
                video_item = video_item_data.to_dict()
                video.append(video_item)

        categories: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        related: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.related, Unset):
            related = []
            for related_item_data in self.related:
                related_item = related_item_data.to_dict()
                related.append(related_item)

        keywords: Union[Unset, List[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        allow_search = self.allow_search

        allow_amp = self.allow_amp

        allow_ads = self.allow_ads

        allow_comments = self.allow_comments

        allow_commerce = self.allow_commerce

        allow_content_reactions = self.allow_content_reactions

        link_text = self.link_text

        source = self.source

        now_id = self.now_id

        data_source_identifier = self.data_source_identifier

        metrics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()
                metrics.append(metrics_item)

        story = self.story

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "headline": headline,
                "type": type,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if published is not UNSET:
            field_dict["published"] = published
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if originally_posted is not UNSET:
            field_dict["originallyPosted"] = originally_posted
        if premium is not UNSET:
            field_dict["premium"] = premium
        if links is not UNSET:
            field_dict["links"] = links
        if images is not UNSET:
            field_dict["images"] = images
        if video is not UNSET:
            field_dict["video"] = video
        if categories is not UNSET:
            field_dict["categories"] = categories
        if related is not UNSET:
            field_dict["related"] = related
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if allow_search is not UNSET:
            field_dict["allowSearch"] = allow_search
        if allow_amp is not UNSET:
            field_dict["allowAMP"] = allow_amp
        if allow_ads is not UNSET:
            field_dict["allowAds"] = allow_ads
        if allow_comments is not UNSET:
            field_dict["allowComments"] = allow_comments
        if allow_commerce is not UNSET:
            field_dict["allowCommerce"] = allow_commerce
        if allow_content_reactions is not UNSET:
            field_dict["allowContentReactions"] = allow_content_reactions
        if link_text is not UNSET:
            field_dict["linkText"] = link_text
        if source is not UNSET:
            field_dict["source"] = source
        if now_id is not UNSET:
            field_dict["nowId"] = now_id
        if data_source_identifier is not UNSET:
            field_dict["dataSourceIdentifier"] = data_source_identifier
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if story is not UNSET:
            field_dict["story"] = story

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.news_category import NewsCategory
        from ..models.news_image import NewsImage
        from ..models.news_links import NewsLinks
        from ..models.news_metric import NewsMetric
        from ..models.news_related import NewsRelated
        from ..models.news_video import NewsVideo

        d = src_dict.copy()
        id = d.pop("id")

        headline = d.pop("headline")

        type = d.pop("type")

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _published = d.pop("published", UNSET)
        published: Union[Unset, datetime.datetime]
        if isinstance(_published, Unset):
            published = UNSET
        else:
            published = isoparse(_published)

        _last_modified = d.pop("lastModified", UNSET)
        last_modified: Union[Unset, datetime.datetime]
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = isoparse(_last_modified)

        _originally_posted = d.pop("originallyPosted", UNSET)
        originally_posted: Union[Unset, datetime.datetime]
        if isinstance(_originally_posted, Unset):
            originally_posted = UNSET
        else:
            originally_posted = isoparse(_originally_posted)

        premium = d.pop("premium", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, NewsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = NewsLinks.from_dict(_links)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = NewsImage.from_dict(images_item_data)

            images.append(images_item)

        video = []
        _video = d.pop("video", UNSET)
        for video_item_data in _video or []:
            video_item = NewsVideo.from_dict(video_item_data)

            video.append(video_item)

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = NewsCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        related = []
        _related = d.pop("related", UNSET)
        for related_item_data in _related or []:
            related_item = NewsRelated.from_dict(related_item_data)

            related.append(related_item)

        keywords = cast(List[str], d.pop("keywords", UNSET))

        allow_search = d.pop("allowSearch", UNSET)

        allow_amp = d.pop("allowAMP", UNSET)

        allow_ads = d.pop("allowAds", UNSET)

        allow_comments = d.pop("allowComments", UNSET)

        allow_commerce = d.pop("allowCommerce", UNSET)

        allow_content_reactions = d.pop("allowContentReactions", UNSET)

        link_text = d.pop("linkText", UNSET)

        source = d.pop("source", UNSET)

        now_id = d.pop("nowId", UNSET)

        data_source_identifier = d.pop("dataSourceIdentifier", UNSET)

        metrics = []
        _metrics = d.pop("metrics", UNSET)
        for metrics_item_data in _metrics or []:
            metrics_item = NewsMetric.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        story = d.pop("story", UNSET)

        news_headline = cls(
            id=id,
            headline=headline,
            type=type,
            title=title,
            description=description,
            published=published,
            last_modified=last_modified,
            originally_posted=originally_posted,
            premium=premium,
            links=links,
            images=images,
            video=video,
            categories=categories,
            related=related,
            keywords=keywords,
            allow_search=allow_search,
            allow_amp=allow_amp,
            allow_ads=allow_ads,
            allow_comments=allow_comments,
            allow_commerce=allow_commerce,
            allow_content_reactions=allow_content_reactions,
            link_text=link_text,
            source=source,
            now_id=now_id,
            data_source_identifier=data_source_identifier,
            metrics=metrics,
            story=story,
        )

        news_headline.additional_properties = d
        return news_headline

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
