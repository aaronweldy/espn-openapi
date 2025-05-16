from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nfl_standings_content import NflStandingsContent
    from ..models.nfl_standings_response_ads import NflStandingsResponseAds
    from ..models.nfl_standings_response_analytics import NflStandingsResponseAnalytics
    from ..models.nfl_standings_response_meta import NflStandingsResponseMeta
    from ..models.nfl_standings_response_tier_2_nav import NflStandingsResponseTier2Nav


T = TypeVar("T", bound="NflStandingsResponse")


@_attrs_define
class NflStandingsResponse:
    """
    Attributes:
        ads (Union[Unset, NflStandingsResponseAds]):
        analytics (Union[Unset, NflStandingsResponseAnalytics]):
        content (Union[Unset, NflStandingsContent]):
        meta (Union[Unset, NflStandingsResponseMeta]):
        now_feed_supported (Union[Unset, bool]):
        sport (Union[Unset, str]):
        tier_2_nav (Union[Unset, NflStandingsResponseTier2Nav]):
        type (Union[Unset, str]):
    """

    ads: Union[Unset, "NflStandingsResponseAds"] = UNSET
    analytics: Union[Unset, "NflStandingsResponseAnalytics"] = UNSET
    content: Union[Unset, "NflStandingsContent"] = UNSET
    meta: Union[Unset, "NflStandingsResponseMeta"] = UNSET
    now_feed_supported: Union[Unset, bool] = UNSET
    sport: Union[Unset, str] = UNSET
    tier_2_nav: Union[Unset, "NflStandingsResponseTier2Nav"] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ads: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ads, Unset):
            ads = self.ads.to_dict()

        analytics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.analytics, Unset):
            analytics = self.analytics.to_dict()

        content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        now_feed_supported = self.now_feed_supported

        sport = self.sport

        tier_2_nav: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tier_2_nav, Unset):
            tier_2_nav = self.tier_2_nav.to_dict()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ads is not UNSET:
            field_dict["ads"] = ads
        if analytics is not UNSET:
            field_dict["analytics"] = analytics
        if content is not UNSET:
            field_dict["content"] = content
        if meta is not UNSET:
            field_dict["meta"] = meta
        if now_feed_supported is not UNSET:
            field_dict["nowFeedSupported"] = now_feed_supported
        if sport is not UNSET:
            field_dict["sport"] = sport
        if tier_2_nav is not UNSET:
            field_dict["tier2Nav"] = tier_2_nav
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_standings_content import NflStandingsContent
        from ..models.nfl_standings_response_ads import NflStandingsResponseAds
        from ..models.nfl_standings_response_analytics import NflStandingsResponseAnalytics
        from ..models.nfl_standings_response_meta import NflStandingsResponseMeta
        from ..models.nfl_standings_response_tier_2_nav import NflStandingsResponseTier2Nav

        d = src_dict.copy()
        _ads = d.pop("ads", UNSET)
        ads: Union[Unset, NflStandingsResponseAds]
        if isinstance(_ads, Unset):
            ads = UNSET
        else:
            ads = NflStandingsResponseAds.from_dict(_ads)

        _analytics = d.pop("analytics", UNSET)
        analytics: Union[Unset, NflStandingsResponseAnalytics]
        if isinstance(_analytics, Unset):
            analytics = UNSET
        else:
            analytics = NflStandingsResponseAnalytics.from_dict(_analytics)

        _content = d.pop("content", UNSET)
        content: Union[Unset, NflStandingsContent]
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = NflStandingsContent.from_dict(_content)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, NflStandingsResponseMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = NflStandingsResponseMeta.from_dict(_meta)

        now_feed_supported = d.pop("nowFeedSupported", UNSET)

        sport = d.pop("sport", UNSET)

        _tier_2_nav = d.pop("tier2Nav", UNSET)
        tier_2_nav: Union[Unset, NflStandingsResponseTier2Nav]
        if isinstance(_tier_2_nav, Unset):
            tier_2_nav = UNSET
        else:
            tier_2_nav = NflStandingsResponseTier2Nav.from_dict(_tier_2_nav)

        type = d.pop("type", UNSET)

        nfl_standings_response = cls(
            ads=ads,
            analytics=analytics,
            content=content,
            meta=meta,
            now_feed_supported=now_feed_supported,
            sport=sport,
            tier_2_nav=tier_2_nav,
            type=type,
        )

        nfl_standings_response.additional_properties = d
        return nfl_standings_response

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
