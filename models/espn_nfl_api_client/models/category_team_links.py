from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_team_links_mobile import CategoryTeamLinksMobile
    from ..models.category_team_links_web import CategoryTeamLinksWeb


T = TypeVar("T", bound="CategoryTeamLinks")


@_attrs_define
class CategoryTeamLinks:
    """
    Attributes:
        web (Union[Unset, CategoryTeamLinksWeb]):
        mobile (Union[Unset, CategoryTeamLinksMobile]):
    """

    web: Union[Unset, "CategoryTeamLinksWeb"] = UNSET
    mobile: Union[Unset, "CategoryTeamLinksMobile"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        web: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.web, Unset):
            web = self.web.to_dict()

        mobile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mobile, Unset):
            mobile = self.mobile.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if web is not UNSET:
            field_dict["web"] = web
        if mobile is not UNSET:
            field_dict["mobile"] = mobile

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.category_team_links_mobile import CategoryTeamLinksMobile
        from ..models.category_team_links_web import CategoryTeamLinksWeb

        d = src_dict.copy()
        _web = d.pop("web", UNSET)
        web: Union[Unset, CategoryTeamLinksWeb]
        if isinstance(_web, Unset):
            web = UNSET
        else:
            web = CategoryTeamLinksWeb.from_dict(_web)

        _mobile = d.pop("mobile", UNSET)
        mobile: Union[Unset, CategoryTeamLinksMobile]
        if isinstance(_mobile, Unset):
            mobile = UNSET
        else:
            mobile = CategoryTeamLinksMobile.from_dict(_mobile)

        category_team_links = cls(
            web=web,
            mobile=mobile,
        )

        category_team_links.additional_properties = d
        return category_team_links

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
