from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.logo import Logo


T = TypeVar("T", bound="LeaderTeam")


@_attrs_define
class LeaderTeam:
    """
    Attributes:
        id (str): Team ID
        display_name (str): Full team display name
        slug (Union[Unset, str]): URL slug
        name (Union[Unset, str]): Team name
        nickname (Union[Unset, str]): Team nickname
        abbreviation (Union[Unset, str]): Team abbreviation
        short_display_name (Union[Unset, str]): Short display name
        color (Union[Unset, str]): Primary team color (hex)
        alternate_color (Union[Unset, str]): Alternate team color (hex)
        logos (Union[Unset, List['Logo']]): Team logos
        links (Union[Unset, List['Link']]): Related links
    """

    id: str
    display_name: str
    slug: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    short_display_name: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    alternate_color: Union[Unset, str] = UNSET
    logos: Union[Unset, List["Logo"]] = UNSET
    links: Union[Unset, List["Link"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        display_name = self.display_name

        slug = self.slug

        name = self.name

        nickname = self.nickname

        abbreviation = self.abbreviation

        short_display_name = self.short_display_name

        color = self.color

        alternate_color = self.alternate_color

        logos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.logos, Unset):
            logos = []
            for logos_item_data in self.logos:
                logos_item = logos_item_data.to_dict()
                logos.append(logos_item)

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
                "displayName": display_name,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if color is not UNSET:
            field_dict["color"] = color
        if alternate_color is not UNSET:
            field_dict["alternateColor"] = alternate_color
        if logos is not UNSET:
            field_dict["logos"] = logos
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link
        from ..models.logo import Logo

        d = src_dict.copy()
        id = d.pop("id")

        display_name = d.pop("displayName")

        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        nickname = d.pop("nickname", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        short_display_name = d.pop("shortDisplayName", UNSET)

        color = d.pop("color", UNSET)

        alternate_color = d.pop("alternateColor", UNSET)

        logos = []
        _logos = d.pop("logos", UNSET)
        for logos_item_data in _logos or []:
            logos_item = Logo.from_dict(logos_item_data)

            logos.append(logos_item)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        leader_team = cls(
            id=id,
            display_name=display_name,
            slug=slug,
            name=name,
            nickname=nickname,
            abbreviation=abbreviation,
            short_display_name=short_display_name,
            color=color,
            alternate_color=alternate_color,
            logos=logos,
            links=links,
        )

        leader_team.additional_properties = d
        return leader_team

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
