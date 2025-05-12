from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.boxscore_player import BoxscorePlayer
    from ..models.boxscore_team import BoxscoreTeam


T = TypeVar("T", bound="Boxscore")


@_attrs_define
class Boxscore:
    """
    Attributes:
        teams (Union[Unset, list['BoxscoreTeam']]):
        players (Union[Unset, list['BoxscorePlayer']]):
    """

    teams: Union[Unset, list["BoxscoreTeam"]] = UNSET
    players: Union[Unset, list["BoxscorePlayer"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        teams: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)

        players: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.players, Unset):
            players = []
            for players_item_data in self.players:
                players_item = players_item_data.to_dict()
                players.append(players_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if teams is not UNSET:
            field_dict["teams"] = teams
        if players is not UNSET:
            field_dict["players"] = players

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.boxscore_player import BoxscorePlayer
        from ..models.boxscore_team import BoxscoreTeam

        d = dict(src_dict)
        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = BoxscoreTeam.from_dict(teams_item_data)

            teams.append(teams_item)

        players = []
        _players = d.pop("players", UNSET)
        for players_item_data in _players or []:
            players_item = BoxscorePlayer.from_dict(players_item_data)

            players.append(players_item)

        boxscore = cls(
            teams=teams,
            players=players,
        )

        boxscore.additional_properties = d
        return boxscore

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
