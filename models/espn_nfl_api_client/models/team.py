from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.logo import Logo
    from ..models.team_venue import TeamVenue


T = TypeVar("T", bound="Team")


@_attrs_define
class Team:
    """
    Attributes:
        id (str):  Example: 21.
        uid (Union[Unset, str]):  Example: s:20~l:28~t:21.
        location (Union[Unset, str]):  Example: Philadelphia.
        name (Union[Unset, str]):  Example: Eagles.
        abbreviation (Union[Unset, str]):  Example: PHI.
        display_name (Union[Unset, str]):  Example: Philadelphia Eagles.
        short_display_name (Union[Unset, str]):  Example: Eagles.
        color (Union[Unset, str]):  Example: 004C54.
        alternate_color (Union[Unset, str]):  Example: 000000.
        is_active (Union[Unset, bool]):
        venue (Union[Unset, TeamVenue]):
        logo (Union[Unset, str]):  Example: https://a.espncdn.com/i/teamlogos/nfl/500/phi.png.
        logos (Union[Unset, list['Logo']]):
        links (Union[Unset, list['Link']]):
    """

    id: str
    uid: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    short_display_name: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    alternate_color: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    venue: Union[Unset, "TeamVenue"] = UNSET
    logo: Union[Unset, str] = UNSET
    logos: Union[Unset, list["Logo"]] = UNSET
    links: Union[Unset, list["Link"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uid = self.uid

        location = self.location

        name = self.name

        abbreviation = self.abbreviation

        display_name = self.display_name

        short_display_name = self.short_display_name

        color = self.color

        alternate_color = self.alternate_color

        is_active = self.is_active

        venue: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.to_dict()

        logo = self.logo

        logos: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.logos, Unset):
            logos = []
            for logos_item_data in self.logos:
                logos_item = logos_item_data.to_dict()
                logos.append(logos_item)

        links: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if color is not UNSET:
            field_dict["color"] = color
        if alternate_color is not UNSET:
            field_dict["alternateColor"] = alternate_color
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if venue is not UNSET:
            field_dict["venue"] = venue
        if logo is not UNSET:
            field_dict["logo"] = logo
        if logos is not UNSET:
            field_dict["logos"] = logos
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link import Link
        from ..models.logo import Logo
        from ..models.team_venue import TeamVenue

        d = dict(src_dict)
        id = d.pop("id")

        uid = d.pop("uid", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        display_name = d.pop("displayName", UNSET)

        short_display_name = d.pop("shortDisplayName", UNSET)

        color = d.pop("color", UNSET)

        alternate_color = d.pop("alternateColor", UNSET)

        is_active = d.pop("isActive", UNSET)

        _venue = d.pop("venue", UNSET)
        venue: Union[Unset, TeamVenue]
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = TeamVenue.from_dict(_venue)

        logo = d.pop("logo", UNSET)

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

        team = cls(
            id=id,
            uid=uid,
            location=location,
            name=name,
            abbreviation=abbreviation,
            display_name=display_name,
            short_display_name=short_display_name,
            color=color,
            alternate_color=alternate_color,
            is_active=is_active,
            venue=venue,
            logo=logo,
            logos=logos,
            links=links,
        )

        team.additional_properties = d
        return team

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
