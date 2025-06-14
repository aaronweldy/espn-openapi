from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OddsValue")


@_attrs_define
class OddsValue:
    """
    Attributes:
        alternate_display_value (str):
        american (str):
        value (Union[Unset, float]):
        display_value (Union[Unset, str]):
        decimal (Union[Unset, float]):
        fraction (Union[Unset, str]):
    """

    alternate_display_value: str
    american: str
    value: Union[Unset, float] = UNSET
    display_value: Union[Unset, str] = UNSET
    decimal: Union[Unset, float] = UNSET
    fraction: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alternate_display_value = self.alternate_display_value

        american = self.american

        value = self.value

        display_value = self.display_value

        decimal = self.decimal

        fraction = self.fraction

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alternateDisplayValue": alternate_display_value,
                "american": american,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value
        if decimal is not UNSET:
            field_dict["decimal"] = decimal
        if fraction is not UNSET:
            field_dict["fraction"] = fraction

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alternate_display_value = d.pop("alternateDisplayValue")

        american = d.pop("american")

        value = d.pop("value", UNSET)

        display_value = d.pop("displayValue", UNSET)

        decimal = d.pop("decimal", UNSET)

        fraction = d.pop("fraction", UNSET)

        odds_value = cls(
            alternate_display_value=alternate_display_value,
            american=american,
            value=value,
            display_value=display_value,
            decimal=decimal,
            fraction=fraction,
        )

        odds_value.additional_properties = d
        return odds_value

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
