from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScoreboardHeaderResponseSportsItemLeaguesItemSmartdatesItem")


@_attrs_define
class ScoreboardHeaderResponseSportsItemLeaguesItemSmartdatesItem:
    """
    Attributes:
        label (Union[Unset, str]):
        season (Union[Unset, int]):
        seasontype (Union[Unset, int]):
        week (Union[Unset, int]):
    """

    label: Union[Unset, str] = UNSET
    season: Union[Unset, int] = UNSET
    seasontype: Union[Unset, int] = UNSET
    week: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label

        season = self.season

        seasontype = self.seasontype

        week = self.week

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if season is not UNSET:
            field_dict["season"] = season
        if seasontype is not UNSET:
            field_dict["seasontype"] = seasontype
        if week is not UNSET:
            field_dict["week"] = week

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label", UNSET)

        season = d.pop("season", UNSET)

        seasontype = d.pop("seasontype", UNSET)

        week = d.pop("week", UNSET)

        scoreboard_header_response_sports_item_leagues_item_smartdates_item = cls(
            label=label,
            season=season,
            seasontype=seasontype,
            week=week,
        )

        scoreboard_header_response_sports_item_leagues_item_smartdates_item.additional_properties = d
        return scoreboard_header_response_sports_item_leagues_item_smartdates_item

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
