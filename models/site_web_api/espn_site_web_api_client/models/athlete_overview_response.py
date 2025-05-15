from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.athlete_details import AthleteDetails
    from ..models.career_statistics import CareerStatistics
    from ..models.news_item_detailed import NewsItemDetailed
    from ..models.season import Season
    from ..models.team import Team
    from ..models.team_reference import TeamReference


T = TypeVar("T", bound="AthleteOverviewResponse")


@_attrs_define
class AthleteOverviewResponse:
    """
    Attributes:
        statistics (Union[Unset, CareerStatistics]):
        news (Union[Unset, List['NewsItemDetailed']]):
        athlete (Union[Unset, AthleteDetails]):
        teams (Union[Unset, List[Union['Team', 'TeamReference']]]):
        season (Union[Unset, Season]):
    """

    statistics: Union[Unset, "CareerStatistics"] = UNSET
    news: Union[Unset, List["NewsItemDetailed"]] = UNSET
    athlete: Union[Unset, "AthleteDetails"] = UNSET
    teams: Union[Unset, List[Union["Team", "TeamReference"]]] = UNSET
    season: Union[Unset, "Season"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.team import Team

        statistics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        news: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.news, Unset):
            news = []
            for news_item_data in self.news:
                news_item = news_item_data.to_dict()
                news.append(news_item)

        athlete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.athlete, Unset):
            athlete = self.athlete.to_dict()

        teams: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item: Dict[str, Any]
                if isinstance(teams_item_data, Team):
                    teams_item = teams_item_data.to_dict()
                else:
                    teams_item = teams_item_data.to_dict()

                teams.append(teams_item)

        season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if news is not UNSET:
            field_dict["news"] = news
        if athlete is not UNSET:
            field_dict["athlete"] = athlete
        if teams is not UNSET:
            field_dict["teams"] = teams
        if season is not UNSET:
            field_dict["season"] = season

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_details import AthleteDetails
        from ..models.career_statistics import CareerStatistics
        from ..models.news_item_detailed import NewsItemDetailed
        from ..models.season import Season
        from ..models.team import Team
        from ..models.team_reference import TeamReference

        d = src_dict.copy()
        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, CareerStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = CareerStatistics.from_dict(_statistics)

        news = []
        _news = d.pop("news", UNSET)
        for news_item_data in _news or []:
            news_item = NewsItemDetailed.from_dict(news_item_data)

            news.append(news_item)

        _athlete = d.pop("athlete", UNSET)
        athlete: Union[Unset, AthleteDetails]
        if isinstance(_athlete, Unset):
            athlete = UNSET
        else:
            athlete = AthleteDetails.from_dict(_athlete)

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:

            def _parse_teams_item(data: object) -> Union["Team", "TeamReference"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    teams_item_type_0 = Team.from_dict(data)

                    return teams_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                teams_item_type_1 = TeamReference.from_dict(data)

                return teams_item_type_1

            teams_item = _parse_teams_item(teams_item_data)

            teams.append(teams_item)

        _season = d.pop("season", UNSET)
        season: Union[Unset, Season]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = Season.from_dict(_season)

        athlete_overview_response = cls(
            statistics=statistics,
            news=news,
            athlete=athlete,
            teams=teams,
            season=season,
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
