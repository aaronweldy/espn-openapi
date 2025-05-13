from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.athlete_overview import AthleteOverview
    from ..models.injury_report import InjuryReport
    from ..models.league_reference import LeagueReference
    from ..models.news_item import NewsItem
    from ..models.position import Position
    from ..models.stat_category import StatCategory
    from ..models.team_reference import TeamReference


T = TypeVar("T", bound="AthleteOverviewResponse")


@_attrs_define
class AthleteOverviewResponse:
    """
    Attributes:
        athlete (AthleteOverview):
        league (Union[Unset, LeagueReference]):
        team (Union[Unset, TeamReference]):
        position (Union[Unset, Position]):
        stats (Union[Unset, List['StatCategory']]):
        news (Union[Unset, List['NewsItem']]):
        injuries (Union[Unset, List['InjuryReport']]):
    """

    athlete: "AthleteOverview"
    league: Union[Unset, "LeagueReference"] = UNSET
    team: Union[Unset, "TeamReference"] = UNSET
    position: Union[Unset, "Position"] = UNSET
    stats: Union[Unset, List["StatCategory"]] = UNSET
    news: Union[Unset, List["NewsItem"]] = UNSET
    injuries: Union[Unset, List["InjuryReport"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        athlete = self.athlete.to_dict()

        league: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.league, Unset):
            league = self.league.to_dict()

        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        stats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = []
            for stats_item_data in self.stats:
                stats_item = stats_item_data.to_dict()
                stats.append(stats_item)

        news: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.news, Unset):
            news = []
            for news_item_data in self.news:
                news_item = news_item_data.to_dict()
                news.append(news_item)

        injuries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.injuries, Unset):
            injuries = []
            for injuries_item_data in self.injuries:
                injuries_item = injuries_item_data.to_dict()
                injuries.append(injuries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "athlete": athlete,
            }
        )
        if league is not UNSET:
            field_dict["league"] = league
        if team is not UNSET:
            field_dict["team"] = team
        if position is not UNSET:
            field_dict["position"] = position
        if stats is not UNSET:
            field_dict["stats"] = stats
        if news is not UNSET:
            field_dict["news"] = news
        if injuries is not UNSET:
            field_dict["injuries"] = injuries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_overview import AthleteOverview
        from ..models.injury_report import InjuryReport
        from ..models.league_reference import LeagueReference
        from ..models.news_item import NewsItem
        from ..models.position import Position
        from ..models.stat_category import StatCategory
        from ..models.team_reference import TeamReference

        d = src_dict.copy()
        athlete = AthleteOverview.from_dict(d.pop("athlete"))

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

        _position = d.pop("position", UNSET)
        position: Union[Unset, Position]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = Position.from_dict(_position)

        stats = []
        _stats = d.pop("stats", UNSET)
        for stats_item_data in _stats or []:
            stats_item = StatCategory.from_dict(stats_item_data)

            stats.append(stats_item)

        news = []
        _news = d.pop("news", UNSET)
        for news_item_data in _news or []:
            news_item = NewsItem.from_dict(news_item_data)

            news.append(news_item)

        injuries = []
        _injuries = d.pop("injuries", UNSET)
        for injuries_item_data in _injuries or []:
            injuries_item = InjuryReport.from_dict(injuries_item_data)

            injuries.append(injuries_item)

        athlete_overview_response = cls(
            athlete=athlete,
            league=league,
            team=team,
            position=position,
            stats=stats,
            news=news,
            injuries=injuries,
        )

        athlete_overview_response.additional_properties = d
        return athlete_overview_response

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
