from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.leader_category import LeaderCategory


T = TypeVar("T", bound="TeamLeadersResponse")


@_attrs_define
class TeamLeadersResponse:
    """
    Attributes:
        ref (str): Reference URL for this team leaders data
        id (str): ID of the leaders record
        name (str): Name of the leaders record Example: Leaders.
        categories (List['LeaderCategory']):
        abbreviation (Union[Unset, str]): Abbreviation for leaders Example: LEAD.
        type (Union[Unset, str]): Type of leaders data Example: team.
    """

    ref: str
    id: str
    name: str
    categories: List["LeaderCategory"]
    abbreviation: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        id = self.id

        name = self.name

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        abbreviation = self.abbreviation

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "id": id,
                "name": name,
                "categories": categories,
            }
        )
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.leader_category import LeaderCategory

        d = src_dict.copy()
        ref = d.pop("$ref")

        id = d.pop("id")

        name = d.pop("name")

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = LeaderCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        abbreviation = d.pop("abbreviation", UNSET)

        type = d.pop("type", UNSET)

        team_leaders_response = cls(
            ref=ref,
            id=id,
            name=name,
            categories=categories,
            abbreviation=abbreviation,
            type=type,
        )

        team_leaders_response.additional_properties = d
        return team_leaders_response

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
