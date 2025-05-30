from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reference import Reference


T = TypeVar("T", bound="NflTeamDepthchartAthlete")


@_attrs_define
class NflTeamDepthchartAthlete:
    """
    Attributes:
        rank (int):
        slot (int):
        athlete (Reference):
    """

    rank: int
    slot: int
    athlete: "Reference"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rank = self.rank

        slot = self.slot

        athlete = self.athlete.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rank": rank,
                "slot": slot,
                "athlete": athlete,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference

        d = src_dict.copy()
        rank = d.pop("rank")

        slot = d.pop("slot")

        athlete = Reference.from_dict(d.pop("athlete"))

        nfl_team_depthchart_athlete = cls(
            rank=rank,
            slot=slot,
            athlete=athlete,
        )

        nfl_team_depthchart_athlete.additional_properties = d
        return nfl_team_depthchart_athlete

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
