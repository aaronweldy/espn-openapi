from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.news_article_link import NewsArticleLink
    from ..models.news_article_links_api import NewsArticleLinksApi
    from ..models.news_article_links_app import NewsArticleLinksApp


T = TypeVar("T", bound="NewsArticleLinks")


@_attrs_define
class NewsArticleLinks:
    """
    Attributes:
        web (Union[Unset, NewsArticleLink]):
        mobile (Union[Unset, NewsArticleLink]):
        api (Union[Unset, NewsArticleLinksApi]):
        app (Union[Unset, NewsArticleLinksApp]):
    """

    web: Union[Unset, "NewsArticleLink"] = UNSET
    mobile: Union[Unset, "NewsArticleLink"] = UNSET
    api: Union[Unset, "NewsArticleLinksApi"] = UNSET
    app: Union[Unset, "NewsArticleLinksApp"] = UNSET
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

        app: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.app, Unset):
            app = self.app.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if web is not UNSET:
            field_dict["web"] = web
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if api is not UNSET:
            field_dict["api"] = api
        if app is not UNSET:
            field_dict["app"] = app

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.news_article_link import NewsArticleLink
        from ..models.news_article_links_api import NewsArticleLinksApi
        from ..models.news_article_links_app import NewsArticleLinksApp

        d = src_dict.copy()
        _web = d.pop("web", UNSET)
        web: Union[Unset, NewsArticleLink]
        if isinstance(_web, Unset):
            web = UNSET
        else:
            web = NewsArticleLink.from_dict(_web)

        _mobile = d.pop("mobile", UNSET)
        mobile: Union[Unset, NewsArticleLink]
        if isinstance(_mobile, Unset):
            mobile = UNSET
        else:
            mobile = NewsArticleLink.from_dict(_mobile)

        _api = d.pop("api", UNSET)
        api: Union[Unset, NewsArticleLinksApi]
        if isinstance(_api, Unset):
            api = UNSET
        else:
            api = NewsArticleLinksApi.from_dict(_api)

        _app = d.pop("app", UNSET)
        app: Union[Unset, NewsArticleLinksApp]
        if isinstance(_app, Unset):
            app = UNSET
        else:
            app = NewsArticleLinksApp.from_dict(_app)

        news_article_links = cls(
            web=web,
            mobile=mobile,
            api=api,
            app=app,
        )

        news_article_links.additional_properties = d
        return news_article_links

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
