from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.career_statistics_categories_item import CareerStatisticsCategoriesItem
    from ..models.career_statistics_splits_item import CareerStatisticsSplitsItem


T = TypeVar("T", bound="CareerStatistics")


@_attrs_define
class CareerStatistics:
    """
    Attributes:
        display_name (str):  Example: Career Passing.
        categories (List['CareerStatisticsCategoriesItem']):
        labels (List[str]): Labels for the statistics. Example: ['CMP', 'ATT', 'CMP%', 'YDS', 'AVG', 'TD', 'INT', 'LNG',
            'RTG'].
        names (List[str]): Internal names for the statistics. Example: ['completions', 'passingAttempts',
            'completionPct', 'passingYards', 'yardsPerPassAttempt', 'passingTouchdowns', 'interceptions', 'longPassing',
            'QBRating'].
        display_names (List[str]): Display names for the statistics. Example: ['Completions', 'Passing Attempts',
            'Completion Percentage', 'Passing Yards', 'Yards Per Pass Attempt', 'Passing Touchdowns', 'Interceptions',
            'Longest Pass', 'Passer Rating'].
        splits (List['CareerStatisticsSplitsItem']): Breakdown of statistics by different criteria (e.g., seasons, game
            types).
    """

    display_name: str
    categories: List["CareerStatisticsCategoriesItem"]
    labels: List[str]
    names: List[str]
    display_names: List[str]
    splits: List["CareerStatisticsSplitsItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        labels = self.labels

        names = self.names

        display_names = self.display_names

        splits = []
        for splits_item_data in self.splits:
            splits_item = splits_item_data.to_dict()
            splits.append(splits_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "categories": categories,
                "labels": labels,
                "names": names,
                "displayNames": display_names,
                "splits": splits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.career_statistics_categories_item import CareerStatisticsCategoriesItem
        from ..models.career_statistics_splits_item import CareerStatisticsSplitsItem

        d = src_dict.copy()
        display_name = d.pop("displayName")

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = CareerStatisticsCategoriesItem.from_dict(categories_item_data)

            categories.append(categories_item)

        labels = cast(List[str], d.pop("labels"))

        names = cast(List[str], d.pop("names"))

        display_names = cast(List[str], d.pop("displayNames"))

        splits = []
        _splits = d.pop("splits")
        for splits_item_data in _splits:
            splits_item = CareerStatisticsSplitsItem.from_dict(splits_item_data)

            splits.append(splits_item)

        career_statistics = cls(
            display_name=display_name,
            categories=categories,
            labels=labels,
            names=names,
            display_names=display_names,
            splits=splits,
        )

        career_statistics.additional_properties = d
        return career_statistics

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
