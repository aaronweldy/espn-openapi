from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference import Reference


T = TypeVar("T", bound="OddsPredictor")


@_attrs_define
class OddsPredictor:
    """
    Attributes:
        rank (int): Predictor rank
        value (float): Prediction value/score
        display_value (str): Display value for prediction
        total (Union[Unset, str]): Total prediction (OVER/UNDER)
        predictor_competition (Union[Unset, Reference]):
        projected_winner (Union[Unset, Reference]):
        cover (Union[Unset, Reference]):
        projected_cover (Union[Unset, Reference]):
    """

    rank: int
    value: float
    display_value: str
    total: Union[Unset, str] = UNSET
    predictor_competition: Union[Unset, "Reference"] = UNSET
    projected_winner: Union[Unset, "Reference"] = UNSET
    cover: Union[Unset, "Reference"] = UNSET
    projected_cover: Union[Unset, "Reference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rank = self.rank

        value = self.value

        display_value = self.display_value

        total = self.total

        predictor_competition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.predictor_competition, Unset):
            predictor_competition = self.predictor_competition.to_dict()

        projected_winner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.projected_winner, Unset):
            projected_winner = self.projected_winner.to_dict()

        cover: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cover, Unset):
            cover = self.cover.to_dict()

        projected_cover: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.projected_cover, Unset):
            projected_cover = self.projected_cover.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rank": rank,
                "value": value,
                "displayValue": display_value,
            }
        )
        if total is not UNSET:
            field_dict["total"] = total
        if predictor_competition is not UNSET:
            field_dict["predictorCompetition"] = predictor_competition
        if projected_winner is not UNSET:
            field_dict["projectedWinner"] = projected_winner
        if cover is not UNSET:
            field_dict["cover"] = cover
        if projected_cover is not UNSET:
            field_dict["projectedCover"] = projected_cover

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference

        d = src_dict.copy()
        rank = d.pop("rank")

        value = d.pop("value")

        display_value = d.pop("displayValue")

        total = d.pop("total", UNSET)

        _predictor_competition = d.pop("predictorCompetition", UNSET)
        predictor_competition: Union[Unset, Reference]
        if isinstance(_predictor_competition, Unset):
            predictor_competition = UNSET
        else:
            predictor_competition = Reference.from_dict(_predictor_competition)

        _projected_winner = d.pop("projectedWinner", UNSET)
        projected_winner: Union[Unset, Reference]
        if isinstance(_projected_winner, Unset):
            projected_winner = UNSET
        else:
            projected_winner = Reference.from_dict(_projected_winner)

        _cover = d.pop("cover", UNSET)
        cover: Union[Unset, Reference]
        if isinstance(_cover, Unset):
            cover = UNSET
        else:
            cover = Reference.from_dict(_cover)

        _projected_cover = d.pop("projectedCover", UNSET)
        projected_cover: Union[Unset, Reference]
        if isinstance(_projected_cover, Unset):
            projected_cover = UNSET
        else:
            projected_cover = Reference.from_dict(_projected_cover)

        odds_predictor = cls(
            rank=rank,
            value=value,
            display_value=display_value,
            total=total,
            predictor_competition=predictor_competition,
            projected_winner=projected_winner,
            cover=cover,
            projected_cover=projected_cover,
        )

        odds_predictor.additional_properties = d
        return odds_predictor

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
