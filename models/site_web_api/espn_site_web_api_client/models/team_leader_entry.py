from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_leader_team import TeamLeaderTeam


T = TypeVar("T", bound="TeamLeaderEntry")


@_attrs_define
class TeamLeaderEntry:
    """
    Attributes:
        display_value (str): Display value for the statistic
        value (float): Numeric value for the statistic
        team (TeamLeaderTeam):
        ranks (Union[Unset, str]): Team's rank for this statistic
    """

    display_value: str
    value: float
    team: "TeamLeaderTeam"
    ranks: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_value = self.display_value

        value = self.value

        team = self.team.to_dict()

        ranks = self.ranks

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayValue": display_value,
                "value": value,
                "team": team,
            }
        )
        if ranks is not UNSET:
            field_dict["ranks"] = ranks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_leader_team import TeamLeaderTeam

        d = src_dict.copy()
        display_value = d.pop("displayValue")

        value = d.pop("value")

        team = TeamLeaderTeam.from_dict(d.pop("team"))

        ranks = d.pop("ranks", UNSET)

        team_leader_entry = cls(
            display_value=display_value,
            value=value,
            team=team,
            ranks=ranks,
        )

        team_leader_entry.additional_properties = d
        return team_leader_entry

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
