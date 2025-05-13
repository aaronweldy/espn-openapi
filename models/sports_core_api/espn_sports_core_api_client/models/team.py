from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Team")


@_attrs_define
class Team:
    """
    Attributes:
        id (str):  Example: 12.
        display_name (str):  Example: Kansas City Chiefs.
        uid (Union[Unset, str]):  Example: s:20~l:28~t:12.
        location (Union[Unset, str]):  Example: Kansas City.
        name (Union[Unset, str]):  Example: Chiefs.
        abbreviation (Union[Unset, str]):  Example: KC.
        short_display_name (Union[Unset, str]):  Example: Chiefs.
        color (Union[Unset, str]):  Example: e31837.
        alternate_color (Union[Unset, str]):  Example: ffb612.
        logo (Union[Unset, str]):  Example: https://a.espncdn.com/i/teamlogos/nfl/500/kc.png.
    """

    id: str
    display_name: str
    uid: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    short_display_name: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    alternate_color: Union[Unset, str] = UNSET
    logo: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        display_name = self.display_name

        uid = self.uid

        location = self.location

        name = self.name

        abbreviation = self.abbreviation

        short_display_name = self.short_display_name

        color = self.color

        alternate_color = self.alternate_color

        logo = self.logo

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
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if color is not UNSET:
            field_dict["color"] = color
        if alternate_color is not UNSET:
            field_dict["alternateColor"] = alternate_color
        if logo is not UNSET:
            field_dict["logo"] = logo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        display_name = d.pop("displayName")

        uid = d.pop("uid", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        short_display_name = d.pop("shortDisplayName", UNSET)

        color = d.pop("color", UNSET)

        alternate_color = d.pop("alternateColor", UNSET)

        logo = d.pop("logo", UNSET)

        team = cls(
            id=id,
            display_name=display_name,
            uid=uid,
            location=location,
            name=name,
            abbreviation=abbreviation,
            short_display_name=short_display_name,
            color=color,
            alternate_color=alternate_color,
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
