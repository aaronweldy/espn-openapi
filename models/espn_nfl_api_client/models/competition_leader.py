from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.leader_performance import LeaderPerformance


T = TypeVar("T", bound="CompetitionLeader")


@_attrs_define
class CompetitionLeader:
    """
    Attributes:
        name (str):  Example: passingYards.
        display_name (str):  Example: Passing Leader.
        leaders (list['LeaderPerformance']):
        short_display_name (Union[Unset, str]):  Example: PASS.
        abbreviation (Union[Unset, str]):  Example: PYDS.
    """

    name: str
    display_name: str
    leaders: list["LeaderPerformance"]
    short_display_name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name = self.display_name

        leaders = []
        for leaders_item_data in self.leaders:
            leaders_item = leaders_item_data.to_dict()
            leaders.append(leaders_item)

        short_display_name = self.short_display_name

        abbreviation = self.abbreviation

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.leader_performance import LeaderPerformance

        d = dict(src_dict)
        name = d.pop("name")

        display_name = d.pop("displayName")

        leaders = []
        _leaders = d.pop("leaders")
        for leaders_item_data in _leaders:
            leaders_item = LeaderPerformance.from_dict(leaders_item_data)

            leaders.append(leaders_item)

        short_display_name = d.pop("shortDisplayName", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        competition_leader = cls(
            name=name,
            display_name=display_name,
            leaders=leaders,
            short_display_name=short_display_name,
            abbreviation=abbreviation,
        )

        competition_leader.additional_properties = d
        return competition_leader

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
