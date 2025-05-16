from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nfl_schedule_game_season import NflScheduleGameSeason
    from ..models.nfl_schedule_game_week import NflScheduleGameWeek
    from ..models.scoreboard_competition import ScoreboardCompetition
    from ..models.scoreboard_link import ScoreboardLink
    from ..models.scoreboard_status import ScoreboardStatus


T = TypeVar("T", bound="NflScheduleGame")


@_attrs_define
class NflScheduleGame:
    """
    Attributes:
        competitions (Union[Unset, List['ScoreboardCompetition']]):
        date (Union[Unset, str]):
        id (Union[Unset, str]):
        links (Union[Unset, List['ScoreboardLink']]):
        name (Union[Unset, str]):
        season (Union[Unset, NflScheduleGameSeason]):
        short_name (Union[Unset, str]):
        status (Union[Unset, ScoreboardStatus]):
        uid (Union[Unset, str]):
        week (Union[Unset, NflScheduleGameWeek]):
    """

    competitions: Union[Unset, List["ScoreboardCompetition"]] = UNSET
    date: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    links: Union[Unset, List["ScoreboardLink"]] = UNSET
    name: Union[Unset, str] = UNSET
    season: Union[Unset, "NflScheduleGameSeason"] = UNSET
    short_name: Union[Unset, str] = UNSET
    status: Union[Unset, "ScoreboardStatus"] = UNSET
    uid: Union[Unset, str] = UNSET
    week: Union[Unset, "NflScheduleGameWeek"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        competitions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitions, Unset):
            competitions = []
            for competitions_item_data in self.competitions:
                competitions_item = competitions_item_data.to_dict()
                competitions.append(competitions_item)

        date = self.date

        id = self.id

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        name = self.name

        season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        short_name = self.short_name

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        uid = self.uid

        week: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.week, Unset):
            week = self.week.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if competitions is not UNSET:
            field_dict["competitions"] = competitions
        if date is not UNSET:
            field_dict["date"] = date
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name
        if season is not UNSET:
            field_dict["season"] = season
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if status is not UNSET:
            field_dict["status"] = status
        if uid is not UNSET:
            field_dict["uid"] = uid
        if week is not UNSET:
            field_dict["week"] = week

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_schedule_game_season import NflScheduleGameSeason
        from ..models.nfl_schedule_game_week import NflScheduleGameWeek
        from ..models.scoreboard_competition import ScoreboardCompetition
        from ..models.scoreboard_link import ScoreboardLink
        from ..models.scoreboard_status import ScoreboardStatus

        d = src_dict.copy()
        competitions = []
        _competitions = d.pop("competitions", UNSET)
        for competitions_item_data in _competitions or []:
            competitions_item = ScoreboardCompetition.from_dict(competitions_item_data)

            competitions.append(competitions_item)

        date = d.pop("date", UNSET)

        id = d.pop("id", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = ScoreboardLink.from_dict(links_item_data)

            links.append(links_item)

        name = d.pop("name", UNSET)

        _season = d.pop("season", UNSET)
        season: Union[Unset, NflScheduleGameSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = NflScheduleGameSeason.from_dict(_season)

        short_name = d.pop("shortName", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ScoreboardStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ScoreboardStatus.from_dict(_status)

        uid = d.pop("uid", UNSET)

        _week = d.pop("week", UNSET)
        week: Union[Unset, NflScheduleGameWeek]
        if isinstance(_week, Unset):
            week = UNSET
        else:
            week = NflScheduleGameWeek.from_dict(_week)

        nfl_schedule_game = cls(
            competitions=competitions,
            date=date,
            id=id,
            links=links,
            name=name,
            season=season,
            short_name=short_name,
            status=status,
            uid=uid,
            week=week,
        )

        nfl_schedule_game.additional_properties = d
        return nfl_schedule_game

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
