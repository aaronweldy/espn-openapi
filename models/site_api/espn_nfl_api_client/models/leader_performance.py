from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.athlete import Athlete
    from ..models.team import Team


T = TypeVar("T", bound="LeaderPerformance")


@_attrs_define
class LeaderPerformance:
    """
    Attributes:
        display_value (str):  Example: 21/32, 257 YDS, 3 TD, 2 INT.
        value (float):  Example: 257.0.
        athlete (Athlete):
        team (Union[Unset, Team]):
    """

    display_value: str
    value: float
    athlete: "Athlete"
    team: Union[Unset, "Team"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_value = self.display_value

        value = self.value

        athlete = self.athlete.to_dict()

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayValue": display_value,
                "value": value,
                "athlete": athlete,
            }
        )
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete import Athlete
        from ..models.team import Team

        d = src_dict.copy()
        display_value = d.pop("displayValue")

        value = d.pop("value")

        athlete = Athlete.from_dict(d.pop("athlete"))

        _team = d.pop("team", UNSET)
        team: Union[Unset, Team]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = Team.from_dict(_team)

        leader_performance = cls(
            display_value=display_value,
            value=value,
            athlete=athlete,
            team=team,
        )

        leader_performance.additional_properties = d
        return leader_performance

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
