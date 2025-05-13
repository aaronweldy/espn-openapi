from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionCounter")


@_attrs_define
class TransactionCounter:
    """
    Attributes:
        acquisitions (int): Number of player acquisitions Example: 5.
        drops (int): Number of player drops Example: 5.
        trades (Union[Unset, int]): Number of trades Example: 1.
        move_to_active (Union[Unset, int]): Number of bench-to-active moves Example: 8.
        move_to_ir (Union[Unset, int]): Number of moves to IR
    """

    acquisitions: int
    drops: int
    trades: Union[Unset, int] = UNSET
    move_to_active: Union[Unset, int] = UNSET
    move_to_ir: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        acquisitions = self.acquisitions

        drops = self.drops

        trades = self.trades

        move_to_active = self.move_to_active

        move_to_ir = self.move_to_ir

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acquisitions": acquisitions,
                "drops": drops,
            }
        )
        if trades is not UNSET:
            field_dict["trades"] = trades
        if move_to_active is not UNSET:
            field_dict["moveToActive"] = move_to_active
        if move_to_ir is not UNSET:
            field_dict["moveToIR"] = move_to_ir

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        acquisitions = d.pop("acquisitions")

        drops = d.pop("drops")

        trades = d.pop("trades", UNSET)

        move_to_active = d.pop("moveToActive", UNSET)

        move_to_ir = d.pop("moveToIR", UNSET)

        transaction_counter = cls(
            acquisitions=acquisitions,
            drops=drops,
            trades=trades,
            move_to_active=move_to_active,
            move_to_ir=move_to_ir,
        )

        transaction_counter.additional_properties = d
        return transaction_counter

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
