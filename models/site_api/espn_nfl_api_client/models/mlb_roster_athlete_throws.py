from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mlb_roster_athlete_throws_abbreviation import MlbRosterAthleteThrowsAbbreviation
from ..models.mlb_roster_athlete_throws_display_value import MlbRosterAthleteThrowsDisplayValue
from ..models.mlb_roster_athlete_throws_type import MlbRosterAthleteThrowsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MlbRosterAthleteThrows")


@_attrs_define
class MlbRosterAthleteThrows:
    """
    Attributes:
        type (Union[Unset, MlbRosterAthleteThrowsType]):
        abbreviation (Union[Unset, MlbRosterAthleteThrowsAbbreviation]):
        display_value (Union[Unset, MlbRosterAthleteThrowsDisplayValue]):
    """

    type: Union[Unset, MlbRosterAthleteThrowsType] = UNSET
    abbreviation: Union[Unset, MlbRosterAthleteThrowsAbbreviation] = UNSET
    display_value: Union[Unset, MlbRosterAthleteThrowsDisplayValue] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        abbreviation: Union[Unset, str] = UNSET
        if not isinstance(self.abbreviation, Unset):
            abbreviation = self.abbreviation.value

        display_value: Union[Unset, str] = UNSET
        if not isinstance(self.display_value, Unset):
            display_value = self.display_value.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, MlbRosterAthleteThrowsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = MlbRosterAthleteThrowsType(_type)

        _abbreviation = d.pop("abbreviation", UNSET)
        abbreviation: Union[Unset, MlbRosterAthleteThrowsAbbreviation]
        if isinstance(_abbreviation, Unset):
            abbreviation = UNSET
        else:
            abbreviation = MlbRosterAthleteThrowsAbbreviation(_abbreviation)

        _display_value = d.pop("displayValue", UNSET)
        display_value: Union[Unset, MlbRosterAthleteThrowsDisplayValue]
        if isinstance(_display_value, Unset):
            display_value = UNSET
        else:
            display_value = MlbRosterAthleteThrowsDisplayValue(_display_value)

        mlb_roster_athlete_throws = cls(
            type=type,
            abbreviation=abbreviation,
            display_value=display_value,
        )

        mlb_roster_athlete_throws.additional_properties = d
        return mlb_roster_athlete_throws

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
