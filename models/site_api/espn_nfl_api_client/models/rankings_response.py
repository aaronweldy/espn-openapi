from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ranking import Ranking
    from ..models.rankings_response_available_rankings_item import RankingsResponseAvailableRankingsItem
    from ..models.rankings_response_latest_season import RankingsResponseLatestSeason
    from ..models.rankings_response_latest_week import RankingsResponseLatestWeek
    from ..models.rankings_response_leagues_item import RankingsResponseLeaguesItem
    from ..models.rankings_response_requested_season import RankingsResponseRequestedSeason
    from ..models.rankings_response_sports_item import RankingsResponseSportsItem
    from ..models.rankings_response_week_counts import RankingsResponseWeekCounts
    from ..models.rankings_response_weeks_item import RankingsResponseWeeksItem


T = TypeVar("T", bound="RankingsResponse")


@_attrs_define
class RankingsResponse:
    """College sports rankings response

    Attributes:
        rankings (Union[Unset, List['Ranking']]): Array of different ranking systems (AP Poll, Coaches Poll, etc.)
        available_rankings (Union[Unset, List['RankingsResponseAvailableRankingsItem']]): List of available ranking
            types
        latest_season (Union[Unset, RankingsResponseLatestSeason]): Information about the latest season
        latest_week (Union[Unset, RankingsResponseLatestWeek]): Information about the latest week
        requested_season (Union[Unset, RankingsResponseRequestedSeason]): The season that was requested
        weeks (Union[Unset, List['RankingsResponseWeeksItem']]): Available weeks for rankings
        week_counts (Union[Unset, RankingsResponseWeekCounts]): Week count information
        sports (Union[Unset, List['RankingsResponseSportsItem']]): Sports information
        leagues (Union[Unset, List['RankingsResponseLeaguesItem']]): League information
    """

    rankings: Union[Unset, List["Ranking"]] = UNSET
    available_rankings: Union[Unset, List["RankingsResponseAvailableRankingsItem"]] = UNSET
    latest_season: Union[Unset, "RankingsResponseLatestSeason"] = UNSET
    latest_week: Union[Unset, "RankingsResponseLatestWeek"] = UNSET
    requested_season: Union[Unset, "RankingsResponseRequestedSeason"] = UNSET
    weeks: Union[Unset, List["RankingsResponseWeeksItem"]] = UNSET
    week_counts: Union[Unset, "RankingsResponseWeekCounts"] = UNSET
    sports: Union[Unset, List["RankingsResponseSportsItem"]] = UNSET
    leagues: Union[Unset, List["RankingsResponseLeaguesItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rankings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rankings, Unset):
            rankings = []
            for rankings_item_data in self.rankings:
                rankings_item = rankings_item_data.to_dict()
                rankings.append(rankings_item)

        available_rankings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.available_rankings, Unset):
            available_rankings = []
            for available_rankings_item_data in self.available_rankings:
                available_rankings_item = available_rankings_item_data.to_dict()
                available_rankings.append(available_rankings_item)

        latest_season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.latest_season, Unset):
            latest_season = self.latest_season.to_dict()

        latest_week: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.latest_week, Unset):
            latest_week = self.latest_week.to_dict()

        requested_season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.requested_season, Unset):
            requested_season = self.requested_season.to_dict()

        weeks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.weeks, Unset):
            weeks = []
            for weeks_item_data in self.weeks:
                weeks_item = weeks_item_data.to_dict()
                weeks.append(weeks_item)

        week_counts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.week_counts, Unset):
            week_counts = self.week_counts.to_dict()

        sports: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sports, Unset):
            sports = []
            for sports_item_data in self.sports:
                sports_item = sports_item_data.to_dict()
                sports.append(sports_item)

        leagues: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.leagues, Unset):
            leagues = []
            for leagues_item_data in self.leagues:
                leagues_item = leagues_item_data.to_dict()
                leagues.append(leagues_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rankings is not UNSET:
            field_dict["rankings"] = rankings
        if available_rankings is not UNSET:
            field_dict["availableRankings"] = available_rankings
        if latest_season is not UNSET:
            field_dict["latestSeason"] = latest_season
        if latest_week is not UNSET:
            field_dict["latestWeek"] = latest_week
        if requested_season is not UNSET:
            field_dict["requestedSeason"] = requested_season
        if weeks is not UNSET:
            field_dict["weeks"] = weeks
        if week_counts is not UNSET:
            field_dict["weekCounts"] = week_counts
        if sports is not UNSET:
            field_dict["sports"] = sports
        if leagues is not UNSET:
            field_dict["leagues"] = leagues

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ranking import Ranking
        from ..models.rankings_response_available_rankings_item import RankingsResponseAvailableRankingsItem
        from ..models.rankings_response_latest_season import RankingsResponseLatestSeason
        from ..models.rankings_response_latest_week import RankingsResponseLatestWeek
        from ..models.rankings_response_leagues_item import RankingsResponseLeaguesItem
        from ..models.rankings_response_requested_season import RankingsResponseRequestedSeason
        from ..models.rankings_response_sports_item import RankingsResponseSportsItem
        from ..models.rankings_response_week_counts import RankingsResponseWeekCounts
        from ..models.rankings_response_weeks_item import RankingsResponseWeeksItem

        d = src_dict.copy()
        rankings = []
        _rankings = d.pop("rankings", UNSET)
        for rankings_item_data in _rankings or []:
            rankings_item = Ranking.from_dict(rankings_item_data)

            rankings.append(rankings_item)

        available_rankings = []
        _available_rankings = d.pop("availableRankings", UNSET)
        for available_rankings_item_data in _available_rankings or []:
            available_rankings_item = RankingsResponseAvailableRankingsItem.from_dict(available_rankings_item_data)

            available_rankings.append(available_rankings_item)

        _latest_season = d.pop("latestSeason", UNSET)
        latest_season: Union[Unset, RankingsResponseLatestSeason]
        if isinstance(_latest_season, Unset):
            latest_season = UNSET
        else:
            latest_season = RankingsResponseLatestSeason.from_dict(_latest_season)

        _latest_week = d.pop("latestWeek", UNSET)
        latest_week: Union[Unset, RankingsResponseLatestWeek]
        if isinstance(_latest_week, Unset):
            latest_week = UNSET
        else:
            latest_week = RankingsResponseLatestWeek.from_dict(_latest_week)

        _requested_season = d.pop("requestedSeason", UNSET)
        requested_season: Union[Unset, RankingsResponseRequestedSeason]
        if isinstance(_requested_season, Unset):
            requested_season = UNSET
        else:
            requested_season = RankingsResponseRequestedSeason.from_dict(_requested_season)

        weeks = []
        _weeks = d.pop("weeks", UNSET)
        for weeks_item_data in _weeks or []:
            weeks_item = RankingsResponseWeeksItem.from_dict(weeks_item_data)

            weeks.append(weeks_item)

        _week_counts = d.pop("weekCounts", UNSET)
        week_counts: Union[Unset, RankingsResponseWeekCounts]
        if isinstance(_week_counts, Unset):
            week_counts = UNSET
        else:
            week_counts = RankingsResponseWeekCounts.from_dict(_week_counts)

        sports = []
        _sports = d.pop("sports", UNSET)
        for sports_item_data in _sports or []:
            sports_item = RankingsResponseSportsItem.from_dict(sports_item_data)

            sports.append(sports_item)

        leagues = []
        _leagues = d.pop("leagues", UNSET)
        for leagues_item_data in _leagues or []:
            leagues_item = RankingsResponseLeaguesItem.from_dict(leagues_item_data)

            leagues.append(leagues_item)

        rankings_response = cls(
            rankings=rankings,
            available_rankings=available_rankings,
            latest_season=latest_season,
            latest_week=latest_week,
            requested_season=requested_season,
            weeks=weeks,
            week_counts=week_counts,
            sports=sports,
            leagues=leagues,
        )

        rankings_response.additional_properties = d
        return rankings_response

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
