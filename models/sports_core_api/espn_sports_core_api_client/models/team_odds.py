from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.head_to_heads import HeadToHeads
    from ..models.odds_team_current import OddsTeamCurrent
    from ..models.spread_record import SpreadRecord


T = TypeVar("T", bound="TeamOdds")


@_attrs_define
class TeamOdds:
    """
    Attributes:
        favorite (bool):
        underdog (bool):
        current (OddsTeamCurrent):
        team (HeadToHeads):
        money_line (Union[Unset, int]):
        spread_odds (Union[Unset, float]):
        win_percentage (Union[Unset, float]):
        average_score (Union[Unset, float]):
        money_line_odds (Union[Unset, float]):
        money_line_return (Union[Unset, float]):
        similarities (Union[Unset, HeadToHeads]):
        spread_return (Union[Unset, float]):
        spread_record (Union[Unset, SpreadRecord]):
        past_performances (Union[Unset, HeadToHeads]):
    """

    favorite: bool
    underdog: bool
    current: "OddsTeamCurrent"
    team: "HeadToHeads"
    money_line: Union[Unset, int] = UNSET
    spread_odds: Union[Unset, float] = UNSET
    win_percentage: Union[Unset, float] = UNSET
    average_score: Union[Unset, float] = UNSET
    money_line_odds: Union[Unset, float] = UNSET
    money_line_return: Union[Unset, float] = UNSET
    similarities: Union[Unset, "HeadToHeads"] = UNSET
    spread_return: Union[Unset, float] = UNSET
    spread_record: Union[Unset, "SpreadRecord"] = UNSET
    past_performances: Union[Unset, "HeadToHeads"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        favorite = self.favorite

        underdog = self.underdog

        current = self.current.to_dict()

        team = self.team.to_dict()

        money_line = self.money_line

        spread_odds = self.spread_odds

        win_percentage = self.win_percentage

        average_score = self.average_score

        money_line_odds = self.money_line_odds

        money_line_return = self.money_line_return

        similarities: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.similarities, Unset):
            similarities = self.similarities.to_dict()

        spread_return = self.spread_return

        spread_record: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spread_record, Unset):
            spread_record = self.spread_record.to_dict()

        past_performances: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.past_performances, Unset):
            past_performances = self.past_performances.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "favorite": favorite,
                "underdog": underdog,
                "current": current,
                "team": team,
            }
        )
        if money_line is not UNSET:
            field_dict["moneyLine"] = money_line
        if spread_odds is not UNSET:
            field_dict["spreadOdds"] = spread_odds
        if win_percentage is not UNSET:
            field_dict["winPercentage"] = win_percentage
        if average_score is not UNSET:
            field_dict["averageScore"] = average_score
        if money_line_odds is not UNSET:
            field_dict["moneyLineOdds"] = money_line_odds
        if money_line_return is not UNSET:
            field_dict["moneyLineReturn"] = money_line_return
        if similarities is not UNSET:
            field_dict["similarities"] = similarities
        if spread_return is not UNSET:
            field_dict["spreadReturn"] = spread_return
        if spread_record is not UNSET:
            field_dict["spreadRecord"] = spread_record
        if past_performances is not UNSET:
            field_dict["pastPerformances"] = past_performances

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.head_to_heads import HeadToHeads
        from ..models.odds_team_current import OddsTeamCurrent
        from ..models.spread_record import SpreadRecord

        d = src_dict.copy()
        favorite = d.pop("favorite")

        underdog = d.pop("underdog")

        current = OddsTeamCurrent.from_dict(d.pop("current"))

        team = HeadToHeads.from_dict(d.pop("team"))

        money_line = d.pop("moneyLine", UNSET)

        spread_odds = d.pop("spreadOdds", UNSET)

        win_percentage = d.pop("winPercentage", UNSET)

        average_score = d.pop("averageScore", UNSET)

        money_line_odds = d.pop("moneyLineOdds", UNSET)

        money_line_return = d.pop("moneyLineReturn", UNSET)

        _similarities = d.pop("similarities", UNSET)
        similarities: Union[Unset, HeadToHeads]
        if isinstance(_similarities, Unset):
            similarities = UNSET
        else:
            similarities = HeadToHeads.from_dict(_similarities)

        spread_return = d.pop("spreadReturn", UNSET)

        _spread_record = d.pop("spreadRecord", UNSET)
        spread_record: Union[Unset, SpreadRecord]
        if isinstance(_spread_record, Unset):
            spread_record = UNSET
        else:
            spread_record = SpreadRecord.from_dict(_spread_record)

        _past_performances = d.pop("pastPerformances", UNSET)
        past_performances: Union[Unset, HeadToHeads]
        if isinstance(_past_performances, Unset):
            past_performances = UNSET
        else:
            past_performances = HeadToHeads.from_dict(_past_performances)

        team_odds = cls(
            favorite=favorite,
            underdog=underdog,
            current=current,
            team=team,
            money_line=money_line,
            spread_odds=spread_odds,
            win_percentage=win_percentage,
            average_score=average_score,
            money_line_odds=money_line_odds,
            money_line_return=money_line_return,
            similarities=similarities,
            spread_return=spread_return,
            spread_record=spread_record,
            past_performances=past_performances,
        )

        team_odds.additional_properties = d
        return team_odds

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
