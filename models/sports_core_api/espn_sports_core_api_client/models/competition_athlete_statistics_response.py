from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.competition_athlete_statistics_response_splits import CompetitionAthleteStatisticsResponseSplits
    from ..models.reference import Reference


T = TypeVar("T", bound="CompetitionAthleteStatisticsResponse")


@_attrs_define
class CompetitionAthleteStatisticsResponse:
    """Statistics for a specific athlete in a competition (game).

    Attributes:
        ref (str):
        competition (Reference):
        splits (CompetitionAthleteStatisticsResponseSplits):
        athlete (Reference):
    """

    ref: str
    competition: "Reference"
    splits: "CompetitionAthleteStatisticsResponseSplits"
    athlete: "Reference"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        competition = self.competition.to_dict()

        splits = self.splits.to_dict()

        athlete = self.athlete.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "competition": competition,
                "splits": splits,
                "athlete": athlete,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.competition_athlete_statistics_response_splits import CompetitionAthleteStatisticsResponseSplits
        from ..models.reference import Reference

        d = src_dict.copy()
        ref = d.pop("$ref")

        competition = Reference.from_dict(d.pop("competition"))

        splits = CompetitionAthleteStatisticsResponseSplits.from_dict(d.pop("splits"))

        athlete = Reference.from_dict(d.pop("athlete"))

        competition_athlete_statistics_response = cls(
            ref=ref,
            competition=competition,
            splits=splits,
            athlete=athlete,
        )

        competition_athlete_statistics_response.additional_properties = d
        return competition_athlete_statistics_response

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
