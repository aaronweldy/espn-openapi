from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_pickcenter_away_team_odds import FantasyPickcenterAwayTeamOdds
    from ..models.fantasy_pickcenter_home_team_odds import FantasyPickcenterHomeTeamOdds
    from ..models.fantasy_pickcenter_provider import FantasyPickcenterProvider


T = TypeVar("T", bound="FantasyPickcenter")


@_attrs_define
class FantasyPickcenter:
    """
    Attributes:
        id (Union[Unset, str]):
        home_team_odds (Union[Unset, FantasyPickcenterHomeTeamOdds]):
        away_team_odds (Union[Unset, FantasyPickcenterAwayTeamOdds]):
        provider (Union[Unset, FantasyPickcenterProvider]):
        details (Union[Unset, str]):
        over_under (Union[Unset, float]):
        spread (Union[Unset, float]):
    """

    id: Union[Unset, str] = UNSET
    home_team_odds: Union[Unset, "FantasyPickcenterHomeTeamOdds"] = UNSET
    away_team_odds: Union[Unset, "FantasyPickcenterAwayTeamOdds"] = UNSET
    provider: Union[Unset, "FantasyPickcenterProvider"] = UNSET
    details: Union[Unset, str] = UNSET
    over_under: Union[Unset, float] = UNSET
    spread: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        home_team_odds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.home_team_odds, Unset):
            home_team_odds = self.home_team_odds.to_dict()

        away_team_odds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.away_team_odds, Unset):
            away_team_odds = self.away_team_odds.to_dict()

        provider: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.to_dict()

        details = self.details

        over_under = self.over_under

        spread = self.spread

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if home_team_odds is not UNSET:
            field_dict["homeTeamOdds"] = home_team_odds
        if away_team_odds is not UNSET:
            field_dict["awayTeamOdds"] = away_team_odds
        if provider is not UNSET:
            field_dict["provider"] = provider
        if details is not UNSET:
            field_dict["details"] = details
        if over_under is not UNSET:
            field_dict["overUnder"] = over_under
        if spread is not UNSET:
            field_dict["spread"] = spread

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_pickcenter_away_team_odds import FantasyPickcenterAwayTeamOdds
        from ..models.fantasy_pickcenter_home_team_odds import FantasyPickcenterHomeTeamOdds
        from ..models.fantasy_pickcenter_provider import FantasyPickcenterProvider

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _home_team_odds = d.pop("homeTeamOdds", UNSET)
        home_team_odds: Union[Unset, FantasyPickcenterHomeTeamOdds]
        if isinstance(_home_team_odds, Unset):
            home_team_odds = UNSET
        else:
            home_team_odds = FantasyPickcenterHomeTeamOdds.from_dict(_home_team_odds)

        _away_team_odds = d.pop("awayTeamOdds", UNSET)
        away_team_odds: Union[Unset, FantasyPickcenterAwayTeamOdds]
        if isinstance(_away_team_odds, Unset):
            away_team_odds = UNSET
        else:
            away_team_odds = FantasyPickcenterAwayTeamOdds.from_dict(_away_team_odds)

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, FantasyPickcenterProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = FantasyPickcenterProvider.from_dict(_provider)

        details = d.pop("details", UNSET)

        over_under = d.pop("overUnder", UNSET)

        spread = d.pop("spread", UNSET)

        fantasy_pickcenter = cls(
            id=id,
            home_team_odds=home_team_odds,
            away_team_odds=away_team_odds,
            provider=provider,
            details=details,
            over_under=over_under,
            spread=spread,
        )

        fantasy_pickcenter.additional_properties = d
        return fantasy_pickcenter

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
