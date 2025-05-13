from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_label import CategoryLabel
    from ..models.game_log_event import GameLogEvent


T = TypeVar("T", bound="GameLogCategory")


@_attrs_define
class GameLogCategory:
    """
    Attributes:
        name (str):  Example: passing.
        display_name (str):  Example: Passing.
        events (List['GameLogEvent']):
        labels (Union[Unset, List['CategoryLabel']]):
    """

    name: str
    display_name: str
    events: List["GameLogEvent"]
    labels: Union[Unset, List["CategoryLabel"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        labels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "displayName": display_name,
                "events": events,
            }
        )
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.category_label import CategoryLabel
        from ..models.game_log_event import GameLogEvent

        d = src_dict.copy()
        name = d.pop("name")

        display_name = d.pop("displayName")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = GameLogEvent.from_dict(events_item_data)

            events.append(events_item)

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = CategoryLabel.from_dict(labels_item_data)

            labels.append(labels_item)

        game_log_category = cls(
            name=name,
            display_name=display_name,
            events=events,
            labels=labels,
        )

        game_log_category.additional_properties = d
        return game_log_category

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
