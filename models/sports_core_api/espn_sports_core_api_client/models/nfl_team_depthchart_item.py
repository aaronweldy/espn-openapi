from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.nfl_team_depthchart_item_positions import NflTeamDepthchartItemPositions


T = TypeVar("T", bound="NflTeamDepthchartItem")


@_attrs_define
class NflTeamDepthchartItem:
    """
    Attributes:
        id (str):
        name (str):
        positions (NflTeamDepthchartItemPositions):
    """

    id: str
    name: str
    positions: "NflTeamDepthchartItemPositions"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        positions = self.positions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "positions": positions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_team_depthchart_item_positions import NflTeamDepthchartItemPositions

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        positions = NflTeamDepthchartItemPositions.from_dict(d.pop("positions"))

        nfl_team_depthchart_item = cls(
            id=id,
            name=name,
            positions=positions,
        )

        nfl_team_depthchart_item.additional_properties = d
        return nfl_team_depthchart_item

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
