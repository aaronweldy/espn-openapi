from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FantasyWeatherLink")


@_attrs_define
class FantasyWeatherLink:
    """
    Attributes:
        text (Union[Unset, str]):
        href (Union[Unset, str]):
        is_external (Union[Unset, bool]):
    """

    text: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    is_external: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        href = self.href

        is_external = self.is_external

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if href is not UNSET:
            field_dict["href"] = href
        if is_external is not UNSET:
            field_dict["isExternal"] = is_external

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text", UNSET)

        href = d.pop("href", UNSET)

        is_external = d.pop("isExternal", UNSET)

        fantasy_weather_link = cls(
            text=text,
            href=href,
            is_external=is_external,
        )

        fantasy_weather_link.additional_properties = d
        return fantasy_weather_link

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
