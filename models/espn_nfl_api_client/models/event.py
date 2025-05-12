import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_competition import EventCompetition
    from ..models.event_season import EventSeason
    from ..models.event_week import EventWeek
    from ..models.game_status import GameStatus
    from ..models.link import Link


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """
    Attributes:
        id (str):  Example: 401671889.
        date (datetime.datetime):
        competitions (List['EventCompetition']):
        uid (Union[Unset, str]):  Example: s:20~l:28~e:401671889.
        name (Union[Unset, str]):  Example: Kansas City Chiefs at Philadelphia Eagles.
        short_name (Union[Unset, str]):  Example: KC VS PHI.
        season (Union[Unset, EventSeason]):
        week (Union[Unset, EventWeek]):
        links (Union[Unset, List['Link']]):
        status (Union[Unset, GameStatus]):
    """

    id: str
    date: datetime.datetime
    competitions: List["EventCompetition"]
    uid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    season: Union[Unset, "EventSeason"] = UNSET
    week: Union[Unset, "EventWeek"] = UNSET
    links: Union[Unset, List["Link"]] = UNSET
    status: Union[Unset, "GameStatus"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        date = self.date.isoformat()

        competitions = []
        for competitions_item_data in self.competitions:
            competitions_item = competitions_item_data.to_dict()
            competitions.append(competitions_item)

        uid = self.uid

        name = self.name

        short_name = self.short_name

        season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        week: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.week, Unset):
            week = self.week.to_dict()

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "competitions": competitions,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if season is not UNSET:
            field_dict["season"] = season
        if week is not UNSET:
            field_dict["week"] = week
        if links is not UNSET:
            field_dict["links"] = links
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_competition import EventCompetition
        from ..models.event_season import EventSeason
        from ..models.event_week import EventWeek
        from ..models.game_status import GameStatus
        from ..models.link import Link

        d = src_dict.copy()
        id = d.pop("id")

        date = isoparse(d.pop("date"))

        competitions = []
        _competitions = d.pop("competitions")
        for competitions_item_data in _competitions:
            competitions_item = EventCompetition.from_dict(competitions_item_data)

            competitions.append(competitions_item)

        uid = d.pop("uid", UNSET)

        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        _season = d.pop("season", UNSET)
        season: Union[Unset, EventSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = EventSeason.from_dict(_season)

        _week = d.pop("week", UNSET)
        week: Union[Unset, EventWeek]
        if isinstance(_week, Unset):
            week = UNSET
        else:
            week = EventWeek.from_dict(_week)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, GameStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GameStatus.from_dict(_status)

        event = cls(
            id=id,
            date=date,
            competitions=competitions,
            uid=uid,
            name=name,
            short_name=short_name,
            season=season,
            week=week,
            links=links,
            status=status,
        )

        event.additional_properties = d
        return event

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
