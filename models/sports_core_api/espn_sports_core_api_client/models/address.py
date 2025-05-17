from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Address")


@_attrs_define
class Address:
    """
    Attributes:
        city (str):
        state (str):
        zip_code (str):
        country (str):
    """

    city: str
    state: str
    zip_code: str
    country: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        city = self.city

        state = self.state

        zip_code = self.zip_code

        country = self.country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "city": city,
                "state": state,
                "zipCode": zip_code,
                "country": country,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        city = d.pop("city")

        state = d.pop("state")

        zip_code = d.pop("zipCode")

        country = d.pop("country")

        address = cls(
            city=city,
            state=state,
            zip_code=zip_code,
            country=country,
        )

        address.additional_properties = d
        return address

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
