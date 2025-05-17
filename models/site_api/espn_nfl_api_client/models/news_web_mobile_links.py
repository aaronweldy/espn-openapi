from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.news_link_item import NewsLinkItem


T = TypeVar("T", bound="NewsWebMobileLinks")


@_attrs_define
class NewsWebMobileLinks:
    """
    Attributes:
        athletes (Union[Unset, NewsLinkItem]):
        teams (Union[Unset, NewsLinkItem]):
        leagues (Union[Unset, NewsLinkItem]):
    """

    athletes: Union[Unset, "NewsLinkItem"] = UNSET
    teams: Union[Unset, "NewsLinkItem"] = UNSET
    leagues: Union[Unset, "NewsLinkItem"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        athletes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.athletes, Unset):
            athletes = self.athletes.to_dict()

        teams: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = self.teams.to_dict()

        leagues: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.leagues, Unset):
            leagues = self.leagues.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if athletes is not UNSET:
            field_dict["athletes"] = athletes
        if teams is not UNSET:
            field_dict["teams"] = teams
        if leagues is not UNSET:
            field_dict["leagues"] = leagues

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.news_link_item import NewsLinkItem

        d = src_dict.copy()
        _athletes = d.pop("athletes", UNSET)
        athletes: Union[Unset, NewsLinkItem]
        if isinstance(_athletes, Unset):
            athletes = UNSET
        else:
            athletes = NewsLinkItem.from_dict(_athletes)

        _teams = d.pop("teams", UNSET)
        teams: Union[Unset, NewsLinkItem]
        if isinstance(_teams, Unset):
            teams = UNSET
        else:
            teams = NewsLinkItem.from_dict(_teams)

        _leagues = d.pop("leagues", UNSET)
        leagues: Union[Unset, NewsLinkItem]
        if isinstance(_leagues, Unset):
            leagues = UNSET
        else:
            leagues = NewsLinkItem.from_dict(_leagues)

        news_web_mobile_links = cls(
            athletes=athletes,
            teams=teams,
            leagues=leagues,
        )

        news_web_mobile_links.additional_properties = d
        return news_web_mobile_links

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
