from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nfl_game_response_gamepackage_json_article import NflGameResponseGamepackageJSONArticle
    from ..models.nfl_game_response_gamepackage_json_boxscore import NflGameResponseGamepackageJSONBoxscore
    from ..models.nfl_game_response_gamepackage_json_broadcasts_item import NflGameResponseGamepackageJSONBroadcastsItem
    from ..models.nfl_game_response_gamepackage_json_drives import NflGameResponseGamepackageJSONDrives
    from ..models.nfl_game_response_gamepackage_json_game_info import NflGameResponseGamepackageJSONGameInfo
    from ..models.nfl_game_response_gamepackage_json_header import NflGameResponseGamepackageJSONHeader
    from ..models.nfl_game_response_gamepackage_json_leaders_item import NflGameResponseGamepackageJSONLeadersItem
    from ..models.nfl_game_response_gamepackage_json_news import NflGameResponseGamepackageJSONNews
    from ..models.nfl_game_response_gamepackage_json_pickcenter_item import NflGameResponseGamepackageJSONPickcenterItem
    from ..models.nfl_game_response_gamepackage_json_scoring_plays_item import (
        NflGameResponseGamepackageJSONScoringPlaysItem,
    )
    from ..models.nfl_game_response_gamepackage_json_standings import NflGameResponseGamepackageJSONStandings
    from ..models.nfl_game_response_gamepackage_json_videos_item import NflGameResponseGamepackageJSONVideosItem
    from ..models.nfl_game_response_gamepackage_json_winprobability_item import (
        NflGameResponseGamepackageJSONWinprobabilityItem,
    )


T = TypeVar("T", bound="NflGameResponseGamepackageJSON")


@_attrs_define
class NflGameResponseGamepackageJSON:
    """Game package data including boxscore, drives, leaders, etc.

    Attributes:
        article (Union[Unset, NflGameResponseGamepackageJSONArticle]):
        boxscore (Union[Unset, NflGameResponseGamepackageJSONBoxscore]):
        broadcasts (Union[Unset, List['NflGameResponseGamepackageJSONBroadcastsItem']]):
        drives (Union[Unset, NflGameResponseGamepackageJSONDrives]):
        game_info (Union[Unset, NflGameResponseGamepackageJSONGameInfo]):
        header (Union[Unset, NflGameResponseGamepackageJSONHeader]):
        leaders (Union[Unset, List['NflGameResponseGamepackageJSONLeadersItem']]):
        news (Union[Unset, NflGameResponseGamepackageJSONNews]):
        pickcenter (Union[Unset, List['NflGameResponseGamepackageJSONPickcenterItem']]):
        scoring_plays (Union[Unset, List['NflGameResponseGamepackageJSONScoringPlaysItem']]):
        standings (Union[Unset, NflGameResponseGamepackageJSONStandings]):
        videos (Union[Unset, List['NflGameResponseGamepackageJSONVideosItem']]):
        winprobability (Union[Unset, List['NflGameResponseGamepackageJSONWinprobabilityItem']]):
    """

    article: Union[Unset, "NflGameResponseGamepackageJSONArticle"] = UNSET
    boxscore: Union[Unset, "NflGameResponseGamepackageJSONBoxscore"] = UNSET
    broadcasts: Union[Unset, List["NflGameResponseGamepackageJSONBroadcastsItem"]] = UNSET
    drives: Union[Unset, "NflGameResponseGamepackageJSONDrives"] = UNSET
    game_info: Union[Unset, "NflGameResponseGamepackageJSONGameInfo"] = UNSET
    header: Union[Unset, "NflGameResponseGamepackageJSONHeader"] = UNSET
    leaders: Union[Unset, List["NflGameResponseGamepackageJSONLeadersItem"]] = UNSET
    news: Union[Unset, "NflGameResponseGamepackageJSONNews"] = UNSET
    pickcenter: Union[Unset, List["NflGameResponseGamepackageJSONPickcenterItem"]] = UNSET
    scoring_plays: Union[Unset, List["NflGameResponseGamepackageJSONScoringPlaysItem"]] = UNSET
    standings: Union[Unset, "NflGameResponseGamepackageJSONStandings"] = UNSET
    videos: Union[Unset, List["NflGameResponseGamepackageJSONVideosItem"]] = UNSET
    winprobability: Union[Unset, List["NflGameResponseGamepackageJSONWinprobabilityItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        article: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.article, Unset):
            article = self.article.to_dict()

        boxscore: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.boxscore, Unset):
            boxscore = self.boxscore.to_dict()

        broadcasts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.broadcasts, Unset):
            broadcasts = []
            for broadcasts_item_data in self.broadcasts:
                broadcasts_item = broadcasts_item_data.to_dict()
                broadcasts.append(broadcasts_item)

        drives: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.drives, Unset):
            drives = self.drives.to_dict()

        game_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.game_info, Unset):
            game_info = self.game_info.to_dict()

        header: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.to_dict()

        leaders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.leaders, Unset):
            leaders = []
            for leaders_item_data in self.leaders:
                leaders_item = leaders_item_data.to_dict()
                leaders.append(leaders_item)

        news: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.news, Unset):
            news = self.news.to_dict()

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

        standings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standings, Unset):
            standings = self.standings.to_dict()

        videos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.videos, Unset):
            videos = []
            for videos_item_data in self.videos:
                videos_item = videos_item_data.to_dict()
                videos.append(videos_item)

        winprobability: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.winprobability, Unset):
            winprobability = []
            for winprobability_item_data in self.winprobability:
                winprobability_item = winprobability_item_data.to_dict()
                winprobability.append(winprobability_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if article is not UNSET:
            field_dict["article"] = article
        if boxscore is not UNSET:
            field_dict["boxscore"] = boxscore
        if broadcasts is not UNSET:
            field_dict["broadcasts"] = broadcasts
        if drives is not UNSET:
            field_dict["drives"] = drives
        if game_info is not UNSET:
            field_dict["gameInfo"] = game_info
        if header is not UNSET:
            field_dict["header"] = header
        if leaders is not UNSET:
            field_dict["leaders"] = leaders
        if news is not UNSET:
            field_dict["news"] = news
        if pickcenter is not UNSET:
            field_dict["pickcenter"] = pickcenter
        if scoring_plays is not UNSET:
            field_dict["scoringPlays"] = scoring_plays
        if standings is not UNSET:
            field_dict["standings"] = standings
        if videos is not UNSET:
            field_dict["videos"] = videos
        if winprobability is not UNSET:
            field_dict["winprobability"] = winprobability

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_game_response_gamepackage_json_article import NflGameResponseGamepackageJSONArticle
        from ..models.nfl_game_response_gamepackage_json_boxscore import NflGameResponseGamepackageJSONBoxscore
        from ..models.nfl_game_response_gamepackage_json_broadcasts_item import (
            NflGameResponseGamepackageJSONBroadcastsItem,
        )
        from ..models.nfl_game_response_gamepackage_json_drives import NflGameResponseGamepackageJSONDrives
        from ..models.nfl_game_response_gamepackage_json_game_info import NflGameResponseGamepackageJSONGameInfo
        from ..models.nfl_game_response_gamepackage_json_header import NflGameResponseGamepackageJSONHeader
        from ..models.nfl_game_response_gamepackage_json_leaders_item import NflGameResponseGamepackageJSONLeadersItem
        from ..models.nfl_game_response_gamepackage_json_news import NflGameResponseGamepackageJSONNews
        from ..models.nfl_game_response_gamepackage_json_pickcenter_item import (
            NflGameResponseGamepackageJSONPickcenterItem,
        )
        from ..models.nfl_game_response_gamepackage_json_scoring_plays_item import (
            NflGameResponseGamepackageJSONScoringPlaysItem,
        )
        from ..models.nfl_game_response_gamepackage_json_standings import NflGameResponseGamepackageJSONStandings
        from ..models.nfl_game_response_gamepackage_json_videos_item import NflGameResponseGamepackageJSONVideosItem
        from ..models.nfl_game_response_gamepackage_json_winprobability_item import (
            NflGameResponseGamepackageJSONWinprobabilityItem,
        )

        d = src_dict.copy()
        _article = d.pop("article", UNSET)
        article: Union[Unset, NflGameResponseGamepackageJSONArticle]
        if isinstance(_article, Unset):
            article = UNSET
        else:
            article = NflGameResponseGamepackageJSONArticle.from_dict(_article)

        _boxscore = d.pop("boxscore", UNSET)
        boxscore: Union[Unset, NflGameResponseGamepackageJSONBoxscore]
        if isinstance(_boxscore, Unset):
            boxscore = UNSET
        else:
            boxscore = NflGameResponseGamepackageJSONBoxscore.from_dict(_boxscore)

        broadcasts = []
        _broadcasts = d.pop("broadcasts", UNSET)
        for broadcasts_item_data in _broadcasts or []:
            broadcasts_item = NflGameResponseGamepackageJSONBroadcastsItem.from_dict(broadcasts_item_data)

            broadcasts.append(broadcasts_item)

        _drives = d.pop("drives", UNSET)
        drives: Union[Unset, NflGameResponseGamepackageJSONDrives]
        if isinstance(_drives, Unset):
            drives = UNSET
        else:
            drives = NflGameResponseGamepackageJSONDrives.from_dict(_drives)

        _game_info = d.pop("gameInfo", UNSET)
        game_info: Union[Unset, NflGameResponseGamepackageJSONGameInfo]
        if isinstance(_game_info, Unset):
            game_info = UNSET
        else:
            game_info = NflGameResponseGamepackageJSONGameInfo.from_dict(_game_info)

        _header = d.pop("header", UNSET)
        header: Union[Unset, NflGameResponseGamepackageJSONHeader]
        if isinstance(_header, Unset):
            header = UNSET
        else:
            header = NflGameResponseGamepackageJSONHeader.from_dict(_header)

        leaders = []
        _leaders = d.pop("leaders", UNSET)
        for leaders_item_data in _leaders or []:
            leaders_item = NflGameResponseGamepackageJSONLeadersItem.from_dict(leaders_item_data)

            leaders.append(leaders_item)

        _news = d.pop("news", UNSET)
        news: Union[Unset, NflGameResponseGamepackageJSONNews]
        if isinstance(_news, Unset):
            news = UNSET
        else:
            news = NflGameResponseGamepackageJSONNews.from_dict(_news)

        pickcenter = []
        _pickcenter = d.pop("pickcenter", UNSET)
        for pickcenter_item_data in _pickcenter or []:
            pickcenter_item = NflGameResponseGamepackageJSONPickcenterItem.from_dict(pickcenter_item_data)

            pickcenter.append(pickcenter_item)

        scoring_plays = []
        _scoring_plays = d.pop("scoringPlays", UNSET)
        for scoring_plays_item_data in _scoring_plays or []:
            scoring_plays_item = NflGameResponseGamepackageJSONScoringPlaysItem.from_dict(scoring_plays_item_data)

            scoring_plays.append(scoring_plays_item)

        _standings = d.pop("standings", UNSET)
        standings: Union[Unset, NflGameResponseGamepackageJSONStandings]
        if isinstance(_standings, Unset):
            standings = UNSET
        else:
            standings = NflGameResponseGamepackageJSONStandings.from_dict(_standings)

        videos = []
        _videos = d.pop("videos", UNSET)
        for videos_item_data in _videos or []:
            videos_item = NflGameResponseGamepackageJSONVideosItem.from_dict(videos_item_data)

            videos.append(videos_item)

        winprobability = []
        _winprobability = d.pop("winprobability", UNSET)
        for winprobability_item_data in _winprobability or []:
            winprobability_item = NflGameResponseGamepackageJSONWinprobabilityItem.from_dict(winprobability_item_data)

            winprobability.append(winprobability_item)

        nfl_game_response_gamepackage_json = cls(
            article=article,
            boxscore=boxscore,
            broadcasts=broadcasts,
            drives=drives,
            game_info=game_info,
            header=header,
            leaders=leaders,
            news=news,
            pickcenter=pickcenter,
            scoring_plays=scoring_plays,
            standings=standings,
            videos=videos,
            winprobability=winprobability,
        )

        nfl_game_response_gamepackage_json.additional_properties = d
        return nfl_game_response_gamepackage_json

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
