from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        wins (int): Number of wins Example: 1.
        losses (int): Number of losses
        percentage (float): Win percentage Example: 1.0.
        ties (Union[Unset, int]): Number of ties
        points_for (Union[Unset, float]): Points scored Example: 108.5.
        points_against (Union[Unset, float]): Points scored against Example: 95.2.
    """

    wins: int
    losses: int
    percentage: float
    ties: Union[Unset, int] = UNSET
    points_for: Union[Unset, float] = UNSET
    points_against: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        wins = self.wins

        losses = self.losses

        percentage = self.percentage

        ties = self.ties

        points_for = self.points_for

        points_against = self.points_against

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wins": wins,
                "losses": losses,
                "percentage": percentage,
            }
        )
        if ties is not UNSET:
            field_dict["ties"] = ties
        if points_for is not UNSET:
            field_dict["pointsFor"] = points_for
        if points_against is not UNSET:
            field_dict["pointsAgainst"] = points_against

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        wins = d.pop("wins")

        losses = d.pop("losses")

        percentage = d.pop("percentage")

        ties = d.pop("ties", UNSET)

        points_for = d.pop("pointsFor", UNSET)

        points_against = d.pop("pointsAgainst", UNSET)

        record = cls(
            wins=wins,
            losses=losses,
            percentage=percentage,
            ties=ties,
            points_for=points_for,
            points_against=points_against,
        )

        record.additional_properties = d
        return record

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
