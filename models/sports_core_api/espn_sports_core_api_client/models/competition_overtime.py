from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CompetitionOvertime")


@_attrs_define
class CompetitionOvertime:
    """
    Attributes:
        periods (int):
        display_name (str):
        slug (str):
        clock (int):
    """

    periods: int
    display_name: str
    slug: str
    clock: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        periods = self.periods

        display_name = self.display_name

        slug = self.slug

        clock = self.clock

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "periods": periods,
                "displayName": display_name,
                "slug": slug,
                "clock": clock,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        periods = d.pop("periods")

        display_name = d.pop("displayName")

        slug = d.pop("slug")

        clock = d.pop("clock")

        competition_overtime = cls(
            periods=periods,
            display_name=display_name,
            slug=slug,
            clock=clock,
        )

        competition_overtime.additional_properties = d
        return competition_overtime

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
