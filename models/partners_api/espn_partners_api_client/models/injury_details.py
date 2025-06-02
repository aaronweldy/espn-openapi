import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="InjuryDetails")


@_attrs_define
class InjuryDetails:
    """
    Attributes:
        type (str): Specific injury description Example: Foot.
        return_date (Union[Unset, datetime.date]): Expected return date Example: 2025-05-01.
    """

    type: str
    return_date: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        return_date: Union[Unset, str] = UNSET
        if not isinstance(self.return_date, Unset):
            return_date = self.return_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if return_date is not UNSET:
            field_dict["returnDate"] = return_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        _return_date = d.pop("returnDate", UNSET)
        return_date: Union[Unset, datetime.date]
        if isinstance(_return_date, Unset):
            return_date = UNSET
        else:
            return_date = isoparse(_return_date).date()

        injury_details = cls(
            type=type,
            return_date=return_date,
        )

        injury_details.additional_properties = d
        return injury_details

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
