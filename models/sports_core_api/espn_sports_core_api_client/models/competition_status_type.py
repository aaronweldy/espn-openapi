from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CompetitionStatusType")


@_attrs_define
class CompetitionStatusType:
    """
    Attributes:
        id (str):
        name (str):
        state (str):
        completed (bool):
        description (str):
        detail (str):
        short_detail (str):
    """

    id: str
    name: str
    state: str
    completed: bool
    description: str
    detail: str
    short_detail: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        state = self.state

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
                "detail": detail,
                "shortDetail": short_detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        state = d.pop("state")

        completed = d.pop("completed")

        description = d.pop("description")

        detail = d.pop("detail")

        short_detail = d.pop("shortDetail")

        competition_status_type = cls(
            id=id,
            name=name,
            state=state,
            completed=completed,
            description=description,
            detail=detail,
            short_detail=short_detail,
        )

        competition_status_type.additional_properties = d
        return competition_status_type

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
