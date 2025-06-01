from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FantasyOddsHomeTeamOddsCurrentLineTeamScore")


@_attrs_define
class FantasyOddsHomeTeamOddsCurrentLineTeamScore:
    """
    Attributes:
        point_spread (Union[Unset, float]):
    """

    point_spread: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        point_spread = self.point_spread

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if point_spread is not UNSET:
            field_dict["pointSpread"] = point_spread

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        point_spread = d.pop("pointSpread", UNSET)

        fantasy_odds_home_team_odds_current_line_team_score = cls(
            point_spread=point_spread,
        )

        fantasy_odds_home_team_odds_current_line_team_score.additional_properties = d
        return fantasy_odds_home_team_odds_current_line_team_score

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
