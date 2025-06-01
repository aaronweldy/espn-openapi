from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.news_link_item import NewsLinkItem


T = TypeVar("T", bound="NewsLinkMobile")


@_attrs_define
class NewsLinkMobile:
    """
    Attributes:
        href (Union[Unset, str]):
        alert (Union[Unset, NewsLinkItem]):
    """

    href: Union[Unset, str] = UNSET
    alert: Union[Unset, "NewsLinkItem"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        alert: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alert, Unset):
            alert = self.alert.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if alert is not UNSET:
            field_dict["alert"] = alert

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.news_link_item import NewsLinkItem

        d = src_dict.copy()
        href = d.pop("href", UNSET)

        _alert = d.pop("alert", UNSET)
        alert: Union[Unset, NewsLinkItem]
        if isinstance(_alert, Unset):
            alert = UNSET
        else:
            alert = NewsLinkItem.from_dict(_alert)

        news_link_mobile = cls(
            href=href,
            alert=alert,
        )

        news_link_mobile.additional_properties = d
        return news_link_mobile

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
