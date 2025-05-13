from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AthleteOverviewHeadshot")


@_attrs_define
class AthleteOverviewHeadshot:
    """
    Attributes:
        href (Union[Unset, str]):  Example: https://a.espncdn.com/i/headshots/nfl/players/full/3139477.png.
        alt (Union[Unset, str]):  Example: Patrick Mahomes.
    """

    href: Union[Unset, str] = UNSET
    alt: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        alt = self.alt

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if alt is not UNSET:
            field_dict["alt"] = alt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        href = d.pop("href", UNSET)

        alt = d.pop("alt", UNSET)

        athlete_overview_headshot = cls(
            href=href,
            alt=alt,
        )

        athlete_overview_headshot.additional_properties = d
        return athlete_overview_headshot

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
