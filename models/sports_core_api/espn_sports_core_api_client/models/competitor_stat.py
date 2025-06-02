from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompetitorStat")


@_attrs_define
class CompetitorStat:
    """
    Attributes:
        name (str): Stat name
        display_name (str): Display name for the stat
        abbreviation (str): Stat abbreviation
        short_display_name (Union[Unset, str]): Short display name
        description (Union[Unset, str]): Stat description
        value (Union[Unset, float]): Stat value
        display_value (Union[Unset, str]): Display value
        per_game_value (Union[Unset, float]): Per game value
        per_game_display_value (Union[Unset, str]): Per game display value
        rank (Union[Unset, int]): Rank for this stat
        rank_display_value (Union[Unset, str]): Rank display value
    """

    name: str
    display_name: str
    abbreviation: str
    short_display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    value: Union[Unset, float] = UNSET
    display_value: Union[Unset, str] = UNSET
    per_game_value: Union[Unset, float] = UNSET
    per_game_display_value: Union[Unset, str] = UNSET
    rank: Union[Unset, int] = UNSET
    rank_display_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        abbreviation = self.abbreviation

        short_display_name = self.short_display_name

        description = self.description

        value = self.value

        display_value = self.display_value

        per_game_value = self.per_game_value

        per_game_display_value = self.per_game_display_value

        rank = self.rank

        rank_display_value = self.rank_display_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "displayName": display_name,
                "abbreviation": abbreviation,
            }
        )
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if description is not UNSET:
            field_dict["description"] = description
        if value is not UNSET:
            field_dict["value"] = value
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value
        if per_game_value is not UNSET:
            field_dict["perGameValue"] = per_game_value
        if per_game_display_value is not UNSET:
            field_dict["perGameDisplayValue"] = per_game_display_value
        if rank is not UNSET:
            field_dict["rank"] = rank
        if rank_display_value is not UNSET:
            field_dict["rankDisplayValue"] = rank_display_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        display_name = d.pop("displayName")

        abbreviation = d.pop("abbreviation")

        short_display_name = d.pop("shortDisplayName", UNSET)

        description = d.pop("description", UNSET)

        value = d.pop("value", UNSET)

        display_value = d.pop("displayValue", UNSET)

        per_game_value = d.pop("perGameValue", UNSET)

        per_game_display_value = d.pop("perGameDisplayValue", UNSET)

        rank = d.pop("rank", UNSET)

        rank_display_value = d.pop("rankDisplayValue", UNSET)

        competitor_stat = cls(
            name=name,
            display_name=display_name,
            abbreviation=abbreviation,
            short_display_name=short_display_name,
            description=description,
            value=value,
            display_value=display_value,
            per_game_value=per_game_value,
            per_game_display_value=per_game_display_value,
            rank=rank,
            rank_display_value=rank_display_value,
        )

        competitor_stat.additional_properties = d
        return competitor_stat

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
