from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.news_team_links import NewsTeamLinks


T = TypeVar("T", bound="NewsTeam")


@_attrs_define
class NewsTeam:
    """
    Attributes:
        id (int): Team identifier Example: 33.
        description (str): Team name Example: Baltimore Ravens.
        links (NewsTeamLinks):
    """

    id: int
    description: str
    links: "NewsTeamLinks"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        description = self.description

        links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "description": description,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.news_team_links import NewsTeamLinks

        d = src_dict.copy()
        id = d.pop("id")

        description = d.pop("description")

        links = NewsTeamLinks.from_dict(d.pop("links"))

        news_team = cls(
            id=id,
            description=description,
            links=links,
        )

        news_team.additional_properties = d
        return news_team

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
