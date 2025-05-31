from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nfl_recap_response_ads import NflRecapResponseAds
    from ..models.nfl_recap_response_analytics import NflRecapResponseAnalytics
    from ..models.nfl_recap_response_content import NflRecapResponseContent
    from ..models.nfl_recap_response_gamepackage_json import NflRecapResponseGamepackageJSON
    from ..models.nfl_recap_response_meta import NflRecapResponseMeta
    from ..models.nfl_recap_response_targeting import NflRecapResponseTargeting
    from ..models.nfl_recap_response_tier_2_nav import NflRecapResponseTier2Nav


T = TypeVar("T", bound="NflRecapResponse")


@_attrs_define
class NflRecapResponse:
    """NFL game recap response with article, news, and game details

    Attributes:
        game_id (Union[Unset, int]): The game ID
        gamepackage_json (Union[Unset, NflRecapResponseGamepackageJSON]): Game package data including article, news,
            standings
        custom_style_sheet (Union[Unset, str]):
        type (Union[Unset, str]):
        content (Union[Unset, NflRecapResponseContent]):
        field_gamepackage (Union[Unset, bool]):
        analytics (Union[Unset, NflRecapResponseAnalytics]):
        ads (Union[Unset, NflRecapResponseAds]):
        targeting (Union[Unset, NflRecapResponseTargeting]):
        meta (Union[Unset, NflRecapResponseMeta]):
        now_feed_supported (Union[Unset, bool]):
        custom_nav (Union[Unset, str]):
        sport (Union[Unset, List[str]]):
        tier_2_nav (Union[Unset, NflRecapResponseTier2Nav]):
    """

    game_id: Union[Unset, int] = UNSET
    gamepackage_json: Union[Unset, "NflRecapResponseGamepackageJSON"] = UNSET
    custom_style_sheet: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    content: Union[Unset, "NflRecapResponseContent"] = UNSET
    field_gamepackage: Union[Unset, bool] = UNSET
    analytics: Union[Unset, "NflRecapResponseAnalytics"] = UNSET
    ads: Union[Unset, "NflRecapResponseAds"] = UNSET
    targeting: Union[Unset, "NflRecapResponseTargeting"] = UNSET
    meta: Union[Unset, "NflRecapResponseMeta"] = UNSET
    now_feed_supported: Union[Unset, bool] = UNSET
    custom_nav: Union[Unset, str] = UNSET
    sport: Union[Unset, List[str]] = UNSET
    tier_2_nav: Union[Unset, "NflRecapResponseTier2Nav"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        game_id = self.game_id

        gamepackage_json: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gamepackage_json, Unset):
            gamepackage_json = self.gamepackage_json.to_dict()

        custom_style_sheet = self.custom_style_sheet

        type = self.type

        content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        field_gamepackage = self.field_gamepackage

        analytics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.analytics, Unset):
            analytics = self.analytics.to_dict()

        ads: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ads, Unset):
            ads = self.ads.to_dict()

        targeting: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.targeting, Unset):
            targeting = self.targeting.to_dict()

        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        now_feed_supported = self.now_feed_supported

        custom_nav = self.custom_nav

        sport: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sport, Unset):
            sport = self.sport

        tier_2_nav: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tier_2_nav, Unset):
            tier_2_nav = self.tier_2_nav.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if game_id is not UNSET:
            field_dict["gameId"] = game_id
        if gamepackage_json is not UNSET:
            field_dict["gamepackageJSON"] = gamepackage_json
        if custom_style_sheet is not UNSET:
            field_dict["customStyleSheet"] = custom_style_sheet
        if type is not UNSET:
            field_dict["type"] = type
        if content is not UNSET:
            field_dict["content"] = content
        if field_gamepackage is not UNSET:
            field_dict["__gamepackage__"] = field_gamepackage
        if analytics is not UNSET:
            field_dict["analytics"] = analytics
        if ads is not UNSET:
            field_dict["ads"] = ads
        if targeting is not UNSET:
            field_dict["targeting"] = targeting
        if meta is not UNSET:
            field_dict["meta"] = meta
        if now_feed_supported is not UNSET:
            field_dict["nowFeedSupported"] = now_feed_supported
        if custom_nav is not UNSET:
            field_dict["customNav"] = custom_nav
        if sport is not UNSET:
            field_dict["sport"] = sport
        if tier_2_nav is not UNSET:
            field_dict["tier2Nav"] = tier_2_nav

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_recap_response_ads import NflRecapResponseAds
        from ..models.nfl_recap_response_analytics import NflRecapResponseAnalytics
        from ..models.nfl_recap_response_content import NflRecapResponseContent
        from ..models.nfl_recap_response_gamepackage_json import NflRecapResponseGamepackageJSON
        from ..models.nfl_recap_response_meta import NflRecapResponseMeta
        from ..models.nfl_recap_response_targeting import NflRecapResponseTargeting
        from ..models.nfl_recap_response_tier_2_nav import NflRecapResponseTier2Nav

        d = src_dict.copy()
        game_id = d.pop("gameId", UNSET)

        _gamepackage_json = d.pop("gamepackageJSON", UNSET)
        gamepackage_json: Union[Unset, NflRecapResponseGamepackageJSON]
        if isinstance(_gamepackage_json, Unset):
            gamepackage_json = UNSET
        else:
            gamepackage_json = NflRecapResponseGamepackageJSON.from_dict(_gamepackage_json)

        custom_style_sheet = d.pop("customStyleSheet", UNSET)

        type = d.pop("type", UNSET)

        _content = d.pop("content", UNSET)
        content: Union[Unset, NflRecapResponseContent]
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = NflRecapResponseContent.from_dict(_content)

        field_gamepackage = d.pop("__gamepackage__", UNSET)

        _analytics = d.pop("analytics", UNSET)
        analytics: Union[Unset, NflRecapResponseAnalytics]
        if isinstance(_analytics, Unset):
            analytics = UNSET
        else:
            analytics = NflRecapResponseAnalytics.from_dict(_analytics)

        _ads = d.pop("ads", UNSET)
        ads: Union[Unset, NflRecapResponseAds]
        if isinstance(_ads, Unset):
            ads = UNSET
        else:
            ads = NflRecapResponseAds.from_dict(_ads)

        _targeting = d.pop("targeting", UNSET)
        targeting: Union[Unset, NflRecapResponseTargeting]
        if isinstance(_targeting, Unset):
            targeting = UNSET
        else:
            targeting = NflRecapResponseTargeting.from_dict(_targeting)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, NflRecapResponseMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = NflRecapResponseMeta.from_dict(_meta)

        now_feed_supported = d.pop("nowFeedSupported", UNSET)

        custom_nav = d.pop("customNav", UNSET)

        sport = cast(List[str], d.pop("sport", UNSET))

        _tier_2_nav = d.pop("tier2Nav", UNSET)
        tier_2_nav: Union[Unset, NflRecapResponseTier2Nav]
        if isinstance(_tier_2_nav, Unset):
            tier_2_nav = UNSET
        else:
            tier_2_nav = NflRecapResponseTier2Nav.from_dict(_tier_2_nav)

        nfl_recap_response = cls(
            game_id=game_id,
            gamepackage_json=gamepackage_json,
            custom_style_sheet=custom_style_sheet,
            type=type,
            content=content,
            field_gamepackage=field_gamepackage,
            analytics=analytics,
            ads=ads,
            targeting=targeting,
            meta=meta,
            now_feed_supported=now_feed_supported,
            custom_nav=custom_nav,
            sport=sport,
            tier_2_nav=tier_2_nav,
        )

        nfl_recap_response.additional_properties = d
        return nfl_recap_response

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
