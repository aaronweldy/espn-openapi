from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.athlete_stats_response_teams import AthleteStatsResponseTeams
    from ..models.glossary_entry import GlossaryEntry
    from ..models.stats_category import StatsCategory
    from ..models.stats_filter import StatsFilter


T = TypeVar("T", bound="AthleteStatsResponse")


@_attrs_define
class AthleteStatsResponse:
    """
    Attributes:
        filters (List['StatsFilter']): Available filters for statistics
        teams (AthleteStatsResponseTeams): Teams the athlete has played for
        categories (List['StatsCategory']): Statistical categories
        glossary (List['GlossaryEntry']): Definitions for abbreviations
    """

    filters: List["StatsFilter"]
    teams: "AthleteStatsResponseTeams"
    categories: List["StatsCategory"]
    glossary: List["GlossaryEntry"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()
            filters.append(filters_item)

        teams = self.teams.to_dict()

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        glossary = []
        for glossary_item_data in self.glossary:
            glossary_item = glossary_item_data.to_dict()
            glossary.append(glossary_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
                "teams": teams,
                "categories": categories,
                "glossary": glossary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_stats_response_teams import AthleteStatsResponseTeams
        from ..models.glossary_entry import GlossaryEntry
        from ..models.stats_category import StatsCategory
        from ..models.stats_filter import StatsFilter

        d = src_dict.copy()
        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = StatsFilter.from_dict(filters_item_data)

            filters.append(filters_item)

        teams = AthleteStatsResponseTeams.from_dict(d.pop("teams"))

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = StatsCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        glossary = []
        _glossary = d.pop("glossary")
        for glossary_item_data in _glossary:
            glossary_item = GlossaryEntry.from_dict(glossary_item_data)

            glossary.append(glossary_item)

        athlete_stats_response = cls(
            filters=filters,
            teams=teams,
            categories=categories,
            glossary=glossary,
        )

        athlete_stats_response.additional_properties = d
        return athlete_stats_response

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
