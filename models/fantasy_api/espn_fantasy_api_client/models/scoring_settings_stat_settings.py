from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoring_settings_stat_settings_stats import ScoringSettingsStatSettingsStats


T = TypeVar("T", bound="ScoringSettingsStatSettings")


@_attrs_define
class ScoringSettingsStatSettings:
    """Scoring rules for each stat

    Attributes:
        stats (Union[Unset, ScoringSettingsStatSettingsStats]):
    """

    stats: Union[Unset, "ScoringSettingsStatSettingsStats"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stats: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoring_settings_stat_settings_stats import ScoringSettingsStatSettingsStats

        d = src_dict.copy()
        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, ScoringSettingsStatSettingsStats]
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = ScoringSettingsStatSettingsStats.from_dict(_stats)

        scoring_settings_stat_settings = cls(
            stats=stats,
        )

        scoring_settings_stat_settings.additional_properties = d
        return scoring_settings_stat_settings

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
