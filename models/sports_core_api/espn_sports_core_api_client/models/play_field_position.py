from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.play_clock import PlayClock
    from ..models.play_period import PlayPeriod


T = TypeVar("T", bound="PlayFieldPosition")


@_attrs_define
class PlayFieldPosition:
    """
    Attributes:
        period (Union[Unset, PlayPeriod]):
        clock (Union[Unset, PlayClock]):
        yard_line (Union[Unset, int]):
        text (Union[Unset, str]):
    """

    period: Union[Unset, "PlayPeriod"] = UNSET
    clock: Union[Unset, "PlayClock"] = UNSET
    yard_line: Union[Unset, int] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        clock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.clock, Unset):
            clock = self.clock.to_dict()

        yard_line = self.yard_line

        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period is not UNSET:
            field_dict["period"] = period
        if clock is not UNSET:
            field_dict["clock"] = clock
        if yard_line is not UNSET:
            field_dict["yardLine"] = yard_line
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.play_clock import PlayClock
        from ..models.play_period import PlayPeriod

        d = src_dict.copy()
        _period = d.pop("period", UNSET)
        period: Union[Unset, PlayPeriod]
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = PlayPeriod.from_dict(_period)

        _clock = d.pop("clock", UNSET)
        clock: Union[Unset, PlayClock]
        if isinstance(_clock, Unset):
            clock = UNSET
        else:
            clock = PlayClock.from_dict(_clock)

        yard_line = d.pop("yardLine", UNSET)

        text = d.pop("text", UNSET)

        play_field_position = cls(
            period=period,
            clock=clock,
            yard_line=yard_line,
            text=text,
        )

        play_field_position.additional_properties = d
        return play_field_position

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
