from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sport_league_season import SportLeagueSeason
    from ..models.team_entry import TeamEntry


T = TypeVar("T", bound="SportLeague")


@_attrs_define
class SportLeague:
    """
    Attributes:
        id (str):  Example: 28.
        name (str):  Example: National Football League.
        teams (list['TeamEntry']):
        uid (Union[Unset, str]):  Example: s:20~l:28.
        abbreviation (Union[Unset, str]):  Example: NFL.
        short_name (Union[Unset, str]):  Example: NFL.
        slug (Union[Unset, str]):  Example: nfl.
        year (Union[Unset, int]):  Example: 2024.
        season (Union[Unset, SportLeagueSeason]):
    """

    id: str
    name: str
    teams: list["TeamEntry"]
    uid: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    year: Union[Unset, int] = UNSET
    season: Union[Unset, "SportLeagueSeason"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        teams = []
        for teams_item_data in self.teams:
            teams_item = teams_item_data.to_dict()
            teams.append(teams_item)

        uid = self.uid

        abbreviation = self.abbreviation

        short_name = self.short_name

        slug = self.slug

        year = self.year

        season: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "teams": teams,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if year is not UNSET:
            field_dict["year"] = year
        if season is not UNSET:
            field_dict["season"] = season

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sport_league_season import SportLeagueSeason
        from ..models.team_entry import TeamEntry

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        teams = []
        _teams = d.pop("teams")
        for teams_item_data in _teams:
            teams_item = TeamEntry.from_dict(teams_item_data)

            teams.append(teams_item)

        uid = d.pop("uid", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        short_name = d.pop("shortName", UNSET)

        slug = d.pop("slug", UNSET)

        year = d.pop("year", UNSET)

        _season = d.pop("season", UNSET)
        season: Union[Unset, SportLeagueSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = SportLeagueSeason.from_dict(_season)

        sport_league = cls(
            id=id,
            name=name,
            teams=teams,
            uid=uid,
            abbreviation=abbreviation,
            short_name=short_name,
            slug=slug,
            year=year,
            season=season,
        )

        sport_league.additional_properties = d
        return sport_league

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
