from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.player import Player
    from ..models.player_pool_entry_ratings import PlayerPoolEntryRatings


T = TypeVar("T", bound="PlayerPoolEntry")


@_attrs_define
class PlayerPoolEntry:
    """
    Attributes:
        id (int): Player ID Example: 3139477.
        player (Player):
        ratings (Union[Unset, PlayerPoolEntryRatings]): Player ratings
        applied_stat_total (Union[Unset, float]): Total stats applied for scoring Example: 22.4.
    """

    id: int
    player: "Player"
    ratings: Union[Unset, "PlayerPoolEntryRatings"] = UNSET
    applied_stat_total: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        player = self.player.to_dict()

        ratings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ratings, Unset):
            ratings = self.ratings.to_dict()

        applied_stat_total = self.applied_stat_total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "player": player,
            }
        )
        if ratings is not UNSET:
            field_dict["ratings"] = ratings
        if applied_stat_total is not UNSET:
            field_dict["appliedStatTotal"] = applied_stat_total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.player import Player
        from ..models.player_pool_entry_ratings import PlayerPoolEntryRatings

        d = src_dict.copy()
        id = d.pop("id")

        player = Player.from_dict(d.pop("player"))

        _ratings = d.pop("ratings", UNSET)
        ratings: Union[Unset, PlayerPoolEntryRatings]
        if isinstance(_ratings, Unset):
            ratings = UNSET
        else:
            ratings = PlayerPoolEntryRatings.from_dict(_ratings)

        applied_stat_total = d.pop("appliedStatTotal", UNSET)

        player_pool_entry = cls(
            id=id,
            player=player,
            ratings=ratings,
            applied_stat_total=applied_stat_total,
        )

        player_pool_entry.additional_properties = d
        return player_pool_entry

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
