from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.stat_item import StatItem


T = TypeVar("T", bound="StatCategory")


@_attrs_define
class StatCategory:
    """A category of statistics within a split stats object.

    Attributes:
        name (str): The category name Example: defensive.
        display_name (str): The display name for the category Example: Defense.
        short_display_name (str): The short display name for the category Example: Defensive.
        abbreviation (str): The abbreviation for the category Example: def.
        summary (str): Summary information for the category
        stats (List['StatItem']):
    """

    name: str
    display_name: str
    short_display_name: str
    abbreviation: str
    summary: str
    stats: List["StatItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        short_display_name = self.short_display_name

        abbreviation = self.abbreviation

        summary = self.summary

        stats = []
        for stats_item_data in self.stats:
            stats_item = stats_item_data.to_dict()
            stats.append(stats_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "displayName": display_name,
                "shortDisplayName": short_display_name,
                "abbreviation": abbreviation,
                "summary": summary,
                "stats": stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stat_item import StatItem

        d = src_dict.copy()
        name = d.pop("name")

        display_name = d.pop("displayName")

        short_display_name = d.pop("shortDisplayName")

        abbreviation = d.pop("abbreviation")

        summary = d.pop("summary")

        stats = []
        _stats = d.pop("stats")
        for stats_item_data in _stats:
            stats_item = StatItem.from_dict(stats_item_data)

            stats.append(stats_item)

        stat_category = cls(
            name=name,
            display_name=display_name,
            short_display_name=short_display_name,
            abbreviation=abbreviation,
            summary=summary,
            stats=stats,
        )

        stat_category.additional_properties = d
        return stat_category

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
