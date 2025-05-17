from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.news_contributor_links import NewsContributorLinks


T = TypeVar("T", bound="NewsContributor")


@_attrs_define
class NewsContributor:
    """
    Attributes:
        id (int): Contributor identifier Example: 2078.
        description (str): Contributor name Example: Jamison Hensley.
        links (NewsContributorLinks):
    """

    id: int
    description: str
    links: "NewsContributorLinks"
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
        from ..models.news_contributor_links import NewsContributorLinks

        d = src_dict.copy()
        id = d.pop("id")

        description = d.pop("description")

        links = NewsContributorLinks.from_dict(d.pop("links"))

        news_contributor = cls(
            id=id,
            description=description,
            links=links,
        )

        news_contributor.additional_properties = d
        return news_contributor

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
