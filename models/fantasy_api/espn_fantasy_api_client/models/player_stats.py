from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.player_stats_stats import PlayerStatsStats


T = TypeVar("T", bound="PlayerStats")


@_attrs_define
class PlayerStats:
    """
    Attributes:
        season_id (int): Season year Example: 2023.
        scoring_period_id (int): Week number Example: 1.
        stats (PlayerStatsStats): Stats by category (keys are stat IDs) Example: {'0': 25, '1': 38, '3': 297, '4': 3}.
        season_value (Union[Unset, int]): Season value Example: 2023.
        stat_source_id (Union[Unset, int]): Source of stats
        stat_split_type_id (Union[Unset, int]): Type of stat split
    """

    season_id: int
    scoring_period_id: int
    stats: "PlayerStatsStats"
    season_value: Union[Unset, int] = UNSET
    stat_source_id: Union[Unset, int] = UNSET
    stat_split_type_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        season_id = self.season_id

        scoring_period_id = self.scoring_period_id

        stats = self.stats.to_dict()

        season_value = self.season_value

        stat_source_id = self.stat_source_id

        stat_split_type_id = self.stat_split_type_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "seasonId": season_id,
                "scoringPeriodId": scoring_period_id,
                "stats": stats,
            }
        )
        if season_value is not UNSET:
            field_dict["seasonValue"] = season_value
        if stat_source_id is not UNSET:
            field_dict["statSourceId"] = stat_source_id
        if stat_split_type_id is not UNSET:
            field_dict["statSplitTypeId"] = stat_split_type_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.player_stats_stats import PlayerStatsStats

        d = src_dict.copy()
        season_id = d.pop("seasonId")

        scoring_period_id = d.pop("scoringPeriodId")

        stats = PlayerStatsStats.from_dict(d.pop("stats"))

        season_value = d.pop("seasonValue", UNSET)

        stat_source_id = d.pop("statSourceId", UNSET)

        stat_split_type_id = d.pop("statSplitTypeId", UNSET)

        player_stats = cls(
            season_id=season_id,
            scoring_period_id=scoring_period_id,
            stats=stats,
            season_value=season_value,
            stat_source_id=stat_source_id,
            stat_split_type_id=stat_split_type_id,
        )

        player_stats.additional_properties = d
        return player_stats

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
