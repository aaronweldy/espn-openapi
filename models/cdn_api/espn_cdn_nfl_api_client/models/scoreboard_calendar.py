from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_calendar_entry import ScoreboardCalendarEntry


T = TypeVar("T", bound="ScoreboardCalendar")


@_attrs_define
class ScoreboardCalendar:
    """
    Attributes:
        entries (Union[Unset, List['ScoreboardCalendarEntry']]):
        end_date (Union[Unset, str]):
        label (Union[Unset, str]):
        value (Union[Unset, str]):
        start_date (Union[Unset, str]):
    """

    entries: Union[Unset, List["ScoreboardCalendarEntry"]] = UNSET
    end_date: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        end_date = self.end_date

        label = self.label

        value = self.value

        start_date = self.start_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entries is not UNSET:
            field_dict["entries"] = entries
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if label is not UNSET:
            field_dict["label"] = label
        if value is not UNSET:
            field_dict["value"] = value
        if start_date is not UNSET:
            field_dict["startDate"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_calendar_entry import ScoreboardCalendarEntry

        d = src_dict.copy()
        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = ScoreboardCalendarEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        end_date = d.pop("endDate", UNSET)

        label = d.pop("label", UNSET)

        value = d.pop("value", UNSET)

        start_date = d.pop("startDate", UNSET)

        scoreboard_calendar = cls(
            entries=entries,
            end_date=end_date,
            label=label,
            value=value,
            start_date=start_date,
        )

        scoreboard_calendar.additional_properties = d
        return scoreboard_calendar

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
