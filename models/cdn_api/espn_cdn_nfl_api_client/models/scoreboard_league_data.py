from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_calendar import ScoreboardCalendar
    from ..models.scoreboard_image import ScoreboardImage
    from ..models.scoreboard_season import ScoreboardSeason


T = TypeVar("T", bound="ScoreboardLeagueData")


@_attrs_define
class ScoreboardLeagueData:
    """
    Attributes:
        calendar_is_whitelist (Union[Unset, bool]):
        calendar (Union[Unset, List['ScoreboardCalendar']]):
        uid (Union[Unset, str]):
        calendar_type (Union[Unset, str]):
        calendar_end_date (Union[Unset, str]):
        calendar_start_date (Union[Unset, str]):
        name (Union[Unset, str]):
        season (Union[Unset, ScoreboardSeason]):
        id (Union[Unset, str]):
        abbreviation (Union[Unset, str]):
        logos (Union[Unset, List['ScoreboardImage']]):
        slug (Union[Unset, str]):
    """

    calendar_is_whitelist: Union[Unset, bool] = UNSET
    calendar: Union[Unset, List["ScoreboardCalendar"]] = UNSET
    uid: Union[Unset, str] = UNSET
    calendar_type: Union[Unset, str] = UNSET
    calendar_end_date: Union[Unset, str] = UNSET
    calendar_start_date: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    season: Union[Unset, "ScoreboardSeason"] = UNSET
    id: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    logos: Union[Unset, List["ScoreboardImage"]] = UNSET
    slug: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        calendar_is_whitelist = self.calendar_is_whitelist

        calendar: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.calendar, Unset):
            calendar = []
            for calendar_item_data in self.calendar:
                calendar_item = calendar_item_data.to_dict()
                calendar.append(calendar_item)

        uid = self.uid

        calendar_type = self.calendar_type

        calendar_end_date = self.calendar_end_date

        calendar_start_date = self.calendar_start_date

        name = self.name

        season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        id = self.id

        abbreviation = self.abbreviation

        logos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.logos, Unset):
            logos = []
            for logos_item_data in self.logos:
                logos_item = logos_item_data.to_dict()
                logos.append(logos_item)

        slug = self.slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if calendar_is_whitelist is not UNSET:
            field_dict["calendarIsWhitelist"] = calendar_is_whitelist
        if calendar is not UNSET:
            field_dict["calendar"] = calendar
        if uid is not UNSET:
            field_dict["uid"] = uid
        if calendar_type is not UNSET:
            field_dict["calendarType"] = calendar_type
        if calendar_end_date is not UNSET:
            field_dict["calendarEndDate"] = calendar_end_date
        if calendar_start_date is not UNSET:
            field_dict["calendarStartDate"] = calendar_start_date
        if name is not UNSET:
            field_dict["name"] = name
        if season is not UNSET:
            field_dict["season"] = season
        if id is not UNSET:
            field_dict["id"] = id
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if logos is not UNSET:
            field_dict["logos"] = logos
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_calendar import ScoreboardCalendar
        from ..models.scoreboard_image import ScoreboardImage
        from ..models.scoreboard_season import ScoreboardSeason

        d = src_dict.copy()
        calendar_is_whitelist = d.pop("calendarIsWhitelist", UNSET)

        calendar = []
        _calendar = d.pop("calendar", UNSET)
        for calendar_item_data in _calendar or []:
            calendar_item = ScoreboardCalendar.from_dict(calendar_item_data)

            calendar.append(calendar_item)

        uid = d.pop("uid", UNSET)

        calendar_type = d.pop("calendarType", UNSET)

        calendar_end_date = d.pop("calendarEndDate", UNSET)

        calendar_start_date = d.pop("calendarStartDate", UNSET)

        name = d.pop("name", UNSET)

        _season = d.pop("season", UNSET)
        season: Union[Unset, ScoreboardSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = ScoreboardSeason.from_dict(_season)

        id = d.pop("id", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        logos = []
        _logos = d.pop("logos", UNSET)
        for logos_item_data in _logos or []:
            logos_item = ScoreboardImage.from_dict(logos_item_data)

            logos.append(logos_item)

        slug = d.pop("slug", UNSET)

        scoreboard_league_data = cls(
            calendar_is_whitelist=calendar_is_whitelist,
            calendar=calendar,
            uid=uid,
            calendar_type=calendar_type,
            calendar_end_date=calendar_end_date,
            calendar_start_date=calendar_start_date,
            name=name,
            season=season,
            id=id,
            abbreviation=abbreviation,
            logos=logos,
            slug=slug,
        )

        scoreboard_league_data.additional_properties = d
        return scoreboard_league_data

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
