from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.article_links_app import ArticleLinksApp
    from ..models.link import Link


T = TypeVar("T", bound="ArticleLinks")


@_attrs_define
class ArticleLinks:
    """
    Attributes:
        api (Union[Unset, Link]):
        web (Union[Unset, Link]):
        mobile (Union[Unset, Link]):
        app (Union[Unset, ArticleLinksApp]):
    """

    api: Union[Unset, "Link"] = UNSET
    web: Union[Unset, "Link"] = UNSET
    mobile: Union[Unset, "Link"] = UNSET
    app: Union[Unset, "ArticleLinksApp"] = UNSET
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

        app: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.app, Unset):
            app = self.app.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api is not UNSET:
            field_dict["api"] = api
        if web is not UNSET:
            field_dict["web"] = web
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if app is not UNSET:
            field_dict["app"] = app

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.article_links_app import ArticleLinksApp
        from ..models.link import Link

        d = src_dict.copy()
        _api = d.pop("api", UNSET)
        api: Union[Unset, Link]
        if isinstance(_api, Unset):
            api = UNSET
        else:
            api = Link.from_dict(_api)

        _web = d.pop("web", UNSET)
        web: Union[Unset, Link]
        if isinstance(_web, Unset):
            web = UNSET
        else:
            web = Link.from_dict(_web)

        _mobile = d.pop("mobile", UNSET)
        mobile: Union[Unset, Link]
        if isinstance(_mobile, Unset):
            mobile = UNSET
        else:
            mobile = Link.from_dict(_mobile)

        _app = d.pop("app", UNSET)
        app: Union[Unset, ArticleLinksApp]
        if isinstance(_app, Unset):
            app = UNSET
        else:
            app = ArticleLinksApp.from_dict(_app)

        article_links = cls(
            api=api,
            web=web,
            mobile=mobile,
            app=app,
        )

        article_links.additional_properties = d
        return article_links

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
