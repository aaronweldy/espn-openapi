from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.article_link import ArticleLink
    from ..models.article_links_api import ArticleLinksApi
    from ..models.article_links_app import ArticleLinksApp


T = TypeVar("T", bound="ArticleLinks")


@_attrs_define
class ArticleLinks:
    """
    Attributes:
        web (ArticleLink):
        mobile (ArticleLink):
        api (ArticleLinksApi):
        app (ArticleLinksApp):
    """

    web: "ArticleLink"
    mobile: "ArticleLink"
    api: "ArticleLinksApi"
    app: "ArticleLinksApp"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        web = self.web.to_dict()

        mobile = self.mobile.to_dict()

        api = self.api.to_dict()

        app = self.app.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "web": web,
                "mobile": mobile,
                "api": api,
                "app": app,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.article_link import ArticleLink
        from ..models.article_links_api import ArticleLinksApi
        from ..models.article_links_app import ArticleLinksApp

        d = src_dict.copy()
        web = ArticleLink.from_dict(d.pop("web"))

        mobile = ArticleLink.from_dict(d.pop("mobile"))

        api = ArticleLinksApi.from_dict(d.pop("api"))

        app = ArticleLinksApp.from_dict(d.pop("app"))

        article_links = cls(
            web=web,
            mobile=mobile,
            api=api,
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
