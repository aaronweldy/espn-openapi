from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.logo import Logo
    from ..models.reference import Reference


T = TypeVar("T", bound="Team")


@_attrs_define
class Team:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 17.
        uid (Union[Unset, str]):  Example: s:20~l:28~t:17.
        slug (Union[None, Unset, str]):  Example: new-england-patriots.
        abbreviation (Union[Unset, str]):  Example: NE.
        display_name (Union[Unset, str]):  Example: New England Patriots.
        short_display_name (Union[None, Unset, str]):  Example: Patriots.
        name (Union[None, Unset, str]):  Example: Patriots.
        nickname (Union[None, Unset, str]):  Example: Patriots.
        location (Union[Unset, str]):  Example: New England.
        color (Union[None, Unset, str]):  Example: 002244.
        alternate_color (Union[None, Unset, str]):  Example: c60c30.
        is_active (Union[Unset, bool]):  Example: True.
        is_all_star (Union[None, Unset, bool]):
        logos (Union[List['Logo'], None, Unset]):
        links (Union[List['Link'], None, Unset]):
        group (Union[Unset, Reference]):
        season_summary (Union[None, Unset, str]):
        clubhouse (Union[None, Unset, str]):
        logo (Union[None, Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    slug: Union[None, Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    short_display_name: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    nickname: Union[None, Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    color: Union[None, Unset, str] = UNSET
    alternate_color: Union[None, Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_all_star: Union[None, Unset, bool] = UNSET
    logos: Union[List["Logo"], None, Unset] = UNSET
    links: Union[List["Link"], None, Unset] = UNSET
    group: Union[Unset, "Reference"] = UNSET
    season_summary: Union[None, Unset, str] = UNSET
    clubhouse: Union[None, Unset, str] = UNSET
    logo: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        uid = self.uid

        slug: Union[None, Unset, str]
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        abbreviation = self.abbreviation

        display_name = self.display_name

        short_display_name: Union[None, Unset, str]
        if isinstance(self.short_display_name, Unset):
            short_display_name = UNSET
        else:
            short_display_name = self.short_display_name

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        nickname: Union[None, Unset, str]
        if isinstance(self.nickname, Unset):
            nickname = UNSET
        else:
            nickname = self.nickname

        location = self.location

        color: Union[None, Unset, str]
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        alternate_color: Union[None, Unset, str]
        if isinstance(self.alternate_color, Unset):
            alternate_color = UNSET
        else:
            alternate_color = self.alternate_color

        is_active = self.is_active

        is_all_star: Union[None, Unset, bool]
        if isinstance(self.is_all_star, Unset):
            is_all_star = UNSET
        else:
            is_all_star = self.is_all_star

        logos: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.logos, Unset):
            logos = UNSET
        elif isinstance(self.logos, list):
            logos = []
            for logos_type_0_item_data in self.logos:
                logos_type_0_item = logos_type_0_item_data.to_dict()
                logos.append(logos_type_0_item)

        else:
            logos = self.logos

        links: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.links, Unset):
            links = UNSET
        elif isinstance(self.links, list):
            links = []
            for links_type_0_item_data in self.links:
                links_type_0_item = links_type_0_item_data.to_dict()
                links.append(links_type_0_item)

        else:
            links = self.links

        group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        season_summary: Union[None, Unset, str]
        if isinstance(self.season_summary, Unset):
            season_summary = UNSET
        else:
            season_summary = self.season_summary

        clubhouse: Union[None, Unset, str]
        if isinstance(self.clubhouse, Unset):
            clubhouse = UNSET
        else:
            clubhouse = self.clubhouse

        logo: Union[None, Unset, str]
        if isinstance(self.logo, Unset):
            logo = UNSET
        else:
            logo = self.logo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uid is not UNSET:
            field_dict["uid"] = uid
        if slug is not UNSET:
            field_dict["slug"] = slug
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
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
        if group is not UNSET:
            field_dict["group"] = group
        if season_summary is not UNSET:
            field_dict["seasonSummary"] = season_summary
        if clubhouse is not UNSET:
            field_dict["clubhouse"] = clubhouse
        if logo is not UNSET:
            field_dict["logo"] = logo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link
        from ..models.logo import Logo
        from ..models.reference import Reference

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        uid = d.pop("uid", UNSET)

        def _parse_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slug = _parse_slug(d.pop("slug", UNSET))

        abbreviation = d.pop("abbreviation", UNSET)

        display_name = d.pop("displayName", UNSET)

        def _parse_short_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        short_display_name = _parse_short_display_name(d.pop("shortDisplayName", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_nickname(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        nickname = _parse_nickname(d.pop("nickname", UNSET))

        location = d.pop("location", UNSET)

        def _parse_color(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_alternate_color(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alternate_color = _parse_alternate_color(d.pop("alternateColor", UNSET))

        is_active = d.pop("isActive", UNSET)

        def _parse_is_all_star(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_all_star = _parse_is_all_star(d.pop("isAllStar", UNSET))

        def _parse_logos(data: object) -> Union[List["Logo"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                logos_type_0 = []
                _logos_type_0 = data
                for logos_type_0_item_data in _logos_type_0:
                    logos_type_0_item = Logo.from_dict(logos_type_0_item_data)

                    logos_type_0.append(logos_type_0_item)

                return logos_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["Logo"], None, Unset], data)

        logos = _parse_logos(d.pop("logos", UNSET))

        def _parse_links(data: object) -> Union[List["Link"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                links_type_0 = []
                _links_type_0 = data
                for links_type_0_item_data in _links_type_0:
                    links_type_0_item = Link.from_dict(links_type_0_item_data)

                    links_type_0.append(links_type_0_item)

                return links_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["Link"], None, Unset], data)

        links = _parse_links(d.pop("links", UNSET))

        _group = d.pop("group", UNSET)
        group: Union[Unset, Reference]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = Reference.from_dict(_group)

        def _parse_season_summary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        season_summary = _parse_season_summary(d.pop("seasonSummary", UNSET))

        def _parse_clubhouse(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        clubhouse = _parse_clubhouse(d.pop("clubhouse", UNSET))

        def _parse_logo(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo = _parse_logo(d.pop("logo", UNSET))

        team = cls(
            id=id,
            uid=uid,
            slug=slug,
            abbreviation=abbreviation,
            display_name=display_name,
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
            group=group,
            season_summary=season_summary,
            clubhouse=clubhouse,
            logo=logo,
        )

        team.additional_properties = d
        return team

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
