from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reference import Reference
    from ..models.split_stats import SplitStats


T = TypeVar("T", bound="StatCorrection")


@_attrs_define
class StatCorrection:
    """A statistical correction record for an athlete in a specific competition.

    Attributes:
        split_stats (SplitStats): Statistical split information containing categories of stats.
        competition (Reference):
        athlete (Reference):
        team (Reference):
    """

    split_stats: "SplitStats"
    competition: "Reference"
    athlete: "Reference"
    team: "Reference"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        split_stats = self.split_stats.to_dict()

        competition = self.competition.to_dict()

        athlete = self.athlete.to_dict()

        team = self.team.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "splitStats": split_stats,
                "competition": competition,
                "athlete": athlete,
                "team": team,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference
        from ..models.split_stats import SplitStats

        d = src_dict.copy()
        split_stats = SplitStats.from_dict(d.pop("splitStats"))

        competition = Reference.from_dict(d.pop("competition"))

        athlete = Reference.from_dict(d.pop("athlete"))

        team = Reference.from_dict(d.pop("team"))

        stat_correction = cls(
            split_stats=split_stats,
            competition=competition,
            athlete=athlete,
            team=team,
        )

        stat_correction.additional_properties = d
        return stat_correction

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
