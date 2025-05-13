import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.calendar_entry import CalendarEntry


T = TypeVar("T", bound="CalendarItem")


@_attrs_define
class CalendarItem:
    """
    Attributes:
        label (str):  Example: Regular Season.
        value (str):  Example: 2.
        start_date (datetime.datetime):
        end_date (datetime.datetime):
        entries (Union[Unset, List['CalendarEntry']]):
    """

    label: str
    value: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    entries: Union[Unset, List["CalendarEntry"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label

        value = self.value

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        entries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

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
        if entries is not UNSET:
            field_dict["entries"] = entries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.calendar_entry import CalendarEntry

        d = src_dict.copy()
        label = d.pop("label")

        value = d.pop("value")

        start_date = isoparse(d.pop("startDate"))

        end_date = isoparse(d.pop("endDate"))

        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = CalendarEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        calendar_item = cls(
            label=label,
            value=value,
            start_date=start_date,
            end_date=end_date,
            entries=entries,
        )

        calendar_item.additional_properties = d
        return calendar_item

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
