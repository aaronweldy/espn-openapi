from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.athlete_splits_category import AthleteSplitsCategory
    from ..models.athlete_splits_filter import AthleteSplitsFilter
    from ..models.athlete_splits_split_category import AthleteSplitsSplitCategory


T = TypeVar("T", bound="AthleteSplitsResponse")


@_attrs_define
class AthleteSplitsResponse:
    """NFL Athlete Splits response object.

    Attributes:
        filters (List['AthleteSplitsFilter']):
        display_name (str):
        categories (List['AthleteSplitsCategory']):
        labels (List[str]):
        names (List[str]):
        display_names (List[str]):
        descriptions (List[str]):
        split_categories (List['AthleteSplitsSplitCategory']):
    """

    filters: List["AthleteSplitsFilter"]
    display_name: str
    categories: List["AthleteSplitsCategory"]
    labels: List[str]
    names: List[str]
    display_names: List[str]
    descriptions: List[str]
    split_categories: List["AthleteSplitsSplitCategory"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()
            filters.append(filters_item)

        display_name = self.display_name

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        labels = self.labels

        names = self.names

        display_names = self.display_names

        descriptions = self.descriptions

        split_categories = []
        for split_categories_item_data in self.split_categories:
            split_categories_item = split_categories_item_data.to_dict()
            split_categories.append(split_categories_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
                "displayName": display_name,
                "categories": categories,
                "labels": labels,
                "names": names,
                "displayNames": display_names,
                "descriptions": descriptions,
                "splitCategories": split_categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_splits_category import AthleteSplitsCategory
        from ..models.athlete_splits_filter import AthleteSplitsFilter
        from ..models.athlete_splits_split_category import AthleteSplitsSplitCategory

        d = src_dict.copy()
        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = AthleteSplitsFilter.from_dict(filters_item_data)

            filters.append(filters_item)

        display_name = d.pop("displayName")

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = AthleteSplitsCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        labels = cast(List[str], d.pop("labels"))

        names = cast(List[str], d.pop("names"))

        display_names = cast(List[str], d.pop("displayNames"))

        descriptions = cast(List[str], d.pop("descriptions"))

        split_categories = []
        _split_categories = d.pop("splitCategories")
        for split_categories_item_data in _split_categories:
            split_categories_item = AthleteSplitsSplitCategory.from_dict(split_categories_item_data)

            split_categories.append(split_categories_item)

        athlete_splits_response = cls(
            filters=filters,
            display_name=display_name,
            categories=categories,
            labels=labels,
            names=names,
            display_names=display_names,
            descriptions=descriptions,
            split_categories=split_categories,
        )

        athlete_splits_response.additional_properties = d
        return athlete_splits_response

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
