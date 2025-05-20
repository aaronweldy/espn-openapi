from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.competition_leader import CompetitionLeader


T = TypeVar("T", bound="CompetitionLeadersCategory")


@_attrs_define
class CompetitionLeadersCategory:
    """
    Attributes:
        name (str):
        display_name (str):
        short_display_name (str):
        abbreviation (str):
        leaders (List['CompetitionLeader']):
    """

    name: str
    display_name: str
    short_display_name: str
    abbreviation: str
    leaders: List["CompetitionLeader"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        short_display_name = self.short_display_name

        abbreviation = self.abbreviation

        leaders = []
        for leaders_item_data in self.leaders:
            leaders_item = leaders_item_data.to_dict()
            leaders.append(leaders_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "displayName": display_name,
                "shortDisplayName": short_display_name,
                "abbreviation": abbreviation,
                "leaders": leaders,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.competition_leader import CompetitionLeader

        d = src_dict.copy()
        name = d.pop("name")

        display_name = d.pop("displayName")

        short_display_name = d.pop("shortDisplayName")

        abbreviation = d.pop("abbreviation")

        leaders = []
        _leaders = d.pop("leaders")
        for leaders_item_data in _leaders:
            leaders_item = CompetitionLeader.from_dict(leaders_item_data)

            leaders.append(leaders_item)

        competition_leaders_category = cls(
            name=name,
            display_name=display_name,
            short_display_name=short_display_name,
            abbreviation=abbreviation,
            leaders=leaders,
        )

        competition_leaders_category.additional_properties = d
        return competition_leaders_category

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
