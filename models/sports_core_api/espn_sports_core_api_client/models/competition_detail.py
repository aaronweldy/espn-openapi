from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.competition_broadcast import CompetitionBroadcast
    from ..models.competition_competitor import CompetitionCompetitor
    from ..models.competition_detail_notes_item import CompetitionDetailNotesItem
    from ..models.competition_format import CompetitionFormat
    from ..models.competition_source import CompetitionSource
    from ..models.competition_type import CompetitionType
    from ..models.link import Link
    from ..models.reference import Reference
    from ..models.venue import Venue


T = TypeVar("T", bound="CompetitionDetail")


@_attrs_define
class CompetitionDetail:
    """
    Attributes:
        ref (str):
        id (str):
        date (str):
        type (CompetitionType):
        venue (Union['Reference', 'Venue']):
        competitors (List[Union['CompetitionCompetitor', 'Reference']]):
        status (Union['CompetitionBroadcast', 'Reference']):
        links (List['Link']):
        guid (Union[Unset, str]):
        uid (Union[Unset, str]):
        attendance (Union[Unset, int]):
        time_valid (Union[Unset, bool]):
        date_valid (Union[Unset, bool]):
        neutral_site (Union[Unset, bool]):
        division_competition (Union[Unset, bool]):
        conference_competition (Union[Unset, bool]):
        preview_available (Union[Unset, bool]):
        recap_available (Union[Unset, bool]):
        boxscore_available (Union[Unset, bool]):
        lineup_available (Union[Unset, bool]):
        gamecast_available (Union[Unset, bool]):
        play_by_play_available (Union[Unset, bool]):
        conversation_available (Union[Unset, bool]):
        commentary_available (Union[Unset, bool]):
        pickcenter_available (Union[Unset, bool]):
        summary_available (Union[Unset, bool]):
        live_available (Union[Unset, bool]):
        tickets_available (Union[Unset, bool]):
        shot_chart_available (Union[Unset, bool]):
        timeouts_available (Union[Unset, bool]):
        possession_arrow_available (Union[Unset, bool]):
        on_watch_espn (Union[Unset, bool]):
        recent (Union[Unset, bool]):
        bracket_available (Union[Unset, bool]):
        wallclock_available (Union[Unset, bool]):
        highlights_available (Union[Unset, bool]):
        game_source (Union[Unset, CompetitionSource]):
        boxscore_source (Union[Unset, CompetitionSource]):
        play_by_play_source (Union[Unset, CompetitionSource]):
        linescore_source (Union[Unset, CompetitionSource]):
        stats_source (Union[Unset, CompetitionSource]):
        notes (Union[Unset, List['CompetitionDetailNotesItem']]):
        situation (Union['CompetitionBroadcast', 'Reference', Unset]):
        odds (Union['CompetitionBroadcast', 'Reference', Unset]):
        broadcasts (Union['CompetitionBroadcast', 'Reference', Unset]):
        officials (Union['CompetitionBroadcast', 'Reference', Unset]):
        details (Union['CompetitionBroadcast', 'Reference', Unset]):
        leaders (Union['CompetitionBroadcast', 'Reference', Unset]):
        predictor (Union['CompetitionBroadcast', 'Reference', Unset]):
        probabilities (Union['CompetitionBroadcast', 'Reference', Unset]):
        power_indexes (Union['CompetitionBroadcast', 'Reference', Unset]):
        format_ (Union[Unset, CompetitionFormat]):
        drives (Union['CompetitionBroadcast', 'Reference', Unset]):
        has_defensive_stats (Union[Unset, bool]):
    """

    ref: str
    id: str
    date: str
    type: "CompetitionType"
    venue: Union["Reference", "Venue"]
    competitors: List[Union["CompetitionCompetitor", "Reference"]]
    status: Union["CompetitionBroadcast", "Reference"]
    links: List["Link"]
    guid: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    attendance: Union[Unset, int] = UNSET
    time_valid: Union[Unset, bool] = UNSET
    date_valid: Union[Unset, bool] = UNSET
    neutral_site: Union[Unset, bool] = UNSET
    division_competition: Union[Unset, bool] = UNSET
    conference_competition: Union[Unset, bool] = UNSET
    preview_available: Union[Unset, bool] = UNSET
    recap_available: Union[Unset, bool] = UNSET
    boxscore_available: Union[Unset, bool] = UNSET
    lineup_available: Union[Unset, bool] = UNSET
    gamecast_available: Union[Unset, bool] = UNSET
    play_by_play_available: Union[Unset, bool] = UNSET
    conversation_available: Union[Unset, bool] = UNSET
    commentary_available: Union[Unset, bool] = UNSET
    pickcenter_available: Union[Unset, bool] = UNSET
    summary_available: Union[Unset, bool] = UNSET
    live_available: Union[Unset, bool] = UNSET
    tickets_available: Union[Unset, bool] = UNSET
    shot_chart_available: Union[Unset, bool] = UNSET
    timeouts_available: Union[Unset, bool] = UNSET
    possession_arrow_available: Union[Unset, bool] = UNSET
    on_watch_espn: Union[Unset, bool] = UNSET
    recent: Union[Unset, bool] = UNSET
    bracket_available: Union[Unset, bool] = UNSET
    wallclock_available: Union[Unset, bool] = UNSET
    highlights_available: Union[Unset, bool] = UNSET
    game_source: Union[Unset, "CompetitionSource"] = UNSET
    boxscore_source: Union[Unset, "CompetitionSource"] = UNSET
    play_by_play_source: Union[Unset, "CompetitionSource"] = UNSET
    linescore_source: Union[Unset, "CompetitionSource"] = UNSET
    stats_source: Union[Unset, "CompetitionSource"] = UNSET
    notes: Union[Unset, List["CompetitionDetailNotesItem"]] = UNSET
    situation: Union["CompetitionBroadcast", "Reference", Unset] = UNSET
    odds: Union["CompetitionBroadcast", "Reference", Unset] = UNSET
    broadcasts: Union["CompetitionBroadcast", "Reference", Unset] = UNSET
    officials: Union["CompetitionBroadcast", "Reference", Unset] = UNSET
    details: Union["CompetitionBroadcast", "Reference", Unset] = UNSET
    leaders: Union["CompetitionBroadcast", "Reference", Unset] = UNSET
    predictor: Union["CompetitionBroadcast", "Reference", Unset] = UNSET
    probabilities: Union["CompetitionBroadcast", "Reference", Unset] = UNSET
    power_indexes: Union["CompetitionBroadcast", "Reference", Unset] = UNSET
    format_: Union[Unset, "CompetitionFormat"] = UNSET
    drives: Union["CompetitionBroadcast", "Reference", Unset] = UNSET
    has_defensive_stats: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.competition_broadcast import CompetitionBroadcast
        from ..models.competition_competitor import CompetitionCompetitor
        from ..models.venue import Venue

        ref = self.ref

        id = self.id

        date = self.date

        type = self.type.to_dict()

        venue: Dict[str, Any]
        if isinstance(self.venue, Venue):
            venue = self.venue.to_dict()
        else:
            venue = self.venue.to_dict()

        competitors = []
        for competitors_item_data in self.competitors:
            competitors_item: Dict[str, Any]
            if isinstance(competitors_item_data, CompetitionCompetitor):
                competitors_item = competitors_item_data.to_dict()
            else:
                competitors_item = competitors_item_data.to_dict()

            competitors.append(competitors_item)

        status: Dict[str, Any]
        if isinstance(self.status, CompetitionBroadcast):
            status = self.status.to_dict()
        else:
            status = self.status.to_dict()

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        guid = self.guid

        uid = self.uid

        attendance = self.attendance

        time_valid = self.time_valid

        date_valid = self.date_valid

        neutral_site = self.neutral_site

        division_competition = self.division_competition

        conference_competition = self.conference_competition

        preview_available = self.preview_available

        recap_available = self.recap_available

        boxscore_available = self.boxscore_available

        lineup_available = self.lineup_available

        gamecast_available = self.gamecast_available

        play_by_play_available = self.play_by_play_available

        conversation_available = self.conversation_available

        commentary_available = self.commentary_available

        pickcenter_available = self.pickcenter_available

        summary_available = self.summary_available

        live_available = self.live_available

        tickets_available = self.tickets_available

        shot_chart_available = self.shot_chart_available

        timeouts_available = self.timeouts_available

        possession_arrow_available = self.possession_arrow_available

        on_watch_espn = self.on_watch_espn

        recent = self.recent

        bracket_available = self.bracket_available

        wallclock_available = self.wallclock_available

        highlights_available = self.highlights_available

        game_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.game_source, Unset):
            game_source = self.game_source.to_dict()

        boxscore_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.boxscore_source, Unset):
            boxscore_source = self.boxscore_source.to_dict()

        play_by_play_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.play_by_play_source, Unset):
            play_by_play_source = self.play_by_play_source.to_dict()

        linescore_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.linescore_source, Unset):
            linescore_source = self.linescore_source.to_dict()

        stats_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stats_source, Unset):
            stats_source = self.stats_source.to_dict()

        notes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()
                notes.append(notes_item)

        situation: Union[Dict[str, Any], Unset]
        if isinstance(self.situation, Unset):
            situation = UNSET
        elif isinstance(self.situation, CompetitionBroadcast):
            situation = self.situation.to_dict()
        else:
            situation = self.situation.to_dict()

        odds: Union[Dict[str, Any], Unset]
        if isinstance(self.odds, Unset):
            odds = UNSET
        elif isinstance(self.odds, CompetitionBroadcast):
            odds = self.odds.to_dict()
        else:
            odds = self.odds.to_dict()

        broadcasts: Union[Dict[str, Any], Unset]
        if isinstance(self.broadcasts, Unset):
            broadcasts = UNSET
        elif isinstance(self.broadcasts, CompetitionBroadcast):
            broadcasts = self.broadcasts.to_dict()
        else:
            broadcasts = self.broadcasts.to_dict()

        officials: Union[Dict[str, Any], Unset]
        if isinstance(self.officials, Unset):
            officials = UNSET
        elif isinstance(self.officials, CompetitionBroadcast):
            officials = self.officials.to_dict()
        else:
            officials = self.officials.to_dict()

        details: Union[Dict[str, Any], Unset]
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, CompetitionBroadcast):
            details = self.details.to_dict()
        else:
            details = self.details.to_dict()

        leaders: Union[Dict[str, Any], Unset]
        if isinstance(self.leaders, Unset):
            leaders = UNSET
        elif isinstance(self.leaders, CompetitionBroadcast):
            leaders = self.leaders.to_dict()
        else:
            leaders = self.leaders.to_dict()

        predictor: Union[Dict[str, Any], Unset]
        if isinstance(self.predictor, Unset):
            predictor = UNSET
        elif isinstance(self.predictor, CompetitionBroadcast):
            predictor = self.predictor.to_dict()
        else:
            predictor = self.predictor.to_dict()

        probabilities: Union[Dict[str, Any], Unset]
        if isinstance(self.probabilities, Unset):
            probabilities = UNSET
        elif isinstance(self.probabilities, CompetitionBroadcast):
            probabilities = self.probabilities.to_dict()
        else:
            probabilities = self.probabilities.to_dict()

        power_indexes: Union[Dict[str, Any], Unset]
        if isinstance(self.power_indexes, Unset):
            power_indexes = UNSET
        elif isinstance(self.power_indexes, CompetitionBroadcast):
            power_indexes = self.power_indexes.to_dict()
        else:
            power_indexes = self.power_indexes.to_dict()

        format_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.to_dict()

        drives: Union[Dict[str, Any], Unset]
        if isinstance(self.drives, Unset):
            drives = UNSET
        elif isinstance(self.drives, CompetitionBroadcast):
            drives = self.drives.to_dict()
        else:
            drives = self.drives.to_dict()

        has_defensive_stats = self.has_defensive_stats

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "id": id,
                "date": date,
                "type": type,
                "venue": venue,
                "competitors": competitors,
                "status": status,
                "links": links,
            }
        )
        if guid is not UNSET:
            field_dict["guid"] = guid
        if uid is not UNSET:
            field_dict["uid"] = uid
        if attendance is not UNSET:
            field_dict["attendance"] = attendance
        if time_valid is not UNSET:
            field_dict["timeValid"] = time_valid
        if date_valid is not UNSET:
            field_dict["dateValid"] = date_valid
        if neutral_site is not UNSET:
            field_dict["neutralSite"] = neutral_site
        if division_competition is not UNSET:
            field_dict["divisionCompetition"] = division_competition
        if conference_competition is not UNSET:
            field_dict["conferenceCompetition"] = conference_competition
        if preview_available is not UNSET:
            field_dict["previewAvailable"] = preview_available
        if recap_available is not UNSET:
            field_dict["recapAvailable"] = recap_available
        if boxscore_available is not UNSET:
            field_dict["boxscoreAvailable"] = boxscore_available
        if lineup_available is not UNSET:
            field_dict["lineupAvailable"] = lineup_available
        if gamecast_available is not UNSET:
            field_dict["gamecastAvailable"] = gamecast_available
        if play_by_play_available is not UNSET:
            field_dict["playByPlayAvailable"] = play_by_play_available
        if conversation_available is not UNSET:
            field_dict["conversationAvailable"] = conversation_available
        if commentary_available is not UNSET:
            field_dict["commentaryAvailable"] = commentary_available
        if pickcenter_available is not UNSET:
            field_dict["pickcenterAvailable"] = pickcenter_available
        if summary_available is not UNSET:
            field_dict["summaryAvailable"] = summary_available
        if live_available is not UNSET:
            field_dict["liveAvailable"] = live_available
        if tickets_available is not UNSET:
            field_dict["ticketsAvailable"] = tickets_available
        if shot_chart_available is not UNSET:
            field_dict["shotChartAvailable"] = shot_chart_available
        if timeouts_available is not UNSET:
            field_dict["timeoutsAvailable"] = timeouts_available
        if possession_arrow_available is not UNSET:
            field_dict["possessionArrowAvailable"] = possession_arrow_available
        if on_watch_espn is not UNSET:
            field_dict["onWatchESPN"] = on_watch_espn
        if recent is not UNSET:
            field_dict["recent"] = recent
        if bracket_available is not UNSET:
            field_dict["bracketAvailable"] = bracket_available
        if wallclock_available is not UNSET:
            field_dict["wallclockAvailable"] = wallclock_available
        if highlights_available is not UNSET:
            field_dict["highlightsAvailable"] = highlights_available
        if game_source is not UNSET:
            field_dict["gameSource"] = game_source
        if boxscore_source is not UNSET:
            field_dict["boxscoreSource"] = boxscore_source
        if play_by_play_source is not UNSET:
            field_dict["playByPlaySource"] = play_by_play_source
        if linescore_source is not UNSET:
            field_dict["linescoreSource"] = linescore_source
        if stats_source is not UNSET:
            field_dict["statsSource"] = stats_source
        if notes is not UNSET:
            field_dict["notes"] = notes
        if situation is not UNSET:
            field_dict["situation"] = situation
        if odds is not UNSET:
            field_dict["odds"] = odds
        if broadcasts is not UNSET:
            field_dict["broadcasts"] = broadcasts
        if officials is not UNSET:
            field_dict["officials"] = officials
        if details is not UNSET:
            field_dict["details"] = details
        if leaders is not UNSET:
            field_dict["leaders"] = leaders
        if predictor is not UNSET:
            field_dict["predictor"] = predictor
        if probabilities is not UNSET:
            field_dict["probabilities"] = probabilities
        if power_indexes is not UNSET:
            field_dict["powerIndexes"] = power_indexes
        if format_ is not UNSET:
            field_dict["format"] = format_
        if drives is not UNSET:
            field_dict["drives"] = drives
        if has_defensive_stats is not UNSET:
            field_dict["hasDefensiveStats"] = has_defensive_stats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.competition_broadcast import CompetitionBroadcast
        from ..models.competition_competitor import CompetitionCompetitor
        from ..models.competition_detail_notes_item import CompetitionDetailNotesItem
        from ..models.competition_format import CompetitionFormat
        from ..models.competition_source import CompetitionSource
        from ..models.competition_type import CompetitionType
        from ..models.link import Link
        from ..models.reference import Reference
        from ..models.venue import Venue

        d = src_dict.copy()
        ref = d.pop("$ref")

        id = d.pop("id")

        date = d.pop("date")

        type = CompetitionType.from_dict(d.pop("type"))

        def _parse_venue(data: object) -> Union["Reference", "Venue"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                venue_type_0 = Venue.from_dict(data)

                return venue_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            venue_type_1 = Reference.from_dict(data)

            return venue_type_1

        venue = _parse_venue(d.pop("venue"))

        competitors = []
        _competitors = d.pop("competitors")
        for competitors_item_data in _competitors:

            def _parse_competitors_item(data: object) -> Union["CompetitionCompetitor", "Reference"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    competitors_item_type_0 = CompetitionCompetitor.from_dict(data)

                    return competitors_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                competitors_item_type_1 = Reference.from_dict(data)

                return competitors_item_type_1

            competitors_item = _parse_competitors_item(competitors_item_data)

            competitors.append(competitors_item)

        def _parse_status(data: object) -> Union["CompetitionBroadcast", "Reference"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_0 = CompetitionBroadcast.from_dict(data)

                return status_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            status_type_1 = Reference.from_dict(data)

            return status_type_1

        status = _parse_status(d.pop("status"))

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        guid = d.pop("guid", UNSET)

        uid = d.pop("uid", UNSET)

        attendance = d.pop("attendance", UNSET)

        time_valid = d.pop("timeValid", UNSET)

        date_valid = d.pop("dateValid", UNSET)

        neutral_site = d.pop("neutralSite", UNSET)

        division_competition = d.pop("divisionCompetition", UNSET)

        conference_competition = d.pop("conferenceCompetition", UNSET)

        preview_available = d.pop("previewAvailable", UNSET)

        recap_available = d.pop("recapAvailable", UNSET)

        boxscore_available = d.pop("boxscoreAvailable", UNSET)

        lineup_available = d.pop("lineupAvailable", UNSET)

        gamecast_available = d.pop("gamecastAvailable", UNSET)

        play_by_play_available = d.pop("playByPlayAvailable", UNSET)

        conversation_available = d.pop("conversationAvailable", UNSET)

        commentary_available = d.pop("commentaryAvailable", UNSET)

        pickcenter_available = d.pop("pickcenterAvailable", UNSET)

        summary_available = d.pop("summaryAvailable", UNSET)

        live_available = d.pop("liveAvailable", UNSET)

        tickets_available = d.pop("ticketsAvailable", UNSET)

        shot_chart_available = d.pop("shotChartAvailable", UNSET)

        timeouts_available = d.pop("timeoutsAvailable", UNSET)

        possession_arrow_available = d.pop("possessionArrowAvailable", UNSET)

        on_watch_espn = d.pop("onWatchESPN", UNSET)

        recent = d.pop("recent", UNSET)

        bracket_available = d.pop("bracketAvailable", UNSET)

        wallclock_available = d.pop("wallclockAvailable", UNSET)

        highlights_available = d.pop("highlightsAvailable", UNSET)

        _game_source = d.pop("gameSource", UNSET)
        game_source: Union[Unset, CompetitionSource]
        if isinstance(_game_source, Unset):
            game_source = UNSET
        else:
            game_source = CompetitionSource.from_dict(_game_source)

        _boxscore_source = d.pop("boxscoreSource", UNSET)
        boxscore_source: Union[Unset, CompetitionSource]
        if isinstance(_boxscore_source, Unset):
            boxscore_source = UNSET
        else:
            boxscore_source = CompetitionSource.from_dict(_boxscore_source)

        _play_by_play_source = d.pop("playByPlaySource", UNSET)
        play_by_play_source: Union[Unset, CompetitionSource]
        if isinstance(_play_by_play_source, Unset):
            play_by_play_source = UNSET
        else:
            play_by_play_source = CompetitionSource.from_dict(_play_by_play_source)

        _linescore_source = d.pop("linescoreSource", UNSET)
        linescore_source: Union[Unset, CompetitionSource]
        if isinstance(_linescore_source, Unset):
            linescore_source = UNSET
        else:
            linescore_source = CompetitionSource.from_dict(_linescore_source)

        _stats_source = d.pop("statsSource", UNSET)
        stats_source: Union[Unset, CompetitionSource]
        if isinstance(_stats_source, Unset):
            stats_source = UNSET
        else:
            stats_source = CompetitionSource.from_dict(_stats_source)

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = CompetitionDetailNotesItem.from_dict(notes_item_data)

            notes.append(notes_item)

        def _parse_situation(data: object) -> Union["CompetitionBroadcast", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                situation_type_0 = CompetitionBroadcast.from_dict(data)

                return situation_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            situation_type_1 = Reference.from_dict(data)

            return situation_type_1

        situation = _parse_situation(d.pop("situation", UNSET))

        def _parse_odds(data: object) -> Union["CompetitionBroadcast", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                odds_type_0 = CompetitionBroadcast.from_dict(data)

                return odds_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            odds_type_1 = Reference.from_dict(data)

            return odds_type_1

        odds = _parse_odds(d.pop("odds", UNSET))

        def _parse_broadcasts(data: object) -> Union["CompetitionBroadcast", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                broadcasts_type_0 = CompetitionBroadcast.from_dict(data)

                return broadcasts_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            broadcasts_type_1 = Reference.from_dict(data)

            return broadcasts_type_1

        broadcasts = _parse_broadcasts(d.pop("broadcasts", UNSET))

        def _parse_officials(data: object) -> Union["CompetitionBroadcast", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                officials_type_0 = CompetitionBroadcast.from_dict(data)

                return officials_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            officials_type_1 = Reference.from_dict(data)

            return officials_type_1

        officials = _parse_officials(d.pop("officials", UNSET))

        def _parse_details(data: object) -> Union["CompetitionBroadcast", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_0 = CompetitionBroadcast.from_dict(data)

                return details_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            details_type_1 = Reference.from_dict(data)

            return details_type_1

        details = _parse_details(d.pop("details", UNSET))

        def _parse_leaders(data: object) -> Union["CompetitionBroadcast", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                leaders_type_0 = CompetitionBroadcast.from_dict(data)

                return leaders_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            leaders_type_1 = Reference.from_dict(data)

            return leaders_type_1

        leaders = _parse_leaders(d.pop("leaders", UNSET))

        def _parse_predictor(data: object) -> Union["CompetitionBroadcast", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                predictor_type_0 = CompetitionBroadcast.from_dict(data)

                return predictor_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            predictor_type_1 = Reference.from_dict(data)

            return predictor_type_1

        predictor = _parse_predictor(d.pop("predictor", UNSET))

        def _parse_probabilities(data: object) -> Union["CompetitionBroadcast", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                probabilities_type_0 = CompetitionBroadcast.from_dict(data)

                return probabilities_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            probabilities_type_1 = Reference.from_dict(data)

            return probabilities_type_1

        probabilities = _parse_probabilities(d.pop("probabilities", UNSET))

        def _parse_power_indexes(data: object) -> Union["CompetitionBroadcast", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                power_indexes_type_0 = CompetitionBroadcast.from_dict(data)

                return power_indexes_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            power_indexes_type_1 = Reference.from_dict(data)

            return power_indexes_type_1

        power_indexes = _parse_power_indexes(d.pop("powerIndexes", UNSET))

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, CompetitionFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = CompetitionFormat.from_dict(_format_)

        def _parse_drives(data: object) -> Union["CompetitionBroadcast", "Reference", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                drives_type_0 = CompetitionBroadcast.from_dict(data)

                return drives_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            drives_type_1 = Reference.from_dict(data)

            return drives_type_1

        drives = _parse_drives(d.pop("drives", UNSET))

        has_defensive_stats = d.pop("hasDefensiveStats", UNSET)

        competition_detail = cls(
            ref=ref,
            id=id,
            date=date,
            type=type,
            venue=venue,
            competitors=competitors,
            status=status,
            links=links,
            guid=guid,
            uid=uid,
            attendance=attendance,
            time_valid=time_valid,
            date_valid=date_valid,
            neutral_site=neutral_site,
            division_competition=division_competition,
            conference_competition=conference_competition,
            preview_available=preview_available,
            recap_available=recap_available,
            boxscore_available=boxscore_available,
            lineup_available=lineup_available,
            gamecast_available=gamecast_available,
            play_by_play_available=play_by_play_available,
            conversation_available=conversation_available,
            commentary_available=commentary_available,
            pickcenter_available=pickcenter_available,
            summary_available=summary_available,
            live_available=live_available,
            tickets_available=tickets_available,
            shot_chart_available=shot_chart_available,
            timeouts_available=timeouts_available,
            possession_arrow_available=possession_arrow_available,
            on_watch_espn=on_watch_espn,
            recent=recent,
            bracket_available=bracket_available,
            wallclock_available=wallclock_available,
            highlights_available=highlights_available,
            game_source=game_source,
            boxscore_source=boxscore_source,
            play_by_play_source=play_by_play_source,
            linescore_source=linescore_source,
            stats_source=stats_source,
            notes=notes,
            situation=situation,
            odds=odds,
            broadcasts=broadcasts,
            officials=officials,
            details=details,
            leaders=leaders,
            predictor=predictor,
            probabilities=probabilities,
            power_indexes=power_indexes,
            format_=format_,
            drives=drives,
            has_defensive_stats=has_defensive_stats,
        )

        competition_detail.additional_properties = d
        return competition_detail

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
