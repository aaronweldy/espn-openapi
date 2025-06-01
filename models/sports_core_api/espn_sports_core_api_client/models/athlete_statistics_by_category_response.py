from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.athlete_reference import AthleteReference
    from ..models.athlete_statistics_by_category_response_splits import AthleteStatisticsByCategoryResponseSplits


T = TypeVar("T", bound="AthleteStatisticsByCategoryResponse")


@_attrs_define
class AthleteStatisticsByCategoryResponse:
    """
    Attributes:
        ref (str):  Example:
            http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes/3139477/statistics/0?lang=en&region=us.
        athlete (AthleteReference):
        splits (AthleteStatisticsByCategoryResponseSplits):
    """

    ref: str
    athlete: "AthleteReference"
    splits: "AthleteStatisticsByCategoryResponseSplits"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        athlete = self.athlete.to_dict()

        splits = self.splits.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "athlete": athlete,
                "splits": splits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_reference import AthleteReference
        from ..models.athlete_statistics_by_category_response_splits import AthleteStatisticsByCategoryResponseSplits

        d = src_dict.copy()
        ref = d.pop("$ref")

        athlete = AthleteReference.from_dict(d.pop("athlete"))

        splits = AthleteStatisticsByCategoryResponseSplits.from_dict(d.pop("splits"))

        athlete_statistics_by_category_response = cls(
            ref=ref,
            athlete=athlete,
            splits=splits,
        )

        athlete_statistics_by_category_response.additional_properties = d
        return athlete_statistics_by_category_response

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
