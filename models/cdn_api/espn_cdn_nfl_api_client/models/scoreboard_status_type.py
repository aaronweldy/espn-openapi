from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScoreboardStatusType")


@_attrs_define
class ScoreboardStatusType:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        id (Union[Unset, str]):
        state (Union[Unset, str]):
        completed (Union[Unset, bool]):
        detail (Union[Unset, str]):
        short_detail (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    completed: Union[Unset, bool] = UNSET
    detail: Union[Unset, str] = UNSET
    short_detail: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        id = self.id

        state = self.state

        completed = self.completed

        detail = self.detail

        short_detail = self.short_detail

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if state is not UNSET:
            field_dict["state"] = state
        if completed is not UNSET:
            field_dict["completed"] = completed
        if detail is not UNSET:
            field_dict["detail"] = detail
        if short_detail is not UNSET:
            field_dict["shortDetail"] = short_detail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        state = d.pop("state", UNSET)

        completed = d.pop("completed", UNSET)

        detail = d.pop("detail", UNSET)

        short_detail = d.pop("shortDetail", UNSET)

        scoreboard_status_type = cls(
            name=name,
            description=description,
            id=id,
            state=state,
            completed=completed,
            detail=detail,
            short_detail=short_detail,
        )

        scoreboard_status_type.additional_properties = d
        return scoreboard_status_type

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
