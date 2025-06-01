from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.attendance_category import AttendanceCategory


T = TypeVar("T", bound="TeamAttendanceResponse")


@_attrs_define
class TeamAttendanceResponse:
    """
    Attributes:
        ref (str): Reference URL for this attendance data
        id (str): ID of the attendance record
        name (str): Name of the attendance record Example: Attendance.
        abbreviation (str): Abbreviation for attendance Example: ATTND.
        categories (List['AttendanceCategory']):
    """

    ref: str
    id: str
    name: str
    abbreviation: str
    categories: List["AttendanceCategory"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        id = self.id

        name = self.name

        abbreviation = self.abbreviation

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "id": id,
                "name": name,
                "abbreviation": abbreviation,
                "categories": categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attendance_category import AttendanceCategory

        d = src_dict.copy()
        ref = d.pop("$ref")

        id = d.pop("id")

        name = d.pop("name")

        abbreviation = d.pop("abbreviation")

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = AttendanceCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        team_attendance_response = cls(
            ref=ref,
            id=id,
            name=name,
            abbreviation=abbreviation,
            categories=categories,
        )

        team_attendance_response.additional_properties = d
        return team_attendance_response

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
