from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_link import TeamLink
    from ..models.team_logo import TeamLogo


T = TypeVar("T", bound="TeamDetail")


@_attrs_define
class TeamDetail:
    """
    Attributes:
        id (str):  Example: 22.
        display_name (str):  Example: Arizona Cardinals.
        uid (Union[Unset, str]):  Example: s:20~l:28~t:22.
        slug (Union[Unset, str]):  Example: arizona-cardinals.
        abbreviation (Union[Unset, str]):  Example: ARI.
        short_display_name (Union[Unset, str]):  Example: Cardinals.
        name (Union[Unset, str]):  Example: Cardinals.
        nickname (Union[Unset, str]):  Example: Cardinals.
        location (Union[Unset, str]):  Example: Arizona.
        color (Union[Unset, str]):  Example: a4113e.
        alternate_color (Union[Unset, str]):  Example: 000000.
        is_active (Union[Unset, bool]):
        is_all_star (Union[Unset, bool]):
        logos (Union[Unset, List['TeamLogo']]):
        links (Union[Unset, List['TeamLink']]):
    """

    id: str
    display_name: str
    uid: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    short_display_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    alternate_color: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_all_star: Union[Unset, bool] = UNSET
    logos: Union[Unset, List["TeamLogo"]] = UNSET
    links: Union[Unset, List["TeamLink"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        display_name = self.display_name

        uid = self.uid

        slug = self.slug

        abbreviation = self.abbreviation

        short_display_name = self.short_display_name

        name = self.name

        nickname = self.nickname

        location = self.location

        color = self.color

        alternate_color = self.alternate_color

        is_active = self.is_active

        is_all_star = self.is_all_star

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
        if uid is not UNSET:
            field_dict["uid"] = uid
        if slug is not UNSET:
            field_dict["slug"] = slug
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if name is not UNSET:
            field_dict["name"] = name
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if location is not UNSET:
            field_dict["location"] = location
        if color is not UNSET:
            field_dict["color"] = color
        if alternate_color is not UNSET:
            field_dict["alternateColor"] = alternate_color
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if is_all_star is not UNSET:
            field_dict["isAllStar"] = is_all_star
        if logos is not UNSET:
            field_dict["logos"] = logos
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_link import TeamLink
        from ..models.team_logo import TeamLogo

        d = src_dict.copy()
        id = d.pop("id")

        display_name = d.pop("displayName")

        uid = d.pop("uid", UNSET)

        slug = d.pop("slug", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        short_display_name = d.pop("shortDisplayName", UNSET)

        name = d.pop("name", UNSET)

        nickname = d.pop("nickname", UNSET)

        location = d.pop("location", UNSET)

        color = d.pop("color", UNSET)

        alternate_color = d.pop("alternateColor", UNSET)

        is_active = d.pop("isActive", UNSET)

        is_all_star = d.pop("isAllStar", UNSET)

        logos = []
        _logos = d.pop("logos", UNSET)
        for logos_item_data in _logos or []:
            logos_item = TeamLogo.from_dict(logos_item_data)

            logos.append(logos_item)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = TeamLink.from_dict(links_item_data)

            links.append(links_item)

        team_detail = cls(
            id=id,
            display_name=display_name,
            uid=uid,
            slug=slug,
            abbreviation=abbreviation,
            short_display_name=short_display_name,
            name=name,
            nickname=nickname,
            location=location,
            color=color,
            alternate_color=alternate_color,
            is_active=is_active,
            is_all_star=is_all_star,
            logos=logos,
            links=links,
        )

        team_detail.additional_properties = d
        return team_detail

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
