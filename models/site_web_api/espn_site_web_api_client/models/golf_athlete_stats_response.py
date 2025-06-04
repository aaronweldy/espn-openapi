from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.glossary_entry import GlossaryEntry
    from ..models.golf_athlete_stats_response_leagues_stats_item import GolfAthleteStatsResponseLeaguesStatsItem
    from ..models.golf_statistics import GolfStatistics
    from ..models.stats_filter import StatsFilter


T = TypeVar("T", bound="GolfAthleteStatsResponse")


@_attrs_define
class GolfAthleteStatsResponse:
    """
    Attributes:
        filters (List['StatsFilter']): Available filters for statistics
        statistics (Union[Unset, GolfStatistics]):
        glossary (Union[Unset, List['GlossaryEntry']]): Definitions for statistical abbreviations
        leagues_stats (Union[Unset, List['GolfAthleteStatsResponseLeaguesStatsItem']]): League-specific statistics
    """

    filters: List["StatsFilter"]
    statistics: Union[Unset, "GolfStatistics"] = UNSET
    glossary: Union[Unset, List["GlossaryEntry"]] = UNSET
    leagues_stats: Union[Unset, List["GolfAthleteStatsResponseLeaguesStatsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()
            filters.append(filters_item)

        statistics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        glossary: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.glossary, Unset):
            glossary = []
            for glossary_item_data in self.glossary:
                glossary_item = glossary_item_data.to_dict()
                glossary.append(glossary_item)

        leagues_stats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.leagues_stats, Unset):
            leagues_stats = []
            for leagues_stats_item_data in self.leagues_stats:
                leagues_stats_item = leagues_stats_item_data.to_dict()
                leagues_stats.append(leagues_stats_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
            }
        )
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if glossary is not UNSET:
            field_dict["glossary"] = glossary
        if leagues_stats is not UNSET:
            field_dict["leaguesStats"] = leagues_stats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.glossary_entry import GlossaryEntry
        from ..models.golf_athlete_stats_response_leagues_stats_item import GolfAthleteStatsResponseLeaguesStatsItem
        from ..models.golf_statistics import GolfStatistics
        from ..models.stats_filter import StatsFilter

        d = src_dict.copy()
        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = StatsFilter.from_dict(filters_item_data)

            filters.append(filters_item)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, GolfStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = GolfStatistics.from_dict(_statistics)

        glossary = []
        _glossary = d.pop("glossary", UNSET)
        for glossary_item_data in _glossary or []:
            glossary_item = GlossaryEntry.from_dict(glossary_item_data)

            glossary.append(glossary_item)

        leagues_stats = []
        _leagues_stats = d.pop("leaguesStats", UNSET)
        for leagues_stats_item_data in _leagues_stats or []:
            leagues_stats_item = GolfAthleteStatsResponseLeaguesStatsItem.from_dict(leagues_stats_item_data)

            leagues_stats.append(leagues_stats_item)

        golf_athlete_stats_response = cls(
            filters=filters,
            statistics=statistics,
            glossary=glossary,
            leagues_stats=leagues_stats,
        )

        golf_athlete_stats_response.additional_properties = d
        return golf_athlete_stats_response

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
