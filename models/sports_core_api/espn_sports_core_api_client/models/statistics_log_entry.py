from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reference import Reference
    from ..models.statistics_type_entry import StatisticsTypeEntry


T = TypeVar("T", bound="StatisticsLogEntry")


@_attrs_define
class StatisticsLogEntry:
    """
    Attributes:
        season (Reference):
        statistics (List['StatisticsTypeEntry']):
    """

    season: "Reference"
    statistics: List["StatisticsTypeEntry"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        season = self.season.to_dict()

        statistics = []
        for statistics_item_data in self.statistics:
            statistics_item = statistics_item_data.to_dict()
            statistics.append(statistics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "season": season,
                "statistics": statistics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference
        from ..models.statistics_type_entry import StatisticsTypeEntry

        d = src_dict.copy()
        season = Reference.from_dict(d.pop("season"))

        statistics = []
        _statistics = d.pop("statistics")
        for statistics_item_data in _statistics:
            statistics_item = StatisticsTypeEntry.from_dict(statistics_item_data)

            statistics.append(statistics_item)

        statistics_log_entry = cls(
            season=season,
            statistics=statistics,
        )

        statistics_log_entry.additional_properties = d
        return statistics_log_entry

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
