from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.nfl_draft_position import NflDraftPosition
    from ..models.nfl_draft_team import NflDraftTeam


T = TypeVar("T", bound="NflDraftTeamNeed")


@_attrs_define
class NflDraftTeamNeed:
    """
    Attributes:
        team (NflDraftTeam):
        positions (List['NflDraftPosition']):
    """

    team: "NflDraftTeam"
    positions: List["NflDraftPosition"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team = self.team.to_dict()

        positions = []
        for positions_item_data in self.positions:
            positions_item = positions_item_data.to_dict()
            positions.append(positions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team": team,
                "positions": positions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_draft_position import NflDraftPosition
        from ..models.nfl_draft_team import NflDraftTeam

        d = src_dict.copy()
        team = NflDraftTeam.from_dict(d.pop("team"))

        positions = []
        _positions = d.pop("positions")
        for positions_item_data in _positions:
            positions_item = NflDraftPosition.from_dict(positions_item_data)

            positions.append(positions_item)

        nfl_draft_team_need = cls(
            team=team,
            positions=positions,
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
