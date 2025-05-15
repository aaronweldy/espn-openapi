import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.game_event_at_vs import GameEventAtVs
from ..models.game_event_game_result import GameEventGameResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.game_event_team import GameEventTeam
    from ..models.link import Link


T = TypeVar("T", bound="GameEvent")


@_attrs_define
class GameEvent:
    """
    Attributes:
        id (str):  Example: 401671788.
        game_date (datetime.datetime):  Example: 2024-12-09T01:20:00.000+00:00.
        score (str):  Example: 19-17.
        opponent (GameEventTeam):
        team (GameEventTeam):
        links (Union[Unset, List['Link']]):
        week (Union[Unset, int]):  Example: 14.
        at_vs (Union[Unset, GameEventAtVs]):  Example: vs.
        home_team_id (Union[Unset, str]):  Example: 12.
        away_team_id (Union[Unset, str]):  Example: 24.
        home_team_score (Union[Unset, str]):  Example: 19.
        away_team_score (Union[Unset, str]):  Example: 17.
        game_result (Union[Unset, GameEventGameResult]):  Example: W.
        league_name (Union[Unset, str]):  Example: National Football League.
        league_abbreviation (Union[Unset, str]):  Example: NFL.
        league_short_name (Union[Unset, str]):  Example: NFL.
    """

    id: str
    game_date: datetime.datetime
    score: str
    opponent: "GameEventTeam"
    team: "GameEventTeam"
    links: Union[Unset, List["Link"]] = UNSET
    week: Union[Unset, int] = UNSET
    at_vs: Union[Unset, GameEventAtVs] = UNSET
    home_team_id: Union[Unset, str] = UNSET
    away_team_id: Union[Unset, str] = UNSET
    home_team_score: Union[Unset, str] = UNSET
    away_team_score: Union[Unset, str] = UNSET
    game_result: Union[Unset, GameEventGameResult] = UNSET
    league_name: Union[Unset, str] = UNSET
    league_abbreviation: Union[Unset, str] = UNSET
    league_short_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        game_date = self.game_date.isoformat()

        score = self.score

        opponent = self.opponent.to_dict()

        team = self.team.to_dict()

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        week = self.week

        at_vs: Union[Unset, str] = UNSET
        if not isinstance(self.at_vs, Unset):
            at_vs = self.at_vs.value

        home_team_id = self.home_team_id

        away_team_id = self.away_team_id

        home_team_score = self.home_team_score

        away_team_score = self.away_team_score

        game_result: Union[Unset, str] = UNSET
        if not isinstance(self.game_result, Unset):
            game_result = self.game_result.value

        league_name = self.league_name

        league_abbreviation = self.league_abbreviation

        league_short_name = self.league_short_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "gameDate": game_date,
                "score": score,
                "opponent": opponent,
                "team": team,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links
        if week is not UNSET:
            field_dict["week"] = week
        if at_vs is not UNSET:
            field_dict["atVs"] = at_vs
        if home_team_id is not UNSET:
            field_dict["homeTeamId"] = home_team_id
        if away_team_id is not UNSET:
            field_dict["awayTeamId"] = away_team_id
        if home_team_score is not UNSET:
            field_dict["homeTeamScore"] = home_team_score
        if away_team_score is not UNSET:
            field_dict["awayTeamScore"] = away_team_score
        if game_result is not UNSET:
            field_dict["gameResult"] = game_result
        if league_name is not UNSET:
            field_dict["leagueName"] = league_name
        if league_abbreviation is not UNSET:
            field_dict["leagueAbbreviation"] = league_abbreviation
        if league_short_name is not UNSET:
            field_dict["leagueShortName"] = league_short_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.game_event_team import GameEventTeam
        from ..models.link import Link

        d = src_dict.copy()
        id = d.pop("id")

        game_date = isoparse(d.pop("gameDate"))

        score = d.pop("score")

        opponent = GameEventTeam.from_dict(d.pop("opponent"))

        team = GameEventTeam.from_dict(d.pop("team"))

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        week = d.pop("week", UNSET)

        _at_vs = d.pop("atVs", UNSET)
        at_vs: Union[Unset, GameEventAtVs]
        if isinstance(_at_vs, Unset):
            at_vs = UNSET
        else:
            at_vs = GameEventAtVs(_at_vs)

        home_team_id = d.pop("homeTeamId", UNSET)

        away_team_id = d.pop("awayTeamId", UNSET)

        home_team_score = d.pop("homeTeamScore", UNSET)

        away_team_score = d.pop("awayTeamScore", UNSET)

        _game_result = d.pop("gameResult", UNSET)
        game_result: Union[Unset, GameEventGameResult]
        if isinstance(_game_result, Unset):
            game_result = UNSET
        else:
            game_result = GameEventGameResult(_game_result)

        league_name = d.pop("leagueName", UNSET)

        league_abbreviation = d.pop("leagueAbbreviation", UNSET)

        league_short_name = d.pop("leagueShortName", UNSET)

        game_event = cls(
            id=id,
            game_date=game_date,
            score=score,
            opponent=opponent,
            team=team,
            links=links,
            week=week,
            at_vs=at_vs,
            home_team_id=home_team_id,
            away_team_id=away_team_id,
            home_team_score=home_team_score,
            away_team_score=away_team_score,
            game_result=game_result,
            league_name=league_name,
            league_abbreviation=league_abbreviation,
            league_short_name=league_short_name,
        )

        game_event.additional_properties = d
        return game_event

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
