from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.competitor_stat import CompetitorStat


T = TypeVar("T", bound="StatisticsCategory")


@_attrs_define
class StatisticsCategory:
    """
    Attributes:
        name (str): Category name (e.g., "passing", "rushing")
        display_name (str): Display name for the category
        stats (List['CompetitorStat']):
        short_display_name (Union[Unset, str]): Short display name
        abbreviation (Union[Unset, str]): Category abbreviation
        summary (Union[Unset, str]): Summary of category stats
    """

    name: str
    display_name: str
    stats: List["CompetitorStat"]
    short_display_name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        stats = []
        for stats_item_data in self.stats:
            stats_item = stats_item_data.to_dict()
            stats.append(stats_item)

        short_display_name = self.short_display_name

        abbreviation = self.abbreviation

        summary = self.summary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "displayName": display_name,
                "stats": stats,
            }
        )
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.competitor_stat import CompetitorStat

        d = src_dict.copy()
        name = d.pop("name")

        display_name = d.pop("displayName")

        stats = []
        _stats = d.pop("stats")
        for stats_item_data in _stats:
            stats_item = CompetitorStat.from_dict(stats_item_data)

            stats.append(stats_item)

        short_display_name = d.pop("shortDisplayName", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        summary = d.pop("summary", UNSET)

        statistics_category = cls(
            name=name,
            display_name=display_name,
            stats=stats,
            short_display_name=short_display_name,
            abbreviation=abbreviation,
            summary=summary,
        )

        statistics_category.additional_properties = d
        return statistics_category

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
