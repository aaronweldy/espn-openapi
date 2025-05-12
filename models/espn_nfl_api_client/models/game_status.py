from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_type import StatusType


T = TypeVar("T", bound="GameStatus")


@_attrs_define
class GameStatus:
    """
    Attributes:
        type_ (StatusType):
        clock (Union[Unset, float]):
        display_clock (Union[Unset, str]):  Example: 0:00.
        period (Union[Unset, int]):  Example: 4.
    """

    type_: "StatusType"
    clock: Union[Unset, float] = UNSET
    display_clock: Union[Unset, str] = UNSET
    period: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.to_dict()

        clock = self.clock

        display_clock = self.display_clock

        period = self.period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_type import StatusType

        d = dict(src_dict)
        type_ = StatusType.from_dict(d.pop("type"))

        clock = d.pop("clock", UNSET)

        display_clock = d.pop("displayClock", UNSET)

        period = d.pop("period", UNSET)

        game_status = cls(
            type_=type_,
            clock=clock,
            display_clock=display_clock,
            period=period,
        )

        game_status.additional_properties = d
        return game_status

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
