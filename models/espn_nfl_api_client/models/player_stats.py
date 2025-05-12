from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.athlete import Athlete
    from ..models.player_stats_stats import PlayerStatsStats


T = TypeVar("T", bound="PlayerStats")


@_attrs_define
class PlayerStats:
    """
    Attributes:
        athlete (Union[Unset, Athlete]):
        stats (Union[Unset, PlayerStatsStats]):
    """

    athlete: Union[Unset, "Athlete"] = UNSET
    stats: Union[Unset, "PlayerStatsStats"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        athlete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.athlete, Unset):
            athlete = self.athlete.to_dict()

        stats: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if athlete is not UNSET:
            field_dict["athlete"] = athlete
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete import Athlete
        from ..models.player_stats_stats import PlayerStatsStats

        d = src_dict.copy()
        _athlete = d.pop("athlete", UNSET)
        athlete: Union[Unset, Athlete]
        if isinstance(_athlete, Unset):
            athlete = UNSET
        else:
            athlete = Athlete.from_dict(_athlete)

        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, PlayerStatsStats]
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = PlayerStatsStats.from_dict(_stats)

        player_stats = cls(
            athlete=athlete,
            stats=stats,
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
