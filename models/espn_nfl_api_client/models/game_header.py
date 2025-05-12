from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.competition import Competition
    from ..models.season import Season


T = TypeVar("T", bound="GameHeader")


@_attrs_define
class GameHeader:
    """
    Attributes:
        id (str): Unique identifier for the game Example: 401547417.
        uid (str): Universal identifier for the game Example: s:20~l:28~e:401547417.
        season (Season):
        competitions (list['Competition']):
        week (Union[Unset, int]): Week number in the season
        time_valid (Union[Unset, bool]): Whether the game time is valid
    """

    id: str
    uid: str
    season: "Season"
    competitions: list["Competition"]
    week: Union[Unset, int] = UNSET
    time_valid: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uid = self.uid

        season = self.season.to_dict()

        competitions = []
        for competitions_item_data in self.competitions:
            competitions_item = competitions_item_data.to_dict()
            competitions.append(competitions_item)

        week = self.week

        time_valid = self.time_valid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uid": uid,
                "season": season,
                "competitions": competitions,
            }
        )
        if week is not UNSET:
            field_dict["week"] = week
        if time_valid is not UNSET:
            field_dict["timeValid"] = time_valid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.competition import Competition
        from ..models.season import Season

        d = dict(src_dict)
        id = d.pop("id")

        uid = d.pop("uid")

        season = Season.from_dict(d.pop("season"))

        competitions = []
        _competitions = d.pop("competitions")
        for competitions_item_data in _competitions:
            competitions_item = Competition.from_dict(competitions_item_data)

            competitions.append(competitions_item)

        week = d.pop("week", UNSET)

        time_valid = d.pop("timeValid", UNSET)

        game_header = cls(
            id=id,
            uid=uid,
            season=season,
            competitions=competitions,
            week=week,
            time_valid=time_valid,
        )

        game_header.additional_properties = d
        return game_header

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
