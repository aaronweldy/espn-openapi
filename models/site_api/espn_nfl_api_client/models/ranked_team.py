from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.logo import Logo
    from ..models.ranked_team_groups import RankedTeamGroups


T = TypeVar("T", bound="RankedTeam")


@_attrs_define
class RankedTeam:
    """Team information in rankings

    Attributes:
        id (Union[Unset, str]): Team ID
        uid (Union[Unset, str]): Unique team identifier
        location (Union[Unset, str]): Team location/city
        name (Union[Unset, str]): Team name
        nickname (Union[Unset, str]): Team nickname
        abbreviation (Union[Unset, str]): Team abbreviation
        color (Union[Unset, str]): Team primary color (hex)
        logo (Union[Unset, str]): URL to team logo
        logos (Union[Unset, List['Logo']]): Array of team logos
        groups (Union[Unset, RankedTeamGroups]): Conference/group information
        links (Union[Unset, List['Link']]): Related links
    """

    id: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    logo: Union[Unset, str] = UNSET
    logos: Union[Unset, List["Logo"]] = UNSET
    groups: Union[Unset, "RankedTeamGroups"] = UNSET
    links: Union[Unset, List["Link"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        uid = self.uid

        location = self.location

        name = self.name

        nickname = self.nickname

        abbreviation = self.abbreviation

        color = self.color

        logo = self.logo

        logos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.logos, Unset):
            logos = []
            for logos_item_data in self.logos:
                logos_item = logos_item_data.to_dict()
                logos.append(logos_item)

        groups: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

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
        if uid is not UNSET:
            field_dict["uid"] = uid
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if color is not UNSET:
            field_dict["color"] = color
        if logo is not UNSET:
            field_dict["logo"] = logo
        if logos is not UNSET:
            field_dict["logos"] = logos
        if groups is not UNSET:
            field_dict["groups"] = groups
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link
        from ..models.logo import Logo
        from ..models.ranked_team_groups import RankedTeamGroups

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        uid = d.pop("uid", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        nickname = d.pop("nickname", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        color = d.pop("color", UNSET)

        logo = d.pop("logo", UNSET)

        logos = []
        _logos = d.pop("logos", UNSET)
        for logos_item_data in _logos or []:
            logos_item = Logo.from_dict(logos_item_data)

            logos.append(logos_item)

        _groups = d.pop("groups", UNSET)
        groups: Union[Unset, RankedTeamGroups]
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = RankedTeamGroups.from_dict(_groups)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        ranked_team = cls(
            id=id,
            uid=uid,
            location=location,
            name=name,
            nickname=nickname,
            abbreviation=abbreviation,
            color=color,
            logo=logo,
            logos=logos,
            groups=groups,
            links=links,
        )

        ranked_team.additional_properties = d
        return ranked_team

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
