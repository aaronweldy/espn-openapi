import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeasonType")


@_attrs_define
class SeasonType:
    """
    Attributes:
        type (int):  Example: 2.
        name (str):  Example: Regular Season.
        abbreviation (Union[Unset, str]):  Example: reg.
        start_date (Union[Unset, datetime.date]):  Example: 2024-09-05.
        end_date (Union[Unset, datetime.date]):  Example: 2025-01-05.
        has_standings (Union[Unset, bool]):  Example: True.
    """

    type: int
    name: str
    abbreviation: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    end_date: Union[Unset, datetime.date] = UNSET
    has_standings: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        name = self.name

        abbreviation = self.abbreviation

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        has_standings = self.has_standings

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "name": name,
            }
        )
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if has_standings is not UNSET:
            field_dict["hasStandings"] = has_standings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        name = d.pop("name")

        abbreviation = d.pop("abbreviation", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        has_standings = d.pop("hasStandings", UNSET)

        season_type = cls(
            type=type,
            name=name,
            abbreviation=abbreviation,
            start_date=start_date,
            end_date=end_date,
            has_standings=has_standings,
        )

        season_type.additional_properties = d
        return season_type

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
