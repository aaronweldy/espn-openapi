from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reference import Reference


T = TypeVar("T", bound="CompetitionLeader")


@_attrs_define
class CompetitionLeader:
    """
    Attributes:
        display_value (str):
        value (float):
        rel (List[str]):
        athlete (Reference):
        team (Reference):
        statistics (Reference):
    """

    display_value: str
    value: float
    rel: List[str]
    athlete: "Reference"
    team: "Reference"
    statistics: "Reference"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_value = self.display_value

        value = self.value

        rel = self.rel

        athlete = self.athlete.to_dict()

        team = self.team.to_dict()

        statistics = self.statistics.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayValue": display_value,
                "value": value,
                "rel": rel,
                "athlete": athlete,
                "team": team,
                "statistics": statistics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference

        d = src_dict.copy()
        display_value = d.pop("displayValue")

        value = d.pop("value")

        rel = cast(List[str], d.pop("rel"))

        athlete = Reference.from_dict(d.pop("athlete"))

        team = Reference.from_dict(d.pop("team"))

        statistics = Reference.from_dict(d.pop("statistics"))

        competition_leader = cls(
            display_value=display_value,
            value=value,
            rel=rel,
            athlete=athlete,
            team=team,
            statistics=statistics,
        )

        competition_leader.additional_properties = d
        return competition_leader

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
