from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nba_game_summary_response_against_the_spread_item import NbaGameSummaryResponseAgainstTheSpreadItem
    from ..models.nba_game_summary_response_article import NbaGameSummaryResponseArticle
    from ..models.nba_game_summary_response_boxscore import NbaGameSummaryResponseBoxscore
    from ..models.nba_game_summary_response_broadcasts_item import NbaGameSummaryResponseBroadcastsItem
    from ..models.nba_game_summary_response_format import NbaGameSummaryResponseFormat
    from ..models.nba_game_summary_response_game_info import NbaGameSummaryResponseGameInfo
    from ..models.nba_game_summary_response_header import NbaGameSummaryResponseHeader
    from ..models.nba_game_summary_response_injuries_item import NbaGameSummaryResponseInjuriesItem
    from ..models.nba_game_summary_response_last_five_games_item import NbaGameSummaryResponseLastFiveGamesItem
    from ..models.nba_game_summary_response_leaders_item import NbaGameSummaryResponseLeadersItem
    from ..models.nba_game_summary_response_news import NbaGameSummaryResponseNews
    from ..models.nba_game_summary_response_odds_item import NbaGameSummaryResponseOddsItem
    from ..models.nba_game_summary_response_pickcenter_item import NbaGameSummaryResponsePickcenterItem
    from ..models.nba_game_summary_response_predictor import NbaGameSummaryResponsePredictor
    from ..models.nba_game_summary_response_seasonseries import NbaGameSummaryResponseSeasonseries
    from ..models.nba_game_summary_response_standings import NbaGameSummaryResponseStandings
    from ..models.nba_game_summary_response_tickets_info import NbaGameSummaryResponseTicketsInfo
    from ..models.nba_game_summary_response_videos_item import NbaGameSummaryResponseVideosItem
    from ..models.nba_game_summary_response_win_probability_item import NbaGameSummaryResponseWinProbabilityItem


T = TypeVar("T", bound="NbaGameSummaryResponse")


@_attrs_define
class NbaGameSummaryResponse:
    """NBA game summary response with comprehensive game data

    Attributes:
        boxscore (NbaGameSummaryResponseBoxscore): Game boxscore data with team and player statistics
        game_info (NbaGameSummaryResponseGameInfo): Game information including venue, attendance, and officials
        header (NbaGameSummaryResponseHeader): Game header information with scores and game status
        against_the_spread (Union[Unset, List['NbaGameSummaryResponseAgainstTheSpreadItem']]): Against the spread
            records for teams
        article (Union[Unset, NbaGameSummaryResponseArticle]): Related article content
        broadcasts (Union[Unset, List['NbaGameSummaryResponseBroadcastsItem']]): Broadcast information
        format_ (Union[Unset, NbaGameSummaryResponseFormat]): Game format details
        injuries (Union[Unset, List['NbaGameSummaryResponseInjuriesItem']]): Injury report for both teams
        last_five_games (Union[Unset, List['NbaGameSummaryResponseLastFiveGamesItem']]): Last five games performance for
            both teams
        leaders (Union[Unset, List['NbaGameSummaryResponseLeadersItem']]): Statistical leaders for the game
        news (Union[Unset, NbaGameSummaryResponseNews]): Related news articles
        odds (Union[Unset, List['NbaGameSummaryResponseOddsItem']]): Betting odds information
        pickcenter (Union[Unset, List['NbaGameSummaryResponsePickcenterItem']]): Pick center predictions
        predictor (Union[Unset, NbaGameSummaryResponsePredictor]): Game predictor information
        seasonseries (Union[Unset, NbaGameSummaryResponseSeasonseries]): Season series information between teams
        standings (Union[Unset, NbaGameSummaryResponseStandings]): Current standings information
        tickets_info (Union[Unset, NbaGameSummaryResponseTicketsInfo]): Ticket availability information
        videos (Union[Unset, List['NbaGameSummaryResponseVideosItem']]): Related video content
        win_probability (Union[Unset, List['NbaGameSummaryResponseWinProbabilityItem']]): Win probability throughout the
            game
    """

    boxscore: "NbaGameSummaryResponseBoxscore"
    game_info: "NbaGameSummaryResponseGameInfo"
    header: "NbaGameSummaryResponseHeader"
    against_the_spread: Union[Unset, List["NbaGameSummaryResponseAgainstTheSpreadItem"]] = UNSET
    article: Union[Unset, "NbaGameSummaryResponseArticle"] = UNSET
    broadcasts: Union[Unset, List["NbaGameSummaryResponseBroadcastsItem"]] = UNSET
    format_: Union[Unset, "NbaGameSummaryResponseFormat"] = UNSET
    injuries: Union[Unset, List["NbaGameSummaryResponseInjuriesItem"]] = UNSET
    last_five_games: Union[Unset, List["NbaGameSummaryResponseLastFiveGamesItem"]] = UNSET
    leaders: Union[Unset, List["NbaGameSummaryResponseLeadersItem"]] = UNSET
    news: Union[Unset, "NbaGameSummaryResponseNews"] = UNSET
    odds: Union[Unset, List["NbaGameSummaryResponseOddsItem"]] = UNSET
    pickcenter: Union[Unset, List["NbaGameSummaryResponsePickcenterItem"]] = UNSET
    predictor: Union[Unset, "NbaGameSummaryResponsePredictor"] = UNSET
    seasonseries: Union[Unset, "NbaGameSummaryResponseSeasonseries"] = UNSET
    standings: Union[Unset, "NbaGameSummaryResponseStandings"] = UNSET
    tickets_info: Union[Unset, "NbaGameSummaryResponseTicketsInfo"] = UNSET
    videos: Union[Unset, List["NbaGameSummaryResponseVideosItem"]] = UNSET
    win_probability: Union[Unset, List["NbaGameSummaryResponseWinProbabilityItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        boxscore = self.boxscore.to_dict()

        game_info = self.game_info.to_dict()

        header = self.header.to_dict()

        against_the_spread: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.against_the_spread, Unset):
            against_the_spread = []
            for against_the_spread_item_data in self.against_the_spread:
                against_the_spread_item = against_the_spread_item_data.to_dict()
                against_the_spread.append(against_the_spread_item)

        article: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.article, Unset):
            article = self.article.to_dict()

        broadcasts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.broadcasts, Unset):
            broadcasts = []
            for broadcasts_item_data in self.broadcasts:
                broadcasts_item = broadcasts_item_data.to_dict()
                broadcasts.append(broadcasts_item)

        format_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.to_dict()

        injuries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.injuries, Unset):
            injuries = []
            for injuries_item_data in self.injuries:
                injuries_item = injuries_item_data.to_dict()
                injuries.append(injuries_item)

        last_five_games: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.last_five_games, Unset):
            last_five_games = []
            for last_five_games_item_data in self.last_five_games:
                last_five_games_item = last_five_games_item_data.to_dict()
                last_five_games.append(last_five_games_item)

        leaders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.leaders, Unset):
            leaders = []
            for leaders_item_data in self.leaders:
                leaders_item = leaders_item_data.to_dict()
                leaders.append(leaders_item)

        news: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.news, Unset):
            news = self.news.to_dict()

        odds: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.odds, Unset):
            odds = []
            for odds_item_data in self.odds:
                odds_item = odds_item_data.to_dict()
                odds.append(odds_item)

        pickcenter: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pickcenter, Unset):
            pickcenter = []
            for pickcenter_item_data in self.pickcenter:
                pickcenter_item = pickcenter_item_data.to_dict()
                pickcenter.append(pickcenter_item)

        predictor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.predictor, Unset):
            predictor = self.predictor.to_dict()

        seasonseries: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.seasonseries, Unset):
            seasonseries = self.seasonseries.to_dict()

        standings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standings, Unset):
            standings = self.standings.to_dict()

        tickets_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tickets_info, Unset):
            tickets_info = self.tickets_info.to_dict()

        videos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.videos, Unset):
            videos = []
            for videos_item_data in self.videos:
                videos_item = videos_item_data.to_dict()
                videos.append(videos_item)

        win_probability: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.win_probability, Unset):
            win_probability = []
            for win_probability_item_data in self.win_probability:
                win_probability_item = win_probability_item_data.to_dict()
                win_probability.append(win_probability_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "boxscore": boxscore,
                "gameInfo": game_info,
                "header": header,
            }
        )
        if against_the_spread is not UNSET:
            field_dict["againstTheSpread"] = against_the_spread
        if article is not UNSET:
            field_dict["article"] = article
        if broadcasts is not UNSET:
            field_dict["broadcasts"] = broadcasts
        if format_ is not UNSET:
            field_dict["format"] = format_
        if injuries is not UNSET:
            field_dict["injuries"] = injuries
        if last_five_games is not UNSET:
            field_dict["lastFiveGames"] = last_five_games
        if leaders is not UNSET:
            field_dict["leaders"] = leaders
        if news is not UNSET:
            field_dict["news"] = news
        if odds is not UNSET:
            field_dict["odds"] = odds
        if pickcenter is not UNSET:
            field_dict["pickcenter"] = pickcenter
        if predictor is not UNSET:
            field_dict["predictor"] = predictor
        if seasonseries is not UNSET:
            field_dict["seasonseries"] = seasonseries
        if standings is not UNSET:
            field_dict["standings"] = standings
        if tickets_info is not UNSET:
            field_dict["ticketsInfo"] = tickets_info
        if videos is not UNSET:
            field_dict["videos"] = videos
        if win_probability is not UNSET:
            field_dict["winProbability"] = win_probability

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nba_game_summary_response_against_the_spread_item import (
            NbaGameSummaryResponseAgainstTheSpreadItem,
        )
        from ..models.nba_game_summary_response_article import NbaGameSummaryResponseArticle
        from ..models.nba_game_summary_response_boxscore import NbaGameSummaryResponseBoxscore
        from ..models.nba_game_summary_response_broadcasts_item import NbaGameSummaryResponseBroadcastsItem
        from ..models.nba_game_summary_response_format import NbaGameSummaryResponseFormat
        from ..models.nba_game_summary_response_game_info import NbaGameSummaryResponseGameInfo
        from ..models.nba_game_summary_response_header import NbaGameSummaryResponseHeader
        from ..models.nba_game_summary_response_injuries_item import NbaGameSummaryResponseInjuriesItem
        from ..models.nba_game_summary_response_last_five_games_item import NbaGameSummaryResponseLastFiveGamesItem
        from ..models.nba_game_summary_response_leaders_item import NbaGameSummaryResponseLeadersItem
        from ..models.nba_game_summary_response_news import NbaGameSummaryResponseNews
        from ..models.nba_game_summary_response_odds_item import NbaGameSummaryResponseOddsItem
        from ..models.nba_game_summary_response_pickcenter_item import NbaGameSummaryResponsePickcenterItem
        from ..models.nba_game_summary_response_predictor import NbaGameSummaryResponsePredictor
        from ..models.nba_game_summary_response_seasonseries import NbaGameSummaryResponseSeasonseries
        from ..models.nba_game_summary_response_standings import NbaGameSummaryResponseStandings
        from ..models.nba_game_summary_response_tickets_info import NbaGameSummaryResponseTicketsInfo
        from ..models.nba_game_summary_response_videos_item import NbaGameSummaryResponseVideosItem
        from ..models.nba_game_summary_response_win_probability_item import NbaGameSummaryResponseWinProbabilityItem

        d = src_dict.copy()
        boxscore = NbaGameSummaryResponseBoxscore.from_dict(d.pop("boxscore"))

        game_info = NbaGameSummaryResponseGameInfo.from_dict(d.pop("gameInfo"))

        header = NbaGameSummaryResponseHeader.from_dict(d.pop("header"))

        against_the_spread = []
        _against_the_spread = d.pop("againstTheSpread", UNSET)
        for against_the_spread_item_data in _against_the_spread or []:
            against_the_spread_item = NbaGameSummaryResponseAgainstTheSpreadItem.from_dict(against_the_spread_item_data)

            against_the_spread.append(against_the_spread_item)

        _article = d.pop("article", UNSET)
        article: Union[Unset, NbaGameSummaryResponseArticle]
        if isinstance(_article, Unset):
            article = UNSET
        else:
            article = NbaGameSummaryResponseArticle.from_dict(_article)

        broadcasts = []
        _broadcasts = d.pop("broadcasts", UNSET)
        for broadcasts_item_data in _broadcasts or []:
            broadcasts_item = NbaGameSummaryResponseBroadcastsItem.from_dict(broadcasts_item_data)

            broadcasts.append(broadcasts_item)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, NbaGameSummaryResponseFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = NbaGameSummaryResponseFormat.from_dict(_format_)

        injuries = []
        _injuries = d.pop("injuries", UNSET)
        for injuries_item_data in _injuries or []:
            injuries_item = NbaGameSummaryResponseInjuriesItem.from_dict(injuries_item_data)

            injuries.append(injuries_item)

        last_five_games = []
        _last_five_games = d.pop("lastFiveGames", UNSET)
        for last_five_games_item_data in _last_five_games or []:
            last_five_games_item = NbaGameSummaryResponseLastFiveGamesItem.from_dict(last_five_games_item_data)

            last_five_games.append(last_five_games_item)

        leaders = []
        _leaders = d.pop("leaders", UNSET)
        for leaders_item_data in _leaders or []:
            leaders_item = NbaGameSummaryResponseLeadersItem.from_dict(leaders_item_data)

            leaders.append(leaders_item)

        _news = d.pop("news", UNSET)
        news: Union[Unset, NbaGameSummaryResponseNews]
        if isinstance(_news, Unset):
            news = UNSET
        else:
            news = NbaGameSummaryResponseNews.from_dict(_news)

        odds = []
        _odds = d.pop("odds", UNSET)
        for odds_item_data in _odds or []:
            odds_item = NbaGameSummaryResponseOddsItem.from_dict(odds_item_data)

            odds.append(odds_item)

        pickcenter = []
        _pickcenter = d.pop("pickcenter", UNSET)
        for pickcenter_item_data in _pickcenter or []:
            pickcenter_item = NbaGameSummaryResponsePickcenterItem.from_dict(pickcenter_item_data)

            pickcenter.append(pickcenter_item)

        _predictor = d.pop("predictor", UNSET)
        predictor: Union[Unset, NbaGameSummaryResponsePredictor]
        if isinstance(_predictor, Unset):
            predictor = UNSET
        else:
            predictor = NbaGameSummaryResponsePredictor.from_dict(_predictor)

        _seasonseries = d.pop("seasonseries", UNSET)
        seasonseries: Union[Unset, NbaGameSummaryResponseSeasonseries]
        if isinstance(_seasonseries, Unset):
            seasonseries = UNSET
        else:
            seasonseries = NbaGameSummaryResponseSeasonseries.from_dict(_seasonseries)

        _standings = d.pop("standings", UNSET)
        standings: Union[Unset, NbaGameSummaryResponseStandings]
        if isinstance(_standings, Unset):
            standings = UNSET
        else:
            standings = NbaGameSummaryResponseStandings.from_dict(_standings)

        _tickets_info = d.pop("ticketsInfo", UNSET)
        tickets_info: Union[Unset, NbaGameSummaryResponseTicketsInfo]
        if isinstance(_tickets_info, Unset):
            tickets_info = UNSET
        else:
            tickets_info = NbaGameSummaryResponseTicketsInfo.from_dict(_tickets_info)

        videos = []
        _videos = d.pop("videos", UNSET)
        for videos_item_data in _videos or []:
            videos_item = NbaGameSummaryResponseVideosItem.from_dict(videos_item_data)

            videos.append(videos_item)

        win_probability = []
        _win_probability = d.pop("winProbability", UNSET)
        for win_probability_item_data in _win_probability or []:
            win_probability_item = NbaGameSummaryResponseWinProbabilityItem.from_dict(win_probability_item_data)

            win_probability.append(win_probability_item)

        nba_game_summary_response = cls(
            boxscore=boxscore,
            game_info=game_info,
            header=header,
            against_the_spread=against_the_spread,
            article=article,
            broadcasts=broadcasts,
            format_=format_,
            injuries=injuries,
            last_five_games=last_five_games,
            leaders=leaders,
            news=news,
            odds=odds,
            pickcenter=pickcenter,
            predictor=predictor,
            seasonseries=seasonseries,
            standings=standings,
            tickets_info=tickets_info,
            videos=videos,
            win_probability=win_probability,
        )

        nba_game_summary_response.additional_properties = d
        return nba_game_summary_response

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
