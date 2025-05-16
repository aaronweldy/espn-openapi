from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScoreboardCalendarEntry")


@_attrs_define
class ScoreboardCalendarEntry:
    """
    Attributes:
        end_date (Union[Unset, str]):
        alternate_label (Union[Unset, str]):
        label (Union[Unset, str]):
        detail (Union[Unset, str]):
        value (Union[Unset, str]):
        start_date (Union[Unset, str]):
    """

    end_date: Union[Unset, str] = UNSET
    alternate_label: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    detail: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end_date = self.end_date

        alternate_label = self.alternate_label

        label = self.label

        detail = self.detail

        value = self.value

        start_date = self.start_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if alternate_label is not UNSET:
            field_dict["alternateLabel"] = alternate_label
        if label is not UNSET:
            field_dict["label"] = label
        if detail is not UNSET:
            field_dict["detail"] = detail
        if value is not UNSET:
            field_dict["value"] = value
        if start_date is not UNSET:
            field_dict["startDate"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        end_date = d.pop("endDate", UNSET)

        alternate_label = d.pop("alternateLabel", UNSET)

        label = d.pop("label", UNSET)

        detail = d.pop("detail", UNSET)

        value = d.pop("value", UNSET)

        start_date = d.pop("startDate", UNSET)

        scoreboard_calendar_entry = cls(
            end_date=end_date,
            alternate_label=alternate_label,
            label=label,
            detail=detail,
            value=value,
            start_date=start_date,
        )

        scoreboard_calendar_entry.additional_properties = d
        return scoreboard_calendar_entry

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
