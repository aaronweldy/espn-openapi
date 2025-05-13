import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.player_pool_entry import PlayerPoolEntry


T = TypeVar("T", bound="RosterEntry")


@_attrs_define
class RosterEntry:
    """
    Attributes:
        player_id (int): Player ID Example: 3139477.
        player_pool_entry (PlayerPoolEntry):
        lineup_slot_id (int): Lineup slot ID (position)
        status (Union[Unset, str]): Player roster status Example: ACTIVE.
        acquisition_date (Union[Unset, datetime.datetime]): Date player was acquired Example: 2023-08-31T23:45:00Z.
        acquisition_type (Union[Unset, str]): How player was acquired Example: DRAFT.
    """

    player_id: int
    player_pool_entry: "PlayerPoolEntry"
    lineup_slot_id: int
    status: Union[Unset, str] = UNSET
    acquisition_date: Union[Unset, datetime.datetime] = UNSET
    acquisition_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        player_id = self.player_id

        player_pool_entry = self.player_pool_entry.to_dict()

        lineup_slot_id = self.lineup_slot_id

        status = self.status

        acquisition_date: Union[Unset, str] = UNSET
        if not isinstance(self.acquisition_date, Unset):
            acquisition_date = self.acquisition_date.isoformat()

        acquisition_type = self.acquisition_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "playerId": player_id,
                "playerPoolEntry": player_pool_entry,
                "lineupSlotId": lineup_slot_id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if acquisition_date is not UNSET:
            field_dict["acquisitionDate"] = acquisition_date
        if acquisition_type is not UNSET:
            field_dict["acquisitionType"] = acquisition_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.player_pool_entry import PlayerPoolEntry

        d = src_dict.copy()
        player_id = d.pop("playerId")

        player_pool_entry = PlayerPoolEntry.from_dict(d.pop("playerPoolEntry"))

        lineup_slot_id = d.pop("lineupSlotId")

        status = d.pop("status", UNSET)

        _acquisition_date = d.pop("acquisitionDate", UNSET)
        acquisition_date: Union[Unset, datetime.datetime]
        if isinstance(_acquisition_date, Unset):
            acquisition_date = UNSET
        else:
            acquisition_date = isoparse(_acquisition_date)

        acquisition_type = d.pop("acquisitionType", UNSET)

        roster_entry = cls(
            player_id=player_id,
            player_pool_entry=player_pool_entry,
            lineup_slot_id=lineup_slot_id,
            status=status,
            acquisition_date=acquisition_date,
            acquisition_type=acquisition_type,
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
