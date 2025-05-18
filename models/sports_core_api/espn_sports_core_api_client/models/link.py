from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Link")


@_attrs_define
class Link:
    """
    Attributes:
        href (str):
        rel (List[str]):
        text (Union[Unset, str]):  Example: Standings.
    """

    href: str
    rel: List[str]
    text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        rel = self.rel

        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "href": href,
                "rel": rel,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        href = d.pop("href")

        rel = cast(List[str], d.pop("rel"))

        text = d.pop("text", UNSET)

        link = cls(
            href=href,
            rel=rel,
            text=text,
        )

        link.additional_properties = d
        return link

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
