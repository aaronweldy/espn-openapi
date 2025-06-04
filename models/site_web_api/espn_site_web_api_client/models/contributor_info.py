from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contributor_ids import ContributorIds
    from ..models.flex_image import FlexImage
    from ..models.flex_link import FlexLink
    from ..models.social_link import SocialLink


T = TypeVar("T", bound="ContributorInfo")


@_attrs_define
class ContributorInfo:
    """
    Attributes:
        id (Union[Unset, str]):
        ids (Union[Unset, ContributorIds]):
        type (Union[Unset, str]):
        display_name (Union[Unset, str]):
        biography (Union[Unset, str]):
        source_line (Union[Unset, str]):
        images (Union[Unset, List['FlexImage']]):
        social (Union[Unset, List['SocialLink']]):
        links (Union[Unset, List['FlexLink']]):
    """

    id: Union[Unset, str] = UNSET
    ids: Union[Unset, "ContributorIds"] = UNSET
    type: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    biography: Union[Unset, str] = UNSET
    source_line: Union[Unset, str] = UNSET
    images: Union[Unset, List["FlexImage"]] = UNSET
    social: Union[Unset, List["SocialLink"]] = UNSET
    links: Union[Unset, List["FlexLink"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        ids: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids.to_dict()

        type = self.type

        display_name = self.display_name

        biography = self.biography

        source_line = self.source_line

        images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        social: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.social, Unset):
            social = []
            for social_item_data in self.social:
                social_item = social_item_data.to_dict()
                social.append(social_item)

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if ids is not UNSET:
            field_dict["ids"] = ids
        if type is not UNSET:
            field_dict["type"] = type
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if biography is not UNSET:
            field_dict["biography"] = biography
        if source_line is not UNSET:
            field_dict["sourceLine"] = source_line
        if images is not UNSET:
            field_dict["images"] = images
        if social is not UNSET:
            field_dict["social"] = social
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contributor_ids import ContributorIds
        from ..models.flex_image import FlexImage
        from ..models.flex_link import FlexLink
        from ..models.social_link import SocialLink

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _ids = d.pop("ids", UNSET)
        ids: Union[Unset, ContributorIds]
        if isinstance(_ids, Unset):
            ids = UNSET
        else:
            ids = ContributorIds.from_dict(_ids)

        type = d.pop("type", UNSET)

        display_name = d.pop("displayName", UNSET)

        biography = d.pop("biography", UNSET)

        source_line = d.pop("sourceLine", UNSET)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = FlexImage.from_dict(images_item_data)

            images.append(images_item)

        social = []
        _social = d.pop("social", UNSET)
        for social_item_data in _social or []:
            social_item = SocialLink.from_dict(social_item_data)

            social.append(social_item)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = FlexLink.from_dict(links_item_data)

            links.append(links_item)

        contributor_info = cls(
            id=id,
            ids=ids,
            type=type,
            display_name=display_name,
            biography=biography,
            source_line=source_line,
            images=images,
            social=social,
            links=links,
        )

        contributor_info.additional_properties = d
        return contributor_info

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
