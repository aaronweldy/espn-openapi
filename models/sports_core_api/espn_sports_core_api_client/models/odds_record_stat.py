from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OddsRecordStat")


@_attrs_define
class OddsRecordStat:
    """
    Attributes:
        display_name (str): Display name for the statistic Example: Wins.
        abbreviation (str): Abbreviation for the statistic Example: W.
        type (str): Type of the statistic Example: win.
        value (float): Numeric value of the statistic Example: 16.0.
        display_value (str): Display value of the statistic Example: 16.
    """

    display_name: str
    abbreviation: str
    type: str
    value: float
    display_value: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name

        abbreviation = self.abbreviation

        type = self.type

        value = self.value

        display_value = self.display_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "abbreviation": abbreviation,
                "type": type,
                "value": value,
                "displayValue": display_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName")

        abbreviation = d.pop("abbreviation")

        type = d.pop("type")

        value = d.pop("value")

        display_value = d.pop("displayValue")

        odds_record_stat = cls(
            display_name=display_name,
            abbreviation=abbreviation,
            type=type,
            value=value,
            display_value=display_value,
        )

        odds_record_stat.additional_properties = d
        return odds_record_stat

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
