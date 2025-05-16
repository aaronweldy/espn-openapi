from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_article_links_api import ScoreboardArticleLinksApi
    from ..models.scoreboard_article_links_app import ScoreboardArticleLinksApp
    from ..models.scoreboard_article_links_mobile_type_1 import ScoreboardArticleLinksMobileType1
    from ..models.scoreboard_article_links_web_type_1 import ScoreboardArticleLinksWebType1
    from ..models.scoreboard_link import ScoreboardLink


T = TypeVar("T", bound="ScoreboardArticleLinks")


@_attrs_define
class ScoreboardArticleLinks:
    """
    Attributes:
        app (Union[Unset, ScoreboardArticleLinksApp]):
        web (Union['ScoreboardArticleLinksWebType1', 'ScoreboardLink', Unset]):
        mobile (Union['ScoreboardArticleLinksMobileType1', 'ScoreboardLink', Unset]):
        api (Union[Unset, ScoreboardArticleLinksApi]):
        sportscenter (Union[Unset, ScoreboardLink]):
    """

    app: Union[Unset, "ScoreboardArticleLinksApp"] = UNSET
    web: Union["ScoreboardArticleLinksWebType1", "ScoreboardLink", Unset] = UNSET
    mobile: Union["ScoreboardArticleLinksMobileType1", "ScoreboardLink", Unset] = UNSET
    api: Union[Unset, "ScoreboardArticleLinksApi"] = UNSET
    sportscenter: Union[Unset, "ScoreboardLink"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.scoreboard_link import ScoreboardLink

        app: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.app, Unset):
            app = self.app.to_dict()

        web: Union[Dict[str, Any], Unset]
        if isinstance(self.web, Unset):
            web = UNSET
        elif isinstance(self.web, ScoreboardLink):
            web = self.web.to_dict()
        else:
            web = self.web.to_dict()

        mobile: Union[Dict[str, Any], Unset]
        if isinstance(self.mobile, Unset):
            mobile = UNSET
        elif isinstance(self.mobile, ScoreboardLink):
            mobile = self.mobile.to_dict()
        else:
            mobile = self.mobile.to_dict()

        api: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.api, Unset):
            api = self.api.to_dict()

        sportscenter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sportscenter, Unset):
            sportscenter = self.sportscenter.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app is not UNSET:
            field_dict["app"] = app
        if web is not UNSET:
            field_dict["web"] = web
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if api is not UNSET:
            field_dict["api"] = api
        if sportscenter is not UNSET:
            field_dict["sportscenter"] = sportscenter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_article_links_api import ScoreboardArticleLinksApi
        from ..models.scoreboard_article_links_app import ScoreboardArticleLinksApp
        from ..models.scoreboard_article_links_mobile_type_1 import ScoreboardArticleLinksMobileType1
        from ..models.scoreboard_article_links_web_type_1 import ScoreboardArticleLinksWebType1
        from ..models.scoreboard_link import ScoreboardLink

        d = src_dict.copy()
        _app = d.pop("app", UNSET)
        app: Union[Unset, ScoreboardArticleLinksApp]
        if isinstance(_app, Unset):
            app = UNSET
        else:
            app = ScoreboardArticleLinksApp.from_dict(_app)

        def _parse_web(data: object) -> Union["ScoreboardArticleLinksWebType1", "ScoreboardLink", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                web_type_0 = ScoreboardLink.from_dict(data)

                return web_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            web_type_1 = ScoreboardArticleLinksWebType1.from_dict(data)

            return web_type_1

        web = _parse_web(d.pop("web", UNSET))

        def _parse_mobile(data: object) -> Union["ScoreboardArticleLinksMobileType1", "ScoreboardLink", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mobile_type_0 = ScoreboardLink.from_dict(data)

                return mobile_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            mobile_type_1 = ScoreboardArticleLinksMobileType1.from_dict(data)

            return mobile_type_1

        mobile = _parse_mobile(d.pop("mobile", UNSET))

        _api = d.pop("api", UNSET)
        api: Union[Unset, ScoreboardArticleLinksApi]
        if isinstance(_api, Unset):
            api = UNSET
        else:
            api = ScoreboardArticleLinksApi.from_dict(_api)

        _sportscenter = d.pop("sportscenter", UNSET)
        sportscenter: Union[Unset, ScoreboardLink]
        if isinstance(_sportscenter, Unset):
            sportscenter = UNSET
        else:
            sportscenter = ScoreboardLink.from_dict(_sportscenter)

        scoreboard_article_links = cls(
            app=app,
            web=web,
            mobile=mobile,
            api=api,
            sportscenter=sportscenter,
        )

        scoreboard_article_links.additional_properties = d
        return scoreboard_article_links

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
