from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mlb_roster_athlete_bats_abbreviation import MlbRosterAthleteBatsAbbreviation
from ..models.mlb_roster_athlete_bats_display_value import MlbRosterAthleteBatsDisplayValue
from ..models.mlb_roster_athlete_bats_type import MlbRosterAthleteBatsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MlbRosterAthleteBats")


@_attrs_define
class MlbRosterAthleteBats:
    """
    Attributes:
        type (Union[Unset, MlbRosterAthleteBatsType]):
        abbreviation (Union[Unset, MlbRosterAthleteBatsAbbreviation]):
        display_value (Union[Unset, MlbRosterAthleteBatsDisplayValue]):
    """

    type: Union[Unset, MlbRosterAthleteBatsType] = UNSET
    abbreviation: Union[Unset, MlbRosterAthleteBatsAbbreviation] = UNSET
    display_value: Union[Unset, MlbRosterAthleteBatsDisplayValue] = UNSET
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
        type: Union[Unset, MlbRosterAthleteBatsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = MlbRosterAthleteBatsType(_type)

        _abbreviation = d.pop("abbreviation", UNSET)
        abbreviation: Union[Unset, MlbRosterAthleteBatsAbbreviation]
        if isinstance(_abbreviation, Unset):
            abbreviation = UNSET
        else:
            abbreviation = MlbRosterAthleteBatsAbbreviation(_abbreviation)

        _display_value = d.pop("displayValue", UNSET)
        display_value: Union[Unset, MlbRosterAthleteBatsDisplayValue]
        if isinstance(_display_value, Unset):
            display_value = UNSET
        else:
            display_value = MlbRosterAthleteBatsDisplayValue(_display_value)

        mlb_roster_athlete_bats = cls(
            type=type,
            abbreviation=abbreviation,
            display_value=display_value,
        )

        mlb_roster_athlete_bats.additional_properties = d
        return mlb_roster_athlete_bats

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
