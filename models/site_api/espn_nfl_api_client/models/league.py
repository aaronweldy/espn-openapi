import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.calendar_item import CalendarItem
    from ..models.league_season import LeagueSeason
    from ..models.logo import Logo


T = TypeVar("T", bound="League")


@_attrs_define
class League:
    """
    Attributes:
        id (str):  Example: 28.
        name (str):  Example: National Football League.
        season (LeagueSeason):
        uid (Union[Unset, str]):  Example: s:20~l:28.
        abbreviation (Union[Unset, str]):  Example: NFL.
        slug (Union[Unset, str]):  Example: nfl.
        logos (Union[Unset, List['Logo']]):
        calendar_type (Union[Unset, str]):  Example: list.
        calendar_is_whitelist (Union[Unset, bool]):
        calendar_start_date (Union[Unset, datetime.datetime]):
        calendar_end_date (Union[Unset, datetime.datetime]):
        calendar (Union[Unset, List[Union['CalendarItem', str]]]):
    """

    id: str
    name: str
    season: "LeagueSeason"
    uid: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    logos: Union[Unset, List["Logo"]] = UNSET
    calendar_type: Union[Unset, str] = UNSET
    calendar_is_whitelist: Union[Unset, bool] = UNSET
    calendar_start_date: Union[Unset, datetime.datetime] = UNSET
    calendar_end_date: Union[Unset, datetime.datetime] = UNSET
    calendar: Union[Unset, List[Union["CalendarItem", str]]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.calendar_item import CalendarItem

        id = self.id

        name = self.name

        season = self.season.to_dict()

        uid = self.uid

        abbreviation = self.abbreviation

        slug = self.slug

        logos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.logos, Unset):
            logos = []
            for logos_item_data in self.logos:
                logos_item = logos_item_data.to_dict()
                logos.append(logos_item)

        calendar_type = self.calendar_type

        calendar_is_whitelist = self.calendar_is_whitelist

        calendar_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.calendar_start_date, Unset):
            calendar_start_date = self.calendar_start_date.isoformat()

        calendar_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.calendar_end_date, Unset):
            calendar_end_date = self.calendar_end_date.isoformat()

        calendar: Union[Unset, List[Union[Dict[str, Any], str]]] = UNSET
        if not isinstance(self.calendar, Unset):
            calendar = []
            for calendar_item_data in self.calendar:
                calendar_item: Union[Dict[str, Any], str]
                if isinstance(calendar_item_data, CalendarItem):
                    calendar_item = calendar_item_data.to_dict()
                else:
                    calendar_item = calendar_item_data
                calendar.append(calendar_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "season": season,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if slug is not UNSET:
            field_dict["slug"] = slug
        if logos is not UNSET:
            field_dict["logos"] = logos
        if calendar_type is not UNSET:
            field_dict["calendarType"] = calendar_type
        if calendar_is_whitelist is not UNSET:
            field_dict["calendarIsWhitelist"] = calendar_is_whitelist
        if calendar_start_date is not UNSET:
            field_dict["calendarStartDate"] = calendar_start_date
        if calendar_end_date is not UNSET:
            field_dict["calendarEndDate"] = calendar_end_date
        if calendar is not UNSET:
            field_dict["calendar"] = calendar

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.calendar_item import CalendarItem
        from ..models.league_season import LeagueSeason
        from ..models.logo import Logo

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        season = LeagueSeason.from_dict(d.pop("season"))

        uid = d.pop("uid", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        slug = d.pop("slug", UNSET)

        logos = []
        _logos = d.pop("logos", UNSET)
        for logos_item_data in _logos or []:
            logos_item = Logo.from_dict(logos_item_data)

            logos.append(logos_item)

        calendar_type = d.pop("calendarType", UNSET)

        calendar_is_whitelist = d.pop("calendarIsWhitelist", UNSET)

        _calendar_start_date = d.pop("calendarStartDate", UNSET)
        calendar_start_date: Union[Unset, datetime.datetime]
        if isinstance(_calendar_start_date, Unset):
            calendar_start_date = UNSET
        else:
            calendar_start_date = isoparse(_calendar_start_date)

        _calendar_end_date = d.pop("calendarEndDate", UNSET)
        calendar_end_date: Union[Unset, datetime.datetime]
        if isinstance(_calendar_end_date, Unset):
            calendar_end_date = UNSET
        else:
            calendar_end_date = isoparse(_calendar_end_date)

        calendar = []
        _calendar = d.pop("calendar", UNSET)
        for calendar_item_data in _calendar or []:

            def _parse_calendar_item(data: object) -> Union["CalendarItem", str]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    calendar_item_type_0 = CalendarItem.from_dict(data)

                    return calendar_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["CalendarItem", str], data)

            calendar_item = _parse_calendar_item(calendar_item_data)

            calendar.append(calendar_item)

        league = cls(
            id=id,
            name=name,
            season=season,
            uid=uid,
            abbreviation=abbreviation,
            slug=slug,
            logos=logos,
            calendar_type=calendar_type,
            calendar_is_whitelist=calendar_is_whitelist,
            calendar_start_date=calendar_start_date,
            calendar_end_date=calendar_end_date,
            calendar=calendar,
        )

        league.additional_properties = d
        return league

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
