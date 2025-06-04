from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialLink")


@_attrs_define
class SocialLink:
    """
    Attributes:
        label (Union[Unset, str]):
        icon (Union[Unset, str]):
        href (Union[Unset, str]):
    """

    label: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label

        icon = self.icon

        href = self.href

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if icon is not UNSET:
            field_dict["icon"] = icon
        if href is not UNSET:
            field_dict["href"] = href

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label", UNSET)

        icon = d.pop("icon", UNSET)

        href = d.pop("href", UNSET)

        social_link = cls(
            label=label,
            icon=icon,
            href=href,
        )

        social_link.additional_properties = d
        return social_link

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
