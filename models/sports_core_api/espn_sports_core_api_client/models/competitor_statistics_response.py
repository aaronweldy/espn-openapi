from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference import Reference
    from ..models.statistics_splits import StatisticsSplits


T = TypeVar("T", bound="CompetitorStatisticsResponse")


@_attrs_define
class CompetitorStatisticsResponse:
    """
    Attributes:
        ref (str): Reference URL for these statistics
        splits (StatisticsSplits):
        competition (Union[Unset, Reference]):
        team (Union[Unset, Reference]):
    """

    ref: str
    splits: "StatisticsSplits"
    competition: Union[Unset, "Reference"] = UNSET
    team: Union[Unset, "Reference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        splits = self.splits.to_dict()

        competition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.competition, Unset):
            competition = self.competition.to_dict()

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "splits": splits,
            }
        )
        if competition is not UNSET:
            field_dict["competition"] = competition
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference
        from ..models.statistics_splits import StatisticsSplits

        d = src_dict.copy()
        ref = d.pop("$ref")

        splits = StatisticsSplits.from_dict(d.pop("splits"))

        _competition = d.pop("competition", UNSET)
        competition: Union[Unset, Reference]
        if isinstance(_competition, Unset):
            competition = UNSET
        else:
            competition = Reference.from_dict(_competition)

        _team = d.pop("team", UNSET)
        team: Union[Unset, Reference]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = Reference.from_dict(_team)

        competitor_statistics_response = cls(
            ref=ref,
            splits=splits,
            competition=competition,
            team=team,
        )

        competitor_statistics_response.additional_properties = d
        return competitor_statistics_response

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
