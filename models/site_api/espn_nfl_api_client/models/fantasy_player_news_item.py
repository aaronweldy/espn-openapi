import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_news_image import FantasyNewsImage
    from ..models.fantasy_player_news_item_links import FantasyPlayerNewsItemLinks


T = TypeVar("T", bound="FantasyPlayerNewsItem")


@_attrs_define
class FantasyPlayerNewsItem:
    """Individual fantasy news item

    Attributes:
        id (Union[Unset, int]): News item ID
        headline (Union[Unset, str]): News headline
        description (Union[Unset, str]): Brief description of the news
        story (Union[Unset, str]): Full news story content
        published (Union[Unset, datetime.datetime]): Publication date
        last_modified (Union[Unset, datetime.datetime]): Last modification date
        premium (Union[Unset, bool]): Whether this is premium content
        type (Union[Unset, str]): Type of news item
        player_id (Union[Unset, int]): Associated player ID
        now_id (Union[Unset, str]): NOW platform ID
        content_key (Union[Unset, str]): Content key information
        data_source_identifier (Union[Unset, str]): Data source identifier
        allow_content_reactions (Union[Unset, bool]): Whether reactions are allowed
        allow_search (Union[Unset, bool]): Whether item is searchable
        categorized (Union[Unset, bool]): Whether item is categorized
        images (Union[Unset, List['FantasyNewsImage']]): Associated images
        links (Union[Unset, FantasyPlayerNewsItemLinks]): Links to different platforms
    """

    id: Union[Unset, int] = UNSET
    headline: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    story: Union[Unset, str] = UNSET
    published: Union[Unset, datetime.datetime] = UNSET
    last_modified: Union[Unset, datetime.datetime] = UNSET
    premium: Union[Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    now_id: Union[Unset, str] = UNSET
    content_key: Union[Unset, str] = UNSET
    data_source_identifier: Union[Unset, str] = UNSET
    allow_content_reactions: Union[Unset, bool] = UNSET
    allow_search: Union[Unset, bool] = UNSET
    categorized: Union[Unset, bool] = UNSET
    images: Union[Unset, List["FantasyNewsImage"]] = UNSET
    links: Union[Unset, "FantasyPlayerNewsItemLinks"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        headline = self.headline

        description = self.description

        story = self.story

        published: Union[Unset, str] = UNSET
        if not isinstance(self.published, Unset):
            published = self.published.isoformat()

        last_modified: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

        premium = self.premium

        type = self.type

        player_id = self.player_id

        now_id = self.now_id

        content_key = self.content_key

        data_source_identifier = self.data_source_identifier

        allow_content_reactions = self.allow_content_reactions

        allow_search = self.allow_search

        categorized = self.categorized

        images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if headline is not UNSET:
            field_dict["headline"] = headline
        if description is not UNSET:
            field_dict["description"] = description
        if story is not UNSET:
            field_dict["story"] = story
        if published is not UNSET:
            field_dict["published"] = published
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if premium is not UNSET:
            field_dict["premium"] = premium
        if type is not UNSET:
            field_dict["type"] = type
        if player_id is not UNSET:
            field_dict["playerId"] = player_id
        if now_id is not UNSET:
            field_dict["nowId"] = now_id
        if content_key is not UNSET:
            field_dict["contentKey"] = content_key
        if data_source_identifier is not UNSET:
            field_dict["dataSourceIdentifier"] = data_source_identifier
        if allow_content_reactions is not UNSET:
            field_dict["allowContentReactions"] = allow_content_reactions
        if allow_search is not UNSET:
            field_dict["allowSearch"] = allow_search
        if categorized is not UNSET:
            field_dict["categorized"] = categorized
        if images is not UNSET:
            field_dict["images"] = images
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_news_image import FantasyNewsImage
        from ..models.fantasy_player_news_item_links import FantasyPlayerNewsItemLinks

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        headline = d.pop("headline", UNSET)

        description = d.pop("description", UNSET)

        story = d.pop("story", UNSET)

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

        premium = d.pop("premium", UNSET)

        type = d.pop("type", UNSET)

        player_id = d.pop("playerId", UNSET)

        now_id = d.pop("nowId", UNSET)

        content_key = d.pop("contentKey", UNSET)

        data_source_identifier = d.pop("dataSourceIdentifier", UNSET)

        allow_content_reactions = d.pop("allowContentReactions", UNSET)

        allow_search = d.pop("allowSearch", UNSET)

        categorized = d.pop("categorized", UNSET)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = FantasyNewsImage.from_dict(images_item_data)

            images.append(images_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, FantasyPlayerNewsItemLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = FantasyPlayerNewsItemLinks.from_dict(_links)

        fantasy_player_news_item = cls(
            id=id,
            headline=headline,
            description=description,
            story=story,
            published=published,
            last_modified=last_modified,
            premium=premium,
            type=type,
            player_id=player_id,
            now_id=now_id,
            content_key=content_key,
            data_source_identifier=data_source_identifier,
            allow_content_reactions=allow_content_reactions,
            allow_search=allow_search,
            categorized=categorized,
            images=images,
            links=links,
        )

        fantasy_player_news_item.additional_properties = d
        return fantasy_player_news_item

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
