import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.injury_type import InjuryType
    from ..models.reference import Reference


T = TypeVar("T", bound="Injury")


@_attrs_define
class Injury:
    """
    Attributes:
        status (Union[Unset, str]):
        date (Union[None, Unset, datetime.datetime]):  Example: 2023-10-10T00:00:00Z.
        comment (Union[None, Unset, str]):
        detail (Union[None, Unset, str]):
        type (Union[Unset, InjuryType]):
        details (Union[Unset, Reference]):
    """

    status: Union[Unset, str] = UNSET
    date: Union[None, Unset, datetime.datetime] = UNSET
    comment: Union[None, Unset, str] = UNSET
    detail: Union[None, Unset, str] = UNSET
    type: Union[Unset, "InjuryType"] = UNSET
    details: Union[Unset, "Reference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status

        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        detail: Union[None, Unset, str]
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if date is not UNSET:
            field_dict["date"] = date
        if comment is not UNSET:
            field_dict["comment"] = comment
        if detail is not UNSET:
            field_dict["detail"] = detail
        if type is not UNSET:
            field_dict["type"] = type
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.injury_type import InjuryType
        from ..models.reference import Reference

        d = src_dict.copy()
        status = d.pop("status", UNSET)

        def _parse_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data)

                return date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_detail(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        detail = _parse_detail(d.pop("detail", UNSET))

        _type = d.pop("type", UNSET)
        type: Union[Unset, InjuryType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = InjuryType.from_dict(_type)

        _details = d.pop("details", UNSET)
        details: Union[Unset, Reference]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = Reference.from_dict(_details)

        injury = cls(
            status=status,
            date=date,
            comment=comment,
            detail=detail,
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
