from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pro_team_pro_games_by_scoring_period import ProTeamProGamesByScoringPeriod
    from ..models.pro_team_team_players_by_position import ProTeamTeamPlayersByPosition


T = TypeVar("T", bound="ProTeam")


@_attrs_define
class ProTeam:
    """
    Attributes:
        abbrev (Union[Unset, str]): Team abbreviation
        bye_week (Union[Unset, int]): Week number of the team's bye week
        id (Union[Unset, int]): Team ID
        location (Union[Unset, str]): Team location/city
        name (Union[Unset, str]): Team name
        pro_games_by_scoring_period (Union[Unset, ProTeamProGamesByScoringPeriod]): Games organized by scoring period
        team_players_by_position (Union[Unset, ProTeamTeamPlayersByPosition]): Player IDs by position
        universe_id (Union[Unset, int]): Universe ID for the team
    """

    abbrev: Union[Unset, str] = UNSET
    bye_week: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    pro_games_by_scoring_period: Union[Unset, "ProTeamProGamesByScoringPeriod"] = UNSET
    team_players_by_position: Union[Unset, "ProTeamTeamPlayersByPosition"] = UNSET
    universe_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        abbrev = self.abbrev

        bye_week = self.bye_week

        id = self.id

        location = self.location

        name = self.name

        pro_games_by_scoring_period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pro_games_by_scoring_period, Unset):
            pro_games_by_scoring_period = self.pro_games_by_scoring_period.to_dict()

        team_players_by_position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team_players_by_position, Unset):
            team_players_by_position = self.team_players_by_position.to_dict()

        universe_id = self.universe_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if abbrev is not UNSET:
            field_dict["abbrev"] = abbrev
        if bye_week is not UNSET:
            field_dict["byeWeek"] = bye_week
        if id is not UNSET:
            field_dict["id"] = id
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if pro_games_by_scoring_period is not UNSET:
            field_dict["proGamesByScoringPeriod"] = pro_games_by_scoring_period
        if team_players_by_position is not UNSET:
            field_dict["teamPlayersByPosition"] = team_players_by_position
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pro_team_pro_games_by_scoring_period import ProTeamProGamesByScoringPeriod
        from ..models.pro_team_team_players_by_position import ProTeamTeamPlayersByPosition

        d = src_dict.copy()
        abbrev = d.pop("abbrev", UNSET)

        bye_week = d.pop("byeWeek", UNSET)

        id = d.pop("id", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        _pro_games_by_scoring_period = d.pop("proGamesByScoringPeriod", UNSET)
        pro_games_by_scoring_period: Union[Unset, ProTeamProGamesByScoringPeriod]
        if isinstance(_pro_games_by_scoring_period, Unset):
            pro_games_by_scoring_period = UNSET
        else:
            pro_games_by_scoring_period = ProTeamProGamesByScoringPeriod.from_dict(_pro_games_by_scoring_period)

        _team_players_by_position = d.pop("teamPlayersByPosition", UNSET)
        team_players_by_position: Union[Unset, ProTeamTeamPlayersByPosition]
        if isinstance(_team_players_by_position, Unset):
            team_players_by_position = UNSET
        else:
            team_players_by_position = ProTeamTeamPlayersByPosition.from_dict(_team_players_by_position)

        universe_id = d.pop("universeId", UNSET)

        pro_team = cls(
            abbrev=abbrev,
            bye_week=bye_week,
            id=id,
            location=location,
            name=name,
            pro_games_by_scoring_period=pro_games_by_scoring_period,
            team_players_by_position=team_players_by_position,
            universe_id=universe_id,
        )

        pro_team.additional_properties = d
        return pro_team

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
