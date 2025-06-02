from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_status_type_state import EventStatusTypeState
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventStatusType")


@_attrs_define
class EventStatusType:
    """
    Attributes:
        id (str): Status type identifier Example: 1.
        name (str): Status name Example: STATUS_SCHEDULED.
        state (EventStatusTypeState): Status state Example: pre.
        completed (bool): Whether the event is completed
        description (str): Status description Example: Scheduled.
        detail (Union[Unset, str]): Status detail Example: Thu, September 4th at 8:20 PM EDT.
        short_detail (Union[Unset, str]): Short status detail Example: 9/4 - 8:20 PM EDT.
    """

    id: str
    name: str
    state: EventStatusTypeState
    completed: bool
    description: str
    detail: Union[Unset, str] = UNSET
    short_detail: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        state = self.state.value

        completed = self.completed

        description = self.description

        detail = self.detail

        short_detail = self.short_detail

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "state": state,
                "completed": completed,
                "description": description,
            }
        )
        if detail is not UNSET:
            field_dict["detail"] = detail
        if short_detail is not UNSET:
            field_dict["shortDetail"] = short_detail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        state = EventStatusTypeState(d.pop("state"))

        completed = d.pop("completed")

        description = d.pop("description")

        detail = d.pop("detail", UNSET)

        short_detail = d.pop("shortDetail", UNSET)

        event_status_type = cls(
            id=id,
            name=name,
            state=state,
            completed=completed,
            description=description,
            detail=detail,
            short_detail=short_detail,
        )

        event_status_type.additional_properties = d
        return event_status_type

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
