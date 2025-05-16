from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_status_type import ScoreboardStatusType


T = TypeVar("T", bound="ScoreboardStatus")


@_attrs_define
class ScoreboardStatus:
    """
    Attributes:
        period (Union[Unset, int]):
        display_clock (Union[Unset, str]):
        is_tbd_flex (Union[Unset, bool]):
        clock (Union[Unset, int]):
        type (Union[Unset, ScoreboardStatusType]):
    """

    period: Union[Unset, int] = UNSET
    display_clock: Union[Unset, str] = UNSET
    is_tbd_flex: Union[Unset, bool] = UNSET
    clock: Union[Unset, int] = UNSET
    type: Union[Unset, "ScoreboardStatusType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period = self.period

        display_clock = self.display_clock

        is_tbd_flex = self.is_tbd_flex

        clock = self.clock

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period is not UNSET:
            field_dict["period"] = period
        if display_clock is not UNSET:
            field_dict["displayClock"] = display_clock
        if is_tbd_flex is not UNSET:
            field_dict["isTBDFlex"] = is_tbd_flex
        if clock is not UNSET:
            field_dict["clock"] = clock
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_status_type import ScoreboardStatusType

        d = src_dict.copy()
        period = d.pop("period", UNSET)

        display_clock = d.pop("displayClock", UNSET)

        is_tbd_flex = d.pop("isTBDFlex", UNSET)

        clock = d.pop("clock", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ScoreboardStatusType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ScoreboardStatusType.from_dict(_type)

        scoreboard_status = cls(
            period=period,
            display_clock=display_clock,
            is_tbd_flex=is_tbd_flex,
            clock=clock,
            type=type,
        )

        scoreboard_status.additional_properties = d
        return scoreboard_status

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
