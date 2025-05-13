from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.stat_rule import StatRule


T = TypeVar("T", bound="ScoringSettingsStatSettingsStats")


@_attrs_define
class ScoringSettingsStatSettingsStats:
    """ """

    additional_properties: Dict[str, "StatRule"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stat_rule import StatRule

        d = src_dict.copy()
        scoring_settings_stat_settings_stats = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = StatRule.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        scoring_settings_stat_settings_stats.additional_properties = additional_properties
        return scoring_settings_stat_settings_stats

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "StatRule":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "StatRule") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
