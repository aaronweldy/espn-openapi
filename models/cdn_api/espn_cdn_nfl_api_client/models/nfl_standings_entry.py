from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nfl_standings_stat import NflStandingsStat
    from ..models.nfl_standings_team import NflStandingsTeam


T = TypeVar("T", bound="NflStandingsEntry")


@_attrs_define
class NflStandingsEntry:
    """
    Attributes:
        stats (Union[Unset, List['NflStandingsStat']]):
        team (Union[Unset, NflStandingsTeam]):
    """

    stats: Union[Unset, List["NflStandingsStat"]] = UNSET
    team: Union[Unset, "NflStandingsTeam"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = []
            for stats_item_data in self.stats:
                stats_item = stats_item_data.to_dict()
                stats.append(stats_item)

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stats is not UNSET:
            field_dict["stats"] = stats
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_standings_stat import NflStandingsStat
        from ..models.nfl_standings_team import NflStandingsTeam

        d = src_dict.copy()
        stats = []
        _stats = d.pop("stats", UNSET)
        for stats_item_data in _stats or []:
            stats_item = NflStandingsStat.from_dict(stats_item_data)

            stats.append(stats_item)

        _team = d.pop("team", UNSET)
        team: Union[Unset, NflStandingsTeam]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = NflStandingsTeam.from_dict(_team)

        nfl_standings_entry = cls(
            stats=stats,
            team=team,
        )

        nfl_standings_entry.additional_properties = d
        return nfl_standings_entry

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
