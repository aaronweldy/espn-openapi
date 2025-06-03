from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_player_stats_stats import FantasyPlayerStatsStats


T = TypeVar("T", bound="FantasyPlayerStats")


@_attrs_define
class FantasyPlayerStats:
    """
    Attributes:
        external_id (Union[Unset, str]): External ID for the stats
        id (Union[Unset, str]): Stats ID
        pro_team_id (Union[Unset, int]): Professional team ID
        scoring_period_id (Union[Unset, int]): Scoring period ID
        season_id (Union[Unset, int]): Season ID
        stat_source_id (Union[Unset, int]): Source ID for the stats
        stat_split_type_id (Union[Unset, int]): Split type ID for the stats
        stats (Union[Unset, FantasyPlayerStatsStats]): Statistical values
    """

    external_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    pro_team_id: Union[Unset, int] = UNSET
    scoring_period_id: Union[Unset, int] = UNSET
    season_id: Union[Unset, int] = UNSET
    stat_source_id: Union[Unset, int] = UNSET
    stat_split_type_id: Union[Unset, int] = UNSET
    stats: Union[Unset, "FantasyPlayerStatsStats"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_id = self.external_id

        id = self.id

        pro_team_id = self.pro_team_id

        scoring_period_id = self.scoring_period_id

        season_id = self.season_id

        stat_source_id = self.stat_source_id

        stat_split_type_id = self.stat_split_type_id

        stats: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if id is not UNSET:
            field_dict["id"] = id
        if pro_team_id is not UNSET:
            field_dict["proTeamId"] = pro_team_id
        if scoring_period_id is not UNSET:
            field_dict["scoringPeriodId"] = scoring_period_id
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if stat_source_id is not UNSET:
            field_dict["statSourceId"] = stat_source_id
        if stat_split_type_id is not UNSET:
            field_dict["statSplitTypeId"] = stat_split_type_id
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_player_stats_stats import FantasyPlayerStatsStats

        d = src_dict.copy()
        external_id = d.pop("externalId", UNSET)

        id = d.pop("id", UNSET)

        pro_team_id = d.pop("proTeamId", UNSET)

        scoring_period_id = d.pop("scoringPeriodId", UNSET)

        season_id = d.pop("seasonId", UNSET)

        stat_source_id = d.pop("statSourceId", UNSET)

        stat_split_type_id = d.pop("statSplitTypeId", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, FantasyPlayerStatsStats]
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = FantasyPlayerStatsStats.from_dict(_stats)

        fantasy_player_stats = cls(
            external_id=external_id,
            id=id,
            pro_team_id=pro_team_id,
            scoring_period_id=scoring_period_id,
            season_id=season_id,
            stat_source_id=stat_source_id,
            stat_split_type_id=stat_split_type_id,
            stats=stats,
        )

        fantasy_player_stats.additional_properties = d
        return fantasy_player_stats

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
