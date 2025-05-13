from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AthleteDetailsResponseAlternateIds")


@_attrs_define
class AthleteDetailsResponseAlternateIds:
    """
    Attributes:
        sdr (Union[Unset, str]):  Example: 3139477.
    """

    sdr: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sdr = self.sdr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sdr is not UNSET:
            field_dict["sdr"] = sdr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sdr = d.pop("sdr", UNSET)

        athlete_details_response_alternate_ids = cls(
            sdr=sdr,
        )

        athlete_details_response_alternate_ids.additional_properties = d
        return athlete_details_response_alternate_ids

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
