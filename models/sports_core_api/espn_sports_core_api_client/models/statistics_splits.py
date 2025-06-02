from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.statistics_category import StatisticsCategory


T = TypeVar("T", bound="StatisticsSplits")


@_attrs_define
class StatisticsSplits:
    """
    Attributes:
        name (str): Split name (e.g., "All Splits")
        categories (List['StatisticsCategory']):
        id (Union[Unset, str]): Split ID
        abbreviation (Union[Unset, str]): Split abbreviation
    """

    name: str
    categories: List["StatisticsCategory"]
    id: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        id = self.id

        abbreviation = self.abbreviation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "categories": categories,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.statistics_category import StatisticsCategory

        d = src_dict.copy()
        name = d.pop("name")

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = StatisticsCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        id = d.pop("id", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        statistics_splits = cls(
            name=name,
            categories=categories,
            id=id,
            abbreviation=abbreviation,
        )

        statistics_splits.additional_properties = d
        return statistics_splits

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
