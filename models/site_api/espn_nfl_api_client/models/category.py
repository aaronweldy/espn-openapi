from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_athlete import CategoryAthlete
    from ..models.category_contributor import CategoryContributor
    from ..models.category_league import CategoryLeague
    from ..models.category_team import CategoryTeam


T = TypeVar("T", bound="Category")


@_attrs_define
class Category:
    """
    Attributes:
        type (str): Category type (e.g., "athlete", "team", "league", "topic", "contributor")
        id (Union[Unset, int]): Category ID
        description (Union[Unset, str]): Category name/description
        sport_id (Union[Unset, int]): ID of the sport if sports-related
        league_id (Union[Unset, int]): ID of the league if league-related
        team_id (Union[Unset, int]): ID of the team if team-related
        athlete_id (Union[Unset, int]): ID of the athlete if athlete-related
        topic_id (Union[Unset, int]): ID of the topic if topic-related
        guid (Union[Unset, str]): Global unique identifier
        uid (Union[Unset, str]): Universal identifier
        slug (Union[Unset, str]): URL slug
        contributor (Union[Unset, CategoryContributor]):
        athlete (Union[Unset, CategoryAthlete]):
        team (Union[Unset, CategoryTeam]):
        league (Union[Unset, CategoryLeague]):
    """

    type: str
    id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    sport_id: Union[Unset, int] = UNSET
    league_id: Union[Unset, int] = UNSET
    team_id: Union[Unset, int] = UNSET
    athlete_id: Union[Unset, int] = UNSET
    topic_id: Union[Unset, int] = UNSET
    guid: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    contributor: Union[Unset, "CategoryContributor"] = UNSET
    athlete: Union[Unset, "CategoryAthlete"] = UNSET
    team: Union[Unset, "CategoryTeam"] = UNSET
    league: Union[Unset, "CategoryLeague"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        id = self.id

        description = self.description

        sport_id = self.sport_id

        league_id = self.league_id

        team_id = self.team_id

        athlete_id = self.athlete_id

        topic_id = self.topic_id

        guid = self.guid

        uid = self.uid

        slug = self.slug

        contributor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contributor, Unset):
            contributor = self.contributor.to_dict()

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
        field_dict.update(
            {
                "type": type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if sport_id is not UNSET:
            field_dict["sportId"] = sport_id
        if league_id is not UNSET:
            field_dict["leagueId"] = league_id
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if athlete_id is not UNSET:
            field_dict["athleteId"] = athlete_id
        if topic_id is not UNSET:
            field_dict["topicId"] = topic_id
        if guid is not UNSET:
            field_dict["guid"] = guid
        if uid is not UNSET:
            field_dict["uid"] = uid
        if slug is not UNSET:
            field_dict["slug"] = slug
        if contributor is not UNSET:
            field_dict["contributor"] = contributor
        if athlete is not UNSET:
            field_dict["athlete"] = athlete
        if team is not UNSET:
            field_dict["team"] = team
        if league is not UNSET:
            field_dict["league"] = league

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.category_athlete import CategoryAthlete
        from ..models.category_contributor import CategoryContributor
        from ..models.category_league import CategoryLeague
        from ..models.category_team import CategoryTeam

        d = src_dict.copy()
        type = d.pop("type")

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        sport_id = d.pop("sportId", UNSET)

        league_id = d.pop("leagueId", UNSET)

        team_id = d.pop("teamId", UNSET)

        athlete_id = d.pop("athleteId", UNSET)

        topic_id = d.pop("topicId", UNSET)

        guid = d.pop("guid", UNSET)

        uid = d.pop("uid", UNSET)

        slug = d.pop("slug", UNSET)

        _contributor = d.pop("contributor", UNSET)
        contributor: Union[Unset, CategoryContributor]
        if isinstance(_contributor, Unset):
            contributor = UNSET
        else:
            contributor = CategoryContributor.from_dict(_contributor)

        _athlete = d.pop("athlete", UNSET)
        athlete: Union[Unset, CategoryAthlete]
        if isinstance(_athlete, Unset):
            athlete = UNSET
        else:
            athlete = CategoryAthlete.from_dict(_athlete)

        _team = d.pop("team", UNSET)
        team: Union[Unset, CategoryTeam]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = CategoryTeam.from_dict(_team)

        _league = d.pop("league", UNSET)
        league: Union[Unset, CategoryLeague]
        if isinstance(_league, Unset):
            league = UNSET
        else:
            league = CategoryLeague.from_dict(_league)

        category = cls(
            type=type,
            id=id,
            description=description,
            sport_id=sport_id,
            league_id=league_id,
            team_id=team_id,
            athlete_id=athlete_id,
            topic_id=topic_id,
            guid=guid,
            uid=uid,
            slug=slug,
            contributor=contributor,
            athlete=athlete,
            team=team,
            league=league,
        )

        category.additional_properties = d
        return category

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
