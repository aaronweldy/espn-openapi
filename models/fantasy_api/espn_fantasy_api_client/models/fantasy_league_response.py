from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_team import FantasyTeam
    from ..models.league_communication import LeagueCommunication
    from ..models.league_member import LeagueMember
    from ..models.league_settings import LeagueSettings
    from ..models.league_status import LeagueStatus
    from ..models.schedule_item import ScheduleItem


T = TypeVar("T", bound="FantasyLeagueResponse")


@_attrs_define
class FantasyLeagueResponse:
    """
    Attributes:
        game_id (int): ID of the fantasy game (1 = fantasy football) Example: 1.
        id (int): League ID Example: 12345678.
        name (str): League name Example: Example League.
        season_id (int): Season year Example: 2023.
        segment_id (int): League segment (0 = regular season)
        abbreviation (Union[Unset, str]): League abbreviation Example: EXL.
        is_public (Union[Unset, bool]): Whether the league is public
        settings (Union[Unset, LeagueSettings]):
        status (Union[Unset, LeagueStatus]):
        teams (Union[Unset, List['FantasyTeam']]):
        members (Union[Unset, List['LeagueMember']]):
        schedule (Union[Unset, List['ScheduleItem']]):
        communication (Union[Unset, LeagueCommunication]):
    """

    game_id: int
    id: int
    name: str
    season_id: int
    segment_id: int
    abbreviation: Union[Unset, str] = UNSET
    is_public: Union[Unset, bool] = UNSET
    settings: Union[Unset, "LeagueSettings"] = UNSET
    status: Union[Unset, "LeagueStatus"] = UNSET
    teams: Union[Unset, List["FantasyTeam"]] = UNSET
    members: Union[Unset, List["LeagueMember"]] = UNSET
    schedule: Union[Unset, List["ScheduleItem"]] = UNSET
    communication: Union[Unset, "LeagueCommunication"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        game_id = self.game_id

        id = self.id

        name = self.name

        season_id = self.season_id

        segment_id = self.segment_id

        abbreviation = self.abbreviation

        is_public = self.is_public

        settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        teams: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)

        members: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        schedule: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = []
            for schedule_item_data in self.schedule:
                schedule_item = schedule_item_data.to_dict()
                schedule.append(schedule_item)

        communication: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.communication, Unset):
            communication = self.communication.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gameId": game_id,
                "id": id,
                "name": name,
                "seasonId": season_id,
                "segmentId": segment_id,
            }
        )
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if settings is not UNSET:
            field_dict["settings"] = settings
        if status is not UNSET:
            field_dict["status"] = status
        if teams is not UNSET:
            field_dict["teams"] = teams
        if members is not UNSET:
            field_dict["members"] = members
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if communication is not UNSET:
            field_dict["communication"] = communication

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_team import FantasyTeam
        from ..models.league_communication import LeagueCommunication
        from ..models.league_member import LeagueMember
        from ..models.league_settings import LeagueSettings
        from ..models.league_status import LeagueStatus
        from ..models.schedule_item import ScheduleItem

        d = src_dict.copy()
        game_id = d.pop("gameId")

        id = d.pop("id")

        name = d.pop("name")

        season_id = d.pop("seasonId")

        segment_id = d.pop("segmentId")

        abbreviation = d.pop("abbreviation", UNSET)

        is_public = d.pop("isPublic", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, LeagueSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = LeagueSettings.from_dict(_settings)

        _status = d.pop("status", UNSET)
        status: Union[Unset, LeagueStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LeagueStatus.from_dict(_status)

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = FantasyTeam.from_dict(teams_item_data)

            teams.append(teams_item)

        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = LeagueMember.from_dict(members_item_data)

            members.append(members_item)

        schedule = []
        _schedule = d.pop("schedule", UNSET)
        for schedule_item_data in _schedule or []:
            schedule_item = ScheduleItem.from_dict(schedule_item_data)

            schedule.append(schedule_item)

        _communication = d.pop("communication", UNSET)
        communication: Union[Unset, LeagueCommunication]
        if isinstance(_communication, Unset):
            communication = UNSET
        else:
            communication = LeagueCommunication.from_dict(_communication)

        fantasy_league_response = cls(
            game_id=game_id,
            id=id,
            name=name,
            season_id=season_id,
            segment_id=segment_id,
            abbreviation=abbreviation,
            is_public=is_public,
            settings=settings,
            status=status,
            teams=teams,
            members=members,
            schedule=schedule,
            communication=communication,
        )

        fantasy_league_response.additional_properties = d
        return fantasy_league_response

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
