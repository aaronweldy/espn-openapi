import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coach import Coach
    from ..models.position_group import PositionGroup
    from ..models.roster_athlete import RosterAthlete
    from ..models.season import Season
    from ..models.team import Team


T = TypeVar("T", bound="TeamRosterResponse")


@_attrs_define
class TeamRosterResponse:
    """The response for a team roster request

    Attributes:
        timestamp (Union[Unset, datetime.datetime]): The timestamp of when the data was generated
        status (Union[Unset, str]): The status of the response
        season (Union[Unset, Season]):
        team (Union[Unset, Team]):
        coach (Union[Unset, List['Coach']]): List of coaches for the team
        athletes (Union[Unset, List[Union['PositionGroup', 'RosterAthlete']]]): List of athletes or position groups
            depending on sport
    """

    timestamp: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, str] = UNSET
    season: Union[Unset, "Season"] = UNSET
    team: Union[Unset, "Team"] = UNSET
    coach: Union[Unset, List["Coach"]] = UNSET
    athletes: Union[Unset, List[Union["PositionGroup", "RosterAthlete"]]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.position_group import PositionGroup

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        status = self.status

        season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        coach: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.coach, Unset):
            coach = []
            for coach_item_data in self.coach:
                coach_item = coach_item_data.to_dict()
                coach.append(coach_item)

        athletes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.athletes, Unset):
            athletes = []
            for athletes_item_data in self.athletes:
                athletes_item: Dict[str, Any]
                if isinstance(athletes_item_data, PositionGroup):
                    athletes_item = athletes_item_data.to_dict()
                else:
                    athletes_item = athletes_item_data.to_dict()

                athletes.append(athletes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if status is not UNSET:
            field_dict["status"] = status
        if season is not UNSET:
            field_dict["season"] = season
        if team is not UNSET:
            field_dict["team"] = team
        if coach is not UNSET:
            field_dict["coach"] = coach
        if athletes is not UNSET:
            field_dict["athletes"] = athletes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.coach import Coach
        from ..models.position_group import PositionGroup
        from ..models.roster_athlete import RosterAthlete
        from ..models.season import Season
        from ..models.team import Team

        d = src_dict.copy()
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

        _team = d.pop("team", UNSET)
        team: Union[Unset, Team]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = Team.from_dict(_team)

        coach = []
        _coach = d.pop("coach", UNSET)
        for coach_item_data in _coach or []:
            coach_item = Coach.from_dict(coach_item_data)

            coach.append(coach_item)

        athletes = []
        _athletes = d.pop("athletes", UNSET)
        for athletes_item_data in _athletes or []:

            def _parse_athletes_item(data: object) -> Union["PositionGroup", "RosterAthlete"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    athletes_item_type_0 = PositionGroup.from_dict(data)

                    return athletes_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                athletes_item_type_1 = RosterAthlete.from_dict(data)

                return athletes_item_type_1

            athletes_item = _parse_athletes_item(athletes_item_data)

            athletes.append(athletes_item)

        team_roster_response = cls(
            timestamp=timestamp,
            status=status,
            season=season,
            team=team,
            coach=coach,
            athletes=athletes,
        )

        team_roster_response.additional_properties = d
        return team_roster_response

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
