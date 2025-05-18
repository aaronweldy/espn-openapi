from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="WebMobileLinks")


@_attrs_define
class WebMobileLinks:
    """
    Attributes:
        athletes (Union[Unset, Link]):
        teams (Union[Unset, Link]):
        leagues (Union[Unset, Link]):
        web (Union['Link', Unset, str]):
        mobile (Union['Link', Unset, str]):
    """

    athletes: Union[Unset, "Link"] = UNSET
    teams: Union[Unset, "Link"] = UNSET
    leagues: Union[Unset, "Link"] = UNSET
    web: Union["Link", Unset, str] = UNSET
    mobile: Union["Link", Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.link import Link

        athletes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.athletes, Unset):
            athletes = self.athletes.to_dict()

        teams: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = self.teams.to_dict()

        leagues: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.leagues, Unset):
            leagues = self.leagues.to_dict()

        web: Union[Dict[str, Any], Unset, str]
        if isinstance(self.web, Unset):
            web = UNSET
        elif isinstance(self.web, Link):
            web = self.web.to_dict()
        else:
            web = self.web

        mobile: Union[Dict[str, Any], Unset, str]
        if isinstance(self.mobile, Unset):
            mobile = UNSET
        elif isinstance(self.mobile, Link):
            mobile = self.mobile.to_dict()
        else:
            mobile = self.mobile

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if athletes is not UNSET:
            field_dict["athletes"] = athletes
        if teams is not UNSET:
            field_dict["teams"] = teams
        if leagues is not UNSET:
            field_dict["leagues"] = leagues
        if web is not UNSET:
            field_dict["web"] = web
        if mobile is not UNSET:
            field_dict["mobile"] = mobile

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        _athletes = d.pop("athletes", UNSET)
        athletes: Union[Unset, Link]
        if isinstance(_athletes, Unset):
            athletes = UNSET
        else:
            athletes = Link.from_dict(_athletes)

        _teams = d.pop("teams", UNSET)
        teams: Union[Unset, Link]
        if isinstance(_teams, Unset):
            teams = UNSET
        else:
            teams = Link.from_dict(_teams)

        _leagues = d.pop("leagues", UNSET)
        leagues: Union[Unset, Link]
        if isinstance(_leagues, Unset):
            leagues = UNSET
        else:
            leagues = Link.from_dict(_leagues)

        def _parse_web(data: object) -> Union["Link", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                web_type_0 = Link.from_dict(data)

                return web_type_0
            except:  # noqa: E722
                pass
            return cast(Union["Link", Unset, str], data)

        web = _parse_web(d.pop("web", UNSET))

        def _parse_mobile(data: object) -> Union["Link", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mobile_type_0 = Link.from_dict(data)

                return mobile_type_0
            except:  # noqa: E722
                pass
            return cast(Union["Link", Unset, str], data)

        mobile = _parse_mobile(d.pop("mobile", UNSET))

        web_mobile_links = cls(
            athletes=athletes,
            teams=teams,
            leagues=leagues,
            web=web,
            mobile=mobile,
        )

        web_mobile_links.additional_properties = d
        return web_mobile_links

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
