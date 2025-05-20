from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.betting_odds_team_odds import BettingOddsTeamOdds
    from ..models.odds_detail import OddsDetail
    from ..models.reference import Reference


T = TypeVar("T", bound="BettingOdds")


@_attrs_define
class BettingOdds:
    """
    Attributes:
        home_team (Reference):
        away_team (Reference):
        team_odds (BettingOddsTeamOdds):
        pre_match_money_line_away (Union[Unset, OddsDetail]):
        pre_match_money_line_home (Union[Unset, OddsDetail]):
        pre_match_spread_handicap_away (Union[Unset, OddsDetail]):
        pre_match_spread_home (Union[Unset, OddsDetail]):
    """

    home_team: "Reference"
    away_team: "Reference"
    team_odds: "BettingOddsTeamOdds"
    pre_match_money_line_away: Union[Unset, "OddsDetail"] = UNSET
    pre_match_money_line_home: Union[Unset, "OddsDetail"] = UNSET
    pre_match_spread_handicap_away: Union[Unset, "OddsDetail"] = UNSET
    pre_match_spread_home: Union[Unset, "OddsDetail"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        home_team = self.home_team.to_dict()

        away_team = self.away_team.to_dict()

        team_odds = self.team_odds.to_dict()

        pre_match_money_line_away: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pre_match_money_line_away, Unset):
            pre_match_money_line_away = self.pre_match_money_line_away.to_dict()

        pre_match_money_line_home: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pre_match_money_line_home, Unset):
            pre_match_money_line_home = self.pre_match_money_line_home.to_dict()

        pre_match_spread_handicap_away: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pre_match_spread_handicap_away, Unset):
            pre_match_spread_handicap_away = self.pre_match_spread_handicap_away.to_dict()

        pre_match_spread_home: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pre_match_spread_home, Unset):
            pre_match_spread_home = self.pre_match_spread_home.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "homeTeam": home_team,
                "awayTeam": away_team,
                "teamOdds": team_odds,
            }
        )
        if pre_match_money_line_away is not UNSET:
            field_dict["preMatchMoneyLineAway"] = pre_match_money_line_away
        if pre_match_money_line_home is not UNSET:
            field_dict["preMatchMoneyLineHome"] = pre_match_money_line_home
        if pre_match_spread_handicap_away is not UNSET:
            field_dict["preMatchSpreadHandicapAway"] = pre_match_spread_handicap_away
        if pre_match_spread_home is not UNSET:
            field_dict["preMatchSpreadHome"] = pre_match_spread_home

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.betting_odds_team_odds import BettingOddsTeamOdds
        from ..models.odds_detail import OddsDetail
        from ..models.reference import Reference

        d = src_dict.copy()
        home_team = Reference.from_dict(d.pop("homeTeam"))

        away_team = Reference.from_dict(d.pop("awayTeam"))

        team_odds = BettingOddsTeamOdds.from_dict(d.pop("teamOdds"))

        _pre_match_money_line_away = d.pop("preMatchMoneyLineAway", UNSET)
        pre_match_money_line_away: Union[Unset, OddsDetail]
        if isinstance(_pre_match_money_line_away, Unset):
            pre_match_money_line_away = UNSET
        else:
            pre_match_money_line_away = OddsDetail.from_dict(_pre_match_money_line_away)

        _pre_match_money_line_home = d.pop("preMatchMoneyLineHome", UNSET)
        pre_match_money_line_home: Union[Unset, OddsDetail]
        if isinstance(_pre_match_money_line_home, Unset):
            pre_match_money_line_home = UNSET
        else:
            pre_match_money_line_home = OddsDetail.from_dict(_pre_match_money_line_home)

        _pre_match_spread_handicap_away = d.pop("preMatchSpreadHandicapAway", UNSET)
        pre_match_spread_handicap_away: Union[Unset, OddsDetail]
        if isinstance(_pre_match_spread_handicap_away, Unset):
            pre_match_spread_handicap_away = UNSET
        else:
            pre_match_spread_handicap_away = OddsDetail.from_dict(_pre_match_spread_handicap_away)

        _pre_match_spread_home = d.pop("preMatchSpreadHome", UNSET)
        pre_match_spread_home: Union[Unset, OddsDetail]
        if isinstance(_pre_match_spread_home, Unset):
            pre_match_spread_home = UNSET
        else:
            pre_match_spread_home = OddsDetail.from_dict(_pre_match_spread_home)

        betting_odds = cls(
            home_team=home_team,
            away_team=away_team,
            team_odds=team_odds,
            pre_match_money_line_away=pre_match_money_line_away,
            pre_match_money_line_home=pre_match_money_line_home,
            pre_match_spread_handicap_away=pre_match_spread_handicap_away,
            pre_match_spread_home=pre_match_spread_home,
        )

        betting_odds.additional_properties = d
        return betting_odds

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
