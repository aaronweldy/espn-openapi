from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_leader import TeamLeader


T = TypeVar("T", bound="LeaderCategory")


@_attrs_define
class LeaderCategory:
    """
    Attributes:
        name (str): Category name (e.g., passingLeader, pointsPerGame) Example: passingLeader.
        display_name (str): Display name for the category Example: Passing Leader.
        leaders (List['TeamLeader']):
        short_display_name (Union[Unset, str]): Short display name Example: Pass.
        abbreviation (Union[Unset, str]): Category abbreviation Example: PASS.
    """

    name: str
    display_name: str
    leaders: List["TeamLeader"]
    short_display_name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        leaders = []
        for leaders_item_data in self.leaders:
            leaders_item = leaders_item_data.to_dict()
            leaders.append(leaders_item)

        short_display_name = self.short_display_name

        abbreviation = self.abbreviation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "displayName": display_name,
                "leaders": leaders,
            }
        )
        if short_display_name is not UNSET:
            field_dict["shortDisplayName"] = short_display_name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_leader import TeamLeader

        d = src_dict.copy()
        name = d.pop("name")

        display_name = d.pop("displayName")

        leaders = []
        _leaders = d.pop("leaders")
        for leaders_item_data in _leaders:
            leaders_item = TeamLeader.from_dict(leaders_item_data)

            leaders.append(leaders_item)

        short_display_name = d.pop("shortDisplayName", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        leader_category = cls(
            name=name,
            display_name=display_name,
            leaders=leaders,
            short_display_name=short_display_name,
            abbreviation=abbreviation,
        )

        leader_category.additional_properties = d
        return leader_category

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
