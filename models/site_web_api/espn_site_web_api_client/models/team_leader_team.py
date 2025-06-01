from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.logo import Logo
    from ..models.team_leader_team_group import TeamLeaderTeamGroup
    from ..models.team_leader_team_ranks import TeamLeaderTeamRanks


T = TypeVar("T", bound="TeamLeaderTeam")


@_attrs_define
class TeamLeaderTeam:
    """
    Attributes:
        id (str): Team ID
        uid (str): Unique identifier for the team
        name (str): Team name
        abbreviation (str): Team abbreviation
        display_name (str): Full display name
        short_display_name (str): Short display name
        guid (Union[Unset, str]): Global unique identifier
        nickname (Union[Unset, str]): Team nickname
        logos (Union[Unset, List['Logo']]): Array of team logos
        links (Union[Unset, List['Link']]): Array of related links
        slug (Union[Unset, str]): URL slug for the team
        group (Union[Unset, TeamLeaderTeamGroup]): Team group information
        ranks (Union[Unset, TeamLeaderTeamRanks]): Team ranking information
    """

    id: str
    uid: str
    name: str
    abbreviation: str
    display_name: str
    short_display_name: str
    guid: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    logos: Union[Unset, List["Logo"]] = UNSET
    links: Union[Unset, List["Link"]] = UNSET
    slug: Union[Unset, str] = UNSET
    group: Union[Unset, "TeamLeaderTeamGroup"] = UNSET
    ranks: Union[Unset, "TeamLeaderTeamRanks"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        uid = self.uid

        name = self.name

        abbreviation = self.abbreviation

        display_name = self.display_name

        short_display_name = self.short_display_name

        guid = self.guid

        nickname = self.nickname

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

        slug = self.slug

        group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        ranks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ranks, Unset):
            ranks = self.ranks.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uid": uid,
                "name": name,
                "abbreviation": abbreviation,
                "displayName": display_name,
                "shortDisplayName": short_display_name,
            }
        )
        if guid is not UNSET:
            field_dict["guid"] = guid
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if logos is not UNSET:
            field_dict["logos"] = logos
        if links is not UNSET:
            field_dict["links"] = links
        if slug is not UNSET:
            field_dict["slug"] = slug
        if group is not UNSET:
            field_dict["group"] = group
        if ranks is not UNSET:
            field_dict["ranks"] = ranks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link
        from ..models.logo import Logo
        from ..models.team_leader_team_group import TeamLeaderTeamGroup
        from ..models.team_leader_team_ranks import TeamLeaderTeamRanks

        d = src_dict.copy()
        id = d.pop("id")

        uid = d.pop("uid")

        name = d.pop("name")

        abbreviation = d.pop("abbreviation")

        display_name = d.pop("displayName")

        short_display_name = d.pop("shortDisplayName")

        guid = d.pop("guid", UNSET)

        nickname = d.pop("nickname", UNSET)

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

        slug = d.pop("slug", UNSET)

        _group = d.pop("group", UNSET)
        group: Union[Unset, TeamLeaderTeamGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = TeamLeaderTeamGroup.from_dict(_group)

        _ranks = d.pop("ranks", UNSET)
        ranks: Union[Unset, TeamLeaderTeamRanks]
        if isinstance(_ranks, Unset):
            ranks = UNSET
        else:
            ranks = TeamLeaderTeamRanks.from_dict(_ranks)

        team_leader_team = cls(
            id=id,
            uid=uid,
            name=name,
            abbreviation=abbreviation,
            display_name=display_name,
            short_display_name=short_display_name,
            guid=guid,
            nickname=nickname,
            logos=logos,
            links=links,
            slug=slug,
            group=group,
            ranks=ranks,
        )

        team_leader_team.additional_properties = d
        return team_leader_team

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
