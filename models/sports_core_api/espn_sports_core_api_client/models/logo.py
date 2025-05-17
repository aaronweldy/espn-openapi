import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Logo")


@_attrs_define
class Logo:
    """
    Attributes:
        href (str):
        width (int):
        height (int):
        alt (str):
        rel (List[str]):
        last_updated (Union[Unset, datetime.datetime]):
    """

    href: str
    width: int
    height: int
    alt: str
    rel: List[str]
    last_updated: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        width = self.width

        height = self.height

        alt = self.alt

        rel = self.rel

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "href": href,
                "width": width,
                "height": height,
                "alt": alt,
                "rel": rel,
            }
        )
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        href = d.pop("href")

        width = d.pop("width")

        height = d.pop("height")

        alt = d.pop("alt")

        rel = cast(List[str], d.pop("rel"))

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        logo = cls(
            href=href,
            width=width,
            height=height,
            alt=alt,
            rel=rel,
            last_updated=last_updated,
        )

        logo.additional_properties = d
        return logo

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
