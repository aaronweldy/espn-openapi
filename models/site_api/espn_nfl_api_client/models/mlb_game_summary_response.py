from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mlb_against_the_spread import MlbAgainstTheSpread
    from ..models.mlb_article import MlbArticle
    from ..models.mlb_boxscore import MlbBoxscore
    from ..models.mlb_broadcast import MlbBroadcast
    from ..models.mlb_format import MlbFormat
    from ..models.mlb_game_info import MlbGameInfo
    from ..models.mlb_game_summary_response_at_bats import MlbGameSummaryResponseAtBats
    from ..models.mlb_game_summary_response_plays_map import MlbGameSummaryResponsePlaysMap
    from ..models.mlb_header import MlbHeader
    from ..models.mlb_injury import MlbInjury
    from ..models.mlb_meta import MlbMeta
    from ..models.mlb_news import MlbNews
    from ..models.mlb_pickcenter import MlbPickcenter
    from ..models.mlb_play import MlbPlay
    from ..models.mlb_roster import MlbRoster
    from ..models.mlb_season_series import MlbSeasonSeries
    from ..models.mlb_standings import MlbStandings
    from ..models.mlb_win_probability import MlbWinProbability


T = TypeVar("T", bound="MlbGameSummaryResponse")


@_attrs_define
class MlbGameSummaryResponse:
    """MLB game summary response.

    Attributes:
        notes (List[Any]):
        boxscore (MlbBoxscore): MLB boxscore object. (To be filled in.)
        format_ (MlbFormat): MLB format object. (To be filled in.)
        game_info (MlbGameInfo): MLB game info object. (To be filled in.)
        seasonseries (List['MlbSeasonSeries']):
        injuries (List['MlbInjury']):
        broadcasts (List['MlbBroadcast']):
        pickcenter (List['MlbPickcenter']):
        against_the_spread (List['MlbAgainstTheSpread']):
        odds (List[Any]):
        rosters (List['MlbRoster']):
        header (MlbHeader): MLB header object. (To be filled in.)
        news (MlbNews): MLB news object. (To be filled in.)
        article (MlbArticle): MLB article object. (To be filled in.)
        videos (List[Any]):
        winprobability (List['MlbWinProbability']):
        plays (List['MlbPlay']):
        plays_map (MlbGameSummaryResponsePlaysMap):
        at_bats (MlbGameSummaryResponseAtBats):
        wallclock_available (bool):
        meta (MlbMeta): MLB meta object. (To be filled in.)
        standings (MlbStandings): MLB standings object. (To be filled in.)
    """

    notes: List[Any]
    boxscore: "MlbBoxscore"
    format_: "MlbFormat"
    game_info: "MlbGameInfo"
    seasonseries: List["MlbSeasonSeries"]
    injuries: List["MlbInjury"]
    broadcasts: List["MlbBroadcast"]
    pickcenter: List["MlbPickcenter"]
    against_the_spread: List["MlbAgainstTheSpread"]
    odds: List[Any]
    rosters: List["MlbRoster"]
    header: "MlbHeader"
    news: "MlbNews"
    article: "MlbArticle"
    videos: List[Any]
    winprobability: List["MlbWinProbability"]
    plays: List["MlbPlay"]
    plays_map: "MlbGameSummaryResponsePlaysMap"
    at_bats: "MlbGameSummaryResponseAtBats"
    wallclock_available: bool
    meta: "MlbMeta"
    standings: "MlbStandings"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        notes = self.notes

        boxscore = self.boxscore.to_dict()

        format_ = self.format_.to_dict()

        game_info = self.game_info.to_dict()

        seasonseries = []
        for seasonseries_item_data in self.seasonseries:
            seasonseries_item = seasonseries_item_data.to_dict()
            seasonseries.append(seasonseries_item)

        injuries = []
        for injuries_item_data in self.injuries:
            injuries_item = injuries_item_data.to_dict()
            injuries.append(injuries_item)

        broadcasts = []
        for broadcasts_item_data in self.broadcasts:
            broadcasts_item = broadcasts_item_data.to_dict()
            broadcasts.append(broadcasts_item)

        pickcenter = []
        for pickcenter_item_data in self.pickcenter:
            pickcenter_item = pickcenter_item_data.to_dict()
            pickcenter.append(pickcenter_item)

        against_the_spread = []
        for against_the_spread_item_data in self.against_the_spread:
            against_the_spread_item = against_the_spread_item_data.to_dict()
            against_the_spread.append(against_the_spread_item)

        odds = self.odds

        rosters = []
        for rosters_item_data in self.rosters:
            rosters_item = rosters_item_data.to_dict()
            rosters.append(rosters_item)

        header = self.header.to_dict()

        news = self.news.to_dict()

        article = self.article.to_dict()

        videos = self.videos

        winprobability = []
        for winprobability_item_data in self.winprobability:
            winprobability_item = winprobability_item_data.to_dict()
            winprobability.append(winprobability_item)

        plays = []
        for plays_item_data in self.plays:
            plays_item = plays_item_data.to_dict()
            plays.append(plays_item)

        plays_map = self.plays_map.to_dict()

        at_bats = self.at_bats.to_dict()

        wallclock_available = self.wallclock_available

        meta = self.meta.to_dict()

        standings = self.standings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notes": notes,
                "boxscore": boxscore,
                "format": format_,
                "gameInfo": game_info,
                "seasonseries": seasonseries,
                "injuries": injuries,
                "broadcasts": broadcasts,
                "pickcenter": pickcenter,
                "againstTheSpread": against_the_spread,
                "odds": odds,
                "rosters": rosters,
                "header": header,
                "news": news,
                "article": article,
                "videos": videos,
                "winprobability": winprobability,
                "plays": plays,
                "playsMap": plays_map,
                "atBats": at_bats,
                "wallclockAvailable": wallclock_available,
                "meta": meta,
                "standings": standings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.mlb_against_the_spread import MlbAgainstTheSpread
        from ..models.mlb_article import MlbArticle
        from ..models.mlb_boxscore import MlbBoxscore
        from ..models.mlb_broadcast import MlbBroadcast
        from ..models.mlb_format import MlbFormat
        from ..models.mlb_game_info import MlbGameInfo
        from ..models.mlb_game_summary_response_at_bats import MlbGameSummaryResponseAtBats
        from ..models.mlb_game_summary_response_plays_map import MlbGameSummaryResponsePlaysMap
        from ..models.mlb_header import MlbHeader
        from ..models.mlb_injury import MlbInjury
        from ..models.mlb_meta import MlbMeta
        from ..models.mlb_news import MlbNews
        from ..models.mlb_pickcenter import MlbPickcenter
        from ..models.mlb_play import MlbPlay
        from ..models.mlb_roster import MlbRoster
        from ..models.mlb_season_series import MlbSeasonSeries
        from ..models.mlb_standings import MlbStandings
        from ..models.mlb_win_probability import MlbWinProbability

        d = src_dict.copy()
        notes = cast(List[Any], d.pop("notes"))

        boxscore = MlbBoxscore.from_dict(d.pop("boxscore"))

        format_ = MlbFormat.from_dict(d.pop("format"))

        game_info = MlbGameInfo.from_dict(d.pop("gameInfo"))

        seasonseries = []
        _seasonseries = d.pop("seasonseries")
        for seasonseries_item_data in _seasonseries:
            seasonseries_item = MlbSeasonSeries.from_dict(seasonseries_item_data)

            seasonseries.append(seasonseries_item)

        injuries = []
        _injuries = d.pop("injuries")
        for injuries_item_data in _injuries:
            injuries_item = MlbInjury.from_dict(injuries_item_data)

            injuries.append(injuries_item)

        broadcasts = []
        _broadcasts = d.pop("broadcasts")
        for broadcasts_item_data in _broadcasts:
            broadcasts_item = MlbBroadcast.from_dict(broadcasts_item_data)

            broadcasts.append(broadcasts_item)

        pickcenter = []
        _pickcenter = d.pop("pickcenter")
        for pickcenter_item_data in _pickcenter:
            pickcenter_item = MlbPickcenter.from_dict(pickcenter_item_data)

            pickcenter.append(pickcenter_item)

        against_the_spread = []
        _against_the_spread = d.pop("againstTheSpread")
        for against_the_spread_item_data in _against_the_spread:
            against_the_spread_item = MlbAgainstTheSpread.from_dict(against_the_spread_item_data)

            against_the_spread.append(against_the_spread_item)

        odds = cast(List[Any], d.pop("odds"))

        rosters = []
        _rosters = d.pop("rosters")
        for rosters_item_data in _rosters:
            rosters_item = MlbRoster.from_dict(rosters_item_data)

            rosters.append(rosters_item)

        header = MlbHeader.from_dict(d.pop("header"))

        news = MlbNews.from_dict(d.pop("news"))

        article = MlbArticle.from_dict(d.pop("article"))

        videos = cast(List[Any], d.pop("videos"))

        winprobability = []
        _winprobability = d.pop("winprobability")
        for winprobability_item_data in _winprobability:
            winprobability_item = MlbWinProbability.from_dict(winprobability_item_data)

            winprobability.append(winprobability_item)

        plays = []
        _plays = d.pop("plays")
        for plays_item_data in _plays:
            plays_item = MlbPlay.from_dict(plays_item_data)

            plays.append(plays_item)

        plays_map = MlbGameSummaryResponsePlaysMap.from_dict(d.pop("playsMap"))

        at_bats = MlbGameSummaryResponseAtBats.from_dict(d.pop("atBats"))

        wallclock_available = d.pop("wallclockAvailable")

        meta = MlbMeta.from_dict(d.pop("meta"))

        standings = MlbStandings.from_dict(d.pop("standings"))

        mlb_game_summary_response = cls(
            notes=notes,
            boxscore=boxscore,
            format_=format_,
            game_info=game_info,
            seasonseries=seasonseries,
            injuries=injuries,
            broadcasts=broadcasts,
            pickcenter=pickcenter,
            against_the_spread=against_the_spread,
            odds=odds,
            rosters=rosters,
            header=header,
            news=news,
            article=article,
            videos=videos,
            winprobability=winprobability,
            plays=plays,
            plays_map=plays_map,
            at_bats=at_bats,
            wallclock_available=wallclock_available,
            meta=meta,
            standings=standings,
        )

        mlb_game_summary_response.additional_properties = d
        return mlb_game_summary_response

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
