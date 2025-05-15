from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.news_category_athlete import NewsCategoryAthlete
    from ..models.news_category_league import NewsCategoryLeague
    from ..models.news_category_team import NewsCategoryTeam


T = TypeVar("T", bound="NewsCategory")


@_attrs_define
class NewsCategory:
    """
    Attributes:
        id (Union[Unset, int]):
        uid (Union[Unset, str]):
        description (Union[Unset, str]):
        type (Union[Unset, str]):
        sport_id (Union[None, Unset, int]):
        league_id (Union[None, Unset, int]):
        athlete_id (Union[None, Unset, int]):
        team_id (Union[None, Unset, int]):
        guid (Union[None, Unset, str]):
        athlete (Union[Unset, NewsCategoryAthlete]):
        team (Union[Unset, NewsCategoryTeam]):
        league (Union[Unset, NewsCategoryLeague]):
    """

    id: Union[Unset, int] = UNSET
    uid: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    sport_id: Union[None, Unset, int] = UNSET
    league_id: Union[None, Unset, int] = UNSET
    athlete_id: Union[None, Unset, int] = UNSET
    team_id: Union[None, Unset, int] = UNSET
    guid: Union[None, Unset, str] = UNSET
    athlete: Union[Unset, "NewsCategoryAthlete"] = UNSET
    team: Union[Unset, "NewsCategoryTeam"] = UNSET
    league: Union[Unset, "NewsCategoryLeague"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        uid = self.uid

        description = self.description

        type = self.type

        sport_id: Union[None, Unset, int]
        if isinstance(self.sport_id, Unset):
            sport_id = UNSET
        else:
            sport_id = self.sport_id

        league_id: Union[None, Unset, int]
        if isinstance(self.league_id, Unset):
            league_id = UNSET
        else:
            league_id = self.league_id

        athlete_id: Union[None, Unset, int]
        if isinstance(self.athlete_id, Unset):
            athlete_id = UNSET
        else:
            athlete_id = self.athlete_id

        team_id: Union[None, Unset, int]
        if isinstance(self.team_id, Unset):
            team_id = UNSET
        else:
            team_id = self.team_id

        guid: Union[None, Unset, str]
        if isinstance(self.guid, Unset):
            guid = UNSET
        else:
            guid = self.guid

        athlete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.athlete, Unset):
            athlete = self.athlete.to_dict()

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        league: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.league, Unset):
            league = self.league.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uid is not UNSET:
            field_dict["uid"] = uid
        if description is not UNSET:
            field_dict["description"] = description
        if type is not UNSET:
            field_dict["type"] = type
        if sport_id is not UNSET:
            field_dict["sportId"] = sport_id
        if league_id is not UNSET:
            field_dict["leagueId"] = league_id
        if athlete_id is not UNSET:
            field_dict["athleteId"] = athlete_id
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if guid is not UNSET:
            field_dict["guid"] = guid
        if athlete is not UNSET:
            field_dict["athlete"] = athlete
        if team is not UNSET:
            field_dict["team"] = team
        if league is not UNSET:
            field_dict["league"] = league

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.news_category_athlete import NewsCategoryAthlete
        from ..models.news_category_league import NewsCategoryLeague
        from ..models.news_category_team import NewsCategoryTeam

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        uid = d.pop("uid", UNSET)

        description = d.pop("description", UNSET)

        type = d.pop("type", UNSET)

        def _parse_sport_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sport_id = _parse_sport_id(d.pop("sportId", UNSET))

        def _parse_league_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        league_id = _parse_league_id(d.pop("leagueId", UNSET))

        def _parse_athlete_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        athlete_id = _parse_athlete_id(d.pop("athleteId", UNSET))

        def _parse_team_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        team_id = _parse_team_id(d.pop("teamId", UNSET))

        def _parse_guid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        guid = _parse_guid(d.pop("guid", UNSET))

        _athlete = d.pop("athlete", UNSET)
        athlete: Union[Unset, NewsCategoryAthlete]
        if isinstance(_athlete, Unset):
            athlete = UNSET
        else:
            athlete = NewsCategoryAthlete.from_dict(_athlete)

        _team = d.pop("team", UNSET)
        team: Union[Unset, NewsCategoryTeam]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = NewsCategoryTeam.from_dict(_team)

        _league = d.pop("league", UNSET)
        league: Union[Unset, NewsCategoryLeague]
        if isinstance(_league, Unset):
            league = UNSET
        else:
            league = NewsCategoryLeague.from_dict(_league)

        news_category = cls(
            id=id,
            uid=uid,
            description=description,
            type=type,
            sport_id=sport_id,
            league_id=league_id,
            athlete_id=athlete_id,
            team_id=team_id,
            guid=guid,
            athlete=athlete,
            team=team,
            league=league,
        )

        news_category.additional_properties = d
        return news_category

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
