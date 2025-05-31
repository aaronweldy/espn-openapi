from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nfl_recap_response_gamepackage_json_article import NflRecapResponseGamepackageJSONArticle
    from ..models.nfl_recap_response_gamepackage_json_broadcasts_item import (
        NflRecapResponseGamepackageJSONBroadcastsItem,
    )
    from ..models.nfl_recap_response_gamepackage_json_header import NflRecapResponseGamepackageJSONHeader
    from ..models.nfl_recap_response_gamepackage_json_news import NflRecapResponseGamepackageJSONNews
    from ..models.nfl_recap_response_gamepackage_json_standings import NflRecapResponseGamepackageJSONStandings
    from ..models.nfl_recap_response_gamepackage_json_winprobability_item import (
        NflRecapResponseGamepackageJSONWinprobabilityItem,
    )


T = TypeVar("T", bound="NflRecapResponseGamepackageJSON")


@_attrs_define
class NflRecapResponseGamepackageJSON:
    """Game package data including article, news, standings

    Attributes:
        article (Union[Unset, NflRecapResponseGamepackageJSONArticle]):
        broadcasts (Union[Unset, List['NflRecapResponseGamepackageJSONBroadcastsItem']]):
        header (Union[Unset, NflRecapResponseGamepackageJSONHeader]):
        news (Union[Unset, NflRecapResponseGamepackageJSONNews]):
        standings (Union[Unset, NflRecapResponseGamepackageJSONStandings]):
        winprobability (Union[Unset, List['NflRecapResponseGamepackageJSONWinprobabilityItem']]):
    """

    article: Union[Unset, "NflRecapResponseGamepackageJSONArticle"] = UNSET
    broadcasts: Union[Unset, List["NflRecapResponseGamepackageJSONBroadcastsItem"]] = UNSET
    header: Union[Unset, "NflRecapResponseGamepackageJSONHeader"] = UNSET
    news: Union[Unset, "NflRecapResponseGamepackageJSONNews"] = UNSET
    standings: Union[Unset, "NflRecapResponseGamepackageJSONStandings"] = UNSET
    winprobability: Union[Unset, List["NflRecapResponseGamepackageJSONWinprobabilityItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        article: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.article, Unset):
            article = self.article.to_dict()

        broadcasts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.broadcasts, Unset):
            broadcasts = []
            for broadcasts_item_data in self.broadcasts:
                broadcasts_item = broadcasts_item_data.to_dict()
                broadcasts.append(broadcasts_item)

        header: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.to_dict()

        news: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.news, Unset):
            news = self.news.to_dict()

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
        if article is not UNSET:
            field_dict["article"] = article
        if broadcasts is not UNSET:
            field_dict["broadcasts"] = broadcasts
        if header is not UNSET:
            field_dict["header"] = header
        if news is not UNSET:
            field_dict["news"] = news
        if standings is not UNSET:
            field_dict["standings"] = standings
        if winprobability is not UNSET:
            field_dict["winprobability"] = winprobability

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_recap_response_gamepackage_json_article import NflRecapResponseGamepackageJSONArticle
        from ..models.nfl_recap_response_gamepackage_json_broadcasts_item import (
            NflRecapResponseGamepackageJSONBroadcastsItem,
        )
        from ..models.nfl_recap_response_gamepackage_json_header import NflRecapResponseGamepackageJSONHeader
        from ..models.nfl_recap_response_gamepackage_json_news import NflRecapResponseGamepackageJSONNews
        from ..models.nfl_recap_response_gamepackage_json_standings import NflRecapResponseGamepackageJSONStandings
        from ..models.nfl_recap_response_gamepackage_json_winprobability_item import (
            NflRecapResponseGamepackageJSONWinprobabilityItem,
        )

        d = src_dict.copy()
        _article = d.pop("article", UNSET)
        article: Union[Unset, NflRecapResponseGamepackageJSONArticle]
        if isinstance(_article, Unset):
            article = UNSET
        else:
            article = NflRecapResponseGamepackageJSONArticle.from_dict(_article)

        broadcasts = []
        _broadcasts = d.pop("broadcasts", UNSET)
        for broadcasts_item_data in _broadcasts or []:
            broadcasts_item = NflRecapResponseGamepackageJSONBroadcastsItem.from_dict(broadcasts_item_data)

            broadcasts.append(broadcasts_item)

        _header = d.pop("header", UNSET)
        header: Union[Unset, NflRecapResponseGamepackageJSONHeader]
        if isinstance(_header, Unset):
            header = UNSET
        else:
            header = NflRecapResponseGamepackageJSONHeader.from_dict(_header)

        _news = d.pop("news", UNSET)
        news: Union[Unset, NflRecapResponseGamepackageJSONNews]
        if isinstance(_news, Unset):
            news = UNSET
        else:
            news = NflRecapResponseGamepackageJSONNews.from_dict(_news)

        _standings = d.pop("standings", UNSET)
        standings: Union[Unset, NflRecapResponseGamepackageJSONStandings]
        if isinstance(_standings, Unset):
            standings = UNSET
        else:
            standings = NflRecapResponseGamepackageJSONStandings.from_dict(_standings)

        winprobability = []
        _winprobability = d.pop("winprobability", UNSET)
        for winprobability_item_data in _winprobability or []:
            winprobability_item = NflRecapResponseGamepackageJSONWinprobabilityItem.from_dict(winprobability_item_data)

            winprobability.append(winprobability_item)

        nfl_recap_response_gamepackage_json = cls(
            article=article,
            broadcasts=broadcasts,
            header=header,
            news=news,
            standings=standings,
            winprobability=winprobability,
        )

        nfl_recap_response_gamepackage_json.additional_properties = d
        return nfl_recap_response_gamepackage_json

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
