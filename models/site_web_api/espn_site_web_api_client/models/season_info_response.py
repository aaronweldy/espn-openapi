import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.season_type_info import SeasonTypeInfo


T = TypeVar("T", bound="SeasonInfoResponse")


@_attrs_define
class SeasonInfoResponse:
    """Season information response from site.web.api.espn.com

    Attributes:
        year (int): The season year Example: 2024.
        display_name (str): Display name for the season Example: 2024.
        start_date (datetime.datetime): Season start date in ISO 8601 format Example: 2024-08-01T07:00:00.000+00:00.
        end_date (datetime.datetime): Season end date in ISO 8601 format Example: 2025-02-15T07:59:00.000+00:00.
        types (List['SeasonTypeInfo']): Array of season types (preseason, regular, postseason, etc.)
    """

    year: int
    display_name: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    types: List["SeasonTypeInfo"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        year = self.year

        display_name = self.display_name

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        types = []
        for types_item_data in self.types:
            types_item = types_item_data.to_dict()
            types.append(types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "year": year,
                "displayName": display_name,
                "startDate": start_date,
                "endDate": end_date,
                "types": types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.season_type_info import SeasonTypeInfo

        d = src_dict.copy()
        year = d.pop("year")

        display_name = d.pop("displayName")

        start_date = isoparse(d.pop("startDate"))

        end_date = isoparse(d.pop("endDate"))

        types = []
        _types = d.pop("types")
        for types_item_data in _types:
            types_item = SeasonTypeInfo.from_dict(types_item_data)

            types.append(types_item)

        season_info_response = cls(
            year=year,
            display_name=display_name,
            start_date=start_date,
            end_date=end_date,
            types=types,
        )

        season_info_response.additional_properties = d
        return season_info_response

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
