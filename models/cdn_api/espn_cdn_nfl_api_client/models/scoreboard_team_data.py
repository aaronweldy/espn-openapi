from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_link import ScoreboardLink
    from ..models.scoreboard_venue import ScoreboardVenue


T = TypeVar("T", bound="ScoreboardTeamData")


@_attrs_define
class ScoreboardTeamData:
    """
    Attributes:
        alternate_color (Union[Unset, str]):
        venue (Union[Unset, ScoreboardVenue]):
        color (Union[Unset, str]):
        display_name (Union[Unset, str]):
        abbreviation (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        short_display_name (Union[Unset, str]):
        uid (Union[Unset, str]):
        name (Union[Unset, str]):
        logo (Union[Unset, str]):
        location (Union[Unset, str]):
        links (Union[Unset, List['ScoreboardLink']]):
        id (Union[Unset, str]):
    """

    alternate_color: Union[Unset, str] = UNSET
    venue: Union[Unset, "ScoreboardVenue"] = UNSET
    color: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    short_display_name: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    logo: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    links: Union[Unset, List["ScoreboardLink"]] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alternate_color = self.alternate_color

        venue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.to_dict()

        color = self.color

        display_name = self.display_name

        abbreviation = self.abbreviation

        is_active = self.is_active

        short_display_name = self.short_display_name

        uid = self.uid

        name = self.name

        logo = self.logo

        location = self.location

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alternate_color is not UNSET:
            field_dict["alternateColor"] = alternate_color
        if venue is not UNSET:
            field_dict["venue"] = venue
        if color is not UNSET:
            field_dict["color"] = color
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if uid is not UNSET:
            field_dict["uid"] = uid
        if name is not UNSET:
            field_dict["name"] = name
        if logo is not UNSET:
            field_dict["logo"] = logo
        if location is not UNSET:
            field_dict["location"] = location
        if links is not UNSET:
            field_dict["links"] = links
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_link import ScoreboardLink
        from ..models.scoreboard_venue import ScoreboardVenue

        d = src_dict.copy()
        alternate_color = d.pop("alternateColor", UNSET)

        _venue = d.pop("venue", UNSET)
        venue: Union[Unset, ScoreboardVenue]
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = ScoreboardVenue.from_dict(_venue)

        color = d.pop("color", UNSET)

        display_name = d.pop("displayName", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        is_active = d.pop("isActive", UNSET)

        short_display_name = d.pop("shortDisplayName", UNSET)

        uid = d.pop("uid", UNSET)

        name = d.pop("name", UNSET)

        logo = d.pop("logo", UNSET)

        location = d.pop("location", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = ScoreboardLink.from_dict(links_item_data)

            links.append(links_item)

        id = d.pop("id", UNSET)

        scoreboard_team_data = cls(
            alternate_color=alternate_color,
            venue=venue,
            color=color,
            display_name=display_name,
            abbreviation=abbreviation,
            is_active=is_active,
            short_display_name=short_display_name,
            uid=uid,
            name=name,
            logo=logo,
            location=location,
            links=links,
            id=id,
        )

        scoreboard_team_data.additional_properties = d
        return scoreboard_team_data

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
