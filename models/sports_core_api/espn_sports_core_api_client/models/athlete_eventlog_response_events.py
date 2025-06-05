from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.athlete_eventlog_response_events_items_item import AthleteEventlogResponseEventsItemsItem


T = TypeVar("T", bound="AthleteEventlogResponseEvents")


@_attrs_define
class AthleteEventlogResponseEvents:
    """
    Attributes:
        count (Union[Unset, int]):
        page_index (Union[Unset, int]):
        page_size (Union[Unset, int]):
        page_count (Union[Unset, int]):
        items (Union[Unset, List['AthleteEventlogResponseEventsItemsItem']]):
    """

    count: Union[Unset, int] = UNSET
    page_index: Union[Unset, int] = UNSET
    page_size: Union[Unset, int] = UNSET
    page_count: Union[Unset, int] = UNSET
    items: Union[Unset, List["AthleteEventlogResponseEventsItemsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        page_index = self.page_index

        page_size = self.page_size

        page_count = self.page_count

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if page_index is not UNSET:
            field_dict["pageIndex"] = page_index
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if page_count is not UNSET:
            field_dict["pageCount"] = page_count
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_eventlog_response_events_items_item import AthleteEventlogResponseEventsItemsItem

        d = src_dict.copy()
        count = d.pop("count", UNSET)

        page_index = d.pop("pageIndex", UNSET)

        page_size = d.pop("pageSize", UNSET)

        page_count = d.pop("pageCount", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = AthleteEventlogResponseEventsItemsItem.from_dict(items_item_data)

            items.append(items_item)

        athlete_eventlog_response_events = cls(
            count=count,
            page_index=page_index,
            page_size=page_size,
            page_count=page_count,
            items=items,
        )

        athlete_eventlog_response_events.additional_properties = d
        return athlete_eventlog_response_events

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
