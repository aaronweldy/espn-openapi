from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.nfl_team_depthchart_athlete import NflTeamDepthchartAthlete
    from ..models.nfl_team_depthchart_position import NflTeamDepthchartPosition


T = TypeVar("T", bound="NflTeamDepthchartPositionValue")


@_attrs_define
class NflTeamDepthchartPositionValue:
    """
    Attributes:
        position (NflTeamDepthchartPosition):
        athletes (List['NflTeamDepthchartAthlete']):
    """

    position: "NflTeamDepthchartPosition"
    athletes: List["NflTeamDepthchartAthlete"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position.to_dict()

        athletes = []
        for athletes_item_data in self.athletes:
            athletes_item = athletes_item_data.to_dict()
            athletes.append(athletes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "athletes": athletes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_team_depthchart_athlete import NflTeamDepthchartAthlete
        from ..models.nfl_team_depthchart_position import NflTeamDepthchartPosition

        d = src_dict.copy()
        position = NflTeamDepthchartPosition.from_dict(d.pop("position"))

        athletes = []
        _athletes = d.pop("athletes")
        for athletes_item_data in _athletes:
            athletes_item = NflTeamDepthchartAthlete.from_dict(athletes_item_data)

            athletes.append(athletes_item)

        nfl_team_depthchart_position_value = cls(
            position=position,
            athletes=athletes,
        )

        nfl_team_depthchart_position_value.additional_properties = d
        return nfl_team_depthchart_position_value

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
