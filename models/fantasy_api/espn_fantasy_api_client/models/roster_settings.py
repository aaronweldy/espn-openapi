from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roster_settings_lineup_slot_counts import RosterSettingsLineupSlotCounts
    from ..models.roster_settings_position_limits import RosterSettingsPositionLimits


T = TypeVar("T", bound="RosterSettings")


@_attrs_define
class RosterSettings:
    """
    Attributes:
        lineup_slot_counts (RosterSettingsLineupSlotCounts): Count of each position slot (keys are position IDs)
            Example: {'0': 1, '2': 2, '4': 2, '6': 1, '23': 1, '20': 1, '21': 7}.
        position_limits (Union[Unset, RosterSettingsPositionLimits]): Maximum number of players per position
        locktime (Union[Unset, int]): Time when lineups lock (0 = game time)
    """

    lineup_slot_counts: "RosterSettingsLineupSlotCounts"
    position_limits: Union[Unset, "RosterSettingsPositionLimits"] = UNSET
    locktime: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lineup_slot_counts = self.lineup_slot_counts.to_dict()

        position_limits: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.position_limits, Unset):
            position_limits = self.position_limits.to_dict()

        locktime = self.locktime

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lineupSlotCounts": lineup_slot_counts,
            }
        )
        if position_limits is not UNSET:
            field_dict["positionLimits"] = position_limits
        if locktime is not UNSET:
            field_dict["locktime"] = locktime

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.roster_settings_lineup_slot_counts import RosterSettingsLineupSlotCounts
        from ..models.roster_settings_position_limits import RosterSettingsPositionLimits

        d = src_dict.copy()
        lineup_slot_counts = RosterSettingsLineupSlotCounts.from_dict(d.pop("lineupSlotCounts"))

        _position_limits = d.pop("positionLimits", UNSET)
        position_limits: Union[Unset, RosterSettingsPositionLimits]
        if isinstance(_position_limits, Unset):
            position_limits = UNSET
        else:
            position_limits = RosterSettingsPositionLimits.from_dict(_position_limits)

        locktime = d.pop("locktime", UNSET)

        roster_settings = cls(
            lineup_slot_counts=lineup_slot_counts,
            position_limits=position_limits,
            locktime=locktime,
        )

        roster_settings.additional_properties = d
        return roster_settings

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
