from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_broadcast import ScoreboardBroadcast
    from ..models.scoreboard_competition_type import ScoreboardCompetitionType
    from ..models.scoreboard_competitor import ScoreboardCompetitor
    from ..models.scoreboard_format import ScoreboardFormat
    from ..models.scoreboard_geo_broadcast import ScoreboardGeoBroadcast
    from ..models.scoreboard_note import ScoreboardNote
    from ..models.scoreboard_ticket import ScoreboardTicket
    from ..models.scoreboard_venue import ScoreboardVenue


T = TypeVar("T", bound="ScoreboardCompetition")


@_attrs_define
class ScoreboardCompetition:
    """
    Attributes:
        date (Union[Unset, str]):
        broadcast (Union[Unset, str]):
        venue (Union[Unset, ScoreboardVenue]):
        conference_competition (Union[Unset, bool]):
        notes (Union[Unset, List['ScoreboardNote']]):
        tickets (Union[Unset, List['ScoreboardTicket']]):
        time_valid (Union[Unset, bool]):
        geo_broadcasts (Union[Unset, List['ScoreboardGeoBroadcast']]):
        format_ (Union[Unset, ScoreboardFormat]):
        broadcasts (Union[Unset, List['ScoreboardBroadcast']]):
        play_by_play_available (Union[Unset, bool]):
        type (Union[Unset, ScoreboardCompetitionType]):
        uid (Union[Unset, str]):
        competitors (Union[Unset, List['ScoreboardCompetitor']]):
    """

    date: Union[Unset, str] = UNSET
    broadcast: Union[Unset, str] = UNSET
    venue: Union[Unset, "ScoreboardVenue"] = UNSET
    conference_competition: Union[Unset, bool] = UNSET
    notes: Union[Unset, List["ScoreboardNote"]] = UNSET
    tickets: Union[Unset, List["ScoreboardTicket"]] = UNSET
    time_valid: Union[Unset, bool] = UNSET
    geo_broadcasts: Union[Unset, List["ScoreboardGeoBroadcast"]] = UNSET
    format_: Union[Unset, "ScoreboardFormat"] = UNSET
    broadcasts: Union[Unset, List["ScoreboardBroadcast"]] = UNSET
    play_by_play_available: Union[Unset, bool] = UNSET
    type: Union[Unset, "ScoreboardCompetitionType"] = UNSET
    uid: Union[Unset, str] = UNSET
    competitors: Union[Unset, List["ScoreboardCompetitor"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date

        broadcast = self.broadcast

        venue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.to_dict()

        conference_competition = self.conference_competition

        notes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()
                notes.append(notes_item)

        tickets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tickets, Unset):
            tickets = []
            for tickets_item_data in self.tickets:
                tickets_item = tickets_item_data.to_dict()
                tickets.append(tickets_item)

        time_valid = self.time_valid

        geo_broadcasts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.geo_broadcasts, Unset):
            geo_broadcasts = []
            for geo_broadcasts_item_data in self.geo_broadcasts:
                geo_broadcasts_item = geo_broadcasts_item_data.to_dict()
                geo_broadcasts.append(geo_broadcasts_item)

        format_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.to_dict()

        broadcasts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.broadcasts, Unset):
            broadcasts = []
            for broadcasts_item_data in self.broadcasts:
                broadcasts_item = broadcasts_item_data.to_dict()
                broadcasts.append(broadcasts_item)

        play_by_play_available = self.play_by_play_available

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        uid = self.uid

        competitors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitors, Unset):
            competitors = []
            for competitors_item_data in self.competitors:
                competitors_item = competitors_item_data.to_dict()
                competitors.append(competitors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if broadcast is not UNSET:
            field_dict["broadcast"] = broadcast
        if venue is not UNSET:
            field_dict["venue"] = venue
        if conference_competition is not UNSET:
            field_dict["conferenceCompetition"] = conference_competition
        if notes is not UNSET:
            field_dict["notes"] = notes
        if tickets is not UNSET:
            field_dict["tickets"] = tickets
        if time_valid is not UNSET:
            field_dict["timeValid"] = time_valid
        if geo_broadcasts is not UNSET:
            field_dict["geoBroadcasts"] = geo_broadcasts
        if format_ is not UNSET:
            field_dict["format"] = format_
        if broadcasts is not UNSET:
            field_dict["broadcasts"] = broadcasts
        if play_by_play_available is not UNSET:
            field_dict["playByPlayAvailable"] = play_by_play_available
        if type is not UNSET:
            field_dict["type"] = type
        if uid is not UNSET:
            field_dict["uid"] = uid
        if competitors is not UNSET:
            field_dict["competitors"] = competitors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_broadcast import ScoreboardBroadcast
        from ..models.scoreboard_competition_type import ScoreboardCompetitionType
        from ..models.scoreboard_competitor import ScoreboardCompetitor
        from ..models.scoreboard_format import ScoreboardFormat
        from ..models.scoreboard_geo_broadcast import ScoreboardGeoBroadcast
        from ..models.scoreboard_note import ScoreboardNote
        from ..models.scoreboard_ticket import ScoreboardTicket
        from ..models.scoreboard_venue import ScoreboardVenue

        d = src_dict.copy()
        date = d.pop("date", UNSET)

        broadcast = d.pop("broadcast", UNSET)

        _venue = d.pop("venue", UNSET)
        venue: Union[Unset, ScoreboardVenue]
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = ScoreboardVenue.from_dict(_venue)

        conference_competition = d.pop("conferenceCompetition", UNSET)

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = ScoreboardNote.from_dict(notes_item_data)

            notes.append(notes_item)

        tickets = []
        _tickets = d.pop("tickets", UNSET)
        for tickets_item_data in _tickets or []:
            tickets_item = ScoreboardTicket.from_dict(tickets_item_data)

            tickets.append(tickets_item)

        time_valid = d.pop("timeValid", UNSET)

        geo_broadcasts = []
        _geo_broadcasts = d.pop("geoBroadcasts", UNSET)
        for geo_broadcasts_item_data in _geo_broadcasts or []:
            geo_broadcasts_item = ScoreboardGeoBroadcast.from_dict(geo_broadcasts_item_data)

            geo_broadcasts.append(geo_broadcasts_item)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, ScoreboardFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = ScoreboardFormat.from_dict(_format_)

        broadcasts = []
        _broadcasts = d.pop("broadcasts", UNSET)
        for broadcasts_item_data in _broadcasts or []:
            broadcasts_item = ScoreboardBroadcast.from_dict(broadcasts_item_data)

            broadcasts.append(broadcasts_item)

        play_by_play_available = d.pop("playByPlayAvailable", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ScoreboardCompetitionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ScoreboardCompetitionType.from_dict(_type)

        uid = d.pop("uid", UNSET)

        competitors = []
        _competitors = d.pop("competitors", UNSET)
        for competitors_item_data in _competitors or []:
            competitors_item = ScoreboardCompetitor.from_dict(competitors_item_data)

            competitors.append(competitors_item)

        scoreboard_competition = cls(
            date=date,
            broadcast=broadcast,
            venue=venue,
            conference_competition=conference_competition,
            notes=notes,
            tickets=tickets,
            time_valid=time_valid,
            geo_broadcasts=geo_broadcasts,
            format_=format_,
            broadcasts=broadcasts,
            play_by_play_available=play_by_play_available,
            type=type,
            uid=uid,
            competitors=competitors,
        )

        scoreboard_competition.additional_properties = d
        return scoreboard_competition

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
