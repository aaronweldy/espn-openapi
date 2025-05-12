from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.game_format_overtime import GameFormatOvertime
    from ..models.game_format_regulation import GameFormatRegulation


T = TypeVar("T", bound="GameFormat")


@_attrs_define
class GameFormat:
    """
    Attributes:
        regulation (Union[Unset, GameFormatRegulation]):
        overtime (Union[Unset, GameFormatOvertime]):
    """

    regulation: Union[Unset, "GameFormatRegulation"] = UNSET
    overtime: Union[Unset, "GameFormatOvertime"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        regulation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.regulation, Unset):
            regulation = self.regulation.to_dict()

        overtime: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.overtime, Unset):
            overtime = self.overtime.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if regulation is not UNSET:
            field_dict["regulation"] = regulation
        if overtime is not UNSET:
            field_dict["overtime"] = overtime

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_format_overtime import GameFormatOvertime
        from ..models.game_format_regulation import GameFormatRegulation

        d = dict(src_dict)
        _regulation = d.pop("regulation", UNSET)
        regulation: Union[Unset, GameFormatRegulation]
        if isinstance(_regulation, Unset):
            regulation = UNSET
        else:
            regulation = GameFormatRegulation.from_dict(_regulation)

        _overtime = d.pop("overtime", UNSET)
        overtime: Union[Unset, GameFormatOvertime]
        if isinstance(_overtime, Unset):
            overtime = UNSET
        else:
            overtime = GameFormatOvertime.from_dict(_overtime)

        game_format = cls(
            regulation=regulation,
            overtime=overtime,
        )

        game_format.additional_properties = d
        return game_format

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
