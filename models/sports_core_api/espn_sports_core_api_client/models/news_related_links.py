from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.news_link_item import NewsLinkItem


T = TypeVar("T", bound="NewsRelatedLinks")


@_attrs_define
class NewsRelatedLinks:
    """
    Attributes:
        web (Union[Unset, NewsLinkItem]):
        mobile (Union[Unset, NewsLinkItem]):
        api (Union[Unset, NewsLinkItem]):
    """

    web: Union[Unset, "NewsLinkItem"] = UNSET
    mobile: Union[Unset, "NewsLinkItem"] = UNSET
    api: Union[Unset, "NewsLinkItem"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        web: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.web, Unset):
            web = self.web.to_dict()

        mobile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mobile, Unset):
            mobile = self.mobile.to_dict()

        api: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.api, Unset):
            api = self.api.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if web is not UNSET:
            field_dict["web"] = web
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if api is not UNSET:
            field_dict["api"] = api

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.news_link_item import NewsLinkItem

        d = src_dict.copy()
        _web = d.pop("web", UNSET)
        web: Union[Unset, NewsLinkItem]
        if isinstance(_web, Unset):
            web = UNSET
        else:
            web = NewsLinkItem.from_dict(_web)

        _mobile = d.pop("mobile", UNSET)
        mobile: Union[Unset, NewsLinkItem]
        if isinstance(_mobile, Unset):
            mobile = UNSET
        else:
            mobile = NewsLinkItem.from_dict(_mobile)

        _api = d.pop("api", UNSET)
        api: Union[Unset, NewsLinkItem]
        if isinstance(_api, Unset):
            api = UNSET
        else:
            api = NewsLinkItem.from_dict(_api)

        news_related_links = cls(
            web=web,
            mobile=mobile,
            api=api,
        )

        news_related_links.additional_properties = d
        return news_related_links

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
