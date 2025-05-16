from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.search_v2_result_group import SearchV2ResultGroup
    from ..models.search_v2_result_type import SearchV2ResultType


T = TypeVar("T", bound="SearchV2Response")


@_attrs_define
class SearchV2Response:
    """
    Attributes:
        total_found (int): Total number of results found
        result_types (List['SearchV2ResultType']): List of result type summaries
        results (List['SearchV2ResultGroup']): List of grouped search results
    """

    total_found: int
    result_types: List["SearchV2ResultType"]
    results: List["SearchV2ResultGroup"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_found = self.total_found

        result_types = []
        for result_types_item_data in self.result_types:
            result_types_item = result_types_item_data.to_dict()
            result_types.append(result_types_item)

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalFound": total_found,
                "resultTypes": result_types,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_v2_result_group import SearchV2ResultGroup
        from ..models.search_v2_result_type import SearchV2ResultType

        d = src_dict.copy()
        total_found = d.pop("totalFound")

        result_types = []
        _result_types = d.pop("resultTypes")
        for result_types_item_data in _result_types:
            result_types_item = SearchV2ResultType.from_dict(result_types_item_data)

            result_types.append(result_types_item)

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = SearchV2ResultGroup.from_dict(results_item_data)

            results.append(results_item)

        search_v2_response = cls(
            total_found=total_found,
            result_types=result_types,
            results=results,
        )

        search_v2_response.additional_properties = d
        return search_v2_response

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
