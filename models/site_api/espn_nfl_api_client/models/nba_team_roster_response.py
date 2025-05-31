import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coach import Coach
    from ..models.nba_team_roster_response_season import NBATeamRosterResponseSeason
    from ..models.nba_team_roster_response_team import NBATeamRosterResponseTeam
    from ..models.roster_athlete import RosterAthlete


T = TypeVar("T", bound="NBATeamRosterResponse")


@_attrs_define
class NBATeamRosterResponse:
    """Response for NBA team roster

    Attributes:
        timestamp (Union[Unset, datetime.datetime]): The timestamp of when the data was generated
        status (Union[Unset, str]): The status of the response
        season (Union[Unset, NBATeamRosterResponseSeason]):
        athletes (Union[Unset, List['RosterAthlete']]): List of players on the roster
        coach (Union[Unset, List['Coach']]): List of coaches for the team
        team (Union[Unset, NBATeamRosterResponseTeam]):
    """

    timestamp: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, str] = UNSET
    season: Union[Unset, "NBATeamRosterResponseSeason"] = UNSET
    athletes: Union[Unset, List["RosterAthlete"]] = UNSET
    coach: Union[Unset, List["Coach"]] = UNSET
    team: Union[Unset, "NBATeamRosterResponseTeam"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        status = self.status

        season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        athletes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.athletes, Unset):
            athletes = []
            for athletes_item_data in self.athletes:
                athletes_item = athletes_item_data.to_dict()
                athletes.append(athletes_item)

        coach: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.coach, Unset):
            coach = []
            for coach_item_data in self.coach:
                coach_item = coach_item_data.to_dict()
                coach.append(coach_item)

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if status is not UNSET:
            field_dict["status"] = status
        if season is not UNSET:
            field_dict["season"] = season
        if athletes is not UNSET:
            field_dict["athletes"] = athletes
        if coach is not UNSET:
            field_dict["coach"] = coach
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.coach import Coach
        from ..models.nba_team_roster_response_season import NBATeamRosterResponseSeason
        from ..models.nba_team_roster_response_team import NBATeamRosterResponseTeam
        from ..models.roster_athlete import RosterAthlete

        d = src_dict.copy()
        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        status = d.pop("status", UNSET)

        _season = d.pop("season", UNSET)
        season: Union[Unset, NBATeamRosterResponseSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = NBATeamRosterResponseSeason.from_dict(_season)

        athletes = []
        _athletes = d.pop("athletes", UNSET)
        for athletes_item_data in _athletes or []:
            athletes_item = RosterAthlete.from_dict(athletes_item_data)

            athletes.append(athletes_item)

        coach = []
        _coach = d.pop("coach", UNSET)
        for coach_item_data in _coach or []:
            coach_item = Coach.from_dict(coach_item_data)

            coach.append(coach_item)

        _team = d.pop("team", UNSET)
        team: Union[Unset, NBATeamRosterResponseTeam]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = NBATeamRosterResponseTeam.from_dict(_team)

        nba_team_roster_response = cls(
            timestamp=timestamp,
            status=status,
            season=season,
            athletes=athletes,
            coach=coach,
            team=team,
        )

        nba_team_roster_response.additional_properties = d
        return nba_team_roster_response

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
