from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nfl_schedule_content_defaults import NflScheduleContentDefaults
    from ..models.nfl_schedule_content_parameters import NflScheduleContentParameters
    from ..models.nfl_schedule_content_schedule import NflScheduleContentSchedule
    from ..models.nfl_schedule_content_week_map import NflScheduleContentWeekMap
    from ..models.nfl_schedule_response_calendar_item import NflScheduleResponseCalendarItem


T = TypeVar("T", bound="NflScheduleContent")


@_attrs_define
class NflScheduleContent:
    """
    Attributes:
        active_date (Union[Unset, str]):
        calendar (Union[Unset, List['NflScheduleResponseCalendarItem']]):
        canonical (Union[Unset, str]):
        days_to_show (Union[Unset, int]):
        defaults (Union[Unset, NflScheduleContentDefaults]):
        description (Union[Unset, str]):
        edition (Union[Unset, str]):
        league (Union[Unset, str]):
        og_type (Union[Unset, str]):
        page_title (Union[Unset, str]):
        parameters (Union[Unset, NflScheduleContentParameters]):
        root (Union[Unset, str]):
        schedule (Union[Unset, NflScheduleContentSchedule]):
        sorted_leagues (Union[Unset, List[str]]):
        sport (Union[Unset, str]):
        title (Union[Unset, str]):
        week_map (Union[Unset, NflScheduleContentWeekMap]):
    """

    active_date: Union[Unset, str] = UNSET
    calendar: Union[Unset, List["NflScheduleResponseCalendarItem"]] = UNSET
    canonical: Union[Unset, str] = UNSET
    days_to_show: Union[Unset, int] = UNSET
    defaults: Union[Unset, "NflScheduleContentDefaults"] = UNSET
    description: Union[Unset, str] = UNSET
    edition: Union[Unset, str] = UNSET
    league: Union[Unset, str] = UNSET
    og_type: Union[Unset, str] = UNSET
    page_title: Union[Unset, str] = UNSET
    parameters: Union[Unset, "NflScheduleContentParameters"] = UNSET
    root: Union[Unset, str] = UNSET
    schedule: Union[Unset, "NflScheduleContentSchedule"] = UNSET
    sorted_leagues: Union[Unset, List[str]] = UNSET
    sport: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    week_map: Union[Unset, "NflScheduleContentWeekMap"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active_date = self.active_date

        calendar: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.calendar, Unset):
            calendar = []
            for calendar_item_data in self.calendar:
                calendar_item = calendar_item_data.to_dict()
                calendar.append(calendar_item)

        canonical = self.canonical

        days_to_show = self.days_to_show

        defaults: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.defaults, Unset):
            defaults = self.defaults.to_dict()

        description = self.description

        edition = self.edition

        league = self.league

        og_type = self.og_type

        page_title = self.page_title

        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        root = self.root

        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        sorted_leagues: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sorted_leagues, Unset):
            sorted_leagues = self.sorted_leagues

        sport = self.sport

        title = self.title

        week_map: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.week_map, Unset):
            week_map = self.week_map.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_date is not UNSET:
            field_dict["activeDate"] = active_date
        if calendar is not UNSET:
            field_dict["calendar"] = calendar
        if canonical is not UNSET:
            field_dict["canonical"] = canonical
        if days_to_show is not UNSET:
            field_dict["daysToShow"] = days_to_show
        if defaults is not UNSET:
            field_dict["defaults"] = defaults
        if description is not UNSET:
            field_dict["description"] = description
        if edition is not UNSET:
            field_dict["edition"] = edition
        if league is not UNSET:
            field_dict["league"] = league
        if og_type is not UNSET:
            field_dict["og_type"] = og_type
        if page_title is not UNSET:
            field_dict["pageTitle"] = page_title
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if root is not UNSET:
            field_dict["root"] = root
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if sorted_leagues is not UNSET:
            field_dict["sortedLeagues"] = sorted_leagues
        if sport is not UNSET:
            field_dict["sport"] = sport
        if title is not UNSET:
            field_dict["title"] = title
        if week_map is not UNSET:
            field_dict["weekMap"] = week_map

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_schedule_content_defaults import NflScheduleContentDefaults
        from ..models.nfl_schedule_content_parameters import NflScheduleContentParameters
        from ..models.nfl_schedule_content_schedule import NflScheduleContentSchedule
        from ..models.nfl_schedule_content_week_map import NflScheduleContentWeekMap
        from ..models.nfl_schedule_response_calendar_item import NflScheduleResponseCalendarItem

        d = src_dict.copy()
        active_date = d.pop("activeDate", UNSET)

        calendar = []
        _calendar = d.pop("calendar", UNSET)
        for calendar_item_data in _calendar or []:
            calendar_item = NflScheduleResponseCalendarItem.from_dict(calendar_item_data)

            calendar.append(calendar_item)

        canonical = d.pop("canonical", UNSET)

        days_to_show = d.pop("daysToShow", UNSET)

        _defaults = d.pop("defaults", UNSET)
        defaults: Union[Unset, NflScheduleContentDefaults]
        if isinstance(_defaults, Unset):
            defaults = UNSET
        else:
            defaults = NflScheduleContentDefaults.from_dict(_defaults)

        description = d.pop("description", UNSET)

        edition = d.pop("edition", UNSET)

        league = d.pop("league", UNSET)

        og_type = d.pop("og_type", UNSET)

        page_title = d.pop("pageTitle", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, NflScheduleContentParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = NflScheduleContentParameters.from_dict(_parameters)

        root = d.pop("root", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, NflScheduleContentSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = NflScheduleContentSchedule.from_dict(_schedule)

        sorted_leagues = cast(List[str], d.pop("sortedLeagues", UNSET))

        sport = d.pop("sport", UNSET)

        title = d.pop("title", UNSET)

        _week_map = d.pop("weekMap", UNSET)
        week_map: Union[Unset, NflScheduleContentWeekMap]
        if isinstance(_week_map, Unset):
            week_map = UNSET
        else:
            week_map = NflScheduleContentWeekMap.from_dict(_week_map)

        nfl_schedule_content = cls(
            active_date=active_date,
            calendar=calendar,
            canonical=canonical,
            days_to_show=days_to_show,
            defaults=defaults,
            description=description,
            edition=edition,
            league=league,
            og_type=og_type,
            page_title=page_title,
            parameters=parameters,
            root=root,
            schedule=schedule,
            sorted_leagues=sorted_leagues,
            sport=sport,
            title=title,
            week_map=week_map,
        )

        nfl_schedule_content.additional_properties = d
        return nfl_schedule_content

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
