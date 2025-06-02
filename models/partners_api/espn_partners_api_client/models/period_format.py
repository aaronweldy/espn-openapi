from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeriodFormat")


@_attrs_define
class PeriodFormat:
    """
    Attributes:
        periods (Union[Unset, int]): Number of periods Example: 4.
        display_name (Union[Unset, str]): Period display name Example: Quarter.
        slug (Union[Unset, str]): Period slug Example: quarter.
        clock (Union[Unset, float]): Period clock duration in seconds Example: 900.0.
    """

    periods: Union[Unset, int] = UNSET
    display_name: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    clock: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        periods = self.periods

        display_name = self.display_name

        slug = self.slug

        clock = self.clock

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if periods is not UNSET:
            field_dict["periods"] = periods
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if clock is not UNSET:
            field_dict["clock"] = clock

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        periods = d.pop("periods", UNSET)

        display_name = d.pop("displayName", UNSET)

        slug = d.pop("slug", UNSET)

        clock = d.pop("clock", UNSET)

        period_format = cls(
            periods=periods,
            display_name=display_name,
            slug=slug,
            clock=clock,
        )

        period_format.additional_properties = d
        return period_format

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
