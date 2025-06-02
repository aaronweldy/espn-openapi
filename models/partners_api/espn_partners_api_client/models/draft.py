from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Draft")


@_attrs_define
class Draft:
    """
    Attributes:
        round_ (int): Draft round Example: 5.
        year (int): Draft year Example: 2023.
        selection (int): Overall draft pick number Example: 143.
    """

    round_: int
    year: int
    selection: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        round_ = self.round_

        year = self.year

        selection = self.selection

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "round": round_,
                "year": year,
                "selection": selection,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        round_ = d.pop("round")

        year = d.pop("year")

        selection = d.pop("selection")

        draft = cls(
            round_=round_,
            year=year,
            selection=selection,
        )

        draft.additional_properties = d
        return draft

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
