from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.href_link import HrefLink
    from ..models.self_link import SelfLink


T = TypeVar("T", bound="NewsLinks")


@_attrs_define
class NewsLinks:
    """
    Attributes:
        api (Union[Unset, SelfLink]):
        mobile (Union[Unset, HrefLink]):
        web (Union[Unset, HrefLink]):
    """

    api: Union[Unset, "SelfLink"] = UNSET
    mobile: Union[Unset, "HrefLink"] = UNSET
    web: Union[Unset, "HrefLink"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.api, Unset):
            api = self.api.to_dict()

        mobile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mobile, Unset):
            mobile = self.mobile.to_dict()

        web: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.web, Unset):
            web = self.web.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api is not UNSET:
            field_dict["api"] = api
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if web is not UNSET:
            field_dict["web"] = web

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href_link import HrefLink
        from ..models.self_link import SelfLink

        d = src_dict.copy()
        _api = d.pop("api", UNSET)
        api: Union[Unset, SelfLink]
        if isinstance(_api, Unset):
            api = UNSET
        else:
            api = SelfLink.from_dict(_api)

        _mobile = d.pop("mobile", UNSET)
        mobile: Union[Unset, HrefLink]
        if isinstance(_mobile, Unset):
            mobile = UNSET
        else:
            mobile = HrefLink.from_dict(_mobile)

        _web = d.pop("web", UNSET)
        web: Union[Unset, HrefLink]
        if isinstance(_web, Unset):
            web = UNSET
        else:
            web = HrefLink.from_dict(_web)

        news_links = cls(
            api=api,
            mobile=mobile,
            web=web,
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
