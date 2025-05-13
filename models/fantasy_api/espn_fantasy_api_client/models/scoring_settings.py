from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoring_settings_stat_settings import ScoringSettingsStatSettings


T = TypeVar("T", bound="ScoringSettings")


@_attrs_define
class ScoringSettings:
    """
    Attributes:
        scoring_type (int): Scoring type (1 = head-to-head, 2 = rotisserie, 3 = points) Example: 1.
        matchup_tie_rule (Union[Unset, int]): Tiebreaker rule
        home_team_bonus (Union[Unset, float]): Home team bonus points
        is_custom_scoring (Union[Unset, bool]):
        is_default_position_scoring (Union[Unset, bool]):
        stat_settings (Union[Unset, ScoringSettingsStatSettings]): Scoring rules for each stat
    """

    scoring_type: int
    matchup_tie_rule: Union[Unset, int] = UNSET
    home_team_bonus: Union[Unset, float] = UNSET
    is_custom_scoring: Union[Unset, bool] = UNSET
    is_default_position_scoring: Union[Unset, bool] = UNSET
    stat_settings: Union[Unset, "ScoringSettingsStatSettings"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scoring_type = self.scoring_type

        matchup_tie_rule = self.matchup_tie_rule

        home_team_bonus = self.home_team_bonus

        is_custom_scoring = self.is_custom_scoring

        is_default_position_scoring = self.is_default_position_scoring

        stat_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stat_settings, Unset):
            stat_settings = self.stat_settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scoringType": scoring_type,
            }
        )
        if matchup_tie_rule is not UNSET:
            field_dict["matchupTieRule"] = matchup_tie_rule
        if home_team_bonus is not UNSET:
            field_dict["homeTeamBonus"] = home_team_bonus
        if is_custom_scoring is not UNSET:
            field_dict["isCustomScoring"] = is_custom_scoring
        if is_default_position_scoring is not UNSET:
            field_dict["isDefaultPositionScoring"] = is_default_position_scoring
        if stat_settings is not UNSET:
            field_dict["statSettings"] = stat_settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoring_settings_stat_settings import ScoringSettingsStatSettings

        d = src_dict.copy()
        scoring_type = d.pop("scoringType")

        matchup_tie_rule = d.pop("matchupTieRule", UNSET)

        home_team_bonus = d.pop("homeTeamBonus", UNSET)

        is_custom_scoring = d.pop("isCustomScoring", UNSET)

        is_default_position_scoring = d.pop("isDefaultPositionScoring", UNSET)

        _stat_settings = d.pop("statSettings", UNSET)
        stat_settings: Union[Unset, ScoringSettingsStatSettings]
        if isinstance(_stat_settings, Unset):
            stat_settings = UNSET
        else:
            stat_settings = ScoringSettingsStatSettings.from_dict(_stat_settings)

        scoring_settings = cls(
            scoring_type=scoring_type,
            matchup_tie_rule=matchup_tie_rule,
            home_team_bonus=home_team_bonus,
            is_custom_scoring=is_custom_scoring,
            is_default_position_scoring=is_default_position_scoring,
            stat_settings=stat_settings,
        )

        scoring_settings.additional_properties = d
        return scoring_settings

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
