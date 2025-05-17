from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference import Reference


T = TypeVar("T", bound="NflDraftTeamNeed")


@_attrs_define
class NflDraftTeamNeed:
    """
    Attributes:
        team (Reference):
        need (str):
        rank (int):
        description (str):
        position (Union[Unset, Reference]):
    """

    team: "Reference"
    need: str
    rank: int
    description: str
    position: Union[Unset, "Reference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team = self.team.to_dict()

        need = self.need

        rank = self.rank

        description = self.description

        position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team": team,
                "need": need,
                "rank": rank,
                "description": description,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference

        d = src_dict.copy()
        team = Reference.from_dict(d.pop("team"))

        need = d.pop("need")

        rank = d.pop("rank")

        description = d.pop("description")

        _position = d.pop("position", UNSET)
        position: Union[Unset, Reference]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = Reference.from_dict(_position)

        nfl_draft_team_need = cls(
            team=team,
            need=need,
            rank=rank,
            description=description,
            position=position,
        )

        nfl_draft_team_need.additional_properties = d
        return nfl_draft_team_need

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
