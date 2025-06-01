from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.news_link_item import NewsLinkItem


T = TypeVar("T", bound="NewsLinkWeb")


@_attrs_define
class NewsLinkWeb:
    """
    Attributes:
        href (Union[Unset, str]):
        short (Union[Unset, NewsLinkItem]):
        self_ (Union[Unset, NewsLinkItem]):
    """

    href: Union[Unset, str] = UNSET
    short: Union[Unset, "NewsLinkItem"] = UNSET
    self_: Union[Unset, "NewsLinkItem"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        short: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.short, Unset):
            short = self.short.to_dict()

        self_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if short is not UNSET:
            field_dict["short"] = short
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.news_link_item import NewsLinkItem

        d = src_dict.copy()
        href = d.pop("href", UNSET)

        _short = d.pop("short", UNSET)
        short: Union[Unset, NewsLinkItem]
        if isinstance(_short, Unset):
            short = UNSET
        else:
            short = NewsLinkItem.from_dict(_short)

        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, NewsLinkItem]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = NewsLinkItem.from_dict(_self_)

        news_link_web = cls(
            href=href,
            short=short,
            self_=self_,
        )

        news_link_web.additional_properties = d
        return news_link_web

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
