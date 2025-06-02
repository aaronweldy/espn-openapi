from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.power_index_stat import PowerIndexStat
    from ..models.reference import Reference


T = TypeVar("T", bound="PowerIndexResponse")


@_attrs_define
class PowerIndexResponse:
    """ESPN Power Index metrics for a team in a specific game

    Attributes:
        team (Reference):
        season (int): Season year Example: 2022.
        stats (List['PowerIndexStat']): Array of power index statistics
        ref (Union[Unset, str]): Reference URL to this power index data
    """

    team: "Reference"
    season: int
    stats: List["PowerIndexStat"]
    ref: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team = self.team.to_dict()

        season = self.season

        stats = []
        for stats_item_data in self.stats:
            stats_item = stats_item_data.to_dict()
            stats.append(stats_item)

        ref = self.ref

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team": team,
                "season": season,
                "stats": stats,
            }
        )
        if ref is not UNSET:
            field_dict["$ref"] = ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.power_index_stat import PowerIndexStat
        from ..models.reference import Reference

        d = src_dict.copy()
        team = Reference.from_dict(d.pop("team"))

        season = d.pop("season")

        stats = []
        _stats = d.pop("stats")
        for stats_item_data in _stats:
            stats_item = PowerIndexStat.from_dict(stats_item_data)

            stats.append(stats_item)

        ref = d.pop("$ref", UNSET)

        power_index_response = cls(
            team=team,
            season=season,
            stats=stats,
            ref=ref,
        )

        power_index_response.additional_properties = d
        return power_index_response

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
