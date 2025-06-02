from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.event import Event


T = TypeVar("T", bound="EventsListResponse")


@_attrs_define
class EventsListResponse:
    """
    Attributes:
        events (List['Event']):
        count (int): Total number of events available Example: 335.
        page_index (int): Current page index (1-based) Example: 1.
        page_size (int): Number of items per page Example: 100.
        page_count (int): Total number of pages Example: 4.
    """

    events: List["Event"]
    count: int
    page_index: int
    page_size: int
    page_count: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        count = self.count

        page_index = self.page_index

        page_size = self.page_size

        page_count = self.page_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
                "count": count,
                "pageIndex": page_index,
                "pageSize": page_size,
                "pageCount": page_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event import Event

        d = src_dict.copy()
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = Event.from_dict(events_item_data)

            events.append(events_item)

        count = d.pop("count")

        page_index = d.pop("pageIndex")

        page_size = d.pop("pageSize")

        page_count = d.pop("pageCount")

        events_list_response = cls(
            events=events,
            count=count,
            page_index=page_index,
            page_size=page_size,
            page_count=page_count,
        )

        events_list_response.additional_properties = d
        return events_list_response

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
