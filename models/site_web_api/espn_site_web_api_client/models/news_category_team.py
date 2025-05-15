from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.news_category_team_links import NewsCategoryTeamLinks


T = TypeVar("T", bound="NewsCategoryTeam")


@_attrs_define
class NewsCategoryTeam:
    """
    Attributes:
        id (Union[Unset, int]):
        links (Union[Unset, NewsCategoryTeamLinks]):
    """

    id: Union[Unset, int] = UNSET
    links: Union[Unset, "NewsCategoryTeamLinks"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.news_category_team_links import NewsCategoryTeamLinks

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, NewsCategoryTeamLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = NewsCategoryTeamLinks.from_dict(_links)

        news_category_team = cls(
            id=id,
            links=links,
        )

        news_category_team.additional_properties = d
        return news_category_team

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
