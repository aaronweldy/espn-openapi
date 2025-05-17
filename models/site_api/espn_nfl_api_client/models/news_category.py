from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.news_category_type import NewsCategoryType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.news_athlete import NewsAthlete
    from ..models.news_contributor import NewsContributor
    from ..models.news_league import NewsLeague
    from ..models.news_team import NewsTeam


T = TypeVar("T", bound="NewsCategory")


@_attrs_define
class NewsCategory:
    """
    Attributes:
        type (NewsCategoryType): Type of category Example: topic.
        guid (UUID): Global unique identifier Example: 52313677-19f8-b106-ec91-d8d17e6087fe.
        id (Union[Unset, int]): Category identifier Example: 409224.
        description (Union[Unset, str]): Description of the category Example: news.
        sport_id (Union[Unset, int]): Sport identifier Example: 28.
        topic_id (Union[Unset, int]): Topic identifier Example: 781.
        uid (Union[Unset, str]): Unique identifier with format Example: s:20~l:28~a:15846.
        athlete_id (Union[Unset, int]): Athlete identifier Example: 15846.
        athlete (Union[Unset, NewsAthlete]):
        team_id (Union[Unset, int]): Team identifier Example: 33.
        team (Union[Unset, NewsTeam]):
        slug (Union[Unset, str]): URL slug Example: jamison-hensley.
        contributor (Union[Unset, NewsContributor]):
        league_id (Union[Unset, int]): League identifier Example: 28.
        league (Union[Unset, NewsLeague]):
    """

    type: NewsCategoryType
    guid: UUID
    id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    sport_id: Union[Unset, int] = UNSET
    topic_id: Union[Unset, int] = UNSET
    uid: Union[Unset, str] = UNSET
    athlete_id: Union[Unset, int] = UNSET
    athlete: Union[Unset, "NewsAthlete"] = UNSET
    team_id: Union[Unset, int] = UNSET
    team: Union[Unset, "NewsTeam"] = UNSET
    slug: Union[Unset, str] = UNSET
    contributor: Union[Unset, "NewsContributor"] = UNSET
    league_id: Union[Unset, int] = UNSET
    league: Union[Unset, "NewsLeague"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        guid = str(self.guid)

        id = self.id

        description = self.description

        sport_id = self.sport_id

        topic_id = self.topic_id

        uid = self.uid

        athlete_id = self.athlete_id

        athlete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.athlete, Unset):
            athlete = self.athlete.to_dict()

        team_id = self.team_id

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        slug = self.slug

        contributor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contributor, Unset):
            contributor = self.contributor.to_dict()

        league_id = self.league_id

        league: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.league, Unset):
            league = self.league.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "guid": guid,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if sport_id is not UNSET:
            field_dict["sportId"] = sport_id
        if topic_id is not UNSET:
            field_dict["topicId"] = topic_id
        if uid is not UNSET:
            field_dict["uid"] = uid
        if athlete_id is not UNSET:
            field_dict["athleteId"] = athlete_id
        if athlete is not UNSET:
            field_dict["athlete"] = athlete
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if team is not UNSET:
            field_dict["team"] = team
        if slug is not UNSET:
            field_dict["slug"] = slug
        if contributor is not UNSET:
            field_dict["contributor"] = contributor
        if league_id is not UNSET:
            field_dict["leagueId"] = league_id
        if league is not UNSET:
            field_dict["league"] = league

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.news_athlete import NewsAthlete
        from ..models.news_contributor import NewsContributor
        from ..models.news_league import NewsLeague
        from ..models.news_team import NewsTeam

        d = src_dict.copy()
        type = NewsCategoryType(d.pop("type"))

        guid = UUID(d.pop("guid"))

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        sport_id = d.pop("sportId", UNSET)

        topic_id = d.pop("topicId", UNSET)

        uid = d.pop("uid", UNSET)

        athlete_id = d.pop("athleteId", UNSET)

        _athlete = d.pop("athlete", UNSET)
        athlete: Union[Unset, NewsAthlete]
        if isinstance(_athlete, Unset):
            athlete = UNSET
        else:
            athlete = NewsAthlete.from_dict(_athlete)

        team_id = d.pop("teamId", UNSET)

        _team = d.pop("team", UNSET)
        team: Union[Unset, NewsTeam]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = NewsTeam.from_dict(_team)

        slug = d.pop("slug", UNSET)

        _contributor = d.pop("contributor", UNSET)
        contributor: Union[Unset, NewsContributor]
        if isinstance(_contributor, Unset):
            contributor = UNSET
        else:
            contributor = NewsContributor.from_dict(_contributor)

        league_id = d.pop("leagueId", UNSET)

        _league = d.pop("league", UNSET)
        league: Union[Unset, NewsLeague]
        if isinstance(_league, Unset):
            league = UNSET
        else:
            league = NewsLeague.from_dict(_league)

        news_category = cls(
            type=type,
            guid=guid,
            id=id,
            description=description,
            sport_id=sport_id,
            topic_id=topic_id,
            uid=uid,
            athlete_id=athlete_id,
            athlete=athlete,
            team_id=team_id,
            team=team,
            slug=slug,
            contributor=contributor,
            league_id=league_id,
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
