from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.leader_athlete import LeaderAthlete
    from ..models.leader_entry_statistics import LeaderEntryStatistics
    from ..models.leader_team import LeaderTeam


T = TypeVar("T", bound="LeaderEntry")


@_attrs_define
class LeaderEntry:
    """
    Attributes:
        display_value (str): Formatted display value of the statistic
        value (float): Numeric value of the statistic
        athlete (LeaderAthlete):
        rel (Union[Unset, List[str]]): Relationship types
        statistics (Union[Unset, LeaderEntryStatistics]): Additional statistics (may be empty)
        team (Union[Unset, LeaderTeam]):
        teams (Union[Unset, List['LeaderTeam']]):
    """

    display_value: str
    value: float
    athlete: "LeaderAthlete"
    rel: Union[Unset, List[str]] = UNSET
    statistics: Union[Unset, "LeaderEntryStatistics"] = UNSET
    team: Union[Unset, "LeaderTeam"] = UNSET
    teams: Union[Unset, List["LeaderTeam"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_value = self.display_value

        value = self.value

        athlete = self.athlete.to_dict()

        rel: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rel, Unset):
            rel = self.rel

        statistics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        teams: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayValue": display_value,
                "value": value,
                "athlete": athlete,
            }
        )
        if rel is not UNSET:
            field_dict["rel"] = rel
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if team is not UNSET:
            field_dict["team"] = team
        if teams is not UNSET:
            field_dict["teams"] = teams

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.leader_athlete import LeaderAthlete
        from ..models.leader_entry_statistics import LeaderEntryStatistics
        from ..models.leader_team import LeaderTeam

        d = src_dict.copy()
        display_value = d.pop("displayValue")

        value = d.pop("value")

        athlete = LeaderAthlete.from_dict(d.pop("athlete"))

        rel = cast(List[str], d.pop("rel", UNSET))

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, LeaderEntryStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = LeaderEntryStatistics.from_dict(_statistics)

        _team = d.pop("team", UNSET)
        team: Union[Unset, LeaderTeam]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = LeaderTeam.from_dict(_team)

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = LeaderTeam.from_dict(teams_item_data)

            teams.append(teams_item)

        leader_entry = cls(
            display_value=display_value,
            value=value,
            athlete=athlete,
            rel=rel,
            statistics=statistics,
            team=team,
            teams=teams,
        )

        leader_entry.additional_properties = d
        return leader_entry

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
