from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.detailed_venue import DetailedVenue
    from ..models.team_franchise_team import TeamFranchiseTeam


T = TypeVar("T", bound="TeamFranchise")


@_attrs_define
class TeamFranchise:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 12.
        uid (Union[Unset, str]):  Example: s:20~l:28~f:12.
        slug (Union[Unset, str]):  Example: kansas-city-chiefs.
        location (Union[Unset, str]):  Example: Kansas City.
        name (Union[Unset, str]):  Example: Chiefs.
        nickname (Union[Unset, str]):  Example: Chiefs.
        abbreviation (Union[Unset, str]):  Example: KC.
        display_name (Union[Unset, str]):  Example: Kansas City Chiefs.
        short_display_name (Union[Unset, str]):  Example: Chiefs.
        color (Union[Unset, str]):  Example: e31837.
        is_active (Union[Unset, bool]):
        venue (Union[Unset, DetailedVenue]):
        team (Union[Unset, TeamFranchiseTeam]):
    """

    id: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    short_display_name: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    venue: Union[Unset, "DetailedVenue"] = UNSET
    team: Union[Unset, "TeamFranchiseTeam"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        uid = self.uid

        slug = self.slug

        location = self.location

        name = self.name

        nickname = self.nickname

        abbreviation = self.abbreviation

        display_name = self.display_name

        short_display_name = self.short_display_name

        color = self.color

        is_active = self.is_active

        venue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.to_dict()

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uid is not UNSET:
            field_dict["uid"] = uid
        if slug is not UNSET:
            field_dict["slug"] = slug
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if color is not UNSET:
            field_dict["color"] = color
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if venue is not UNSET:
            field_dict["venue"] = venue
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.detailed_venue import DetailedVenue
        from ..models.team_franchise_team import TeamFranchiseTeam

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        uid = d.pop("uid", UNSET)

        slug = d.pop("slug", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        nickname = d.pop("nickname", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        display_name = d.pop("displayName", UNSET)

        short_display_name = d.pop("shortDisplayName", UNSET)

        color = d.pop("color", UNSET)

        is_active = d.pop("isActive", UNSET)

        _venue = d.pop("venue", UNSET)
        venue: Union[Unset, DetailedVenue]
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = DetailedVenue.from_dict(_venue)

        _team = d.pop("team", UNSET)
        team: Union[Unset, TeamFranchiseTeam]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = TeamFranchiseTeam.from_dict(_team)

        team_franchise = cls(
            id=id,
            uid=uid,
            slug=slug,
            location=location,
            name=name,
            nickname=nickname,
            abbreviation=abbreviation,
            display_name=display_name,
            short_display_name=short_display_name,
            color=color,
            is_active=is_active,
            venue=venue,
            team=team,
        )

        team_franchise.additional_properties = d
        return team_franchise

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
