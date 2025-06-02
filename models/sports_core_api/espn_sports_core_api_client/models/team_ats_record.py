from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ats_record_type import AtsRecordType


T = TypeVar("T", bound="TeamAtsRecord")


@_attrs_define
class TeamAtsRecord:
    """
    Attributes:
        wins (int): Number of wins against the spread Example: 9.
        losses (int): Number of losses against the spread Example: 7.
        pushes (int): Number of pushes (ties) against the spread Example: 1.
        type (AtsRecordType):
    """

    wins: int
    losses: int
    pushes: int
    type: "AtsRecordType"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        wins = self.wins

        losses = self.losses

        pushes = self.pushes

        type = self.type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wins": wins,
                "losses": losses,
                "pushes": pushes,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ats_record_type import AtsRecordType

        d = src_dict.copy()
        wins = d.pop("wins")

        losses = d.pop("losses")

        pushes = d.pop("pushes")

        type = AtsRecordType.from_dict(d.pop("type"))

        team_ats_record = cls(
            wins=wins,
            losses=losses,
            pushes=pushes,
            type=type,
        )

        team_ats_record.additional_properties = d
        return team_ats_record

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
