from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MlbRosterAthleteBirthPlace")


@_attrs_define
class MlbRosterAthleteBirthPlace:
    """
    Attributes:
        city (Union[Unset, str]):
        state (Union[Unset, str]):
        country (Union[Unset, str]):
        display_text (Union[Unset, str]):
    """

    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    display_text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        city = self.city

        state = self.state

        country = self.country

        display_text = self.display_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country
        if display_text is not UNSET:
            field_dict["displayText"] = display_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        country = d.pop("country", UNSET)

        display_text = d.pop("displayText", UNSET)

        mlb_roster_athlete_birth_place = cls(
            city=city,
            state=state,
            country=country,
            display_text=display_text,
        )

        mlb_roster_athlete_birth_place.additional_properties = d
        return mlb_roster_athlete_birth_place

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
