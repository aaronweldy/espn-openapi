from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_contributor_links import CategoryContributorLinks


T = TypeVar("T", bound="CategoryContributor")


@_attrs_define
class CategoryContributor:
    """
    Attributes:
        id (Union[Unset, int]):
        description (Union[Unset, str]):
        links (Union[Unset, CategoryContributorLinks]):
    """

    id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    links: Union[Unset, "CategoryContributorLinks"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        description = self.description

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.category_contributor_links import CategoryContributorLinks

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, CategoryContributorLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = CategoryContributorLinks.from_dict(_links)

        category_contributor = cls(
            id=id,
            description=description,
            links=links,
        )

        category_contributor.additional_properties = d
        return category_contributor

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
