from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_type_state import StatusTypeState
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusType")


@_attrs_define
class StatusType:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 3.
        name (Union[Unset, str]):  Example: STATUS_FINAL.
        state (Union[Unset, StatusTypeState]):  Example: post.
        completed (Union[Unset, bool]):
        description (Union[Unset, str]):  Example: Final.
        detail (Union[Unset, str]):  Example: Final.
        short_detail (Union[Unset, str]):  Example: Final.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    state: Union[Unset, StatusTypeState] = UNSET
    completed: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    detail: Union[Unset, str] = UNSET
    short_detail: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        completed = self.completed

        description = self.description

        detail = self.detail

        short_detail = self.short_detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if state is not UNSET:
            field_dict["state"] = state
        if completed is not UNSET:
            field_dict["completed"] = completed
        if description is not UNSET:
            field_dict["description"] = description
        if detail is not UNSET:
            field_dict["detail"] = detail
        if short_detail is not UNSET:
            field_dict["shortDetail"] = short_detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, StatusTypeState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = StatusTypeState(_state)

        completed = d.pop("completed", UNSET)

        description = d.pop("description", UNSET)

        detail = d.pop("detail", UNSET)

        short_detail = d.pop("shortDetail", UNSET)

        status_type = cls(
            id=id,
            name=name,
            state=state,
            completed=completed,
            description=description,
            detail=detail,
            short_detail=short_detail,
        )

        status_type.additional_properties = d
        return status_type

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
