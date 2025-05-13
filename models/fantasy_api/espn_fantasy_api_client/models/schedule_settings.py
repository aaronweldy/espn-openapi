from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleSettings")


@_attrs_define
class ScheduleSettings:
    """
    Attributes:
        matchup_period_count (int): Number of regular season matchup periods Example: 14.
        playoff_team_count (int): Number of teams that make playoffs Example: 6.
        matchup_period_length (Union[Unset, int]): Length of each matchup in weeks Example: 1.
        playoff_matchup_period_length (Union[Unset, int]): Length of playoff matchups in weeks Example: 1.
    """

    matchup_period_count: int
    playoff_team_count: int
    matchup_period_length: Union[Unset, int] = UNSET
    playoff_matchup_period_length: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        matchup_period_count = self.matchup_period_count

        playoff_team_count = self.playoff_team_count

        matchup_period_length = self.matchup_period_length

        playoff_matchup_period_length = self.playoff_matchup_period_length

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "matchupPeriodCount": matchup_period_count,
                "playoffTeamCount": playoff_team_count,
            }
        )
        if matchup_period_length is not UNSET:
            field_dict["matchupPeriodLength"] = matchup_period_length
        if playoff_matchup_period_length is not UNSET:
            field_dict["playoffMatchupPeriodLength"] = playoff_matchup_period_length

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        matchup_period_count = d.pop("matchupPeriodCount")

        playoff_team_count = d.pop("playoffTeamCount")

        matchup_period_length = d.pop("matchupPeriodLength", UNSET)

        playoff_matchup_period_length = d.pop("playoffMatchupPeriodLength", UNSET)

        schedule_settings = cls(
            matchup_period_count=matchup_period_count,
            playoff_team_count=playoff_team_count,
            matchup_period_length=matchup_period_length,
            playoff_matchup_period_length=playoff_matchup_period_length,
        )

        schedule_settings.additional_properties = d
        return schedule_settings

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
