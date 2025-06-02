import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.injury_details import InjuryDetails
    from ..models.injury_type import InjuryType


T = TypeVar("T", bound="Injury")


@_attrs_define
class Injury:
    """
    Attributes:
        id (str): Injury identifier Example: -1676597.
        status (str): Injury status Example: Questionable.
        date (Union[Unset, datetime.datetime]): Date of injury report Example: 2025-01-06T13:42Z.
        type (Union[Unset, InjuryType]):
        details (Union[Unset, InjuryDetails]):
    """

    id: str
    status: str
    date: Union[Unset, datetime.datetime] = UNSET
    type: Union[Unset, "InjuryType"] = UNSET
    details: Union[Unset, "InjuryDetails"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        status = self.status

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if type is not UNSET:
            field_dict["type"] = type
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.injury_details import InjuryDetails
        from ..models.injury_type import InjuryType

        d = src_dict.copy()
        id = d.pop("id")

        status = d.pop("status")

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _type = d.pop("type", UNSET)
        type: Union[Unset, InjuryType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = InjuryType.from_dict(_type)

        _details = d.pop("details", UNSET)
        details: Union[Unset, InjuryDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = InjuryDetails.from_dict(_details)

        injury = cls(
            id=id,
            status=status,
            date=date,
            type=type,
            details=details,
        )

        injury.additional_properties = d
        return injury

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
