import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.competition_type import CompetitionType
    from ..models.competitor import Competitor
    from ..models.game_status import GameStatus
    from ..models.venue import Venue


T = TypeVar("T", bound="Competition")


@_attrs_define
class Competition:
    """
    Attributes:
        id (str):  Example: 401547417.
        uid (str):  Example: s:20~l:28~e:401547417~c:401547417.
        date (datetime.datetime):  Example: 2023-02-12T23:30:00Z.
        competitors (List['Competitor']):
        attendance (Union[Unset, int]):  Example: 70048.
        type (Union[Unset, CompetitionType]):
        time_valid (Union[Unset, bool]):
        neutral_site (Union[Unset, bool]):
        conference_competition (Union[Unset, bool]):
        play_by_play_available (Union[Unset, bool]):
        recent (Union[Unset, bool]):
        venue (Union[Unset, Venue]):
        notes (Union[Unset, List[str]]):
        status (Union[Unset, GameStatus]):
    """

    id: str
    uid: str
    date: datetime.datetime
    competitors: List["Competitor"]
    attendance: Union[Unset, int] = UNSET
    type: Union[Unset, "CompetitionType"] = UNSET
    time_valid: Union[Unset, bool] = UNSET
    neutral_site: Union[Unset, bool] = UNSET
    conference_competition: Union[Unset, bool] = UNSET
    play_by_play_available: Union[Unset, bool] = UNSET
    recent: Union[Unset, bool] = UNSET
    venue: Union[Unset, "Venue"] = UNSET
    notes: Union[Unset, List[str]] = UNSET
    status: Union[Unset, "GameStatus"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        uid = self.uid

        date = self.date.isoformat()

        competitors = []
        for competitors_item_data in self.competitors:
            competitors_item = competitors_item_data.to_dict()
            competitors.append(competitors_item)

        attendance = self.attendance

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        time_valid = self.time_valid

        neutral_site = self.neutral_site

        conference_competition = self.conference_competition

        play_by_play_available = self.play_by_play_available

        recent = self.recent

        venue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.to_dict()

        notes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = self.notes

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uid": uid,
                "date": date,
                "competitors": competitors,
            }
        )
        if attendance is not UNSET:
            field_dict["attendance"] = attendance
        if type is not UNSET:
            field_dict["type"] = type
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.competition_type import CompetitionType
        from ..models.competitor import Competitor
        from ..models.game_status import GameStatus
        from ..models.venue import Venue

        d = src_dict.copy()
        id = d.pop("id")

        uid = d.pop("uid")

        date = isoparse(d.pop("date"))

        competitors = []
        _competitors = d.pop("competitors")
        for competitors_item_data in _competitors:
            competitors_item = Competitor.from_dict(competitors_item_data)

            competitors.append(competitors_item)

        attendance = d.pop("attendance", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CompetitionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CompetitionType.from_dict(_type)

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

        notes = cast(List[str], d.pop("notes", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, GameStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GameStatus.from_dict(_status)

        competition = cls(
            id=id,
            uid=uid,
            date=date,
            competitors=competitors,
            attendance=attendance,
            type=type,
            time_valid=time_valid,
            neutral_site=neutral_site,
            conference_competition=conference_competition,
            play_by_play_available=play_by_play_available,
            recent=recent,
            venue=venue,
            notes=notes,
            status=status,
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
