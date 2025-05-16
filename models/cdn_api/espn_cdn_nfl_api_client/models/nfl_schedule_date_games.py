from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nfl_schedule_game import NflScheduleGame


T = TypeVar("T", bound="NflScheduleDateGames")


@_attrs_define
class NflScheduleDateGames:
    """
    Attributes:
        games (Union[Unset, List['NflScheduleGame']]):
    """

    games: Union[Unset, List["NflScheduleGame"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        games: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.games, Unset):
            games = []
            for games_item_data in self.games:
                games_item = games_item_data.to_dict()
                games.append(games_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if games is not UNSET:
            field_dict["games"] = games

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_schedule_game import NflScheduleGame

        d = src_dict.copy()
        games = []
        _games = d.pop("games", UNSET)
        for games_item_data in _games or []:
            games_item = NflScheduleGame.from_dict(games_item_data)

            games.append(games_item)

        nfl_schedule_date_games = cls(
            games=games,
        )

        nfl_schedule_date_games.additional_properties = d
        return nfl_schedule_date_games

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
