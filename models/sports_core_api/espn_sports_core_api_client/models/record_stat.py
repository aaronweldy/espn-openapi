from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordStat")


@_attrs_define
class RecordStat:
    """Individual statistic within a team record

    Attributes:
        name (str): Internal name of the statistic Example: wins.
        display_name (str): Display name of the statistic Example: Wins.
        type (str): Type of statistic Example: wins.
        value (float): Numeric value of the statistic Example: 2.0.
        display_value (str): Formatted display value Example: 2.
        short_display_name (Union[Unset, str]): Short display name Example: W.
        description (Union[Unset, str]): Description of the statistic Example: Wins.
        abbreviation (Union[Unset, str]): Abbreviation for the statistic Example: W.
    """

    name: str
    display_name: str
    type: str
    value: float
    display_value: str
    short_display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        type = self.type

        value = self.value

        display_value = self.display_value

        short_display_name = self.short_display_name

        description = self.description

        abbreviation = self.abbreviation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "displayName": display_name,
                "type": type,
                "value": value,
                "displayValue": display_value,
            }
        )
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if description is not UNSET:
            field_dict["description"] = description
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        display_name = d.pop("displayName")

        type = d.pop("type")

        value = d.pop("value")

        display_value = d.pop("displayValue")

        short_display_name = d.pop("shortDisplayName", UNSET)

        description = d.pop("description", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        record_stat = cls(
            name=name,
            display_name=display_name,
            type=type,
            value=value,
            display_value=display_value,
            short_display_name=short_display_name,
            description=description,
            abbreviation=abbreviation,
        )

        record_stat.additional_properties = d
        return record_stat

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
