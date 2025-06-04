from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flex_image import FlexImage
    from ..models.flex_link import FlexLink


T = TypeVar("T", bound="FeedCategory")


@_attrs_define
class FeedCategory:
    """
    Attributes:
        id (Union[Unset, str]):
        type (Union[Unset, str]):
        description (Union[Unset, str]):
        links (Union[Unset, List['FlexLink']]):
        images (Union[Unset, List['FlexImage']]):
        sport (Union[Unset, str]):
        league (Union[Unset, str]):
        uid (Union[Unset, str]):
        color (Union[Unset, str]):
        alternate_color (Union[Unset, str]):
        sub_text (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    links: Union[Unset, List["FlexLink"]] = UNSET
    images: Union[Unset, List["FlexImage"]] = UNSET
    sport: Union[Unset, str] = UNSET
    league: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    alternate_color: Union[Unset, str] = UNSET
    sub_text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type

        description = self.description

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        sport = self.sport

        league = self.league

        uid = self.uid

        color = self.color

        alternate_color = self.alternate_color

        sub_text = self.sub_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if description is not UNSET:
            field_dict["description"] = description
        if links is not UNSET:
            field_dict["links"] = links
        if images is not UNSET:
            field_dict["images"] = images
        if sport is not UNSET:
            field_dict["sport"] = sport
        if league is not UNSET:
            field_dict["league"] = league
        if uid is not UNSET:
            field_dict["uid"] = uid
        if color is not UNSET:
            field_dict["color"] = color
        if alternate_color is not UNSET:
            field_dict["alternateColor"] = alternate_color
        if sub_text is not UNSET:
            field_dict["subText"] = sub_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.flex_image import FlexImage
        from ..models.flex_link import FlexLink

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        type = d.pop("type", UNSET)

        description = d.pop("description", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = FlexLink.from_dict(links_item_data)

            links.append(links_item)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = FlexImage.from_dict(images_item_data)

            images.append(images_item)

        sport = d.pop("sport", UNSET)

        league = d.pop("league", UNSET)

        uid = d.pop("uid", UNSET)

        color = d.pop("color", UNSET)

        alternate_color = d.pop("alternateColor", UNSET)

        sub_text = d.pop("subText", UNSET)

        feed_category = cls(
            id=id,
            type=type,
            description=description,
            links=links,
            images=images,
            sport=sport,
            league=league,
            uid=uid,
            color=color,
            alternate_color=alternate_color,
            sub_text=sub_text,
        )

        feed_category.additional_properties = d
        return feed_category

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
