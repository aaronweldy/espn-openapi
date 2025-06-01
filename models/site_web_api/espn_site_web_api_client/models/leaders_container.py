from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.leader_category import LeaderCategory


T = TypeVar("T", bound="LeadersContainer")


@_attrs_define
class LeadersContainer:
    """
    Attributes:
        id (str): Leaders container ID
        name (str): Leaders container name
        abbreviation (str): Leaders container abbreviation
        categories (List['LeaderCategory']):
    """

    id: str
    name: str
    abbreviation: str
    categories: List["LeaderCategory"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        abbreviation = self.abbreviation

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "abbreviation": abbreviation,
                "categories": categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.leader_category import LeaderCategory

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        abbreviation = d.pop("abbreviation")

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = LeaderCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        leaders_container = cls(
            id=id,
            name=name,
            abbreviation=abbreviation,
            categories=categories,
        )

        leaders_container.additional_properties = d
        return leaders_container

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
