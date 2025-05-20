from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.betting_odds import BettingOdds
    from ..models.head_to_heads import HeadToHeads
    from ..models.odds_item_current import OddsItemCurrent
    from ..models.odds_provider import OddsProvider
    from ..models.team_odds import TeamOdds


T = TypeVar("T", bound="OddsItem")


@_attrs_define
class OddsItem:
    """
    Attributes:
        ref (str):
        provider (OddsProvider):
        moneyline_winner (bool):
        spread_winner (bool):
        betting_odds (Union[Unset, BettingOdds]):
        details (Union[Unset, str]):
        over_under (Union[Unset, float]):
        spread (Union[Unset, float]):
        over_odds (Union[Unset, float]):
        under_odds (Union[Unset, float]):
        away_team_odds (Union[Unset, TeamOdds]):
        home_team_odds (Union[Unset, TeamOdds]):
        current (Union[Unset, OddsItemCurrent]):
        head_to_heads (Union[Unset, HeadToHeads]):
        predictors (Union[Unset, HeadToHeads]):
        money_line_history (Union[Unset, HeadToHeads]):
        spread_history (Union[Unset, HeadToHeads]):
        total_history (Union[Unset, HeadToHeads]):
    """

    ref: str
    provider: "OddsProvider"
    moneyline_winner: bool
    spread_winner: bool
    betting_odds: Union[Unset, "BettingOdds"] = UNSET
    details: Union[Unset, str] = UNSET
    over_under: Union[Unset, float] = UNSET
    spread: Union[Unset, float] = UNSET
    over_odds: Union[Unset, float] = UNSET
    under_odds: Union[Unset, float] = UNSET
    away_team_odds: Union[Unset, "TeamOdds"] = UNSET
    home_team_odds: Union[Unset, "TeamOdds"] = UNSET
    current: Union[Unset, "OddsItemCurrent"] = UNSET
    head_to_heads: Union[Unset, "HeadToHeads"] = UNSET
    predictors: Union[Unset, "HeadToHeads"] = UNSET
    money_line_history: Union[Unset, "HeadToHeads"] = UNSET
    spread_history: Union[Unset, "HeadToHeads"] = UNSET
    total_history: Union[Unset, "HeadToHeads"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        provider = self.provider.to_dict()

        moneyline_winner = self.moneyline_winner

        spread_winner = self.spread_winner

        betting_odds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.betting_odds, Unset):
            betting_odds = self.betting_odds.to_dict()

        details = self.details

        over_under = self.over_under

        spread = self.spread

        over_odds = self.over_odds

        under_odds = self.under_odds

        away_team_odds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.away_team_odds, Unset):
            away_team_odds = self.away_team_odds.to_dict()

        home_team_odds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.home_team_odds, Unset):
            home_team_odds = self.home_team_odds.to_dict()

        current: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.current, Unset):
            current = self.current.to_dict()

        head_to_heads: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.head_to_heads, Unset):
            head_to_heads = self.head_to_heads.to_dict()

        predictors: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.predictors, Unset):
            predictors = self.predictors.to_dict()

        money_line_history: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.money_line_history, Unset):
            money_line_history = self.money_line_history.to_dict()

        spread_history: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spread_history, Unset):
            spread_history = self.spread_history.to_dict()

        total_history: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_history, Unset):
            total_history = self.total_history.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "provider": provider,
                "moneylineWinner": moneyline_winner,
                "spreadWinner": spread_winner,
            }
        )
        if betting_odds is not UNSET:
            field_dict["bettingOdds"] = betting_odds
        if details is not UNSET:
            field_dict["details"] = details
        if over_under is not UNSET:
            field_dict["overUnder"] = over_under
        if spread is not UNSET:
            field_dict["spread"] = spread
        if over_odds is not UNSET:
            field_dict["overOdds"] = over_odds
        if under_odds is not UNSET:
            field_dict["underOdds"] = under_odds
        if away_team_odds is not UNSET:
            field_dict["awayTeamOdds"] = away_team_odds
        if home_team_odds is not UNSET:
            field_dict["homeTeamOdds"] = home_team_odds
        if current is not UNSET:
            field_dict["current"] = current
        if head_to_heads is not UNSET:
            field_dict["headToHeads"] = head_to_heads
        if predictors is not UNSET:
            field_dict["predictors"] = predictors
        if money_line_history is not UNSET:
            field_dict["moneyLineHistory"] = money_line_history
        if spread_history is not UNSET:
            field_dict["spreadHistory"] = spread_history
        if total_history is not UNSET:
            field_dict["totalHistory"] = total_history

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.betting_odds import BettingOdds
        from ..models.head_to_heads import HeadToHeads
        from ..models.odds_item_current import OddsItemCurrent
        from ..models.odds_provider import OddsProvider
        from ..models.team_odds import TeamOdds

        d = src_dict.copy()
        ref = d.pop("$ref")

        provider = OddsProvider.from_dict(d.pop("provider"))

        moneyline_winner = d.pop("moneylineWinner")

        spread_winner = d.pop("spreadWinner")

        _betting_odds = d.pop("bettingOdds", UNSET)
        betting_odds: Union[Unset, BettingOdds]
        if isinstance(_betting_odds, Unset):
            betting_odds = UNSET
        else:
            betting_odds = BettingOdds.from_dict(_betting_odds)

        details = d.pop("details", UNSET)

        over_under = d.pop("overUnder", UNSET)

        spread = d.pop("spread", UNSET)

        over_odds = d.pop("overOdds", UNSET)

        under_odds = d.pop("underOdds", UNSET)

        _away_team_odds = d.pop("awayTeamOdds", UNSET)
        away_team_odds: Union[Unset, TeamOdds]
        if isinstance(_away_team_odds, Unset):
            away_team_odds = UNSET
        else:
            away_team_odds = TeamOdds.from_dict(_away_team_odds)

        _home_team_odds = d.pop("homeTeamOdds", UNSET)
        home_team_odds: Union[Unset, TeamOdds]
        if isinstance(_home_team_odds, Unset):
            home_team_odds = UNSET
        else:
            home_team_odds = TeamOdds.from_dict(_home_team_odds)

        _current = d.pop("current", UNSET)
        current: Union[Unset, OddsItemCurrent]
        if isinstance(_current, Unset):
            current = UNSET
        else:
            current = OddsItemCurrent.from_dict(_current)

        _head_to_heads = d.pop("headToHeads", UNSET)
        head_to_heads: Union[Unset, HeadToHeads]
        if isinstance(_head_to_heads, Unset):
            head_to_heads = UNSET
        else:
            head_to_heads = HeadToHeads.from_dict(_head_to_heads)

        _predictors = d.pop("predictors", UNSET)
        predictors: Union[Unset, HeadToHeads]
        if isinstance(_predictors, Unset):
            predictors = UNSET
        else:
            predictors = HeadToHeads.from_dict(_predictors)

        _money_line_history = d.pop("moneyLineHistory", UNSET)
        money_line_history: Union[Unset, HeadToHeads]
        if isinstance(_money_line_history, Unset):
            money_line_history = UNSET
        else:
            money_line_history = HeadToHeads.from_dict(_money_line_history)

        _spread_history = d.pop("spreadHistory", UNSET)
        spread_history: Union[Unset, HeadToHeads]
        if isinstance(_spread_history, Unset):
            spread_history = UNSET
        else:
            spread_history = HeadToHeads.from_dict(_spread_history)

        _total_history = d.pop("totalHistory", UNSET)
        total_history: Union[Unset, HeadToHeads]
        if isinstance(_total_history, Unset):
            total_history = UNSET
        else:
            total_history = HeadToHeads.from_dict(_total_history)

        odds_item = cls(
            ref=ref,
            provider=provider,
            moneyline_winner=moneyline_winner,
            spread_winner=spread_winner,
            betting_odds=betting_odds,
            details=details,
            over_under=over_under,
            spread=spread,
            over_odds=over_odds,
            under_odds=under_odds,
            away_team_odds=away_team_odds,
            home_team_odds=home_team_odds,
            current=current,
            head_to_heads=head_to_heads,
            predictors=predictors,
            money_line_history=money_line_history,
            spread_history=spread_history,
            total_history=total_history,
        )

        odds_item.additional_properties = d
        return odds_item

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
