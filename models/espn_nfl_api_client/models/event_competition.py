import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.broadcast import Broadcast
    from ..models.competition_leader import CompetitionLeader
    from ..models.competition_type import CompetitionType
    from ..models.competitor import Competitor
    from ..models.event_competition_highlights_item import EventCompetitionHighlightsItem
    from ..models.event_competition_notes_item import EventCompetitionNotesItem
    from ..models.game_format import GameFormat
    from ..models.game_status import GameStatus
    from ..models.geo_broadcast import GeoBroadcast
    from ..models.headline import Headline
    from ..models.venue import Venue


T = TypeVar("T", bound="EventCompetition")


@_attrs_define
class EventCompetition:
    """
    Attributes:
        id (str):  Example: 401671889.
        date (datetime.datetime):
        competitors (list['Competitor']):
        uid (Union[Unset, str]):  Example: s:20~l:28~e:401671889~c:401671889.
        attendance (Union[Unset, int]):  Example: 65719.
        type_ (Union[Unset, CompetitionType]):
        time_valid (Union[Unset, bool]):
        neutral_site (Union[Unset, bool]):
        conference_competition (Union[Unset, bool]):
        play_by_play_available (Union[Unset, bool]):
        recent (Union[Unset, bool]):
        venue (Union[Unset, Venue]):
        notes (Union[Unset, list['EventCompetitionNotesItem']]):
        status (Union[Unset, GameStatus]):
        broadcasts (Union[Unset, list['Broadcast']]):
        leaders (Union[Unset, list['CompetitionLeader']]):
        format_ (Union[Unset, GameFormat]):
        start_date (Union[Unset, datetime.datetime]):
        broadcast (Union[Unset, str]):  Example: FOX.
        geo_broadcasts (Union[Unset, list['GeoBroadcast']]):
        highlights (Union[Unset, list['EventCompetitionHighlightsItem']]):
        headlines (Union[Unset, list['Headline']]):
    """

    id: str
    date: datetime.datetime
    competitors: list["Competitor"]
    uid: Union[Unset, str] = UNSET
    attendance: Union[Unset, int] = UNSET
    type_: Union[Unset, "CompetitionType"] = UNSET
    time_valid: Union[Unset, bool] = UNSET
    neutral_site: Union[Unset, bool] = UNSET
    conference_competition: Union[Unset, bool] = UNSET
    play_by_play_available: Union[Unset, bool] = UNSET
    recent: Union[Unset, bool] = UNSET
    venue: Union[Unset, "Venue"] = UNSET
    notes: Union[Unset, list["EventCompetitionNotesItem"]] = UNSET
    status: Union[Unset, "GameStatus"] = UNSET
    broadcasts: Union[Unset, list["Broadcast"]] = UNSET
    leaders: Union[Unset, list["CompetitionLeader"]] = UNSET
    format_: Union[Unset, "GameFormat"] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    broadcast: Union[Unset, str] = UNSET
    geo_broadcasts: Union[Unset, list["GeoBroadcast"]] = UNSET
    highlights: Union[Unset, list["EventCompetitionHighlightsItem"]] = UNSET
    headlines: Union[Unset, list["Headline"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        date = self.date.isoformat()

        competitors = []
        for competitors_item_data in self.competitors:
            competitors_item = competitors_item_data.to_dict()
            competitors.append(competitors_item)

        uid = self.uid

        attendance = self.attendance

        type_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        time_valid = self.time_valid

        neutral_site = self.neutral_site

        conference_competition = self.conference_competition

        play_by_play_available = self.play_by_play_available

        recent = self.recent

        venue: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.to_dict()

        notes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()
                notes.append(notes_item)

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        broadcasts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.broadcasts, Unset):
            broadcasts = []
            for broadcasts_item_data in self.broadcasts:
                broadcasts_item = broadcasts_item_data.to_dict()
                broadcasts.append(broadcasts_item)

        leaders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.leaders, Unset):
            leaders = []
            for leaders_item_data in self.leaders:
                leaders_item = leaders_item_data.to_dict()
                leaders.append(leaders_item)

        format_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.to_dict()

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        broadcast = self.broadcast

        geo_broadcasts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.geo_broadcasts, Unset):
            geo_broadcasts = []
            for geo_broadcasts_item_data in self.geo_broadcasts:
                geo_broadcasts_item = geo_broadcasts_item_data.to_dict()
                geo_broadcasts.append(geo_broadcasts_item)

        highlights: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.highlights, Unset):
            highlights = []
            for highlights_item_data in self.highlights:
                highlights_item = highlights_item_data.to_dict()
                highlights.append(highlights_item)

        headlines: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.headlines, Unset):
            headlines = []
            for headlines_item_data in self.headlines:
                headlines_item = headlines_item_data.to_dict()
                headlines.append(headlines_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "competitors": competitors,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if attendance is not UNSET:
            field_dict["attendance"] = attendance
        if type_ is not UNSET:
            field_dict["type"] = type_
        if time_valid is not UNSET:
            field_dict["timeValid"] = time_valid
        if neutral_site is not UNSET:
            field_dict["neutralSite"] = neutral_site
        if conference_competition is not UNSET:
            field_dict["conferenceCompetition"] = conference_competition
        if play_by_play_available is not UNSET:
            field_dict["playByPlayAvailable"] = play_by_play_available
        if recent is not UNSET:
            field_dict["recent"] = recent
        if venue is not UNSET:
            field_dict["venue"] = venue
        if notes is not UNSET:
            field_dict["notes"] = notes
        if status is not UNSET:
            field_dict["status"] = status
        if broadcasts is not UNSET:
            field_dict["broadcasts"] = broadcasts
        if leaders is not UNSET:
            field_dict["leaders"] = leaders
        if format_ is not UNSET:
            field_dict["format"] = format_
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if broadcast is not UNSET:
            field_dict["broadcast"] = broadcast
        if geo_broadcasts is not UNSET:
            field_dict["geoBroadcasts"] = geo_broadcasts
        if highlights is not UNSET:
            field_dict["highlights"] = highlights
        if headlines is not UNSET:
            field_dict["headlines"] = headlines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast import Broadcast
        from ..models.competition_leader import CompetitionLeader
        from ..models.competition_type import CompetitionType
        from ..models.competitor import Competitor
        from ..models.event_competition_highlights_item import EventCompetitionHighlightsItem
        from ..models.event_competition_notes_item import EventCompetitionNotesItem
        from ..models.game_format import GameFormat
        from ..models.game_status import GameStatus
        from ..models.geo_broadcast import GeoBroadcast
        from ..models.headline import Headline
        from ..models.venue import Venue

        d = dict(src_dict)
        id = d.pop("id")

        date = isoparse(d.pop("date"))

        competitors = []
        _competitors = d.pop("competitors")
        for competitors_item_data in _competitors:
            competitors_item = Competitor.from_dict(competitors_item_data)

            competitors.append(competitors_item)

        uid = d.pop("uid", UNSET)

        attendance = d.pop("attendance", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CompetitionType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CompetitionType.from_dict(_type_)

        time_valid = d.pop("timeValid", UNSET)

        neutral_site = d.pop("neutralSite", UNSET)

        conference_competition = d.pop("conferenceCompetition", UNSET)

        play_by_play_available = d.pop("playByPlayAvailable", UNSET)

        recent = d.pop("recent", UNSET)

        _venue = d.pop("venue", UNSET)
        venue: Union[Unset, Venue]
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = Venue.from_dict(_venue)

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = EventCompetitionNotesItem.from_dict(notes_item_data)

            notes.append(notes_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, GameStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GameStatus.from_dict(_status)

        broadcasts = []
        _broadcasts = d.pop("broadcasts", UNSET)
        for broadcasts_item_data in _broadcasts or []:
            broadcasts_item = Broadcast.from_dict(broadcasts_item_data)

            broadcasts.append(broadcasts_item)

        leaders = []
        _leaders = d.pop("leaders", UNSET)
        for leaders_item_data in _leaders or []:
            leaders_item = CompetitionLeader.from_dict(leaders_item_data)

            leaders.append(leaders_item)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, GameFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = GameFormat.from_dict(_format_)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        broadcast = d.pop("broadcast", UNSET)

        geo_broadcasts = []
        _geo_broadcasts = d.pop("geoBroadcasts", UNSET)
        for geo_broadcasts_item_data in _geo_broadcasts or []:
            geo_broadcasts_item = GeoBroadcast.from_dict(geo_broadcasts_item_data)

            geo_broadcasts.append(geo_broadcasts_item)

        highlights = []
        _highlights = d.pop("highlights", UNSET)
        for highlights_item_data in _highlights or []:
            highlights_item = EventCompetitionHighlightsItem.from_dict(highlights_item_data)

            highlights.append(highlights_item)

        headlines = []
        _headlines = d.pop("headlines", UNSET)
        for headlines_item_data in _headlines or []:
            headlines_item = Headline.from_dict(headlines_item_data)

            headlines.append(headlines_item)

        event_competition = cls(
            id=id,
            date=date,
            competitors=competitors,
            uid=uid,
            attendance=attendance,
            type_=type_,
            time_valid=time_valid,
            neutral_site=neutral_site,
            conference_competition=conference_competition,
            play_by_play_available=play_by_play_available,
            recent=recent,
            venue=venue,
            notes=notes,
            status=status,
            broadcasts=broadcasts,
            leaders=leaders,
            format_=format_,
            start_date=start_date,
            broadcast=broadcast,
            geo_broadcasts=geo_broadcasts,
            highlights=highlights,
            headlines=headlines,
        )

        event_competition.additional_properties = d
        return event_competition

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
