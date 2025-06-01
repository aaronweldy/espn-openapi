import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_leaders_season_type_week import TeamLeadersSeasonTypeWeek


T = TypeVar("T", bound="TeamLeadersSeasonType")


@_attrs_define
class TeamLeadersSeasonType:
    """
    Attributes:
        id (str): Season type ID
        type (int): Season type number
        name (str): Season type name (e.g., "Regular Season", "Off Season")
        start_date (Union[Unset, datetime.datetime]): Season type start date
        end_date (Union[Unset, datetime.datetime]): Season type end date
        week (Union[Unset, TeamLeadersSeasonTypeWeek]): Current week information
    """

    id: str
    type: int
    name: str
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    week: Union[Unset, "TeamLeadersSeasonTypeWeek"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type

        name = self.name

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
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
            }
        )
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if week is not UNSET:
            field_dict["week"] = week

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_leaders_season_type_week import TeamLeadersSeasonTypeWeek

        d = src_dict.copy()
        id = d.pop("id")

        type = d.pop("type")

        name = d.pop("name")

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

        _week = d.pop("week", UNSET)
        week: Union[Unset, TeamLeadersSeasonTypeWeek]
        if isinstance(_week, Unset):
            week = UNSET
        else:
            week = TeamLeadersSeasonTypeWeek.from_dict(_week)

        team_leaders_season_type = cls(
            id=id,
            type=type,
            name=name,
            start_date=start_date,
            end_date=end_date,
            week=week,
        )

        team_leaders_season_type.additional_properties = d
        return team_leaders_season_type

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
