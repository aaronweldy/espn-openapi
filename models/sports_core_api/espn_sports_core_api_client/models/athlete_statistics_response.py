from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.athlete_reference import AthleteReference
    from ..models.athlete_statistics_response_splits import AthleteStatisticsResponseSplits
    from ..models.season import Season


T = TypeVar("T", bound="AthleteStatisticsResponse")


@_attrs_define
class AthleteStatisticsResponse:
    """
    Attributes:
        athlete (AthleteReference):
        splits (AthleteStatisticsResponseSplits):
        season (Union[Unset, Season]):
    """

    athlete: "AthleteReference"
    splits: "AthleteStatisticsResponseSplits"
    season: Union[Unset, "Season"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        athlete = self.athlete.to_dict()

        splits = self.splits.to_dict()

        season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "athlete": athlete,
                "splits": splits,
            }
        )
        if season is not UNSET:
            field_dict["season"] = season

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_reference import AthleteReference
        from ..models.athlete_statistics_response_splits import AthleteStatisticsResponseSplits
        from ..models.season import Season

        d = src_dict.copy()
        athlete = AthleteReference.from_dict(d.pop("athlete"))

        splits = AthleteStatisticsResponseSplits.from_dict(d.pop("splits"))

        _season = d.pop("season", UNSET)
        season: Union[Unset, Season]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = Season.from_dict(_season)

        athlete_statistics_response = cls(
            athlete=athlete,
            splits=splits,
            season=season,
        )

        athlete_statistics_response.additional_properties = d
        return athlete_statistics_response

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
