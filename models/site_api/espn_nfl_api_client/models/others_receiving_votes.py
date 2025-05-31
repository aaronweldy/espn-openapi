from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ranked_team import RankedTeam


T = TypeVar("T", bound="OthersReceivingVotes")


@_attrs_define
class OthersReceivingVotes:
    """Team receiving votes but not in top 25

    Attributes:
        team (Union[Unset, RankedTeam]): Team information in rankings
        points (Union[Unset, int]): Points received
    """

    team: Union[Unset, "RankedTeam"] = UNSET
    points: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        points = self.points

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team is not UNSET:
            field_dict["team"] = team
        if points is not UNSET:
            field_dict["points"] = points

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

        points = d.pop("points", UNSET)

        others_receiving_votes = cls(
            team=team,
            points=points,
        )

        others_receiving_votes.additional_properties = d
        return others_receiving_votes

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
