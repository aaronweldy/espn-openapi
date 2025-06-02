from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Score")


@_attrs_define
class Score:
    """
    Attributes:
        display_value (str): Display score value Example: 31.
        value (Union[Unset, float]): Numeric score value Example: 31.0.
        winner (Union[Unset, bool]): Whether this is the winning score
    """

    display_value: str
    value: Union[Unset, float] = UNSET
    winner: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_value = self.display_value

        value = self.value

        winner = self.winner

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayValue": display_value,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if winner is not UNSET:
            field_dict["winner"] = winner

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_value = d.pop("displayValue")

        value = d.pop("value", UNSET)

        winner = d.pop("winner", UNSET)

        score = cls(
            display_value=display_value,
            value=value,
            winner=winner,
        )

        score.additional_properties = d
        return score

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
