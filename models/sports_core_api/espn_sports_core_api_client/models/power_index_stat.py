from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PowerIndexStat")


@_attrs_define
class PowerIndexStat:
    """Individual power index statistic

    Attributes:
        name (str): Internal name of the statistic Example: teampredptdiff.
        display_name (str): Display name of the statistic Example: PRED PT DIFF.
        description (Union[Unset, str]): Detailed description of what this statistic represents Example: Expected margin
            of victory for the FPI favorite..
        abbreviation (Union[Unset, str]): Abbreviation for the statistic Example: PRED PT DIFF.
        value (Union[Unset, float]): Numeric value of the statistic Example: 12.175.
        display_value (Union[Unset, str]): Formatted display value of the statistic Example: 12.2.
    """

    name: str
    display_name: str
    description: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    value: Union[Unset, float] = UNSET
    display_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        description = self.description

        abbreviation = self.abbreviation

        value = self.value

        display_value = self.display_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "displayName": display_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if value is not UNSET:
            field_dict["value"] = value
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        display_name = d.pop("displayName")

        description = d.pop("description", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        value = d.pop("value", UNSET)

        display_value = d.pop("displayValue", UNSET)

        power_index_stat = cls(
            name=name,
            display_name=display_name,
            description=description,
            abbreviation=abbreviation,
            value=value,
            display_value=display_value,
        )

        power_index_stat.additional_properties = d
        return power_index_stat

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
