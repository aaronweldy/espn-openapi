from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleTeam")


@_attrs_define
class ScheduleTeam:
    """
    Attributes:
        team_id (int): Team ID Example: 1.
        total_points (Union[Unset, float]): Total points scored Example: 108.5.
        total_points_live (Union[Unset, float]): Live points total Example: 108.5.
    """

    team_id: int
    total_points: Union[Unset, float] = UNSET
    total_points_live: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team_id = self.team_id

        total_points = self.total_points

        total_points_live = self.total_points_live

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "teamId": team_id,
            }
        )
        if total_points is not UNSET:
            field_dict["totalPoints"] = total_points
        if total_points_live is not UNSET:
            field_dict["totalPointsLive"] = total_points_live

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        team_id = d.pop("teamId")

        total_points = d.pop("totalPoints", UNSET)

        total_points_live = d.pop("totalPointsLive", UNSET)

        schedule_team = cls(
            team_id=team_id,
            total_points=total_points,
            total_points_live=total_points_live,
        )

        schedule_team.additional_properties = d
        return schedule_team

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
