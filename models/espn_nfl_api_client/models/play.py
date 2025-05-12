from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.play_clock import PlayClock
    from ..models.play_period import PlayPeriod
    from ..models.play_type import PlayType


T = TypeVar("T", bound="Play")


@_attrs_define
class Play:
    """
    Attributes:
        id (Union[Unset, str]):
        sequence_number (Union[Unset, str]):
        type_ (Union[Unset, PlayType]):
        text (Union[Unset, str]):
        period (Union[Unset, PlayPeriod]):
        clock (Union[Unset, PlayClock]):
    """

    id: Union[Unset, str] = UNSET
    sequence_number: Union[Unset, str] = UNSET
    type_: Union[Unset, "PlayType"] = UNSET
    text: Union[Unset, str] = UNSET
    period: Union[Unset, "PlayPeriod"] = UNSET
    clock: Union[Unset, "PlayClock"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sequence_number = self.sequence_number

        type_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        text = self.text

        period: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        clock: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.clock, Unset):
            clock = self.clock.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if sequence_number is not UNSET:
            field_dict["sequenceNumber"] = sequence_number
        if type_ is not UNSET:
            field_dict["type"] = type_
        if text is not UNSET:
            field_dict["text"] = text
        if period is not UNSET:
            field_dict["period"] = period
        if clock is not UNSET:
            field_dict["clock"] = clock

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.play_clock import PlayClock
        from ..models.play_period import PlayPeriod
        from ..models.play_type import PlayType

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        sequence_number = d.pop("sequenceNumber", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, PlayType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PlayType.from_dict(_type_)

        text = d.pop("text", UNSET)

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

        play = cls(
            id=id,
            sequence_number=sequence_number,
            type_=type_,
            text=text,
            period=period,
            clock=clock,
        )

        play.additional_properties = d
        return play

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
