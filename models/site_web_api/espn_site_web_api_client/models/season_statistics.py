from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stats_season import StatsSeason


T = TypeVar("T", bound="SeasonStatistics")


@_attrs_define
class SeasonStatistics:
    """
    Attributes:
        team_id (str): Team ID
        season (StatsSeason):
        stats (List[str]): Statistical values
        team_slug (Union[Unset, str]): Team slug
        position (Union[Unset, str]): Player position
        season_totals (Union[Unset, List[str]]): Season totals
    """

    team_id: str
    season: "StatsSeason"
    stats: List[str]
    team_slug: Union[Unset, str] = UNSET
    position: Union[Unset, str] = UNSET
    season_totals: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team_id = self.team_id

        season = self.season.to_dict()

        stats = self.stats

        team_slug = self.team_slug

        position = self.position

        season_totals: Union[Unset, List[str]] = UNSET
        if not isinstance(self.season_totals, Unset):
            season_totals = self.season_totals

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "teamId": team_id,
                "season": season,
                "stats": stats,
            }
        )
        if team_slug is not UNSET:
            field_dict["teamSlug"] = team_slug
        if position is not UNSET:
            field_dict["position"] = position
        if season_totals is not UNSET:
            field_dict["seasonTotals"] = season_totals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stats_season import StatsSeason

        d = src_dict.copy()
        team_id = d.pop("teamId")

        season = StatsSeason.from_dict(d.pop("season"))

        stats = cast(List[str], d.pop("stats"))

        team_slug = d.pop("teamSlug", UNSET)

        position = d.pop("position", UNSET)

        season_totals = cast(List[str], d.pop("seasonTotals", UNSET))

        season_statistics = cls(
            team_id=team_id,
            season=season,
            stats=stats,
            team_slug=team_slug,
            position=position,
            season_totals=season_totals,
        )

        season_statistics.additional_properties = d
        return season_statistics

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
