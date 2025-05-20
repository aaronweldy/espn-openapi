from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MlbAthleteDetailsResponseExperience")


@_attrs_define
class MlbAthleteDetailsResponseExperience:
    """
    Attributes:
        years (Union[Unset, int]):
        display_value (Union[Unset, str]):
    """

    years: Union[Unset, int] = UNSET
    display_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        years = self.years

        display_value = self.display_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if years is not UNSET:
            field_dict["years"] = years
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        years = d.pop("years", UNSET)

        display_value = d.pop("displayValue", UNSET)

        mlb_athlete_details_response_experience = cls(
            years=years,
            display_value=display_value,
        )

        mlb_athlete_details_response_experience.additional_properties = d
        return mlb_athlete_details_response_experience

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
