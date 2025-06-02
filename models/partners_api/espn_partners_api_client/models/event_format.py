from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.period_format import PeriodFormat


T = TypeVar("T", bound="EventFormat")


@_attrs_define
class EventFormat:
    """
    Attributes:
        regulation (Union[Unset, PeriodFormat]):
        overtime (Union[Unset, PeriodFormat]):
    """

    regulation: Union[Unset, "PeriodFormat"] = UNSET
    overtime: Union[Unset, "PeriodFormat"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        regulation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.regulation, Unset):
            regulation = self.regulation.to_dict()

        overtime: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.overtime, Unset):
            overtime = self.overtime.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if regulation is not UNSET:
            field_dict["regulation"] = regulation
        if overtime is not UNSET:
            field_dict["overtime"] = overtime

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.period_format import PeriodFormat

        d = src_dict.copy()
        _regulation = d.pop("regulation", UNSET)
        regulation: Union[Unset, PeriodFormat]
        if isinstance(_regulation, Unset):
            regulation = UNSET
        else:
            regulation = PeriodFormat.from_dict(_regulation)

        _overtime = d.pop("overtime", UNSET)
        overtime: Union[Unset, PeriodFormat]
        if isinstance(_overtime, Unset):
            overtime = UNSET
        else:
            overtime = PeriodFormat.from_dict(_overtime)

        event_format = cls(
            regulation=regulation,
            overtime=overtime,
        )

        event_format.additional_properties = d
        return event_format

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
