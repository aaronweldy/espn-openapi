from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SpreadRecord")


@_attrs_define
class SpreadRecord:
    """
    Attributes:
        wins (int):
        losses (int):
        pushes (int):
        summary (str):
    """

    wins: int
    losses: int
    pushes: int
    summary: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        wins = self.wins

        losses = self.losses

        pushes = self.pushes

        summary = self.summary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wins": wins,
                "losses": losses,
                "pushes": pushes,
                "summary": summary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        wins = d.pop("wins")

        losses = d.pop("losses")

        pushes = d.pop("pushes")

        summary = d.pop("summary")

        spread_record = cls(
            wins=wins,
            losses=losses,
            pushes=pushes,
            summary=summary,
        )

        spread_record.additional_properties = d
        return spread_record

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
