from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_player import FantasyPlayer
    from ..models.fantasy_player_defaults_response_players_item_ratings import (
        FantasyPlayerDefaultsResponsePlayersItemRatings,
    )


T = TypeVar("T", bound="FantasyPlayerDefaultsResponsePlayersItem")


@_attrs_define
class FantasyPlayerDefaultsResponsePlayersItem:
    """
    Attributes:
        id (Union[Unset, str]): Player entry ID
        draft_auction_value (Union[Unset, float]): Auction draft value
        keeper_value (Union[Unset, float]): Keeper league value
        keeper_value_future (Union[Unset, float]): Future keeper value
        lineup_locked (Union[Unset, bool]): Whether player is locked in lineup
        on_team_id (Union[Unset, int]): Team ID player is on (0 if free agent)
        player (Union[Unset, FantasyPlayer]):
        ratings (Union[Unset, FantasyPlayerDefaultsResponsePlayersItemRatings]): Player ratings by period
        roster_locked (Union[Unset, bool]): Whether player is locked on roster
        status (Union[Unset, str]): Player status
        trade_locked (Union[Unset, bool]): Whether player is locked from trades
        waiver_process_date (Union[Unset, int]): Waiver process date timestamp
    """

    id: Union[Unset, str] = UNSET
    draft_auction_value: Union[Unset, float] = UNSET
    keeper_value: Union[Unset, float] = UNSET
    keeper_value_future: Union[Unset, float] = UNSET
    lineup_locked: Union[Unset, bool] = UNSET
    on_team_id: Union[Unset, int] = UNSET
    player: Union[Unset, "FantasyPlayer"] = UNSET
    ratings: Union[Unset, "FantasyPlayerDefaultsResponsePlayersItemRatings"] = UNSET
    roster_locked: Union[Unset, bool] = UNSET
    status: Union[Unset, str] = UNSET
    trade_locked: Union[Unset, bool] = UNSET
    waiver_process_date: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        draft_auction_value = self.draft_auction_value

        keeper_value = self.keeper_value

        keeper_value_future = self.keeper_value_future

        lineup_locked = self.lineup_locked

        on_team_id = self.on_team_id

        player: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.player, Unset):
            player = self.player.to_dict()

        ratings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ratings, Unset):
            ratings = self.ratings.to_dict()

        roster_locked = self.roster_locked

        status = self.status

        trade_locked = self.trade_locked

        waiver_process_date = self.waiver_process_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if draft_auction_value is not UNSET:
            field_dict["draftAuctionValue"] = draft_auction_value
        if keeper_value is not UNSET:
            field_dict["keeperValue"] = keeper_value
        if keeper_value_future is not UNSET:
            field_dict["keeperValueFuture"] = keeper_value_future
        if lineup_locked is not UNSET:
            field_dict["lineupLocked"] = lineup_locked
        if on_team_id is not UNSET:
            field_dict["onTeamId"] = on_team_id
        if player is not UNSET:
            field_dict["player"] = player
        if ratings is not UNSET:
            field_dict["ratings"] = ratings
        if roster_locked is not UNSET:
            field_dict["rosterLocked"] = roster_locked
        if status is not UNSET:
            field_dict["status"] = status
        if trade_locked is not UNSET:
            field_dict["tradeLocked"] = trade_locked
        if waiver_process_date is not UNSET:
            field_dict["waiverProcessDate"] = waiver_process_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_player import FantasyPlayer
        from ..models.fantasy_player_defaults_response_players_item_ratings import (
            FantasyPlayerDefaultsResponsePlayersItemRatings,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        draft_auction_value = d.pop("draftAuctionValue", UNSET)

        keeper_value = d.pop("keeperValue", UNSET)

        keeper_value_future = d.pop("keeperValueFuture", UNSET)

        lineup_locked = d.pop("lineupLocked", UNSET)

        on_team_id = d.pop("onTeamId", UNSET)

        _player = d.pop("player", UNSET)
        player: Union[Unset, FantasyPlayer]
        if isinstance(_player, Unset):
            player = UNSET
        else:
            player = FantasyPlayer.from_dict(_player)

        _ratings = d.pop("ratings", UNSET)
        ratings: Union[Unset, FantasyPlayerDefaultsResponsePlayersItemRatings]
        if isinstance(_ratings, Unset):
            ratings = UNSET
        else:
            ratings = FantasyPlayerDefaultsResponsePlayersItemRatings.from_dict(_ratings)

        roster_locked = d.pop("rosterLocked", UNSET)

        status = d.pop("status", UNSET)

        trade_locked = d.pop("tradeLocked", UNSET)

        waiver_process_date = d.pop("waiverProcessDate", UNSET)

        fantasy_player_defaults_response_players_item = cls(
            id=id,
            draft_auction_value=draft_auction_value,
            keeper_value=keeper_value,
            keeper_value_future=keeper_value_future,
            lineup_locked=lineup_locked,
            on_team_id=on_team_id,
            player=player,
            ratings=ratings,
            roster_locked=roster_locked,
            status=status,
            trade_locked=trade_locked,
            waiver_process_date=waiver_process_date,
        )

        fantasy_player_defaults_response_players_item.additional_properties = d
        return fantasy_player_defaults_response_players_item

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
