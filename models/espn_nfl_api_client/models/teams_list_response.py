from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sport import Sport


T = TypeVar("T", bound="TeamsListResponse")


@_attrs_define
class TeamsListResponse:
    """
    Attributes:
        sports (list['Sport']):
    """

    sports: list["Sport"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sports = []
        for sports_item_data in self.sports:
            sports_item = sports_item_data.to_dict()
            sports.append(sports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sports": sports,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sport import Sport

        d = dict(src_dict)
        sports = []
        _sports = d.pop("sports")
        for sports_item_data in _sports:
            sports_item = Sport.from_dict(sports_item_data)

            sports.append(sports_item)

        teams_list_response = cls(
            sports=sports,
        )

        teams_list_response.additional_properties = d
        return teams_list_response

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
