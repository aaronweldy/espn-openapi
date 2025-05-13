from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.athlete_reference import AthleteReference
    from ..models.game_log_category import GameLogCategory
    from ..models.league_reference import LeagueReference
    from ..models.season import Season


T = TypeVar("T", bound="AthleteGameLogResponse")


@_attrs_define
class AthleteGameLogResponse:
    """
    Attributes:
        athlete (AthleteReference):
        categories (List['GameLogCategory']):
        league (Union[Unset, LeagueReference]):
        season (Union[Unset, Season]):
    """

    athlete: "AthleteReference"
    categories: List["GameLogCategory"]
    league: Union[Unset, "LeagueReference"] = UNSET
    season: Union[Unset, "Season"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        athlete = self.athlete.to_dict()

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        league: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.league, Unset):
            league = self.league.to_dict()

        season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "athlete": athlete,
                "categories": categories,
            }
        )
        if league is not UNSET:
            field_dict["league"] = league
        if season is not UNSET:
            field_dict["season"] = season

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.athlete_reference import AthleteReference
        from ..models.game_log_category import GameLogCategory
        from ..models.league_reference import LeagueReference
        from ..models.season import Season

        d = src_dict.copy()
        athlete = AthleteReference.from_dict(d.pop("athlete"))

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = GameLogCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        _league = d.pop("league", UNSET)
        league: Union[Unset, LeagueReference]
        if isinstance(_league, Unset):
            league = UNSET
        else:
            league = LeagueReference.from_dict(_league)

        _season = d.pop("season", UNSET)
        season: Union[Unset, Season]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = Season.from_dict(_season)

        athlete_game_log_response = cls(
            athlete=athlete,
            categories=categories,
            league=league,
            season=season,
        )

        athlete_game_log_response.additional_properties = d
        return athlete_game_log_response

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
