from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_statistics import SeasonStatistics


T = TypeVar("T", bound="StatsCategory")


@_attrs_define
class StatsCategory:
    """
    Attributes:
        name (str): Category name
        display_name (str): Display name
        labels (List[str]): Column labels
        statistics (List['SeasonStatistics']):
        names (Union[Unset, List[str]]): Field names
        display_names (Union[Unset, List[str]]): Field display names
        descriptions (Union[Unset, List[str]]): Field descriptions
        totals (Union[Unset, List[str]]): Career totals
        sort_key (Union[Unset, str]): Sort key for category
    """

    name: str
    display_name: str
    labels: List[str]
    statistics: List["SeasonStatistics"]
    names: Union[Unset, List[str]] = UNSET
    display_names: Union[Unset, List[str]] = UNSET
    descriptions: Union[Unset, List[str]] = UNSET
    totals: Union[Unset, List[str]] = UNSET
    sort_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        labels = self.labels

        statistics = []
        for statistics_item_data in self.statistics:
            statistics_item = statistics_item_data.to_dict()
            statistics.append(statistics_item)

        names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.names, Unset):
            names = self.names

        display_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.display_names, Unset):
            display_names = self.display_names

        descriptions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.descriptions, Unset):
            descriptions = self.descriptions

        totals: Union[Unset, List[str]] = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals

        sort_key = self.sort_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "displayName": display_name,
                "labels": labels,
                "statistics": statistics,
            }
        )
        if names is not UNSET:
            field_dict["names"] = names
        if display_names is not UNSET:
            field_dict["displayNames"] = display_names
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if totals is not UNSET:
            field_dict["totals"] = totals
        if sort_key is not UNSET:
            field_dict["sortKey"] = sort_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.season_statistics import SeasonStatistics

        d = src_dict.copy()
        name = d.pop("name")

        display_name = d.pop("displayName")

        labels = cast(List[str], d.pop("labels"))

        statistics = []
        _statistics = d.pop("statistics")
        for statistics_item_data in _statistics:
            statistics_item = SeasonStatistics.from_dict(statistics_item_data)

            statistics.append(statistics_item)

        names = cast(List[str], d.pop("names", UNSET))

        display_names = cast(List[str], d.pop("displayNames", UNSET))

        descriptions = cast(List[str], d.pop("descriptions", UNSET))

        totals = cast(List[str], d.pop("totals", UNSET))

        sort_key = d.pop("sortKey", UNSET)

        stats_category = cls(
            name=name,
            display_name=display_name,
            labels=labels,
            statistics=statistics,
            names=names,
            display_names=display_names,
            descriptions=descriptions,
            totals=totals,
            sort_key=sort_key,
        )

        stats_category.additional_properties = d
        return stats_category

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
