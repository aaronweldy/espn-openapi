from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Weather")


@_attrs_define
class Weather:
    """
    Attributes:
        temperature (Union[Unset, int]):  Example: 73.
        condition (Union[Unset, str]):  Example: Clear.
        humidity (Union[Unset, int]):  Example: 45.
        display_value (Union[Unset, str]):  Example: Clear.
    """

    temperature: Union[Unset, int] = UNSET
    condition: Union[Unset, str] = UNSET
    humidity: Union[Unset, int] = UNSET
    display_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        temperature = self.temperature

        condition = self.condition

        humidity = self.humidity

        display_value = self.display_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if condition is not UNSET:
            field_dict["condition"] = condition
        if humidity is not UNSET:
            field_dict["humidity"] = humidity
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        temperature = d.pop("temperature", UNSET)

        condition = d.pop("condition", UNSET)

        humidity = d.pop("humidity", UNSET)

        display_value = d.pop("displayValue", UNSET)

        weather = cls(
            temperature=temperature,
            condition=condition,
            humidity=humidity,
            display_value=display_value,
        )

        weather.additional_properties = d
        return weather

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
