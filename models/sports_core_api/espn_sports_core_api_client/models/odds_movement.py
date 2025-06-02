import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="OddsMovement")


@_attrs_define
class OddsMovement:
    """
    Attributes:
        over_odds (float): Over odds for totals betting
        under_odds (float): Under odds for totals betting
        draw_odds (float): Draw odds (typically 0 for US sports)
        away_odds (float): Away team odds
        home_odds (float): Home team odds
        line_date (datetime.datetime): Timestamp when this line was recorded
        moneyline_winner (bool): Whether this was the winning moneyline
        spread_winner (bool): Whether this was the winning spread
        line (float): The line/spread value
    """

    over_odds: float
    under_odds: float
    draw_odds: float
    away_odds: float
    home_odds: float
    line_date: datetime.datetime
    moneyline_winner: bool
    spread_winner: bool
    line: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        over_odds = self.over_odds

        under_odds = self.under_odds

        draw_odds = self.draw_odds

        away_odds = self.away_odds

        home_odds = self.home_odds

        line_date = self.line_date.isoformat()

        moneyline_winner = self.moneyline_winner

        spread_winner = self.spread_winner

        line = self.line

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "overOdds": over_odds,
                "underOdds": under_odds,
                "drawOdds": draw_odds,
                "awayOdds": away_odds,
                "homeOdds": home_odds,
                "lineDate": line_date,
                "moneylineWinner": moneyline_winner,
                "spreadWinner": spread_winner,
                "line": line,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        over_odds = d.pop("overOdds")

        under_odds = d.pop("underOdds")

        draw_odds = d.pop("drawOdds")

        away_odds = d.pop("awayOdds")

        home_odds = d.pop("homeOdds")

        line_date = isoparse(d.pop("lineDate"))

        moneyline_winner = d.pop("moneylineWinner")

        spread_winner = d.pop("spreadWinner")

        line = d.pop("line")

        odds_movement = cls(
            over_odds=over_odds,
            under_odds=under_odds,
            draw_odds=draw_odds,
            away_odds=away_odds,
            home_odds=home_odds,
            line_date=line_date,
            moneyline_winner=moneyline_winner,
            spread_winner=spread_winner,
            line=line,
        )

        odds_movement.additional_properties = d
        return odds_movement

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
