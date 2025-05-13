from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message import Message


T = TypeVar("T", bound="Topic")


@_attrs_define
class Topic:
    """
    Attributes:
        id (str): Topic ID Example: topic-1234.
        type (str): Topic type Example: GROUP.
        date (float): Topic timestamp Example: 1630464000000.
        messages (Union[Unset, List['Message']]):
    """

    id: str
    type: str
    date: float
    messages: Union[Unset, List["Message"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type

        date = self.date

        messages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "date": date,
            }
        )
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.message import Message

        d = src_dict.copy()
        id = d.pop("id")

        type = d.pop("type")

        date = d.pop("date")

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = Message.from_dict(messages_item_data)

            messages.append(messages_item)

        topic = cls(
            id=id,
            type=type,
            date=date,
            messages=messages,
        )

        topic.additional_properties = d
        return topic

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
