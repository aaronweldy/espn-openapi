import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.competitor import Competitor
    from ..models.event_format import EventFormat
    from ..models.event_note import EventNote
    from ..models.event_status import EventStatus
    from ..models.event_time import EventTime


T = TypeVar("T", bound="Competition")


@_attrs_define
class Competition:
    """
    Attributes:
        id (str): Competition identifier Example: 401772510.
        date (datetime.datetime): Competition date and time Example: 2025-09-05T00:20Z.
        competitors (List['Competitor']):
        status (EventStatus):
        attendance (Union[Unset, int]): Attendance count Example: 70355.
        date_valid (Union[Unset, bool]): Whether the date is confirmed Example: True.
        neutral_site (Union[Unset, bool]): Whether the game is at a neutral site
        on_watch_espn (Union[Unset, bool]): Whether available on WatchESPN
        wallclock_available (Union[Unset, bool]): Whether wallclock time is available
        highlights_available (Union[Unset, bool]): Whether highlights are available Example: True.
        division_competition (Union[Unset, bool]): Whether this is a division competition (NBA/NHL)
        conference_competition (Union[Unset, bool]): Whether this is a conference competition (NBA/NHL)
        notes (Union[Unset, List['EventNote']]):
        format_ (Union[Unset, EventFormat]):
        has_defensive_stats (Union[Unset, bool]): Whether defensive stats are available
        time (Union[Unset, EventTime]):
    """

    id: str
    date: datetime.datetime
    competitors: List["Competitor"]
    status: "EventStatus"
    attendance: Union[Unset, int] = UNSET
    date_valid: Union[Unset, bool] = UNSET
    neutral_site: Union[Unset, bool] = UNSET
    on_watch_espn: Union[Unset, bool] = UNSET
    wallclock_available: Union[Unset, bool] = UNSET
    highlights_available: Union[Unset, bool] = UNSET
    division_competition: Union[Unset, bool] = UNSET
    conference_competition: Union[Unset, bool] = UNSET
    notes: Union[Unset, List["EventNote"]] = UNSET
    format_: Union[Unset, "EventFormat"] = UNSET
    has_defensive_stats: Union[Unset, bool] = UNSET
    time: Union[Unset, "EventTime"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        date = self.date.isoformat()

        competitors = []
        for competitors_item_data in self.competitors:
            competitors_item = competitors_item_data.to_dict()
            competitors.append(competitors_item)

        status = self.status.to_dict()

        attendance = self.attendance

        date_valid = self.date_valid

        neutral_site = self.neutral_site

        on_watch_espn = self.on_watch_espn

        wallclock_available = self.wallclock_available

        highlights_available = self.highlights_available

        division_competition = self.division_competition

        conference_competition = self.conference_competition

        notes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()
                notes.append(notes_item)

        format_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.to_dict()

        has_defensive_stats = self.has_defensive_stats

        time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "competitors": competitors,
                "status": status,
            }
        )
        if attendance is not UNSET:
            field_dict["attendance"] = attendance
        if date_valid is not UNSET:
            field_dict["dateValid"] = date_valid
        if neutral_site is not UNSET:
            field_dict["neutralSite"] = neutral_site
        if on_watch_espn is not UNSET:
            field_dict["onWatchESPN"] = on_watch_espn
        if wallclock_available is not UNSET:
            field_dict["wallclockAvailable"] = wallclock_available
        if highlights_available is not UNSET:
            field_dict["highlightsAvailable"] = highlights_available
        if division_competition is not UNSET:
            field_dict["divisionCompetition"] = division_competition
        if conference_competition is not UNSET:
            field_dict["conferenceCompetition"] = conference_competition
        if notes is not UNSET:
            field_dict["notes"] = notes
        if format_ is not UNSET:
            field_dict["format"] = format_
        if has_defensive_stats is not UNSET:
            field_dict["hasDefensiveStats"] = has_defensive_stats
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.competitor import Competitor
        from ..models.event_format import EventFormat
        from ..models.event_note import EventNote
        from ..models.event_status import EventStatus
        from ..models.event_time import EventTime

        d = src_dict.copy()
        id = d.pop("id")

        date = isoparse(d.pop("date"))

        competitors = []
        _competitors = d.pop("competitors")
        for competitors_item_data in _competitors:
            competitors_item = Competitor.from_dict(competitors_item_data)

            competitors.append(competitors_item)

        status = EventStatus.from_dict(d.pop("status"))

        attendance = d.pop("attendance", UNSET)

        date_valid = d.pop("dateValid", UNSET)

        neutral_site = d.pop("neutralSite", UNSET)

        on_watch_espn = d.pop("onWatchESPN", UNSET)

        wallclock_available = d.pop("wallclockAvailable", UNSET)

        highlights_available = d.pop("highlightsAvailable", UNSET)

        division_competition = d.pop("divisionCompetition", UNSET)

        conference_competition = d.pop("conferenceCompetition", UNSET)

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = EventNote.from_dict(notes_item_data)

            notes.append(notes_item)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, EventFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = EventFormat.from_dict(_format_)

        has_defensive_stats = d.pop("hasDefensiveStats", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, EventTime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = EventTime.from_dict(_time)

        competition = cls(
            id=id,
            date=date,
            competitors=competitors,
            status=status,
            attendance=attendance,
            date_valid=date_valid,
            neutral_site=neutral_site,
            on_watch_espn=on_watch_espn,
            wallclock_available=wallclock_available,
            highlights_available=highlights_available,
            division_competition=division_competition,
            conference_competition=conference_competition,
            notes=notes,
            format_=format_,
            has_defensive_stats=has_defensive_stats,
            time=time,
        )

        competition.additional_properties = d
        return competition

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
