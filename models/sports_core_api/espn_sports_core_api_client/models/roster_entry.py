from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference import Reference


T = TypeVar("T", bound="RosterEntry")


@_attrs_define
class RosterEntry:
    """
    Attributes:
        player_id (int): Player ID
        starter (bool): Whether the player is a starter
        jersey (str): Jersey number
        valid (bool): Whether the entry is valid
        athlete (Reference):
        did_not_play (bool): Whether the player did not play
        display_name (str): Player display name
        period (Union[Unset, int]): Period number
        active (Union[Unset, bool]): Whether the player is active
        for_player_id (Union[Unset, int]): For player ID (replacement scenarios)
        position (Union[Unset, Reference]):
        statistics (Union[Unset, Reference]):
    """

    player_id: int
    starter: bool
    jersey: str
    valid: bool
    athlete: "Reference"
    did_not_play: bool
    display_name: str
    period: Union[Unset, int] = UNSET
    active: Union[Unset, bool] = UNSET
    for_player_id: Union[Unset, int] = UNSET
    position: Union[Unset, "Reference"] = UNSET
    statistics: Union[Unset, "Reference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        player_id = self.player_id

        starter = self.starter

        jersey = self.jersey

        valid = self.valid

        athlete = self.athlete.to_dict()

        did_not_play = self.did_not_play

        display_name = self.display_name

        period = self.period

        active = self.active

        for_player_id = self.for_player_id

        position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        statistics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "playerId": player_id,
                "starter": starter,
                "jersey": jersey,
                "valid": valid,
                "athlete": athlete,
                "didNotPlay": did_not_play,
                "displayName": display_name,
            }
        )
        if period is not UNSET:
            field_dict["period"] = period
        if active is not UNSET:
            field_dict["active"] = active
        if for_player_id is not UNSET:
            field_dict["forPlayerId"] = for_player_id
        if position is not UNSET:
            field_dict["position"] = position
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference

        d = src_dict.copy()
        player_id = d.pop("playerId")

        starter = d.pop("starter")

        jersey = d.pop("jersey")

        valid = d.pop("valid")

        athlete = Reference.from_dict(d.pop("athlete"))

        did_not_play = d.pop("didNotPlay")

        display_name = d.pop("displayName")

        period = d.pop("period", UNSET)

        active = d.pop("active", UNSET)

        for_player_id = d.pop("forPlayerId", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, Reference]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = Reference.from_dict(_position)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, Reference]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = Reference.from_dict(_statistics)

        roster_entry = cls(
            player_id=player_id,
            starter=starter,
            jersey=jersey,
            valid=valid,
            athlete=athlete,
            did_not_play=did_not_play,
            display_name=display_name,
            period=period,
            active=active,
            for_player_id=for_player_id,
            position=position,
            statistics=statistics,
        )

        roster_entry.additional_properties = d
        return roster_entry

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
