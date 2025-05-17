import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_header_response_sports_item_leagues_item_events_item_app_links_item import (
        ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemAppLinksItem,
    )
    from ..models.scoreboard_header_response_sports_item_leagues_item_events_item_broadcasts_item import (
        ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemBroadcastsItem,
    )
    from ..models.scoreboard_header_response_sports_item_leagues_item_events_item_competitors_item import (
        ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemCompetitorsItem,
    )
    from ..models.scoreboard_header_response_sports_item_leagues_item_events_item_full_status import (
        ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemFullStatus,
    )
    from ..models.scoreboard_header_response_sports_item_leagues_item_events_item_group import (
        ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemGroup,
    )
    from ..models.scoreboard_header_response_sports_item_leagues_item_events_item_links_item import (
        ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemLinksItem,
    )
    from ..models.scoreboard_header_response_sports_item_leagues_item_events_item_odds import (
        ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemOdds,
    )


T = TypeVar("T", bound="ScoreboardHeaderResponseSportsItemLeaguesItemEventsItem")


@_attrs_define
class ScoreboardHeaderResponseSportsItemLeaguesItemEventsItem:
    """
    Attributes:
        id (Union[Unset, str]):
        uid (Union[Unset, str]):
        guid (Union[Unset, str]):
        date (Union[Unset, datetime.datetime]):
        time_valid (Union[Unset, bool]):
        recent (Union[Unset, bool]):
        name (Union[Unset, str]):
        short_name (Union[Unset, str]):
        links (Union[Unset, List['ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemLinksItem']]):
        gamecast_available (Union[Unset, bool]):
        play_by_play_available (Union[Unset, bool]):
        commentary_available (Union[Unset, bool]):
        wallclock_available (Union[Unset, bool]):
        on_watch (Union[Unset, bool]):
        competition_id (Union[Unset, str]):
        location (Union[Unset, str]):
        season (Union[Unset, int]):
        season_start_date (Union[Unset, str]):
        season_end_date (Union[Unset, str]):
        season_type (Union[Unset, str]):
        season_type_has_groups (Union[Unset, bool]):
        group (Union[Unset, ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemGroup]):
        week (Union[Unset, int]):
        week_text (Union[Unset, str]):
        link (Union[Unset, str]):
        status (Union[Unset, str]):
        summary (Union[Unset, str]):
        period (Union[Unset, int]):
        clock (Union[Unset, str]):
        broadcasts (Union[Unset, List['ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemBroadcastsItem']]):
        broadcast (Union[Unset, str]):
        odds (Union[Unset, ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemOdds]):
        full_status (Union[Unset, ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemFullStatus]):
        competitors (Union[Unset, List['ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemCompetitorsItem']]):
        neutral_site (Union[Unset, bool]):
        app_links (Union[Unset, List['ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemAppLinksItem']]):
    """

    id: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    time_valid: Union[Unset, bool] = UNSET
    recent: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    links: Union[Unset, List["ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemLinksItem"]] = UNSET
    gamecast_available: Union[Unset, bool] = UNSET
    play_by_play_available: Union[Unset, bool] = UNSET
    commentary_available: Union[Unset, bool] = UNSET
    wallclock_available: Union[Unset, bool] = UNSET
    on_watch: Union[Unset, bool] = UNSET
    competition_id: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    season: Union[Unset, int] = UNSET
    season_start_date: Union[Unset, str] = UNSET
    season_end_date: Union[Unset, str] = UNSET
    season_type: Union[Unset, str] = UNSET
    season_type_has_groups: Union[Unset, bool] = UNSET
    group: Union[Unset, "ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemGroup"] = UNSET
    week: Union[Unset, int] = UNSET
    week_text: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    period: Union[Unset, int] = UNSET
    clock: Union[Unset, str] = UNSET
    broadcasts: Union[Unset, List["ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemBroadcastsItem"]] = UNSET
    broadcast: Union[Unset, str] = UNSET
    odds: Union[Unset, "ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemOdds"] = UNSET
    full_status: Union[Unset, "ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemFullStatus"] = UNSET
    competitors: Union[Unset, List["ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemCompetitorsItem"]] = UNSET
    neutral_site: Union[Unset, bool] = UNSET
    app_links: Union[Unset, List["ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemAppLinksItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        uid = self.uid

        guid = self.guid

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        time_valid = self.time_valid

        recent = self.recent

        name = self.name

        short_name = self.short_name

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        gamecast_available = self.gamecast_available

        play_by_play_available = self.play_by_play_available

        commentary_available = self.commentary_available

        wallclock_available = self.wallclock_available

        on_watch = self.on_watch

        competition_id = self.competition_id

        location = self.location

        season = self.season

        season_start_date = self.season_start_date

        season_end_date = self.season_end_date

        season_type = self.season_type

        season_type_has_groups = self.season_type_has_groups

        group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        week = self.week

        week_text = self.week_text

        link = self.link

        status = self.status

        summary = self.summary

        period = self.period

        clock = self.clock

        broadcasts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.broadcasts, Unset):
            broadcasts = []
            for broadcasts_item_data in self.broadcasts:
                broadcasts_item = broadcasts_item_data.to_dict()
                broadcasts.append(broadcasts_item)

        broadcast = self.broadcast

        odds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odds, Unset):
            odds = self.odds.to_dict()

        full_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.full_status, Unset):
            full_status = self.full_status.to_dict()

        competitors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitors, Unset):
            competitors = []
            for competitors_item_data in self.competitors:
                competitors_item = competitors_item_data.to_dict()
                competitors.append(competitors_item)

        neutral_site = self.neutral_site

        app_links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.app_links, Unset):
            app_links = []
            for app_links_item_data in self.app_links:
                app_links_item = app_links_item_data.to_dict()
                app_links.append(app_links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uid is not UNSET:
            field_dict["uid"] = uid
        if guid is not UNSET:
            field_dict["guid"] = guid
        if date is not UNSET:
            field_dict["date"] = date
        if time_valid is not UNSET:
            field_dict["timeValid"] = time_valid
        if recent is not UNSET:
            field_dict["recent"] = recent
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if links is not UNSET:
            field_dict["links"] = links
        if gamecast_available is not UNSET:
            field_dict["gamecastAvailable"] = gamecast_available
        if play_by_play_available is not UNSET:
            field_dict["playByPlayAvailable"] = play_by_play_available
        if commentary_available is not UNSET:
            field_dict["commentaryAvailable"] = commentary_available
        if wallclock_available is not UNSET:
            field_dict["wallclockAvailable"] = wallclock_available
        if on_watch is not UNSET:
            field_dict["onWatch"] = on_watch
        if competition_id is not UNSET:
            field_dict["competitionId"] = competition_id
        if location is not UNSET:
            field_dict["location"] = location
        if season is not UNSET:
            field_dict["season"] = season
        if season_start_date is not UNSET:
            field_dict["seasonStartDate"] = season_start_date
        if season_end_date is not UNSET:
            field_dict["seasonEndDate"] = season_end_date
        if season_type is not UNSET:
            field_dict["seasonType"] = season_type
        if season_type_has_groups is not UNSET:
            field_dict["seasonTypeHasGroups"] = season_type_has_groups
        if group is not UNSET:
            field_dict["group"] = group
        if week is not UNSET:
            field_dict["week"] = week
        if week_text is not UNSET:
            field_dict["weekText"] = week_text
        if link is not UNSET:
            field_dict["link"] = link
        if status is not UNSET:
            field_dict["status"] = status
        if summary is not UNSET:
            field_dict["summary"] = summary
        if period is not UNSET:
            field_dict["period"] = period
        if clock is not UNSET:
            field_dict["clock"] = clock
        if broadcasts is not UNSET:
            field_dict["broadcasts"] = broadcasts
        if broadcast is not UNSET:
            field_dict["broadcast"] = broadcast
        if odds is not UNSET:
            field_dict["odds"] = odds
        if full_status is not UNSET:
            field_dict["fullStatus"] = full_status
        if competitors is not UNSET:
            field_dict["competitors"] = competitors
        if neutral_site is not UNSET:
            field_dict["neutralSite"] = neutral_site
        if app_links is not UNSET:
            field_dict["appLinks"] = app_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_header_response_sports_item_leagues_item_events_item_app_links_item import (
            ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemAppLinksItem,
        )
        from ..models.scoreboard_header_response_sports_item_leagues_item_events_item_broadcasts_item import (
            ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemBroadcastsItem,
        )
        from ..models.scoreboard_header_response_sports_item_leagues_item_events_item_competitors_item import (
            ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemCompetitorsItem,
        )
        from ..models.scoreboard_header_response_sports_item_leagues_item_events_item_full_status import (
            ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemFullStatus,
        )
        from ..models.scoreboard_header_response_sports_item_leagues_item_events_item_group import (
            ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemGroup,
        )
        from ..models.scoreboard_header_response_sports_item_leagues_item_events_item_links_item import (
            ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemLinksItem,
        )
        from ..models.scoreboard_header_response_sports_item_leagues_item_events_item_odds import (
            ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemOdds,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        uid = d.pop("uid", UNSET)

        guid = d.pop("guid", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        time_valid = d.pop("timeValid", UNSET)

        recent = d.pop("recent", UNSET)

        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemLinksItem.from_dict(links_item_data)

            links.append(links_item)

        gamecast_available = d.pop("gamecastAvailable", UNSET)

        play_by_play_available = d.pop("playByPlayAvailable", UNSET)

        commentary_available = d.pop("commentaryAvailable", UNSET)

        wallclock_available = d.pop("wallclockAvailable", UNSET)

        on_watch = d.pop("onWatch", UNSET)

        competition_id = d.pop("competitionId", UNSET)

        location = d.pop("location", UNSET)

        season = d.pop("season", UNSET)

        season_start_date = d.pop("seasonStartDate", UNSET)

        season_end_date = d.pop("seasonEndDate", UNSET)

        season_type = d.pop("seasonType", UNSET)

        season_type_has_groups = d.pop("seasonTypeHasGroups", UNSET)

        _group = d.pop("group", UNSET)
        group: Union[Unset, ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemGroup.from_dict(_group)

        week = d.pop("week", UNSET)

        week_text = d.pop("weekText", UNSET)

        link = d.pop("link", UNSET)

        status = d.pop("status", UNSET)

        summary = d.pop("summary", UNSET)

        period = d.pop("period", UNSET)

        clock = d.pop("clock", UNSET)

        broadcasts = []
        _broadcasts = d.pop("broadcasts", UNSET)
        for broadcasts_item_data in _broadcasts or []:
            broadcasts_item = ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemBroadcastsItem.from_dict(
                broadcasts_item_data
            )

            broadcasts.append(broadcasts_item)

        broadcast = d.pop("broadcast", UNSET)

        _odds = d.pop("odds", UNSET)
        odds: Union[Unset, ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemOdds]
        if isinstance(_odds, Unset):
            odds = UNSET
        else:
            odds = ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemOdds.from_dict(_odds)

        _full_status = d.pop("fullStatus", UNSET)
        full_status: Union[Unset, ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemFullStatus]
        if isinstance(_full_status, Unset):
            full_status = UNSET
        else:
            full_status = ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemFullStatus.from_dict(_full_status)

        competitors = []
        _competitors = d.pop("competitors", UNSET)
        for competitors_item_data in _competitors or []:
            competitors_item = ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemCompetitorsItem.from_dict(
                competitors_item_data
            )

            competitors.append(competitors_item)

        neutral_site = d.pop("neutralSite", UNSET)

        app_links = []
        _app_links = d.pop("appLinks", UNSET)
        for app_links_item_data in _app_links or []:
            app_links_item = ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemAppLinksItem.from_dict(
                app_links_item_data
            )

            app_links.append(app_links_item)

        scoreboard_header_response_sports_item_leagues_item_events_item = cls(
            id=id,
            uid=uid,
            guid=guid,
            date=date,
            time_valid=time_valid,
            recent=recent,
            name=name,
            short_name=short_name,
            links=links,
            gamecast_available=gamecast_available,
            play_by_play_available=play_by_play_available,
            commentary_available=commentary_available,
            wallclock_available=wallclock_available,
            on_watch=on_watch,
            competition_id=competition_id,
            location=location,
            season=season,
            season_start_date=season_start_date,
            season_end_date=season_end_date,
            season_type=season_type,
            season_type_has_groups=season_type_has_groups,
            group=group,
            week=week,
            week_text=week_text,
            link=link,
            status=status,
            summary=summary,
            period=period,
            clock=clock,
            broadcasts=broadcasts,
            broadcast=broadcast,
            odds=odds,
            full_status=full_status,
            competitors=competitors,
            neutral_site=neutral_site,
            app_links=app_links,
        )

        scoreboard_header_response_sports_item_leagues_item_events_item.additional_properties = d
        return scoreboard_header_response_sports_item_leagues_item_events_item

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
