import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LeagueStatus")


@_attrs_define
class LeagueStatus:
    """
    Attributes:
        current_matchup_period (int): Current matchup period (week) Example: 1.
        is_active (bool): Whether the league is active Example: True.
        current_scoring_period (Union[Unset, int]): Current scoring period (week) Example: 1.
        latest_scoring_period (Union[Unset, int]): Latest completed scoring period Example: 1.
        teams_joined (Union[Unset, int]): Number of teams joined Example: 10.
        waiver_last_execution_date (Union[Unset, datetime.datetime]): Last time waivers were processed
    """

    current_matchup_period: int
    is_active: bool
    current_scoring_period: Union[Unset, int] = UNSET
    latest_scoring_period: Union[Unset, int] = UNSET
    teams_joined: Union[Unset, int] = UNSET
    waiver_last_execution_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_matchup_period = self.current_matchup_period

        is_active = self.is_active

        current_scoring_period = self.current_scoring_period

        latest_scoring_period = self.latest_scoring_period

        teams_joined = self.teams_joined

        waiver_last_execution_date: Union[Unset, str] = UNSET
        if not isinstance(self.waiver_last_execution_date, Unset):
            waiver_last_execution_date = self.waiver_last_execution_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currentMatchupPeriod": current_matchup_period,
                "isActive": is_active,
            }
        )
        if current_scoring_period is not UNSET:
            field_dict["currentScoringPeriod"] = current_scoring_period
        if latest_scoring_period is not UNSET:
            field_dict["latestScoringPeriod"] = latest_scoring_period
        if teams_joined is not UNSET:
            field_dict["teamsJoined"] = teams_joined
        if waiver_last_execution_date is not UNSET:
            field_dict["waiverLastExecutionDate"] = waiver_last_execution_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_matchup_period = d.pop("currentMatchupPeriod")

        is_active = d.pop("isActive")

        current_scoring_period = d.pop("currentScoringPeriod", UNSET)

        latest_scoring_period = d.pop("latestScoringPeriod", UNSET)

        teams_joined = d.pop("teamsJoined", UNSET)

        _waiver_last_execution_date = d.pop("waiverLastExecutionDate", UNSET)
        waiver_last_execution_date: Union[Unset, datetime.datetime]
        if isinstance(_waiver_last_execution_date, Unset):
            waiver_last_execution_date = UNSET
        else:
            waiver_last_execution_date = isoparse(_waiver_last_execution_date)

        league_status = cls(
            current_matchup_period=current_matchup_period,
            is_active=is_active,
            current_scoring_period=current_scoring_period,
            latest_scoring_period=latest_scoring_period,
            teams_joined=teams_joined,
            waiver_last_execution_date=waiver_last_execution_date,
        )

        league_status.additional_properties = d
        return league_status

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
