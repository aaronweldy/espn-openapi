from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.stat_correction import StatCorrection


T = TypeVar("T", bound="StatCorrectionsResponse")


@_attrs_define
class StatCorrectionsResponse:
    """Paginated list of statistical corrections for a given sport, league, season, and season type.

    Attributes:
        count (int):
        page_index (int):
        page_size (int):
        page_count (int):
        items (List['StatCorrection']):
    """

    count: int
    page_index: int
    page_size: int
    page_count: int
    items: List["StatCorrection"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        page_index = self.page_index

        page_size = self.page_size

        page_count = self.page_count

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "pageIndex": page_index,
                "pageSize": page_size,
                "pageCount": page_count,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stat_correction import StatCorrection

        d = src_dict.copy()
        count = d.pop("count")

        page_index = d.pop("pageIndex")

        page_size = d.pop("pageSize")

        page_count = d.pop("pageCount")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = StatCorrection.from_dict(items_item_data)

            items.append(items_item)

        stat_corrections_response = cls(
            count=count,
            page_index=page_index,
            page_size=page_size,
            page_count=page_count,
            items=items,
        )

        stat_corrections_response.additional_properties = d
        return stat_corrections_response

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
