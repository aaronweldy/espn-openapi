from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_status_state import EventStatusState
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventStatus")


@_attrs_define
class EventStatus:
    """
    Attributes:
        state (EventStatusState):  Example: post.
        detail (Union[Unset, str]):  Example: Final.
        short_detail (Union[Unset, str]):  Example: Final.
    """

    state: EventStatusState
    detail: Union[Unset, str] = UNSET
    short_detail: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state = self.state.value

        detail = self.detail

        short_detail = self.short_detail

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
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
        state = EventStatusState(d.pop("state"))

        detail = d.pop("detail", UNSET)

        short_detail = d.pop("shortDetail", UNSET)

        event_status = cls(
            state=state,
            detail=detail,
            short_detail=short_detail,
        )

        event_status.additional_properties = d
        return event_status

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
