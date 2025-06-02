from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_status_type import EventStatusType


T = TypeVar("T", bound="EventStatus")


@_attrs_define
class EventStatus:
    """
    Attributes:
        type (EventStatusType):
        clock (Union[Unset, float]): Game clock in seconds
        display_clock (Union[Unset, str]): Display clock value Example: 0:00.
        period (Union[Unset, int]): Current period
    """

    type: "EventStatusType"
    clock: Union[Unset, float] = UNSET
    display_clock: Union[Unset, str] = UNSET
    period: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.to_dict()

        clock = self.clock

        display_clock = self.display_clock

        period = self.period

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if clock is not UNSET:
            field_dict["clock"] = clock
        if display_clock is not UNSET:
            field_dict["displayClock"] = display_clock
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_status_type import EventStatusType

        d = src_dict.copy()
        type = EventStatusType.from_dict(d.pop("type"))

        clock = d.pop("clock", UNSET)

        display_clock = d.pop("displayClock", UNSET)

        period = d.pop("period", UNSET)

        event_status = cls(
            type=type,
            clock=clock,
            display_clock=display_clock,
            period=period,
        )

        event_status.additional_properties = d
        return event_status

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
