from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DraftInfo")


@_attrs_define
class DraftInfo:
    """
    Attributes:
        year (int):  Example: 2017.
        round_ (Union[Unset, int]):  Example: 1.
        pick (Union[Unset, int]):  Example: 10.
        display_text (Union[Unset, str]):  Example: 2017 Round 1 (10th overall).
    """

    year: int
    round_: Union[Unset, int] = UNSET
    pick: Union[Unset, int] = UNSET
    display_text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        year = self.year

        round_ = self.round_

        pick = self.pick

        display_text = self.display_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "year": year,
            }
        )
        if round_ is not UNSET:
            field_dict["round"] = round_
        if pick is not UNSET:
            field_dict["pick"] = pick
        if display_text is not UNSET:
            field_dict["displayText"] = display_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        year = d.pop("year")

        round_ = d.pop("round", UNSET)

        pick = d.pop("pick", UNSET)

        display_text = d.pop("displayText", UNSET)

        draft_info = cls(
            year=year,
            round_=round_,
            pick=pick,
            display_text=display_text,
        )

        draft_info.additional_properties = d
        return draft_info

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
