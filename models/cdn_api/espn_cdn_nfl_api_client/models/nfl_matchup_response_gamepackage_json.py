from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nfl_matchup_response_gamepackage_json_boxscore import NflMatchupResponseGamepackageJSONBoxscore
    from ..models.nfl_matchup_response_gamepackage_json_broadcasts_item import (
        NflMatchupResponseGamepackageJSONBroadcastsItem,
    )
    from ..models.nfl_matchup_response_gamepackage_json_game_info import NflMatchupResponseGamepackageJSONGameInfo
    from ..models.nfl_matchup_response_gamepackage_json_header import NflMatchupResponseGamepackageJSONHeader
    from ..models.nfl_matchup_response_gamepackage_json_leaders_item import NflMatchupResponseGamepackageJSONLeadersItem
    from ..models.nfl_matchup_response_gamepackage_json_news import NflMatchupResponseGamepackageJSONNews
    from ..models.nfl_matchup_response_gamepackage_json_pickcenter_item import (
        NflMatchupResponseGamepackageJSONPickcenterItem,
    )
    from ..models.nfl_matchup_response_gamepackage_json_standings import NflMatchupResponseGamepackageJSONStandings
    from ..models.nfl_matchup_response_gamepackage_json_winprobability_item import (
        NflMatchupResponseGamepackageJSONWinprobabilityItem,
    )


T = TypeVar("T", bound="NflMatchupResponseGamepackageJSON")


@_attrs_define
class NflMatchupResponseGamepackageJSON:
    """Game package data for matchup including boxscore, leaders, etc.

    Attributes:
        boxscore (Union[Unset, NflMatchupResponseGamepackageJSONBoxscore]):
        broadcasts (Union[Unset, List['NflMatchupResponseGamepackageJSONBroadcastsItem']]):
        game_info (Union[Unset, NflMatchupResponseGamepackageJSONGameInfo]):
        header (Union[Unset, NflMatchupResponseGamepackageJSONHeader]):
        leaders (Union[Unset, List['NflMatchupResponseGamepackageJSONLeadersItem']]):
        news (Union[Unset, NflMatchupResponseGamepackageJSONNews]):
        pickcenter (Union[Unset, List['NflMatchupResponseGamepackageJSONPickcenterItem']]):
        standings (Union[Unset, NflMatchupResponseGamepackageJSONStandings]):
        winprobability (Union[Unset, List['NflMatchupResponseGamepackageJSONWinprobabilityItem']]):
    """

    boxscore: Union[Unset, "NflMatchupResponseGamepackageJSONBoxscore"] = UNSET
    broadcasts: Union[Unset, List["NflMatchupResponseGamepackageJSONBroadcastsItem"]] = UNSET
    game_info: Union[Unset, "NflMatchupResponseGamepackageJSONGameInfo"] = UNSET
    header: Union[Unset, "NflMatchupResponseGamepackageJSONHeader"] = UNSET
    leaders: Union[Unset, List["NflMatchupResponseGamepackageJSONLeadersItem"]] = UNSET
    news: Union[Unset, "NflMatchupResponseGamepackageJSONNews"] = UNSET
    pickcenter: Union[Unset, List["NflMatchupResponseGamepackageJSONPickcenterItem"]] = UNSET
    standings: Union[Unset, "NflMatchupResponseGamepackageJSONStandings"] = UNSET
    winprobability: Union[Unset, List["NflMatchupResponseGamepackageJSONWinprobabilityItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        boxscore: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.boxscore, Unset):
            boxscore = self.boxscore.to_dict()

        broadcasts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.broadcasts, Unset):
            broadcasts = []
            for broadcasts_item_data in self.broadcasts:
                broadcasts_item = broadcasts_item_data.to_dict()
                broadcasts.append(broadcasts_item)

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

        standings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standings, Unset):
            standings = self.standings.to_dict()

        winprobability: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.winprobability, Unset):
            winprobability = []
            for winprobability_item_data in self.winprobability:
                winprobability_item = winprobability_item_data.to_dict()
                winprobability.append(winprobability_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if boxscore is not UNSET:
            field_dict["boxscore"] = boxscore
        if broadcasts is not UNSET:
            field_dict["broadcasts"] = broadcasts
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
        if standings is not UNSET:
            field_dict["standings"] = standings
        if winprobability is not UNSET:
            field_dict["winprobability"] = winprobability

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_matchup_response_gamepackage_json_boxscore import NflMatchupResponseGamepackageJSONBoxscore
        from ..models.nfl_matchup_response_gamepackage_json_broadcasts_item import (
            NflMatchupResponseGamepackageJSONBroadcastsItem,
        )
        from ..models.nfl_matchup_response_gamepackage_json_game_info import NflMatchupResponseGamepackageJSONGameInfo
        from ..models.nfl_matchup_response_gamepackage_json_header import NflMatchupResponseGamepackageJSONHeader
        from ..models.nfl_matchup_response_gamepackage_json_leaders_item import (
            NflMatchupResponseGamepackageJSONLeadersItem,
        )
        from ..models.nfl_matchup_response_gamepackage_json_news import NflMatchupResponseGamepackageJSONNews
        from ..models.nfl_matchup_response_gamepackage_json_pickcenter_item import (
            NflMatchupResponseGamepackageJSONPickcenterItem,
        )
        from ..models.nfl_matchup_response_gamepackage_json_standings import NflMatchupResponseGamepackageJSONStandings
        from ..models.nfl_matchup_response_gamepackage_json_winprobability_item import (
            NflMatchupResponseGamepackageJSONWinprobabilityItem,
        )

        d = src_dict.copy()
        _boxscore = d.pop("boxscore", UNSET)
        boxscore: Union[Unset, NflMatchupResponseGamepackageJSONBoxscore]
        if isinstance(_boxscore, Unset):
            boxscore = UNSET
        else:
            boxscore = NflMatchupResponseGamepackageJSONBoxscore.from_dict(_boxscore)

        broadcasts = []
        _broadcasts = d.pop("broadcasts", UNSET)
        for broadcasts_item_data in _broadcasts or []:
            broadcasts_item = NflMatchupResponseGamepackageJSONBroadcastsItem.from_dict(broadcasts_item_data)

            broadcasts.append(broadcasts_item)

        _game_info = d.pop("gameInfo", UNSET)
        game_info: Union[Unset, NflMatchupResponseGamepackageJSONGameInfo]
        if isinstance(_game_info, Unset):
            game_info = UNSET
        else:
            game_info = NflMatchupResponseGamepackageJSONGameInfo.from_dict(_game_info)

        _header = d.pop("header", UNSET)
        header: Union[Unset, NflMatchupResponseGamepackageJSONHeader]
        if isinstance(_header, Unset):
            header = UNSET
        else:
            header = NflMatchupResponseGamepackageJSONHeader.from_dict(_header)

        leaders = []
        _leaders = d.pop("leaders", UNSET)
        for leaders_item_data in _leaders or []:
            leaders_item = NflMatchupResponseGamepackageJSONLeadersItem.from_dict(leaders_item_data)

            leaders.append(leaders_item)

        _news = d.pop("news", UNSET)
        news: Union[Unset, NflMatchupResponseGamepackageJSONNews]
        if isinstance(_news, Unset):
            news = UNSET
        else:
            news = NflMatchupResponseGamepackageJSONNews.from_dict(_news)

        pickcenter = []
        _pickcenter = d.pop("pickcenter", UNSET)
        for pickcenter_item_data in _pickcenter or []:
            pickcenter_item = NflMatchupResponseGamepackageJSONPickcenterItem.from_dict(pickcenter_item_data)

            pickcenter.append(pickcenter_item)

        _standings = d.pop("standings", UNSET)
        standings: Union[Unset, NflMatchupResponseGamepackageJSONStandings]
        if isinstance(_standings, Unset):
            standings = UNSET
        else:
            standings = NflMatchupResponseGamepackageJSONStandings.from_dict(_standings)

        winprobability = []
        _winprobability = d.pop("winprobability", UNSET)
        for winprobability_item_data in _winprobability or []:
            winprobability_item = NflMatchupResponseGamepackageJSONWinprobabilityItem.from_dict(
                winprobability_item_data
            )

            winprobability.append(winprobability_item)

        nfl_matchup_response_gamepackage_json = cls(
            boxscore=boxscore,
            broadcasts=broadcasts,
            game_info=game_info,
            header=header,
            leaders=leaders,
            news=news,
            pickcenter=pickcenter,
            standings=standings,
            winprobability=winprobability,
        )

        nfl_matchup_response_gamepackage_json.additional_properties = d
        return nfl_matchup_response_gamepackage_json

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
