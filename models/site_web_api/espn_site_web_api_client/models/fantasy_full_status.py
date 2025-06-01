from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_full_status_type import FantasyFullStatusType


T = TypeVar("T", bound="FantasyFullStatus")


@_attrs_define
class FantasyFullStatus:
    """
    Attributes:
        clock (Union[Unset, str]):
        display_clock (Union[Unset, str]):
        period (Union[Unset, int]):
        type (Union[Unset, FantasyFullStatusType]):
    """

    clock: Union[Unset, str] = UNSET
    display_clock: Union[Unset, str] = UNSET
    period: Union[Unset, int] = UNSET
    type: Union[Unset, "FantasyFullStatusType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        clock = self.clock

        display_clock = self.display_clock

        period = self.period

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clock is not UNSET:
            field_dict["clock"] = clock
        if display_clock is not UNSET:
            field_dict["displayClock"] = display_clock
        if period is not UNSET:
            field_dict["period"] = period
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_full_status_type import FantasyFullStatusType

        d = src_dict.copy()
        clock = d.pop("clock", UNSET)

        display_clock = d.pop("displayClock", UNSET)

        period = d.pop("period", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, FantasyFullStatusType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = FantasyFullStatusType.from_dict(_type)

        fantasy_full_status = cls(
            clock=clock,
            display_clock=display_clock,
            period=period,
            type=type,
        )

        fantasy_full_status.additional_properties = d
        return fantasy_full_status

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
