from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.news_web_mobile_links import NewsWebMobileLinks


T = TypeVar("T", bound="NewsTeamLinks")


@_attrs_define
class NewsTeamLinks:
    """
    Attributes:
        web (Union['NewsWebMobileLinks', str]):
        mobile (Union['NewsWebMobileLinks', str]):
    """

    web: Union["NewsWebMobileLinks", str]
    mobile: Union["NewsWebMobileLinks", str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.news_web_mobile_links import NewsWebMobileLinks

        web: Union[Dict[str, Any], str]
        if isinstance(self.web, NewsWebMobileLinks):
            web = self.web.to_dict()
        else:
            web = self.web

        mobile: Union[Dict[str, Any], str]
        if isinstance(self.mobile, NewsWebMobileLinks):
            mobile = self.mobile.to_dict()
        else:
            mobile = self.mobile

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "web": web,
                "mobile": mobile,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.news_web_mobile_links import NewsWebMobileLinks

        d = src_dict.copy()

        def _parse_web(data: object) -> Union["NewsWebMobileLinks", str]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                web_type_0 = NewsWebMobileLinks.from_dict(data)

                return web_type_0
            except:  # noqa: E722
                pass
            return cast(Union["NewsWebMobileLinks", str], data)

        web = _parse_web(d.pop("web"))

        def _parse_mobile(data: object) -> Union["NewsWebMobileLinks", str]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mobile_type_0 = NewsWebMobileLinks.from_dict(data)

                return mobile_type_0
            except:  # noqa: E722
                pass
            return cast(Union["NewsWebMobileLinks", str], data)

        mobile = _parse_mobile(d.pop("mobile"))

        news_team_links = cls(
            web=web,
            mobile=mobile,
        )

        news_team_links.additional_properties = d
        return news_team_links

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
