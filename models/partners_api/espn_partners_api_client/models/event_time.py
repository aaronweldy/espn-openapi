import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventTime")


@_attrs_define
class EventTime:
    """
    Attributes:
        value (Union[Unset, datetime.datetime]): Event time value Example: 2025-09-05T00:20Z.
        time_valid (Union[Unset, bool]): Whether the time is confirmed Example: True.
        display_value (Union[Unset, str]): Display time value Example: 8:20 ET.
    """

    value: Union[Unset, datetime.datetime] = UNSET
    time_valid: Union[Unset, bool] = UNSET
    display_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value: Union[Unset, str] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.isoformat()

        time_valid = self.time_valid

        display_value = self.display_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if time_valid is not UNSET:
            field_dict["timeValid"] = time_valid
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _value = d.pop("value", UNSET)
        value: Union[Unset, datetime.datetime]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = isoparse(_value)

        time_valid = d.pop("timeValid", UNSET)

        display_value = d.pop("displayValue", UNSET)

        event_time = cls(
            value=value,
            time_valid=time_valid,
            display_value=display_value,
        )

        event_time.additional_properties = d
        return event_time

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
