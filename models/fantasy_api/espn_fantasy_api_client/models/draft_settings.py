import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DraftSettings")


@_attrs_define
class DraftSettings:
    """
    Attributes:
        type (int): Draft type (1 = snake, 2 = auction) Example: 1.
        slot_count (int): Number of roster slots per team Example: 16.
        date (Union[Unset, datetime.datetime]): Draft date Example: 2023-08-31T23:00:00Z.
        time_per_selection (Union[Unset, int]): Seconds per pick Example: 90.
    """

    type: int
    slot_count: int
    date: Union[Unset, datetime.datetime] = UNSET
    time_per_selection: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        slot_count = self.slot_count

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        time_per_selection = self.time_per_selection

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "slotCount": slot_count,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if time_per_selection is not UNSET:
            field_dict["timePerSelection"] = time_per_selection

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        slot_count = d.pop("slotCount")

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        time_per_selection = d.pop("timePerSelection", UNSET)

        draft_settings = cls(
            type=type,
            slot_count=slot_count,
            date=date,
            time_per_selection=time_per_selection,
        )

        draft_settings.additional_properties = d
        return draft_settings

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
