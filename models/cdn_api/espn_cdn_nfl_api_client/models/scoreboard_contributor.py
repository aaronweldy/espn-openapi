from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_contributor_links import ScoreboardContributorLinks


T = TypeVar("T", bound="ScoreboardContributor")


@_attrs_define
class ScoreboardContributor:
    """
    Attributes:
        description (Union[Unset, str]):
        links (Union[Unset, ScoreboardContributorLinks]):
        id (Union[Unset, int]):
    """

    description: Union[Unset, str] = UNSET
    links: Union[Unset, "ScoreboardContributorLinks"] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if links is not UNSET:
            field_dict["links"] = links
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_contributor_links import ScoreboardContributorLinks

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ScoreboardContributorLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ScoreboardContributorLinks.from_dict(_links)

        id = d.pop("id", UNSET)

        scoreboard_contributor = cls(
            description=description,
            links=links,
            id=id,
        )

        scoreboard_contributor.additional_properties = d
        return scoreboard_contributor

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
