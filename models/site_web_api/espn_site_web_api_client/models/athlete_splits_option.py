from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AthleteSplitsOption")


@_attrs_define
class AthleteSplitsOption:
    """Option in NFL Athlete Splits filter.

    Attributes:
        value (str):
        display_value (str):
        short_display_name (Union[None, Unset, str]):
    """

    value: str
    display_value: str
    short_display_name: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value

        display_value = self.display_value

        short_display_name: Union[None, Unset, str]
        if isinstance(self.short_display_name, Unset):
            short_display_name = UNSET
        else:
            short_display_name = self.short_display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "displayValue": display_value,
            }
        )
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value")

        display_value = d.pop("displayValue")

        def _parse_short_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        short_display_name = _parse_short_display_name(d.pop("shortDisplayName", UNSET))

        athlete_splits_option = cls(
            value=value,
            display_value=display_value,
            short_display_name=short_display_name,
        )

        athlete_splits_option.additional_properties = d
        return athlete_splits_option

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
