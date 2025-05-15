import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_detail_competitions_item_type_1 import EventDetailCompetitionsItemType1
    from ..models.event_detail_league_type_1 import EventDetailLeagueType1
    from ..models.event_detail_season_type_1 import EventDetailSeasonType1
    from ..models.event_detail_season_type_type_1 import EventDetailSeasonTypeType1
    from ..models.event_detail_venues_item_type_1 import EventDetailVenuesItemType1
    from ..models.event_detail_week_type_1 import EventDetailWeekType1
    from ..models.link import Link
    from ..models.reference import Reference


T = TypeVar("T", bound="EventDetail")


@_attrs_define
class EventDetail:
    """
    Attributes:
        id (str):
        date (datetime.datetime):
        competitions (List[Union['EventDetailCompetitionsItemType1', 'Reference']]):
        ref (Union[Unset, str]):
        uid (Union[Unset, str]):
        name (Union[Unset, str]):
        short_name (Union[Unset, str]):
        season (Union['EventDetailSeasonType1', 'Reference', Unset]):
        season_type (Union['EventDetailSeasonTypeType1', 'Reference', Unset]):
        week (Union['EventDetailWeekType1', 'Reference', Unset]):
        time_valid (Union[Unset, bool]):
        links (Union[Unset, List['Link']]):
        venues (Union[Unset, List[Union['EventDetailVenuesItemType1', 'Reference']]]):
        league (Union['EventDetailLeagueType1', 'Reference', Unset]):
    """

    id: str
    date: datetime.datetime
    competitions: List[Union["EventDetailCompetitionsItemType1", "Reference"]]
    ref: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    season: Union["EventDetailSeasonType1", "Reference", Unset] = UNSET
    season_type: Union["EventDetailSeasonTypeType1", "Reference", Unset] = UNSET
    week: Union["EventDetailWeekType1", "Reference", Unset] = UNSET
    time_valid: Union[Unset, bool] = UNSET
    links: Union[Unset, List["Link"]] = UNSET
    venues: Union[Unset, List[Union["EventDetailVenuesItemType1", "Reference"]]] = UNSET
    league: Union["EventDetailLeagueType1", "Reference", Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.reference import Reference

        id = self.id

        date = self.date.isoformat()

        competitions = []
        for competitions_item_data in self.competitions:
            competitions_item: Dict[str, Any]
            if isinstance(competitions_item_data, Reference):
                competitions_item = competitions_item_data.to_dict()
            else:
                competitions_item = competitions_item_data.to_dict()

            competitions.append(competitions_item)

        ref = self.ref

        uid = self.uid

        name = self.name

        short_name = self.short_name

        season: Union[Dict[str, Any], Unset]
        if isinstance(self.season, Unset):
            season = UNSET
        elif isinstance(self.season, Reference):
            season = self.season.to_dict()
        else:
            season = self.season.to_dict()

        season_type: Union[Dict[str, Any], Unset]
        if isinstance(self.season_type, Unset):
            season_type = UNSET
        elif isinstance(self.season_type, Reference):
            season_type = self.season_type.to_dict()
        else:
            season_type = self.season_type.to_dict()

        week: Union[Dict[str, Any], Unset]
        if isinstance(self.week, Unset):
            week = UNSET
        elif isinstance(self.week, Reference):
            week = self.week.to_dict()
        else:
            week = self.week.to_dict()

        time_valid = self.time_valid

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        venues: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.venues, Unset):
            venues = []
            for venues_item_data in self.venues:
                venues_item: Dict[str, Any]
                if isinstance(venues_item_data, Reference):
                    venues_item = venues_item_data.to_dict()
                else:
                    venues_item = venues_item_data.to_dict()

                venues.append(venues_item)

        league: Union[Dict[str, Any], Unset]
        if isinstance(self.league, Unset):
            league = UNSET
        elif isinstance(self.league, Reference):
            league = self.league.to_dict()
        else:
            league = self.league.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "competitions": competitions,
            }
        )
        if ref is not UNSET:
            field_dict["$ref"] = ref
        if uid is not UNSET:
            field_dict["uid"] = uid
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if season is not UNSET:
            field_dict["season"] = season
        if season_type is not UNSET:
            field_dict["seasonType"] = season_type
        if week is not UNSET:
            field_dict["week"] = week
        if time_valid is not UNSET:
            field_dict["timeValid"] = time_valid
        if links is not UNSET:
            field_dict["links"] = links
        if venues is not UNSET:
            field_dict["venues"] = venues
        if league is not UNSET:
            field_dict["league"] = league

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_detail_competitions_item_type_1 import EventDetailCompetitionsItemType1
        from ..models.event_detail_league_type_1 import EventDetailLeagueType1
        from ..models.event_detail_season_type_1 import EventDetailSeasonType1
        from ..models.event_detail_season_type_type_1 import EventDetailSeasonTypeType1
        from ..models.event_detail_venues_item_type_1 import EventDetailVenuesItemType1
        from ..models.event_detail_week_type_1 import EventDetailWeekType1
        from ..models.link import Link
        from ..models.reference import Reference

        d = src_dict.copy()
        id = d.pop("id")

        date = isoparse(d.pop("date"))

        competitions = []
        _competitions = d.pop("competitions")
        for competitions_item_data in _competitions:

            def _parse_competitions_item(data: object) -> Union["EventDetailCompetitionsItemType1", "Reference"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    competitions_item_type_0 = Reference.from_dict(data)

                    return competitions_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                competitions_item_type_1 = EventDetailCompetitionsItemType1.from_dict(data)

                return competitions_item_type_1

            competitions_item = _parse_competitions_item(competitions_item_data)

            competitions.append(competitions_item)

        ref = d.pop("$ref", UNSET)

        uid = d.pop("uid", UNSET)

        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        def _parse_season(data: object) -> Union["EventDetailSeasonType1", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                season_type_0 = Reference.from_dict(data)

                return season_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            season_type_1 = EventDetailSeasonType1.from_dict(data)

            return season_type_1

        season = _parse_season(d.pop("season", UNSET))

        def _parse_season_type(data: object) -> Union["EventDetailSeasonTypeType1", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                season_type_type_0 = Reference.from_dict(data)

                return season_type_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            season_type_type_1 = EventDetailSeasonTypeType1.from_dict(data)

            return season_type_type_1

        season_type = _parse_season_type(d.pop("seasonType", UNSET))

        def _parse_week(data: object) -> Union["EventDetailWeekType1", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                week_type_0 = Reference.from_dict(data)

                return week_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            week_type_1 = EventDetailWeekType1.from_dict(data)

            return week_type_1

        week = _parse_week(d.pop("week", UNSET))

        time_valid = d.pop("timeValid", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        venues = []
        _venues = d.pop("venues", UNSET)
        for venues_item_data in _venues or []:

            def _parse_venues_item(data: object) -> Union["EventDetailVenuesItemType1", "Reference"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    venues_item_type_0 = Reference.from_dict(data)

                    return venues_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                venues_item_type_1 = EventDetailVenuesItemType1.from_dict(data)

                return venues_item_type_1

            venues_item = _parse_venues_item(venues_item_data)

            venues.append(venues_item)

        def _parse_league(data: object) -> Union["EventDetailLeagueType1", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                league_type_0 = Reference.from_dict(data)

                return league_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            league_type_1 = EventDetailLeagueType1.from_dict(data)

            return league_type_1

        league = _parse_league(d.pop("league", UNSET))

        event_detail = cls(
            id=id,
            date=date,
            competitions=competitions,
            ref=ref,
            uid=uid,
            name=name,
            short_name=short_name,
            season=season,
            season_type=season_type,
            week=week,
            time_valid=time_valid,
            links=links,
            venues=venues,
            league=league,
        )

        event_detail.additional_properties = d
        return event_detail

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
