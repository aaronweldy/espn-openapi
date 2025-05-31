from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ranked_team import RankedTeam


T = TypeVar("T", bound="DroppedOutTeam")


@_attrs_define
class DroppedOutTeam:
    """Team that dropped out of rankings

    Attributes:
        team (Union[Unset, RankedTeam]): Team information in rankings
        previous (Union[Unset, int]): Previous ranking before dropping out
    """

    team: Union[Unset, "RankedTeam"] = UNSET
    previous: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        previous = self.previous

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team is not UNSET:
            field_dict["team"] = team
        if previous is not UNSET:
            field_dict["previous"] = previous

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ranked_team import RankedTeam

        d = src_dict.copy()
        _team = d.pop("team", UNSET)
        team: Union[Unset, RankedTeam]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = RankedTeam.from_dict(_team)

        previous = d.pop("previous", UNSET)

        dropped_out_team = cls(
            team=team,
            previous=previous,
        )

        dropped_out_team.additional_properties = d
        return dropped_out_team

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
