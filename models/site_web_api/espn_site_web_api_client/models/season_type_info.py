import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="SeasonTypeInfo")


@_attrs_define
class SeasonTypeInfo:
    """Season type information (e.g., preseason, regular season, postseason)

    Attributes:
        id (str): Season type ID as string Example: 1.
        type (int): Season type as integer (1=preseason, 2=regular, 3=postseason, 4=offseason, 5=play-in) Example: 1.
        name (str): Name of the season type Example: Preseason.
        start_date (datetime.datetime): Season type start date in ISO 8601 format Example:
            2024-08-01T07:00:00.000+00:00.
        end_date (datetime.datetime): Season type end date in ISO 8601 format Example: 2024-09-05T06:59:00.000+00:00.
    """

    id: str
    type: int
    name: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type

        name = self.name

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "name": name,
                "startDate": start_date,
                "endDate": end_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = d.pop("type")

        name = d.pop("name")

        start_date = isoparse(d.pop("startDate"))

        end_date = isoparse(d.pop("endDate"))

        season_type_info = cls(
            id=id,
            type=type,
            name=name,
            start_date=start_date,
            end_date=end_date,
        )

        season_type_info.additional_properties = d
        return season_type_info

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
