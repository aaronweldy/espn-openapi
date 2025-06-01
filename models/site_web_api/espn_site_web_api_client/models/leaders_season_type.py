import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.leaders_season_type_week import LeadersSeasonTypeWeek


T = TypeVar("T", bound="LeadersSeasonType")


@_attrs_define
class LeadersSeasonType:
    """
    Attributes:
        id (str): Season type ID
        type (int): Season type number
        name (str): Season type name (e.g., "Off Season", "Regular Season")
        start_date (datetime.datetime):
        end_date (datetime.datetime):
        week (Union[Unset, LeadersSeasonTypeWeek]): Week information (may be empty)
    """

    id: str
    type: int
    name: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    week: Union[Unset, "LeadersSeasonTypeWeek"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type

        name = self.name

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        week: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.week, Unset):
            week = self.week.to_dict()

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
        if week is not UNSET:
            field_dict["week"] = week

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.leaders_season_type_week import LeadersSeasonTypeWeek

        d = src_dict.copy()
        id = d.pop("id")

        type = d.pop("type")

        name = d.pop("name")

        start_date = isoparse(d.pop("startDate"))

        end_date = isoparse(d.pop("endDate"))

        _week = d.pop("week", UNSET)
        week: Union[Unset, LeadersSeasonTypeWeek]
        if isinstance(_week, Unset):
            week = UNSET
        else:
            week = LeadersSeasonTypeWeek.from_dict(_week)

        leaders_season_type = cls(
            id=id,
            type=type,
            name=name,
            start_date=start_date,
            end_date=end_date,
            week=week,
        )

        leaders_season_type.additional_properties = d
        return leaders_season_type

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
