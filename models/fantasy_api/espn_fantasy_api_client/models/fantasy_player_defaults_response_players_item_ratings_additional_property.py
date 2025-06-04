from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FantasyPlayerDefaultsResponsePlayersItemRatingsAdditionalProperty")


@_attrs_define
class FantasyPlayerDefaultsResponsePlayersItemRatingsAdditionalProperty:
    """
    Attributes:
        positional_ranking (Union[Unset, float]):
        total_ranking (Union[Unset, float]):
        total_rating (Union[Unset, float]):
    """

    positional_ranking: Union[Unset, float] = UNSET
    total_ranking: Union[Unset, float] = UNSET
    total_rating: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        positional_ranking = self.positional_ranking

        total_ranking = self.total_ranking

        total_rating = self.total_rating

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if positional_ranking is not UNSET:
            field_dict["positionalRanking"] = positional_ranking
        if total_ranking is not UNSET:
            field_dict["totalRanking"] = total_ranking
        if total_rating is not UNSET:
            field_dict["totalRating"] = total_rating

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        positional_ranking = d.pop("positionalRanking", UNSET)

        total_ranking = d.pop("totalRanking", UNSET)

        total_rating = d.pop("totalRating", UNSET)

        fantasy_player_defaults_response_players_item_ratings_additional_property = cls(
            positional_ranking=positional_ranking,
            total_ranking=total_ranking,
            total_rating=total_rating,
        )

        fantasy_player_defaults_response_players_item_ratings_additional_property.additional_properties = d
        return fantasy_player_defaults_response_players_item_ratings_additional_property

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
