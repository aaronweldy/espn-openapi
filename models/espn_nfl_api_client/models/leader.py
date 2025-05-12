from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.leader_category import LeaderCategory
    from ..models.team import Team


T = TypeVar("T", bound="Leader")


@_attrs_define
class Leader:
    """
    Attributes:
        team (Union[Unset, Team]):
        leaders (Union[Unset, list['LeaderCategory']]):
    """

    team: Union[Unset, "Team"] = UNSET
    leaders: Union[Unset, list["LeaderCategory"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        leaders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.leaders, Unset):
            leaders = []
            for leaders_item_data in self.leaders:
                leaders_item = leaders_item_data.to_dict()
                leaders.append(leaders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team is not UNSET:
            field_dict["team"] = team
        if leaders is not UNSET:
            field_dict["leaders"] = leaders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.leader_category import LeaderCategory
        from ..models.team import Team

        d = dict(src_dict)
        _team = d.pop("team", UNSET)
        team: Union[Unset, Team]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = Team.from_dict(_team)

        leaders = []
        _leaders = d.pop("leaders", UNSET)
        for leaders_item_data in _leaders or []:
            leaders_item = LeaderCategory.from_dict(leaders_item_data)

            leaders.append(leaders_item)

        leader = cls(
            team=team,
            leaders=leaders,
        )

        leader.additional_properties = d
        return leader

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
