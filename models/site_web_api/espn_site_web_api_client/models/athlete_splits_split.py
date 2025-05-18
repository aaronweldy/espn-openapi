from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AthleteSplitsSplit")


@_attrs_define
class AthleteSplitsSplit:
    """Split in NFL Athlete Splits response.

    Attributes:
        display_name (str):
        stats (List[str]):
        abbreviation (str):
    """

    display_name: str
    stats: List[str]
    abbreviation: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name

        stats = self.stats

        abbreviation = self.abbreviation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "stats": stats,
                "abbreviation": abbreviation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName")

        stats = cast(List[str], d.pop("stats"))

        abbreviation = d.pop("abbreviation")

        athlete_splits_split = cls(
            display_name=display_name,
            stats=stats,
            abbreviation=abbreviation,
        )

        athlete_splits_split.additional_properties = d
        return athlete_splits_split

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
