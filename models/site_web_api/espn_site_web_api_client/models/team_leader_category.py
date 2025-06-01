from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.team_leader_entry import TeamLeaderEntry


T = TypeVar("T", bound="TeamLeaderCategory")


@_attrs_define
class TeamLeaderCategory:
    """
    Attributes:
        display_name (str): Display name for the category
        name (str): Internal name for the category
        abbreviation (str): Abbreviation for the category
        leaders (List['TeamLeaderEntry']): Array of team leaders for this category
    """

    display_name: str
    name: str
    abbreviation: str
    leaders: List["TeamLeaderEntry"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name

        name = self.name

        abbreviation = self.abbreviation

        leaders = []
        for leaders_item_data in self.leaders:
            leaders_item = leaders_item_data.to_dict()
            leaders.append(leaders_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "name": name,
                "abbreviation": abbreviation,
                "leaders": leaders,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_leader_entry import TeamLeaderEntry

        d = src_dict.copy()
        display_name = d.pop("displayName")

        name = d.pop("name")

        abbreviation = d.pop("abbreviation")

        leaders = []
        _leaders = d.pop("leaders")
        for leaders_item_data in _leaders:
            leaders_item = TeamLeaderEntry.from_dict(leaders_item_data)

            leaders.append(leaders_item)

        team_leader_category = cls(
            display_name=display_name,
            name=name,
            abbreviation=abbreviation,
            leaders=leaders,
        )

        team_leader_category.additional_properties = d
        return team_leader_category

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
