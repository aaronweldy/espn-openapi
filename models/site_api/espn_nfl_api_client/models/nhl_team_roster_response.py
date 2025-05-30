import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nhl_coach import NhlCoach
    from ..models.nhl_position_group import NhlPositionGroup
    from ..models.season import Season
    from ..models.team_detail import TeamDetail


T = TypeVar("T", bound="NhlTeamRosterResponse")


@_attrs_define
class NhlTeamRosterResponse:
    """NHL team roster response with player and coach information

    Attributes:
        team (TeamDetail):
        athletes (List['NhlPositionGroup']):
        timestamp (Union[Unset, datetime.datetime]):
        status (Union[Unset, str]):
        season (Union[Unset, Season]):
        coach (Union[Unset, List['NhlCoach']]):
    """

    team: "TeamDetail"
    athletes: List["NhlPositionGroup"]
    timestamp: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, str] = UNSET
    season: Union[Unset, "Season"] = UNSET
    coach: Union[Unset, List["NhlCoach"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team = self.team.to_dict()

        athletes = []
        for athletes_item_data in self.athletes:
            athletes_item = athletes_item_data.to_dict()
            athletes.append(athletes_item)

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        status = self.status

        season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        coach: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.coach, Unset):
            coach = []
            for coach_item_data in self.coach:
                coach_item = coach_item_data.to_dict()
                coach.append(coach_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team": team,
                "athletes": athletes,
            }
        )
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if status is not UNSET:
            field_dict["status"] = status
        if season is not UNSET:
            field_dict["season"] = season
        if coach is not UNSET:
            field_dict["coach"] = coach

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nhl_coach import NhlCoach
        from ..models.nhl_position_group import NhlPositionGroup
        from ..models.season import Season
        from ..models.team_detail import TeamDetail

        d = src_dict.copy()
        team = TeamDetail.from_dict(d.pop("team"))

        athletes = []
        _athletes = d.pop("athletes")
        for athletes_item_data in _athletes:
            athletes_item = NhlPositionGroup.from_dict(athletes_item_data)

            athletes.append(athletes_item)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        status = d.pop("status", UNSET)

        _season = d.pop("season", UNSET)
        season: Union[Unset, Season]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = Season.from_dict(_season)

        coach = []
        _coach = d.pop("coach", UNSET)
        for coach_item_data in _coach or []:
            coach_item = NhlCoach.from_dict(coach_item_data)

            coach.append(coach_item)

        nhl_team_roster_response = cls(
            team=team,
            athletes=athletes,
            timestamp=timestamp,
            status=status,
            season=season,
            coach=coach,
        )

        nhl_team_roster_response.additional_properties = d
        return nhl_team_roster_response

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
