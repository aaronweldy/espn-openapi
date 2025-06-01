from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.team_leader_category import TeamLeaderCategory


T = TypeVar("T", bound="TeamLeadersContainer")


@_attrs_define
class TeamLeadersContainer:
    """
    Attributes:
        abbreviation (str): Abbreviation for the leaders container (e.g., "Total")
        id (str): ID for the leaders container
        name (str): Name of the leaders container
        categories (List['TeamLeaderCategory']): Array of statistical categories
    """

    abbreviation: str
    id: str
    name: str
    categories: List["TeamLeaderCategory"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        abbreviation = self.abbreviation

        id = self.id

        name = self.name

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "abbreviation": abbreviation,
                "id": id,
                "name": name,
                "categories": categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_leader_category import TeamLeaderCategory

        d = src_dict.copy()
        abbreviation = d.pop("abbreviation")

        id = d.pop("id")

        name = d.pop("name")

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = TeamLeaderCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        team_leaders_container = cls(
            abbreviation=abbreviation,
            id=id,
            name=name,
            categories=categories,
        )

        team_leaders_container.additional_properties = d
        return team_leaders_container

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
