from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.league_reference import LeagueReference
    from ..models.sport_reference import SportReference
    from ..models.team_reference import TeamReference


T = TypeVar("T", bound="SearchResult")


@_attrs_define
class SearchResult:
    """
    Attributes:
        type (str): Type of search result (athlete, team, article, etc.) Example: athlete.
        id (str):  Example: 3139477.
        name (str):  Example: Patrick Mahomes.
        uid (Union[Unset, str]):  Example: s:20~l:28~a:3139477.
        description (Union[Unset, str]):  Example: Kansas City Chiefs quarterback.
        sport (Union[Unset, SportReference]):
        league (Union[Unset, LeagueReference]):
        team (Union[Unset, TeamReference]):
        image (Union[Unset, str]):  Example: https://a.espncdn.com/i/headshots/nfl/players/full/3139477.png.
        url (Union[Unset, str]):  Example: https://www.espn.com/nfl/player/_/id/3139477/patrick-mahomes.
    """

    type: str
    id: str
    name: str
    uid: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    sport: Union[Unset, "SportReference"] = UNSET
    league: Union[Unset, "LeagueReference"] = UNSET
    team: Union[Unset, "TeamReference"] = UNSET
    image: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        id = self.id

        name = self.name

        uid = self.uid

        description = self.description

        sport: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sport, Unset):
            sport = self.sport.to_dict()

        league: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.league, Unset):
            league = self.league.to_dict()

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        image = self.image

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "id": id,
                "name": name,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if description is not UNSET:
            field_dict["description"] = description
        if sport is not UNSET:
            field_dict["sport"] = sport
        if league is not UNSET:
            field_dict["league"] = league
        if team is not UNSET:
            field_dict["team"] = team
        if image is not UNSET:
            field_dict["image"] = image
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.league_reference import LeagueReference
        from ..models.sport_reference import SportReference
        from ..models.team_reference import TeamReference

        d = src_dict.copy()
        type = d.pop("type")

        id = d.pop("id")

        name = d.pop("name")

        uid = d.pop("uid", UNSET)

        description = d.pop("description", UNSET)

        _sport = d.pop("sport", UNSET)
        sport: Union[Unset, SportReference]
        if isinstance(_sport, Unset):
            sport = UNSET
        else:
            sport = SportReference.from_dict(_sport)

        _league = d.pop("league", UNSET)
        league: Union[Unset, LeagueReference]
        if isinstance(_league, Unset):
            league = UNSET
        else:
            league = LeagueReference.from_dict(_league)

        _team = d.pop("team", UNSET)
        team: Union[Unset, TeamReference]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = TeamReference.from_dict(_team)

        image = d.pop("image", UNSET)

        url = d.pop("url", UNSET)

        search_result = cls(
            type=type,
            id=id,
            name=name,
            uid=uid,
            description=description,
            sport=sport,
            league=league,
            team=team,
            image=image,
            url=url,
        )

        search_result.additional_properties = d
        return search_result

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
