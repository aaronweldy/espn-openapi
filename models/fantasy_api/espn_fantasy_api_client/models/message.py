from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Message")


@_attrs_define
class Message:
    """
    Attributes:
        id (str): Message ID Example: message-5678.
        topic_id (str): Topic ID Example: topic-1234.
        date (float): Message timestamp Example: 1630464000000.
        membership_id (str): ID of the member who sent the message Example: {123456789-ABCD-EF12-3456-7890ABCDEF12}.
        text (str): Message text Example: Good luck everyone this season!.
    """

    id: str
    topic_id: str
    date: float
    membership_id: str
    text: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        topic_id = self.topic_id

        date = self.date

        membership_id = self.membership_id

        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "topicId": topic_id,
                "date": date,
                "membershipId": membership_id,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        topic_id = d.pop("topicId")

        date = d.pop("date")

        membership_id = d.pop("membershipId")

        text = d.pop("text")

        message = cls(
            id=id,
            topic_id=topic_id,
            date=date,
            membership_id=membership_id,
            text=text,
        )

        message.additional_properties = d
        return message

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
