from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.athlete import Athlete
    from ..models.team import Team


T = TypeVar("T", bound="LeaderEntry")


@_attrs_define
class LeaderEntry:
    """
    Attributes:
        display_value (Union[Unset, str]):
        value (Union[Unset, float]):
        athlete (Union[Unset, Athlete]):
        team (Union[Unset, Team]):
    """

    display_value: Union[Unset, str] = UNSET
    value: Union[Unset, float] = UNSET
    athlete: Union[Unset, "Athlete"] = UNSET
    team: Union[Unset, "Team"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_value = self.display_value

        value = self.value

        athlete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.athlete, Unset):
            athlete = self.athlete.to_dict()

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value
        if value is not UNSET:
            field_dict["value"] = value
        if athlete is not UNSET:
            field_dict["athlete"] = athlete
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete import Athlete
        from ..models.team import Team

        d = src_dict.copy()
        display_value = d.pop("displayValue", UNSET)

        value = d.pop("value", UNSET)

        _athlete = d.pop("athlete", UNSET)
        athlete: Union[Unset, Athlete]
        if isinstance(_athlete, Unset):
            athlete = UNSET
        else:
            athlete = Athlete.from_dict(_athlete)

        _team = d.pop("team", UNSET)
        team: Union[Unset, Team]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = Team.from_dict(_team)

        leader_entry = cls(
            display_value=display_value,
            value=value,
            athlete=athlete,
            team=team,
        )

        leader_entry.additional_properties = d
        return leader_entry

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
