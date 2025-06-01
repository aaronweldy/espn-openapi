from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_odds_home_team_odds import FantasyOddsHomeTeamOdds
    from ..models.fantasy_odds_provider import FantasyOddsProvider


T = TypeVar("T", bound="FantasyOdds")


@_attrs_define
class FantasyOdds:
    """
    Attributes:
        details (Union[Unset, str]):
        over_under (Union[Unset, float]):
        spread (Union[Unset, float]):
        over_odds (Union[Unset, float]):
        under_odds (Union[Unset, float]):
        provider (Union[Unset, FantasyOddsProvider]):
        home_team_odds (Union[Unset, FantasyOddsHomeTeamOdds]):
    """

    details: Union[Unset, str] = UNSET
    over_under: Union[Unset, float] = UNSET
    spread: Union[Unset, float] = UNSET
    over_odds: Union[Unset, float] = UNSET
    under_odds: Union[Unset, float] = UNSET
    provider: Union[Unset, "FantasyOddsProvider"] = UNSET
    home_team_odds: Union[Unset, "FantasyOddsHomeTeamOdds"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        details = self.details

        over_under = self.over_under

        spread = self.spread

        over_odds = self.over_odds

        under_odds = self.under_odds

        provider: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.to_dict()

        home_team_odds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.home_team_odds, Unset):
            home_team_odds = self.home_team_odds.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if provider is not UNSET:
            field_dict["provider"] = provider
        if home_team_odds is not UNSET:
            field_dict["homeTeamOdds"] = home_team_odds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_odds_home_team_odds import FantasyOddsHomeTeamOdds
        from ..models.fantasy_odds_provider import FantasyOddsProvider

        d = src_dict.copy()
        details = d.pop("details", UNSET)

        over_under = d.pop("overUnder", UNSET)

        spread = d.pop("spread", UNSET)

        over_odds = d.pop("overOdds", UNSET)

        under_odds = d.pop("underOdds", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, FantasyOddsProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = FantasyOddsProvider.from_dict(_provider)

        _home_team_odds = d.pop("homeTeamOdds", UNSET)
        home_team_odds: Union[Unset, FantasyOddsHomeTeamOdds]
        if isinstance(_home_team_odds, Unset):
            home_team_odds = UNSET
        else:
            home_team_odds = FantasyOddsHomeTeamOdds.from_dict(_home_team_odds)

        fantasy_odds = cls(
            details=details,
            over_under=over_under,
            spread=spread,
            over_odds=over_odds,
            under_odds=under_odds,
            provider=provider,
            home_team_odds=home_team_odds,
        )

        fantasy_odds.additional_properties = d
        return fantasy_odds

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
