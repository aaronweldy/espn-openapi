from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamLogo")


@_attrs_define
class TeamLogo:
    """
    Attributes:
        href (str):  Example: https://a.espncdn.com/i/teamlogos/nfl/500/ari.png.
        alt (Union[Unset, str]):
        rel (Union[Unset, List[str]]):
        width (Union[Unset, int]):  Example: 500.
        height (Union[Unset, int]):  Example: 500.
    """

    href: str
    alt: Union[Unset, str] = UNSET
    rel: Union[Unset, List[str]] = UNSET
    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        alt = self.alt

        rel: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rel, Unset):
            rel = self.rel

        width = self.width

        height = self.height

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "href": href,
            }
        )
        if alt is not UNSET:
            field_dict["alt"] = alt
        if rel is not UNSET:
            field_dict["rel"] = rel
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        href = d.pop("href")

        alt = d.pop("alt", UNSET)

        rel = cast(List[str], d.pop("rel", UNSET))

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        team_logo = cls(
            href=href,
            alt=alt,
            rel=rel,
            width=width,
            height=height,
        )

        team_logo.additional_properties = d
        return team_logo

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
