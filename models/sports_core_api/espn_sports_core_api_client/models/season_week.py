import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference import Reference


T = TypeVar("T", bound="SeasonWeek")


@_attrs_define
class SeasonWeek:
    """
    Attributes:
        ref (Union[Unset, str]):
        number (Union[Unset, int]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        text (Union[Unset, str]):
        rankings (Union[Unset, Reference]):
    """

    ref: Union[Unset, str] = UNSET
    number: Union[Unset, int] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    text: Union[Unset, str] = UNSET
    rankings: Union[Unset, "Reference"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        number = self.number

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        text = self.text

        rankings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rankings, Unset):
            rankings = self.rankings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ref is not UNSET:
            field_dict["$ref"] = ref
        if number is not UNSET:
            field_dict["number"] = number
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if text is not UNSET:
            field_dict["text"] = text
        if rankings is not UNSET:
            field_dict["rankings"] = rankings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference import Reference

        d = src_dict.copy()
        ref = d.pop("$ref", UNSET)

        number = d.pop("number", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        text = d.pop("text", UNSET)

        _rankings = d.pop("rankings", UNSET)
        rankings: Union[Unset, Reference]
        if isinstance(_rankings, Unset):
            rankings = UNSET
        else:
            rankings = Reference.from_dict(_rankings)

        season_week = cls(
            ref=ref,
            number=number,
            start_date=start_date,
            end_date=end_date,
            text=text,
            rankings=rankings,
        )

        season_week.additional_properties = d
        return season_week

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
