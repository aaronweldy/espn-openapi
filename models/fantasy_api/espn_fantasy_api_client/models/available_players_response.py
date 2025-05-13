from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.player_pool_entry import PlayerPoolEntry


T = TypeVar("T", bound="AvailablePlayersResponse")


@_attrs_define
class AvailablePlayersResponse:
    """
    Attributes:
        players (List['PlayerPoolEntry']):
        scoring_period_id (int): Scoring period (week) ID Example: 1.
    """

    players: List["PlayerPoolEntry"]
    scoring_period_id: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        players = []
        for players_item_data in self.players:
            players_item = players_item_data.to_dict()
            players.append(players_item)

        scoring_period_id = self.scoring_period_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "players": players,
                "scoringPeriodId": scoring_period_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.player_pool_entry import PlayerPoolEntry

        d = src_dict.copy()
        players = []
        _players = d.pop("players")
        for players_item_data in _players:
            players_item = PlayerPoolEntry.from_dict(players_item_data)

            players.append(players_item)

        scoring_period_id = d.pop("scoringPeriodId")

        available_players_response = cls(
            players=players,
            scoring_period_id=scoring_period_id,
        )

        available_players_response.additional_properties = d
        return available_players_response

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
