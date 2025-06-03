from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProGame")


@_attrs_define
class ProGame:
    """
    Attributes:
        away_pro_team_id (Union[Unset, int]): Away team ID
        date (Union[Unset, int]): Game date in milliseconds
        home_pro_team_id (Union[Unset, int]): Home team ID
        id (Union[Unset, int]): Game ID
        scoring_period_id (Union[Unset, int]): Scoring period ID (week number)
        start_time_tbd (Union[Unset, bool]): Whether start time is to be determined
        stats_official (Union[Unset, bool]): Whether stats are official
        valid_for_locking (Union[Unset, bool]): Whether game is valid for lineup locking
    """

    away_pro_team_id: Union[Unset, int] = UNSET
    date: Union[Unset, int] = UNSET
    home_pro_team_id: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    scoring_period_id: Union[Unset, int] = UNSET
    start_time_tbd: Union[Unset, bool] = UNSET
    stats_official: Union[Unset, bool] = UNSET
    valid_for_locking: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        away_pro_team_id = self.away_pro_team_id

        date = self.date

        home_pro_team_id = self.home_pro_team_id

        id = self.id

        scoring_period_id = self.scoring_period_id

        start_time_tbd = self.start_time_tbd

        stats_official = self.stats_official

        valid_for_locking = self.valid_for_locking

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if away_pro_team_id is not UNSET:
            field_dict["awayProTeamId"] = away_pro_team_id
        if date is not UNSET:
            field_dict["date"] = date
        if home_pro_team_id is not UNSET:
            field_dict["homeProTeamId"] = home_pro_team_id
        if id is not UNSET:
            field_dict["id"] = id
        if scoring_period_id is not UNSET:
            field_dict["scoringPeriodId"] = scoring_period_id
        if start_time_tbd is not UNSET:
            field_dict["startTimeTBD"] = start_time_tbd
        if stats_official is not UNSET:
            field_dict["statsOfficial"] = stats_official
        if valid_for_locking is not UNSET:
            field_dict["validForLocking"] = valid_for_locking

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        away_pro_team_id = d.pop("awayProTeamId", UNSET)

        date = d.pop("date", UNSET)

        home_pro_team_id = d.pop("homeProTeamId", UNSET)

        id = d.pop("id", UNSET)

        scoring_period_id = d.pop("scoringPeriodId", UNSET)

        start_time_tbd = d.pop("startTimeTBD", UNSET)

        stats_official = d.pop("statsOfficial", UNSET)

        valid_for_locking = d.pop("validForLocking", UNSET)

        pro_game = cls(
            away_pro_team_id=away_pro_team_id,
            date=date,
            home_pro_team_id=home_pro_team_id,
            id=id,
            scoring_period_id=scoring_period_id,
            start_time_tbd=start_time_tbd,
            stats_official=stats_official,
            valid_for_locking=valid_for_locking,
        )

        pro_game.additional_properties = d
        return pro_game

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
