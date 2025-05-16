from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nfl_standings_team_logos_item import NflStandingsTeamLogosItem


T = TypeVar("T", bound="NflStandingsTeam")


@_attrs_define
class NflStandingsTeam:
    """
    Attributes:
        short_display_name (Union[Unset, str]):
        uid (Union[Unset, str]):
        seed (Union[Unset, str]):
        display_name (Union[Unset, str]):
        name (Union[Unset, str]):
        link (Union[Unset, str]):
        location (Union[Unset, str]):
        id (Union[Unset, str]):
        abbreviation (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        logos (Union[Unset, List['NflStandingsTeamLogosItem']]):
        clincher (Union[Unset, str]):
    """

    short_display_name: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    seed: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    logos: Union[Unset, List["NflStandingsTeamLogosItem"]] = UNSET
    clincher: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        short_display_name = self.short_display_name

        uid = self.uid

        seed = self.seed

        display_name = self.display_name

        name = self.name

        link = self.link

        location = self.location

        id = self.id

        abbreviation = self.abbreviation

        is_active = self.is_active

        logos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.logos, Unset):
            logos = []
            for logos_item_data in self.logos:
                logos_item = logos_item_data.to_dict()
                logos.append(logos_item)

        clincher = self.clincher

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if uid is not UNSET:
            field_dict["uid"] = uid
        if seed is not UNSET:
            field_dict["seed"] = seed
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if name is not UNSET:
            field_dict["name"] = name
        if link is not UNSET:
            field_dict["link"] = link
        if location is not UNSET:
            field_dict["location"] = location
        if id is not UNSET:
            field_dict["id"] = id
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if logos is not UNSET:
            field_dict["logos"] = logos
        if clincher is not UNSET:
            field_dict["clincher"] = clincher

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_standings_team_logos_item import NflStandingsTeamLogosItem

        d = src_dict.copy()
        short_display_name = d.pop("shortDisplayName", UNSET)

        uid = d.pop("uid", UNSET)

        seed = d.pop("seed", UNSET)

        display_name = d.pop("displayName", UNSET)

        name = d.pop("name", UNSET)

        link = d.pop("link", UNSET)

        location = d.pop("location", UNSET)

        id = d.pop("id", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        is_active = d.pop("isActive", UNSET)

        logos = []
        _logos = d.pop("logos", UNSET)
        for logos_item_data in _logos or []:
            logos_item = NflStandingsTeamLogosItem.from_dict(logos_item_data)

            logos.append(logos_item)

        clincher = d.pop("clincher", UNSET)

        nfl_standings_team = cls(
            short_display_name=short_display_name,
            uid=uid,
            seed=seed,
            display_name=display_name,
            name=name,
            link=link,
            location=location,
            id=id,
            abbreviation=abbreviation,
            is_active=is_active,
            logos=logos,
            clincher=clincher,
        )

        nfl_standings_team.additional_properties = d
        return nfl_standings_team

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
