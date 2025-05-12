from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GameFormatOvertime")


@_attrs_define
class GameFormatOvertime:
    """
    Attributes:
        periods (Union[Unset, int]):
        half_length (Union[Unset, bool]):
    """

    periods: Union[Unset, int] = UNSET
    half_length: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        periods = self.periods

        half_length = self.half_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if periods is not UNSET:
            field_dict["periods"] = periods
        if half_length is not UNSET:
            field_dict["halfLength"] = half_length

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        periods = d.pop("periods", UNSET)

        half_length = d.pop("halfLength", UNSET)

        game_format_overtime = cls(
            periods=periods,
            half_length=half_length,
        )

        game_format_overtime.additional_properties = d
        return game_format_overtime

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
