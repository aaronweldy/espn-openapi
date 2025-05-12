import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SportLeagueSeason")


@_attrs_define
class SportLeagueSeason:
    """
    Attributes:
        year (Union[Unset, int]):  Example: 2024.
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        display_name (Union[Unset, str]):  Example: 2024-25.
        type_ (Union[Unset, int]):  Example: 2.
    """

    year: Union[Unset, int] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    display_name: Union[Unset, str] = UNSET
    type_: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        year = self.year

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        display_name = self.display_name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if year is not UNSET:
            field_dict["year"] = year
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        year = d.pop("year", UNSET)

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

        display_name = d.pop("displayName", UNSET)

        type_ = d.pop("type", UNSET)

        sport_league_season = cls(
            year=year,
            start_date=start_date,
            end_date=end_date,
            display_name=display_name,
            type_=type_,
        )

        sport_league_season.additional_properties = d
        return sport_league_season

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
