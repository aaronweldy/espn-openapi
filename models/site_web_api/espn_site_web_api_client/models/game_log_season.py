from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.season_type import SeasonType


T = TypeVar("T", bound="GameLogSeason")


@_attrs_define
class GameLogSeason:
    """
    Attributes:
        types (List['SeasonType']):
        year (int):  Example: 2024.
    """

    types: List["SeasonType"]
    year: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        types = []
        for types_item_data in self.types:
            types_item = types_item_data.to_dict()
            types.append(types_item)

        year = self.year

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "types": types,
                "year": year,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.season_type import SeasonType

        d = src_dict.copy()
        types = []
        _types = d.pop("types")
        for types_item_data in _types:
            types_item = SeasonType.from_dict(types_item_data)

            types.append(types_item)

        year = d.pop("year")

        game_log_season = cls(
            types=types,
            year=year,
        )

        game_log_season.additional_properties = d
        return game_log_season

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
