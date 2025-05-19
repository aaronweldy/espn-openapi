import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.mlb_coach import MlbCoach
    from ..models.mlb_position_group import MlbPositionGroup
    from ..models.mlb_team_roster_response_season import MlbTeamRosterResponseSeason
    from ..models.mlb_team_roster_response_team import MlbTeamRosterResponseTeam


T = TypeVar("T", bound="MlbTeamRosterResponse")


@_attrs_define
class MlbTeamRosterResponse:
    """The response for an MLB team roster request

    Attributes:
        timestamp (datetime.datetime): The timestamp of when the data was generated
        status (str): The status of the response
        season (MlbTeamRosterResponseSeason):
        athletes (List['MlbPositionGroup']): List of roster position groups
        coach (List['MlbCoach']): List of coaches for the team
        team (MlbTeamRosterResponseTeam):
    """

    timestamp: datetime.datetime
    status: str
    season: "MlbTeamRosterResponseSeason"
    athletes: List["MlbPositionGroup"]
    coach: List["MlbCoach"]
    team: "MlbTeamRosterResponseTeam"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        status = self.status

        season = self.season.to_dict()

        athletes = []
        for athletes_item_data in self.athletes:
            athletes_item = athletes_item_data.to_dict()
            athletes.append(athletes_item)

        coach = []
        for coach_item_data in self.coach:
            coach_item = coach_item_data.to_dict()
            coach.append(coach_item)

        team = self.team.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "status": status,
                "season": season,
                "athletes": athletes,
                "coach": coach,
                "team": team,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.mlb_coach import MlbCoach
        from ..models.mlb_position_group import MlbPositionGroup
        from ..models.mlb_team_roster_response_season import MlbTeamRosterResponseSeason
        from ..models.mlb_team_roster_response_team import MlbTeamRosterResponseTeam

        d = src_dict.copy()
        timestamp = isoparse(d.pop("timestamp"))

        status = d.pop("status")

        season = MlbTeamRosterResponseSeason.from_dict(d.pop("season"))

        athletes = []
        _athletes = d.pop("athletes")
        for athletes_item_data in _athletes:
            athletes_item = MlbPositionGroup.from_dict(athletes_item_data)

            athletes.append(athletes_item)

        coach = []
        _coach = d.pop("coach")
        for coach_item_data in _coach:
            coach_item = MlbCoach.from_dict(coach_item_data)

            coach.append(coach_item)

        team = MlbTeamRosterResponseTeam.from_dict(d.pop("team"))

        mlb_team_roster_response = cls(
            timestamp=timestamp,
            status=status,
            season=season,
            athletes=athletes,
            coach=coach,
            team=team,
        )

        mlb_team_roster_response.additional_properties = d
        return mlb_team_roster_response

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
