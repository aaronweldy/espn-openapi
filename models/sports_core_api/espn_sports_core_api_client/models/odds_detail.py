from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OddsDetail")


@_attrs_define
class OddsDetail:
    """
    Attributes:
        odd_id (str):
        value (str):
        bet_slip_url (str):
    """

    odd_id: str
    value: str
    bet_slip_url: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        odd_id = self.odd_id

        value = self.value

        bet_slip_url = self.bet_slip_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "oddId": odd_id,
                "value": value,
                "betSlipUrl": bet_slip_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        odd_id = d.pop("oddId")

        value = d.pop("value")

        bet_slip_url = d.pop("betSlipUrl")

        odds_detail = cls(
            odd_id=odd_id,
            value=value,
            bet_slip_url=bet_slip_url,
        )

        odds_detail.additional_properties = d
        return odds_detail

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
