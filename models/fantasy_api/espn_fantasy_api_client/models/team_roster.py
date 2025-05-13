from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roster_entry import RosterEntry
    from ..models.team_roster_lineup_slot_counts import TeamRosterLineupSlotCounts


T = TypeVar("T", bound="TeamRoster")


@_attrs_define
class TeamRoster:
    """
    Attributes:
        entries (List['RosterEntry']):
        lineup_slot_counts (Union[Unset, TeamRosterLineupSlotCounts]): Count of each position slot (keys are position
            IDs)
    """

    entries: List["RosterEntry"]
    lineup_slot_counts: Union[Unset, "TeamRosterLineupSlotCounts"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        lineup_slot_counts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lineup_slot_counts, Unset):
            lineup_slot_counts = self.lineup_slot_counts.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entries": entries,
            }
        )
        if lineup_slot_counts is not UNSET:
            field_dict["lineupSlotCounts"] = lineup_slot_counts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.roster_entry import RosterEntry
        from ..models.team_roster_lineup_slot_counts import TeamRosterLineupSlotCounts

        d = src_dict.copy()
        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = RosterEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        _lineup_slot_counts = d.pop("lineupSlotCounts", UNSET)
        lineup_slot_counts: Union[Unset, TeamRosterLineupSlotCounts]
        if isinstance(_lineup_slot_counts, Unset):
            lineup_slot_counts = UNSET
        else:
            lineup_slot_counts = TeamRosterLineupSlotCounts.from_dict(_lineup_slot_counts)

        team_roster = cls(
            entries=entries,
            lineup_slot_counts=lineup_slot_counts,
        )

        team_roster.additional_properties = d
        return team_roster

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
