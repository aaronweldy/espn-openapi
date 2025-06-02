import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.past_performance_total_result import PastPerformanceTotalResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference import Reference


T = TypeVar("T", bound="PastPerformance")


@_attrs_define
class PastPerformance:
    """Individual past performance record showing betting results

    Attributes:
        spread (Union[Unset, float]): Point spread for the game (negative means team was favored) Example: -3.5.
        spread_odds (Union[Unset, float]): Odds for the spread bet Example: -108.
        spread_winner (Union[Unset, bool]): Whether the team covered the spread
        over_odds (Union[Unset, float]): Odds for the over bet Example: -101.
        under_odds (Union[Unset, float]): Odds for the under bet Example: -109.
        line_date (Union[Unset, datetime.datetime]): Date and time when the betting line was set Example:
            2012-09-23T17:00Z.
        total_line (Union[Unset, float]): Over/under total line Example: 47.0.
        total_result (Union[Unset, PastPerformanceTotalResult]): Result of the total bet (O=Over, U=Under, P=Push)
            Example: O.
        money_line_odds (Union[Unset, float]): Money line odds for the team Example: -195.
        moneyline_winner (Union[Unset, bool]): Whether the team won the game outright
        past_competition (Union[Unset, Reference]):
    """

    spread: Union[Unset, float] = UNSET
    spread_odds: Union[Unset, float] = UNSET
    spread_winner: Union[Unset, bool] = UNSET
    over_odds: Union[Unset, float] = UNSET
    under_odds: Union[Unset, float] = UNSET
    line_date: Union[Unset, datetime.datetime] = UNSET
    total_line: Union[Unset, float] = UNSET
    total_result: Union[Unset, PastPerformanceTotalResult] = UNSET
    money_line_odds: Union[Unset, float] = UNSET
    moneyline_winner: Union[Unset, bool] = UNSET
    past_competition: Union[Unset, "Reference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        spread = self.spread

        spread_odds = self.spread_odds

        spread_winner = self.spread_winner

        over_odds = self.over_odds

        under_odds = self.under_odds

        line_date: Union[Unset, str] = UNSET
        if not isinstance(self.line_date, Unset):
            line_date = self.line_date.isoformat()

        total_line = self.total_line

        total_result: Union[Unset, str] = UNSET
        if not isinstance(self.total_result, Unset):
            total_result = self.total_result.value

        money_line_odds = self.money_line_odds

        moneyline_winner = self.moneyline_winner

        past_competition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.past_competition, Unset):
            past_competition = self.past_competition.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if spread is not UNSET:
            field_dict["spread"] = spread
        if spread_odds is not UNSET:
            field_dict["spreadOdds"] = spread_odds
        if spread_winner is not UNSET:
            field_dict["spreadWinner"] = spread_winner
        if over_odds is not UNSET:
            field_dict["overOdds"] = over_odds
        if under_odds is not UNSET:
            field_dict["underOdds"] = under_odds
        if line_date is not UNSET:
            field_dict["lineDate"] = line_date
        if total_line is not UNSET:
            field_dict["totalLine"] = total_line
        if total_result is not UNSET:
            field_dict["totalResult"] = total_result
        if money_line_odds is not UNSET:
            field_dict["moneyLineOdds"] = money_line_odds
        if moneyline_winner is not UNSET:
            field_dict["moneylineWinner"] = moneyline_winner
        if past_competition is not UNSET:
            field_dict["pastCompetition"] = past_competition

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference

        d = src_dict.copy()
        spread = d.pop("spread", UNSET)

        spread_odds = d.pop("spreadOdds", UNSET)

        spread_winner = d.pop("spreadWinner", UNSET)

        over_odds = d.pop("overOdds", UNSET)

        under_odds = d.pop("underOdds", UNSET)

        _line_date = d.pop("lineDate", UNSET)
        line_date: Union[Unset, datetime.datetime]
        if isinstance(_line_date, Unset):
            line_date = UNSET
        else:
            line_date = isoparse(_line_date)

        total_line = d.pop("totalLine", UNSET)

        _total_result = d.pop("totalResult", UNSET)
        total_result: Union[Unset, PastPerformanceTotalResult]
        if isinstance(_total_result, Unset):
            total_result = UNSET
        else:
            total_result = PastPerformanceTotalResult(_total_result)

        money_line_odds = d.pop("moneyLineOdds", UNSET)

        moneyline_winner = d.pop("moneylineWinner", UNSET)

        _past_competition = d.pop("pastCompetition", UNSET)
        past_competition: Union[Unset, Reference]
        if isinstance(_past_competition, Unset):
            past_competition = UNSET
        else:
            past_competition = Reference.from_dict(_past_competition)

        past_performance = cls(
            spread=spread,
            spread_odds=spread_odds,
            spread_winner=spread_winner,
            over_odds=over_odds,
            under_odds=under_odds,
            line_date=line_date,
            total_line=total_line,
            total_result=total_result,
            money_line_odds=money_line_odds,
            moneyline_winner=moneyline_winner,
            past_competition=past_competition,
        )

        past_performance.additional_properties = d
        return past_performance

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
