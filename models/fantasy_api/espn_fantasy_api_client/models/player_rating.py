from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerRating")


@_attrs_define
class PlayerRating:
    """
    Attributes:
        positional_ranking (int): Ranking at position Example: 1.
        total_ranking (int): Overall ranking Example: 15.
        total_rating (Union[Unset, float]): Player rating (1-10 scale) Example: 8.5.
    """

    positional_ranking: int
    total_ranking: int
    total_rating: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        positional_ranking = self.positional_ranking

        total_ranking = self.total_ranking

        total_rating = self.total_rating

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "positionalRanking": positional_ranking,
                "totalRanking": total_ranking,
            }
        )
        if total_rating is not UNSET:
            field_dict["totalRating"] = total_rating

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        positional_ranking = d.pop("positionalRanking")

        total_ranking = d.pop("totalRanking")

        total_rating = d.pop("totalRating", UNSET)

        player_rating = cls(
            positional_ranking=positional_ranking,
            total_ranking=total_ranking,
            total_rating=total_rating,
        )

        player_rating.additional_properties = d
        return player_rating

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
