from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.news_link_amp import NewsLinkAmp
    from ..models.news_link_api import NewsLinkApi
    from ..models.news_link_mobile import NewsLinkMobile
    from ..models.news_link_web import NewsLinkWeb


T = TypeVar("T", bound="NewsLinks")


@_attrs_define
class NewsLinks:
    """
    Attributes:
        api (Union[Unset, NewsLinkApi]):
        web (Union[Unset, NewsLinkWeb]):
        mobile (Union[Unset, NewsLinkMobile]):
        amp (Union[Unset, NewsLinkAmp]):
    """

    api: Union[Unset, "NewsLinkApi"] = UNSET
    web: Union[Unset, "NewsLinkWeb"] = UNSET
    mobile: Union[Unset, "NewsLinkMobile"] = UNSET
    amp: Union[Unset, "NewsLinkAmp"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.api, Unset):
            api = self.api.to_dict()

        web: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.web, Unset):
            web = self.web.to_dict()

        mobile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mobile, Unset):
            mobile = self.mobile.to_dict()

        amp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.amp, Unset):
            amp = self.amp.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api is not UNSET:
            field_dict["api"] = api
        if web is not UNSET:
            field_dict["web"] = web
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if amp is not UNSET:
            field_dict["amp"] = amp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.news_link_amp import NewsLinkAmp
        from ..models.news_link_api import NewsLinkApi
        from ..models.news_link_mobile import NewsLinkMobile
        from ..models.news_link_web import NewsLinkWeb

        d = src_dict.copy()
        _api = d.pop("api", UNSET)
        api: Union[Unset, NewsLinkApi]
        if isinstance(_api, Unset):
            api = UNSET
        else:
            api = NewsLinkApi.from_dict(_api)

        _web = d.pop("web", UNSET)
        web: Union[Unset, NewsLinkWeb]
        if isinstance(_web, Unset):
            web = UNSET
        else:
            web = NewsLinkWeb.from_dict(_web)

        _mobile = d.pop("mobile", UNSET)
        mobile: Union[Unset, NewsLinkMobile]
        if isinstance(_mobile, Unset):
            mobile = UNSET
        else:
            mobile = NewsLinkMobile.from_dict(_mobile)

        _amp = d.pop("amp", UNSET)
        amp: Union[Unset, NewsLinkAmp]
        if isinstance(_amp, Unset):
            amp = UNSET
        else:
            amp = NewsLinkAmp.from_dict(_amp)

        news_links = cls(
            api=api,
            web=web,
            mobile=mobile,
            amp=amp,
        )

        news_links.additional_properties = d
        return news_links

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
