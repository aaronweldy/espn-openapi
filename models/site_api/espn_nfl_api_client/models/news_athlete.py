from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.news_athlete_links import NewsAthleteLinks


T = TypeVar("T", bound="NewsAthlete")


@_attrs_define
class NewsAthlete:
    """
    Attributes:
        id (int): Athlete identifier Example: 15846.
        description (str): Athlete name Example: John Jenkins.
        links (NewsAthleteLinks):
    """

    id: int
    description: str
    links: "NewsAthleteLinks"
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
        from ..models.news_athlete_links import NewsAthleteLinks

        d = src_dict.copy()
        id = d.pop("id")

        description = d.pop("description")

        links = NewsAthleteLinks.from_dict(d.pop("links"))

        news_athlete = cls(
            id=id,
            description=description,
            links=links,
        )

        news_athlete.additional_properties = d
        return news_athlete

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
