from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventTeam")


@_attrs_define
class EventTeam:
    """
    Attributes:
        id (str): Team identifier Example: 21.
        abbreviation (str): Team abbreviation Example: PHI.
        display_name (str): Full team name Example: Philadelphia Eagles.
        location (Union[Unset, str]): Team location Example: Philadelphia.
        name (Union[Unset, str]): Team name Example: Eagles.
        short_display_name (Union[Unset, str]): Short team name Example: Eagles.
        color (Union[Unset, str]): Primary team color (hex) Example: 06424d.
        alternate_color (Union[Unset, str]): Alternate team color (hex) Example: 000000.
    """

    id: str
    abbreviation: str
    display_name: str
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    short_display_name: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    alternate_color: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        abbreviation = self.abbreviation

        display_name = self.display_name

        location = self.location

        name = self.name

        short_display_name = self.short_display_name

        color = self.color

        alternate_color = self.alternate_color

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "abbreviation": abbreviation,
                "displayName": display_name,
            }
        )
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if color is not UNSET:
            field_dict["color"] = color
        if alternate_color is not UNSET:
            field_dict["alternateColor"] = alternate_color

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        abbreviation = d.pop("abbreviation")

        display_name = d.pop("displayName")

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        short_display_name = d.pop("shortDisplayName", UNSET)

        color = d.pop("color", UNSET)

        alternate_color = d.pop("alternateColor", UNSET)

        event_team = cls(
            id=id,
            abbreviation=abbreviation,
            display_name=display_name,
            location=location,
            name=name,
            short_display_name=short_display_name,
            color=color,
            alternate_color=alternate_color,
        )

        event_team.additional_properties = d
        return event_team

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
