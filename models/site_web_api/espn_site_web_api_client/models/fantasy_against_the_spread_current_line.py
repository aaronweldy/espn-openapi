from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_against_the_spread_current_line_team_score import FantasyAgainstTheSpreadCurrentLineTeamScore


T = TypeVar("T", bound="FantasyAgainstTheSpreadCurrentLine")


@_attrs_define
class FantasyAgainstTheSpreadCurrentLine:
    """
    Attributes:
        spread_odds (Union[Unset, float]):
        team_score (Union[Unset, FantasyAgainstTheSpreadCurrentLineTeamScore]):
    """

    spread_odds: Union[Unset, float] = UNSET
    team_score: Union[Unset, "FantasyAgainstTheSpreadCurrentLineTeamScore"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        spread_odds = self.spread_odds

        team_score: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team_score, Unset):
            team_score = self.team_score.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if spread_odds is not UNSET:
            field_dict["spreadOdds"] = spread_odds
        if team_score is not UNSET:
            field_dict["teamScore"] = team_score

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_against_the_spread_current_line_team_score import (
            FantasyAgainstTheSpreadCurrentLineTeamScore,
        )

        d = src_dict.copy()
        spread_odds = d.pop("spreadOdds", UNSET)

        _team_score = d.pop("teamScore", UNSET)
        team_score: Union[Unset, FantasyAgainstTheSpreadCurrentLineTeamScore]
        if isinstance(_team_score, Unset):
            team_score = UNSET
        else:
            team_score = FantasyAgainstTheSpreadCurrentLineTeamScore.from_dict(_team_score)

        fantasy_against_the_spread_current_line = cls(
            spread_odds=spread_odds,
            team_score=team_score,
        )

        fantasy_against_the_spread_current_line.additional_properties = d
        return fantasy_against_the_spread_current_line

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
