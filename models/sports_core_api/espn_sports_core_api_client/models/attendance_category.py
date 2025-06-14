from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attendance_stat import AttendanceStat


T = TypeVar("T", bound="AttendanceCategory")


@_attrs_define
class AttendanceCategory:
    """
    Attributes:
        name (str): Category name (home, away, all) Example: home.
        display_name (str): Display name for the category Example: Home.
        stats (List['AttendanceStat']):
        short_display_name (Union[Unset, str]): Short display name Example: Home.
        abbreviation (Union[Unset, str]): Category abbreviation Example: home.
    """

    name: str
    display_name: str
    stats: List["AttendanceStat"]
    short_display_name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        stats = []
        for stats_item_data in self.stats:
            stats_item = stats_item_data.to_dict()
            stats.append(stats_item)

        short_display_name = self.short_display_name

        abbreviation = self.abbreviation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "displayName": display_name,
                "stats": stats,
            }
        )
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attendance_stat import AttendanceStat

        d = src_dict.copy()
        name = d.pop("name")

        display_name = d.pop("displayName")

        stats = []
        _stats = d.pop("stats")
        for stats_item_data in _stats:
            stats_item = AttendanceStat.from_dict(stats_item_data)

            stats.append(stats_item)

        short_display_name = d.pop("shortDisplayName", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        attendance_category = cls(
            name=name,
            display_name=display_name,
            stats=stats,
            short_display_name=short_display_name,
            abbreviation=abbreviation,
        )

        attendance_category.additional_properties = d
        return attendance_category

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
