from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topic import Topic


T = TypeVar("T", bound="LeagueCommunication")


@_attrs_define
class LeagueCommunication:
    """
    Attributes:
        last_read (float): Timestamp of last read message Example: 1630464000000.
        topics (Union[Unset, List['Topic']]):
    """

    last_read: float
    topics: Union[Unset, List["Topic"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_read = self.last_read

        topics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.topics, Unset):
            topics = []
            for topics_item_data in self.topics:
                topics_item = topics_item_data.to_dict()
                topics.append(topics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lastRead": last_read,
            }
        )
        if topics is not UNSET:
            field_dict["topics"] = topics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.topic import Topic

        d = src_dict.copy()
        last_read = d.pop("lastRead")

        topics = []
        _topics = d.pop("topics", UNSET)
        for topics_item_data in _topics or []:
            topics_item = Topic.from_dict(topics_item_data)

            topics.append(topics_item)

        league_communication = cls(
            last_read=last_read,
            topics=topics,
        )

        league_communication.additional_properties = d
        return league_communication

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
