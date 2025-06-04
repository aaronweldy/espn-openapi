from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlexLink")


@_attrs_define
class FlexLink:
    """
    Attributes:
        rels (Union[Unset, List[str]]):
        href (Union[Unset, str]):
        locale (Union[Unset, str]):
    """

    rels: Union[Unset, List[str]] = UNSET
    href: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rels, Unset):
            rels = self.rels

        href = self.href

        locale = self.locale

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rels is not UNSET:
            field_dict["rels"] = rels
        if href is not UNSET:
            field_dict["href"] = href
        if locale is not UNSET:
            field_dict["locale"] = locale

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rels = cast(List[str], d.pop("rels", UNSET))

        href = d.pop("href", UNSET)

        locale = d.pop("locale", UNSET)

        flex_link = cls(
            rels=rels,
            href=href,
            locale=locale,
        )

        flex_link.additional_properties = d
        return flex_link

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
