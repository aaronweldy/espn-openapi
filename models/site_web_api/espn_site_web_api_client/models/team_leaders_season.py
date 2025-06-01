import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.team_leaders_season_type import TeamLeadersSeasonType


T = TypeVar("T", bound="TeamLeadersSeason")


@_attrs_define
class TeamLeadersSeason:
    """
    Attributes:
        year (int): The season year
        display_name (str): Display name for the season
        start_date (datetime.datetime): Season start date
        end_date (datetime.datetime): Season end date
        type (TeamLeadersSeasonType):
    """

    year: int
    display_name: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    type: "TeamLeadersSeasonType"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        year = self.year

        display_name = self.display_name

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        type = self.type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "year": year,
                "displayName": display_name,
                "startDate": start_date,
                "endDate": end_date,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_leaders_season_type import TeamLeadersSeasonType

        d = src_dict.copy()
        year = d.pop("year")

        display_name = d.pop("displayName")

        start_date = isoparse(d.pop("startDate"))

        end_date = isoparse(d.pop("endDate"))

        type = TeamLeadersSeasonType.from_dict(d.pop("type"))

        team_leaders_season = cls(
            year=year,
            display_name=display_name,
            start_date=start_date,
            end_date=end_date,
            type=type,
        )

        team_leaders_season.additional_properties = d
        return team_leaders_season

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
