from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.predictor_statistic import PredictorStatistic
    from ..models.reference import Reference


T = TypeVar("T", bound="PredictorTeam")


@_attrs_define
class PredictorTeam:
    """
    Attributes:
        team (Reference):
        statistics (Union[Unset, List['PredictorStatistic']]):
    """

    team: "Reference"
    statistics: Union[Unset, List["PredictorStatistic"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team = self.team.to_dict()

        statistics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = []
            for statistics_item_data in self.statistics:
                statistics_item = statistics_item_data.to_dict()
                statistics.append(statistics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team": team,
            }
        )
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.predictor_statistic import PredictorStatistic
        from ..models.reference import Reference

        d = src_dict.copy()
        team = Reference.from_dict(d.pop("team"))

        statistics = []
        _statistics = d.pop("statistics", UNSET)
        for statistics_item_data in _statistics or []:
            statistics_item = PredictorStatistic.from_dict(statistics_item_data)

            statistics.append(statistics_item)

        predictor_team = cls(
            team=team,
            statistics=statistics,
        )

        predictor_team.additional_properties = d
        return predictor_team

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
