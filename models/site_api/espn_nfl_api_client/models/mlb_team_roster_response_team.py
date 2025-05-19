from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MlbTeamRosterResponseTeam")


@_attrs_define
class MlbTeamRosterResponseTeam:
    """
    Attributes:
        id (Union[Unset, str]):
        abbreviation (Union[Unset, str]):
        location (Union[Unset, str]):
        name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        clubhouse (Union[Unset, str]):
        color (Union[Unset, str]):
        logo (Union[Unset, str]):
        record_summary (Union[Unset, str]):
        season_summary (Union[Unset, str]):
        standing_summary (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    clubhouse: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    logo: Union[Unset, str] = UNSET
    record_summary: Union[Unset, str] = UNSET
    season_summary: Union[Unset, str] = UNSET
    standing_summary: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        abbreviation = self.abbreviation

        location = self.location

        name = self.name

        display_name = self.display_name

        clubhouse = self.clubhouse

        color = self.color

        logo = self.logo

        record_summary = self.record_summary

        season_summary = self.season_summary

        standing_summary = self.standing_summary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if clubhouse is not UNSET:
            field_dict["clubhouse"] = clubhouse
        if color is not UNSET:
            field_dict["color"] = color
        if logo is not UNSET:
            field_dict["logo"] = logo
        if record_summary is not UNSET:
            field_dict["recordSummary"] = record_summary
        if season_summary is not UNSET:
            field_dict["seasonSummary"] = season_summary
        if standing_summary is not UNSET:
            field_dict["standingSummary"] = standing_summary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        clubhouse = d.pop("clubhouse", UNSET)

        color = d.pop("color", UNSET)

        logo = d.pop("logo", UNSET)

        record_summary = d.pop("recordSummary", UNSET)

        season_summary = d.pop("seasonSummary", UNSET)

        standing_summary = d.pop("standingSummary", UNSET)

        mlb_team_roster_response_team = cls(
            id=id,
            abbreviation=abbreviation,
            location=location,
            name=name,
            display_name=display_name,
            clubhouse=clubhouse,
            color=color,
            logo=logo,
            record_summary=record_summary,
            season_summary=season_summary,
            standing_summary=standing_summary,
        )

        mlb_team_roster_response_team.additional_properties = d
        return mlb_team_roster_response_team

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
