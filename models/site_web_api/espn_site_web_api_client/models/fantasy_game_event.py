import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fantasy_broadcast import FantasyBroadcast
    from ..models.fantasy_competitor import FantasyCompetitor
    from ..models.fantasy_full_status import FantasyFullStatus
    from ..models.fantasy_game_event_against_the_spread import FantasyGameEventAgainstTheSpread
    from ..models.fantasy_game_event_drive import FantasyGameEventDrive
    from ..models.fantasy_game_event_last_play import FantasyGameEventLastPlay
    from ..models.fantasy_game_event_links_item import FantasyGameEventLinksItem
    from ..models.fantasy_game_event_odds import FantasyGameEventOdds
    from ..models.fantasy_game_event_pickcenter_item import FantasyGameEventPickcenterItem
    from ..models.fantasy_game_event_scoring_plays_item import FantasyGameEventScoringPlaysItem
    from ..models.fantasy_venue import FantasyVenue
    from ..models.fantasy_weather import FantasyWeather


T = TypeVar("T", bound="FantasyGameEvent")


@_attrs_define
class FantasyGameEvent:
    """
    Attributes:
        id (Union[Unset, str]): Event ID
        competition_id (Union[Unset, str]): Competition ID
        uid (Union[Unset, str]): Unique identifier
        date (Union[Unset, datetime.datetime]): Game date and time
        time_valid (Union[Unset, bool]): Whether the time is confirmed
        period (Union[Unset, int]): Current period/quarter
        clock (Union[Unset, str]): Game clock
        status (Union[Unset, str]): Game status (pre, in, post, etc.)
        summary (Union[Unset, str]): Game summary text
        full_status (Union[Unset, FantasyFullStatus]):
        competitors (Union[Unset, List['FantasyCompetitor']]):
        venue (Union[Unset, FantasyVenue]):
        weather (Union[Unset, FantasyWeather]):
        broadcasts (Union[Unset, List['FantasyBroadcast']]):
        links (Union[Unset, List['FantasyGameEventLinksItem']]):
        odds (Union[Unset, FantasyGameEventOdds]): Odds information
        against_the_spread (Union[Unset, FantasyGameEventAgainstTheSpread]): Against the spread information
        pickcenter (Union[Unset, List['FantasyGameEventPickcenterItem']]):
        scoring_plays (Union[Unset, List['FantasyGameEventScoringPlaysItem']]):
        percent_complete (Union[Unset, int]): Percentage of game completed
        last_play (Union[Unset, FantasyGameEventLastPlay]): Last play information
        drive (Union[Unset, FantasyGameEventDrive]): Current drive information
        broadcast (Union[Unset, str]): Broadcast information
        link (Union[Unset, str]): Link to game
    """

    id: Union[Unset, str] = UNSET
    competition_id: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    time_valid: Union[Unset, bool] = UNSET
    period: Union[Unset, int] = UNSET
    clock: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    full_status: Union[Unset, "FantasyFullStatus"] = UNSET
    competitors: Union[Unset, List["FantasyCompetitor"]] = UNSET
    venue: Union[Unset, "FantasyVenue"] = UNSET
    weather: Union[Unset, "FantasyWeather"] = UNSET
    broadcasts: Union[Unset, List["FantasyBroadcast"]] = UNSET
    links: Union[Unset, List["FantasyGameEventLinksItem"]] = UNSET
    odds: Union[Unset, "FantasyGameEventOdds"] = UNSET
    against_the_spread: Union[Unset, "FantasyGameEventAgainstTheSpread"] = UNSET
    pickcenter: Union[Unset, List["FantasyGameEventPickcenterItem"]] = UNSET
    scoring_plays: Union[Unset, List["FantasyGameEventScoringPlaysItem"]] = UNSET
    percent_complete: Union[Unset, int] = UNSET
    last_play: Union[Unset, "FantasyGameEventLastPlay"] = UNSET
    drive: Union[Unset, "FantasyGameEventDrive"] = UNSET
    broadcast: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        competition_id = self.competition_id

        uid = self.uid

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        time_valid = self.time_valid

        period = self.period

        clock = self.clock

        status = self.status

        summary = self.summary

        full_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.full_status, Unset):
            full_status = self.full_status.to_dict()

        competitors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitors, Unset):
            competitors = []
            for competitors_item_data in self.competitors:
                competitors_item = competitors_item_data.to_dict()
                competitors.append(competitors_item)

        venue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.to_dict()

        weather: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.weather, Unset):
            weather = self.weather.to_dict()

        broadcasts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.broadcasts, Unset):
            broadcasts = []
            for broadcasts_item_data in self.broadcasts:
                broadcasts_item = broadcasts_item_data.to_dict()
                broadcasts.append(broadcasts_item)

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        odds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odds, Unset):
            odds = self.odds.to_dict()

        against_the_spread: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.against_the_spread, Unset):
            against_the_spread = self.against_the_spread.to_dict()

        pickcenter: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pickcenter, Unset):
            pickcenter = []
            for pickcenter_item_data in self.pickcenter:
                pickcenter_item = pickcenter_item_data.to_dict()
                pickcenter.append(pickcenter_item)

        scoring_plays: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.scoring_plays, Unset):
            scoring_plays = []
            for scoring_plays_item_data in self.scoring_plays:
                scoring_plays_item = scoring_plays_item_data.to_dict()
                scoring_plays.append(scoring_plays_item)

        percent_complete = self.percent_complete

        last_play: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_play, Unset):
            last_play = self.last_play.to_dict()

        drive: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.drive, Unset):
            drive = self.drive.to_dict()

        broadcast = self.broadcast

        link = self.link

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if competition_id is not UNSET:
            field_dict["competitionId"] = competition_id
        if uid is not UNSET:
            field_dict["uid"] = uid
        if date is not UNSET:
            field_dict["date"] = date
        if time_valid is not UNSET:
            field_dict["timeValid"] = time_valid
        if period is not UNSET:
            field_dict["period"] = period
        if clock is not UNSET:
            field_dict["clock"] = clock
        if status is not UNSET:
            field_dict["status"] = status
        if summary is not UNSET:
            field_dict["summary"] = summary
        if full_status is not UNSET:
            field_dict["fullStatus"] = full_status
        if competitors is not UNSET:
            field_dict["competitors"] = competitors
        if venue is not UNSET:
            field_dict["venue"] = venue
        if weather is not UNSET:
            field_dict["weather"] = weather
        if broadcasts is not UNSET:
            field_dict["broadcasts"] = broadcasts
        if links is not UNSET:
            field_dict["links"] = links
        if odds is not UNSET:
            field_dict["odds"] = odds
        if against_the_spread is not UNSET:
            field_dict["againstTheSpread"] = against_the_spread
        if pickcenter is not UNSET:
            field_dict["pickcenter"] = pickcenter
        if scoring_plays is not UNSET:
            field_dict["scoringPlays"] = scoring_plays
        if percent_complete is not UNSET:
            field_dict["percentComplete"] = percent_complete
        if last_play is not UNSET:
            field_dict["lastPlay"] = last_play
        if drive is not UNSET:
            field_dict["drive"] = drive
        if broadcast is not UNSET:
            field_dict["broadcast"] = broadcast
        if link is not UNSET:
            field_dict["link"] = link

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fantasy_broadcast import FantasyBroadcast
        from ..models.fantasy_competitor import FantasyCompetitor
        from ..models.fantasy_full_status import FantasyFullStatus
        from ..models.fantasy_game_event_against_the_spread import FantasyGameEventAgainstTheSpread
        from ..models.fantasy_game_event_drive import FantasyGameEventDrive
        from ..models.fantasy_game_event_last_play import FantasyGameEventLastPlay
        from ..models.fantasy_game_event_links_item import FantasyGameEventLinksItem
        from ..models.fantasy_game_event_odds import FantasyGameEventOdds
        from ..models.fantasy_game_event_pickcenter_item import FantasyGameEventPickcenterItem
        from ..models.fantasy_game_event_scoring_plays_item import FantasyGameEventScoringPlaysItem
        from ..models.fantasy_venue import FantasyVenue
        from ..models.fantasy_weather import FantasyWeather

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        competition_id = d.pop("competitionId", UNSET)

        uid = d.pop("uid", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        time_valid = d.pop("timeValid", UNSET)

        period = d.pop("period", UNSET)

        clock = d.pop("clock", UNSET)

        status = d.pop("status", UNSET)

        summary = d.pop("summary", UNSET)

        _full_status = d.pop("fullStatus", UNSET)
        full_status: Union[Unset, FantasyFullStatus]
        if isinstance(_full_status, Unset):
            full_status = UNSET
        else:
            full_status = FantasyFullStatus.from_dict(_full_status)

        competitors = []
        _competitors = d.pop("competitors", UNSET)
        for competitors_item_data in _competitors or []:
            competitors_item = FantasyCompetitor.from_dict(competitors_item_data)

            competitors.append(competitors_item)

        _venue = d.pop("venue", UNSET)
        venue: Union[Unset, FantasyVenue]
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = FantasyVenue.from_dict(_venue)

        _weather = d.pop("weather", UNSET)
        weather: Union[Unset, FantasyWeather]
        if isinstance(_weather, Unset):
            weather = UNSET
        else:
            weather = FantasyWeather.from_dict(_weather)

        broadcasts = []
        _broadcasts = d.pop("broadcasts", UNSET)
        for broadcasts_item_data in _broadcasts or []:
            broadcasts_item = FantasyBroadcast.from_dict(broadcasts_item_data)

            broadcasts.append(broadcasts_item)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = FantasyGameEventLinksItem.from_dict(links_item_data)

            links.append(links_item)

        _odds = d.pop("odds", UNSET)
        odds: Union[Unset, FantasyGameEventOdds]
        if isinstance(_odds, Unset):
            odds = UNSET
        else:
            odds = FantasyGameEventOdds.from_dict(_odds)

        _against_the_spread = d.pop("againstTheSpread", UNSET)
        against_the_spread: Union[Unset, FantasyGameEventAgainstTheSpread]
        if isinstance(_against_the_spread, Unset):
            against_the_spread = UNSET
        else:
            against_the_spread = FantasyGameEventAgainstTheSpread.from_dict(_against_the_spread)

        pickcenter = []
        _pickcenter = d.pop("pickcenter", UNSET)
        for pickcenter_item_data in _pickcenter or []:
            pickcenter_item = FantasyGameEventPickcenterItem.from_dict(pickcenter_item_data)

            pickcenter.append(pickcenter_item)

        scoring_plays = []
        _scoring_plays = d.pop("scoringPlays", UNSET)
        for scoring_plays_item_data in _scoring_plays or []:
            scoring_plays_item = FantasyGameEventScoringPlaysItem.from_dict(scoring_plays_item_data)

            scoring_plays.append(scoring_plays_item)

        percent_complete = d.pop("percentComplete", UNSET)

        _last_play = d.pop("lastPlay", UNSET)
        last_play: Union[Unset, FantasyGameEventLastPlay]
        if isinstance(_last_play, Unset):
            last_play = UNSET
        else:
            last_play = FantasyGameEventLastPlay.from_dict(_last_play)

        _drive = d.pop("drive", UNSET)
        drive: Union[Unset, FantasyGameEventDrive]
        if isinstance(_drive, Unset):
            drive = UNSET
        else:
            drive = FantasyGameEventDrive.from_dict(_drive)

        broadcast = d.pop("broadcast", UNSET)

        link = d.pop("link", UNSET)

        fantasy_game_event = cls(
            id=id,
            competition_id=competition_id,
            uid=uid,
            date=date,
            time_valid=time_valid,
            period=period,
            clock=clock,
            status=status,
            summary=summary,
            full_status=full_status,
            competitors=competitors,
            venue=venue,
            weather=weather,
            broadcasts=broadcasts,
            links=links,
            odds=odds,
            against_the_spread=against_the_spread,
            pickcenter=pickcenter,
            scoring_plays=scoring_plays,
            percent_complete=percent_complete,
            last_play=last_play,
            drive=drive,
            broadcast=broadcast,
            link=link,
        )

        fantasy_game_event.additional_properties = d
        return fantasy_game_event

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
