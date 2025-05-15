import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="VideoTimeRestrictions")


@_attrs_define
class VideoTimeRestrictions:
    """
    Attributes:
        embargo_date (Union[Unset, datetime.datetime]):
        expiration_date (Union[Unset, datetime.datetime]):
    """

    embargo_date: Union[Unset, datetime.datetime] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        embargo_date: Union[Unset, str] = UNSET
        if not isinstance(self.embargo_date, Unset):
            embargo_date = self.embargo_date.isoformat()

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if embargo_date is not UNSET:
            field_dict["embargoDate"] = embargo_date
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _embargo_date = d.pop("embargoDate", UNSET)
        embargo_date: Union[Unset, datetime.datetime]
        if isinstance(_embargo_date, Unset):
            embargo_date = UNSET
        else:
            embargo_date = isoparse(_embargo_date)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        video_time_restrictions = cls(
            embargo_date=embargo_date,
            expiration_date=expiration_date,
        )

        video_time_restrictions.additional_properties = d
        return video_time_restrictions

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
