import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.author import Author
    from ..models.image import Image
    from ..models.news_category import NewsCategory
    from ..models.news_links import NewsLinks
    from ..models.reference import Reference
    from ..models.video_item import VideoItem


T = TypeVar("T", bound="NewsItemDetailed")


@_attrs_define
class NewsItemDetailed:
    """
    Attributes:
        headline (Union[Unset, str]):
        last_modified (Union[Unset, datetime.datetime]):
        root (Union[None, Unset, str]):
        premium (Union[Unset, bool]):
        links (Union[Unset, NewsLinks]):
        type (Union[Unset, str]):
        section (Union['Reference', None, Unset, str]):  Example: NFL.
        id (Union[Unset, int]):
        link_text (Union[None, Unset, str]):
        categorized (Union[None, Unset, datetime.datetime]):
        description (Union[None, Unset, str]):
        now_id (Union[None, Unset, str]):
        allow_comments (Union[None, Unset, bool]):
        images (Union[List['Image'], None, Unset]):
        categories (Union[List['NewsCategory'], None, Unset]):
        published (Union[None, Unset, datetime.datetime]):
        video (Union[List['VideoItem'], None, Unset]):
        byline (Union[None, Unset, str]):
        data_source_identifier (Union[None, Unset, str]):
        authors (Union[List['Author'], None, Unset]):
    """

    headline: Union[Unset, str] = UNSET
    last_modified: Union[Unset, datetime.datetime] = UNSET
    root: Union[None, Unset, str] = UNSET
    premium: Union[Unset, bool] = UNSET
    links: Union[Unset, "NewsLinks"] = UNSET
    type: Union[Unset, str] = UNSET
    section: Union["Reference", None, Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    link_text: Union[None, Unset, str] = UNSET
    categorized: Union[None, Unset, datetime.datetime] = UNSET
    description: Union[None, Unset, str] = UNSET
    now_id: Union[None, Unset, str] = UNSET
    allow_comments: Union[None, Unset, bool] = UNSET
    images: Union[List["Image"], None, Unset] = UNSET
    categories: Union[List["NewsCategory"], None, Unset] = UNSET
    published: Union[None, Unset, datetime.datetime] = UNSET
    video: Union[List["VideoItem"], None, Unset] = UNSET
    byline: Union[None, Unset, str] = UNSET
    data_source_identifier: Union[None, Unset, str] = UNSET
    authors: Union[List["Author"], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.reference import Reference

        headline = self.headline

        last_modified: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

        root: Union[None, Unset, str]
        if isinstance(self.root, Unset):
            root = UNSET
        else:
            root = self.root

        premium = self.premium

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        type = self.type

        section: Union[Dict[str, Any], None, Unset, str]
        if isinstance(self.section, Unset):
            section = UNSET
        elif isinstance(self.section, Reference):
            section = self.section.to_dict()
        else:
            section = self.section

        id = self.id

        link_text: Union[None, Unset, str]
        if isinstance(self.link_text, Unset):
            link_text = UNSET
        else:
            link_text = self.link_text

        categorized: Union[None, Unset, str]
        if isinstance(self.categorized, Unset):
            categorized = UNSET
        elif isinstance(self.categorized, datetime.datetime):
            categorized = self.categorized.isoformat()
        else:
            categorized = self.categorized

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        now_id: Union[None, Unset, str]
        if isinstance(self.now_id, Unset):
            now_id = UNSET
        else:
            now_id = self.now_id

        allow_comments: Union[None, Unset, bool]
        if isinstance(self.allow_comments, Unset):
            allow_comments = UNSET
        else:
            allow_comments = self.allow_comments

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

        published: Union[None, Unset, str]
        if isinstance(self.published, Unset):
            published = UNSET
        elif isinstance(self.published, datetime.datetime):
            published = self.published.isoformat()
        else:
            published = self.published

        video: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.video, Unset):
            video = UNSET
        elif isinstance(self.video, list):
            video = []
            for video_type_0_item_data in self.video:
                video_type_0_item = video_type_0_item_data.to_dict()
                video.append(video_type_0_item)

        else:
            video = self.video

        byline: Union[None, Unset, str]
        if isinstance(self.byline, Unset):
            byline = UNSET
        else:
            byline = self.byline

        data_source_identifier: Union[None, Unset, str]
        if isinstance(self.data_source_identifier, Unset):
            data_source_identifier = UNSET
        else:
            data_source_identifier = self.data_source_identifier

        authors: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.authors, Unset):
            authors = UNSET
        elif isinstance(self.authors, list):
            authors = []
            for authors_type_0_item_data in self.authors:
                authors_type_0_item = authors_type_0_item_data.to_dict()
                authors.append(authors_type_0_item)

        else:
            authors = self.authors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headline is not UNSET:
            field_dict["headline"] = headline
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if root is not UNSET:
            field_dict["root"] = root
        if premium is not UNSET:
            field_dict["premium"] = premium
        if links is not UNSET:
            field_dict["links"] = links
        if type is not UNSET:
            field_dict["type"] = type
        if section is not UNSET:
            field_dict["section"] = section
        if id is not UNSET:
            field_dict["id"] = id
        if link_text is not UNSET:
            field_dict["linkText"] = link_text
        if categorized is not UNSET:
            field_dict["categorized"] = categorized
        if description is not UNSET:
            field_dict["description"] = description
        if now_id is not UNSET:
            field_dict["nowId"] = now_id
        if allow_comments is not UNSET:
            field_dict["allowComments"] = allow_comments
        if images is not UNSET:
            field_dict["images"] = images
        if categories is not UNSET:
            field_dict["categories"] = categories
        if published is not UNSET:
            field_dict["published"] = published
        if video is not UNSET:
            field_dict["video"] = video
        if byline is not UNSET:
            field_dict["byline"] = byline
        if data_source_identifier is not UNSET:
            field_dict["dataSourceIdentifier"] = data_source_identifier
        if authors is not UNSET:
            field_dict["authors"] = authors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.author import Author
        from ..models.image import Image
        from ..models.news_category import NewsCategory
        from ..models.news_links import NewsLinks
        from ..models.reference import Reference
        from ..models.video_item import VideoItem

        d = src_dict.copy()
        headline = d.pop("headline", UNSET)

        _last_modified = d.pop("lastModified", UNSET)
        last_modified: Union[Unset, datetime.datetime]
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = isoparse(_last_modified)

        def _parse_root(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        root = _parse_root(d.pop("root", UNSET))

        premium = d.pop("premium", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, NewsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = NewsLinks.from_dict(_links)

        type = d.pop("type", UNSET)

        def _parse_section(data: object) -> Union["Reference", None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                section_type_1 = Reference.from_dict(data)

                return section_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Reference", None, Unset, str], data)

        section = _parse_section(d.pop("section", UNSET))

        id = d.pop("id", UNSET)

        def _parse_link_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        link_text = _parse_link_text(d.pop("linkText", UNSET))

        def _parse_categorized(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                categorized_type_0 = isoparse(data)

                return categorized_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        categorized = _parse_categorized(d.pop("categorized", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_now_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        now_id = _parse_now_id(d.pop("nowId", UNSET))

        def _parse_allow_comments(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        allow_comments = _parse_allow_comments(d.pop("allowComments", UNSET))

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

        def _parse_published(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_type_0 = isoparse(data)

                return published_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        published = _parse_published(d.pop("published", UNSET))

        def _parse_video(data: object) -> Union[List["VideoItem"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                video_type_0 = []
                _video_type_0 = data
                for video_type_0_item_data in _video_type_0:
                    video_type_0_item = VideoItem.from_dict(video_type_0_item_data)

                    video_type_0.append(video_type_0_item)

                return video_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["VideoItem"], None, Unset], data)

        video = _parse_video(d.pop("video", UNSET))

        def _parse_byline(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        byline = _parse_byline(d.pop("byline", UNSET))

        def _parse_data_source_identifier(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        data_source_identifier = _parse_data_source_identifier(d.pop("dataSourceIdentifier", UNSET))

        def _parse_authors(data: object) -> Union[List["Author"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                authors_type_0 = []
                _authors_type_0 = data
                for authors_type_0_item_data in _authors_type_0:
                    authors_type_0_item = Author.from_dict(authors_type_0_item_data)

                    authors_type_0.append(authors_type_0_item)

                return authors_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["Author"], None, Unset], data)

        authors = _parse_authors(d.pop("authors", UNSET))

        news_item_detailed = cls(
            headline=headline,
            last_modified=last_modified,
            root=root,
            premium=premium,
            links=links,
            type=type,
            section=section,
            id=id,
            link_text=link_text,
            categorized=categorized,
            description=description,
            now_id=now_id,
            allow_comments=allow_comments,
            images=images,
            categories=categories,
            published=published,
            video=video,
            byline=byline,
            data_source_identifier=data_source_identifier,
            authors=authors,
        )

        news_item_detailed.additional_properties = d
        return news_item_detailed

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
