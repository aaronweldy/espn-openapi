from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_contributor import ScoreboardContributor
    from ..models.scoreboard_league import ScoreboardLeague
    from ..models.scoreboard_team import ScoreboardTeam


T = TypeVar("T", bound="ScoreboardCategory")


@_attrs_define
class ScoreboardCategory:
    """
    Attributes:
        sport_id (Union[Unset, int]):
        topic_id (Union[Unset, int]):
        guid (Union[Unset, str]):
        description (Union[Unset, str]):
        id (Union[Unset, int]):
        type (Union[Unset, str]):
        team_id (Union[Unset, int]):
        team (Union[Unset, ScoreboardTeam]):
        league_id (Union[Unset, int]):
        league (Union[Unset, ScoreboardLeague]):
        contributor (Union[Unset, ScoreboardContributor]):
        slug (Union[Unset, str]):
        uid (Union[Unset, str]):
    """

    sport_id: Union[Unset, int] = UNSET
    topic_id: Union[Unset, int] = UNSET
    guid: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    team_id: Union[Unset, int] = UNSET
    team: Union[Unset, "ScoreboardTeam"] = UNSET
    league_id: Union[Unset, int] = UNSET
    league: Union[Unset, "ScoreboardLeague"] = UNSET
    contributor: Union[Unset, "ScoreboardContributor"] = UNSET
    slug: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sport_id = self.sport_id

        topic_id = self.topic_id

        guid = self.guid

        description = self.description

        id = self.id

        type = self.type

        team_id = self.team_id

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        league_id = self.league_id

        league: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.league, Unset):
            league = self.league.to_dict()

        contributor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contributor, Unset):
            contributor = self.contributor.to_dict()

        slug = self.slug

        uid = self.uid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sport_id is not UNSET:
            field_dict["sportId"] = sport_id
        if topic_id is not UNSET:
            field_dict["topicId"] = topic_id
        if guid is not UNSET:
            field_dict["guid"] = guid
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if team is not UNSET:
            field_dict["team"] = team
        if league_id is not UNSET:
            field_dict["leagueId"] = league_id
        if league is not UNSET:
            field_dict["league"] = league
        if contributor is not UNSET:
            field_dict["contributor"] = contributor
        if slug is not UNSET:
            field_dict["slug"] = slug
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_contributor import ScoreboardContributor
        from ..models.scoreboard_league import ScoreboardLeague
        from ..models.scoreboard_team import ScoreboardTeam

        d = src_dict.copy()
        sport_id = d.pop("sportId", UNSET)

        topic_id = d.pop("topicId", UNSET)

        guid = d.pop("guid", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        type = d.pop("type", UNSET)

        team_id = d.pop("teamId", UNSET)

        _team = d.pop("team", UNSET)
        team: Union[Unset, ScoreboardTeam]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = ScoreboardTeam.from_dict(_team)

        league_id = d.pop("leagueId", UNSET)

        _league = d.pop("league", UNSET)
        league: Union[Unset, ScoreboardLeague]
        if isinstance(_league, Unset):
            league = UNSET
        else:
            league = ScoreboardLeague.from_dict(_league)

        _contributor = d.pop("contributor", UNSET)
        contributor: Union[Unset, ScoreboardContributor]
        if isinstance(_contributor, Unset):
            contributor = UNSET
        else:
            contributor = ScoreboardContributor.from_dict(_contributor)

        slug = d.pop("slug", UNSET)

        uid = d.pop("uid", UNSET)

        scoreboard_category = cls(
            sport_id=sport_id,
            topic_id=topic_id,
            guid=guid,
            description=description,
            id=id,
            type=type,
            team_id=team_id,
            team=team,
            league_id=league_id,
            league=league,
            contributor=contributor,
            slug=slug,
            uid=uid,
        )

        scoreboard_category.additional_properties = d
        return scoreboard_category

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
