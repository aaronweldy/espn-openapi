from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.nfl_team_depthchart_group_positions import NflTeamDepthchartGroupPositions


T = TypeVar("T", bound="NflTeamDepthchartGroup")


@_attrs_define
class NflTeamDepthchartGroup:
    """
    Attributes:
        name (str):
        positions (NflTeamDepthchartGroupPositions):
    """

    name: str
    positions: "NflTeamDepthchartGroupPositions"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        positions = self.positions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "positions": positions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_team_depthchart_group_positions import NflTeamDepthchartGroupPositions

        d = src_dict.copy()
        name = d.pop("name")

        positions = NflTeamDepthchartGroupPositions.from_dict(d.pop("positions"))

        nfl_team_depthchart_group = cls(
            name=name,
            positions=positions,
        )

        nfl_team_depthchart_group.additional_properties = d
        return nfl_team_depthchart_group

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
