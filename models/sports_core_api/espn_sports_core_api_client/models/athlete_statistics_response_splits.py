from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.statistic_category import StatisticCategory


T = TypeVar("T", bound="AthleteStatisticsResponseSplits")


@_attrs_define
class AthleteStatisticsResponseSplits:
    """
    Attributes:
        id (str):  Example: 0.
        name (str):  Example: All Splits.
        abbreviation (str):  Example: Total.
        categories (List['StatisticCategory']):
        type (Union[None, Unset, str]):  Example: total.
    """

    id: str
    name: str
    abbreviation: str
    categories: List["StatisticCategory"]
    type: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        abbreviation = self.abbreviation

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        type: Union[None, Unset, str]
        if isinstance(self.type, Unset):
            type = UNSET
        else:
            type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "abbreviation": abbreviation,
                "categories": categories,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.statistic_category import StatisticCategory

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        abbreviation = d.pop("abbreviation")

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = StatisticCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        def _parse_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type = _parse_type(d.pop("type", UNSET))

        athlete_statistics_response_splits = cls(
            id=id,
            name=name,
            abbreviation=abbreviation,
            categories=categories,
            type=type,
        )

        athlete_statistics_response_splits.additional_properties = d
        return athlete_statistics_response_splits

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
