import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarEntry")


@_attrs_define
class CalendarEntry:
    """
    Attributes:
        label (str):  Example: Week 1.
        value (str):  Example: 1.
        start_date (datetime.datetime):
        end_date (datetime.datetime):
        alternate_label (Union[Unset, str]):  Example: Week 1.
        detail (Union[Unset, str]):  Example: Sep 5-10.
    """

    label: str
    value: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    alternate_label: Union[Unset, str] = UNSET
    detail: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label

        value = self.value

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        alternate_label = self.alternate_label

        detail = self.detail

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "value": value,
                "startDate": start_date,
                "endDate": end_date,
            }
        )
        if alternate_label is not UNSET:
            field_dict["alternateLabel"] = alternate_label
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label")

        value = d.pop("value")

        start_date = isoparse(d.pop("startDate"))

        end_date = isoparse(d.pop("endDate"))

        alternate_label = d.pop("alternateLabel", UNSET)

        detail = d.pop("detail", UNSET)

        calendar_entry = cls(
            label=label,
            value=value,
            start_date=start_date,
            end_date=end_date,
            alternate_label=alternate_label,
            detail=detail,
        )

        calendar_entry.additional_properties = d
        return calendar_entry

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
