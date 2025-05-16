from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_geo_broadcast_type import ScoreboardGeoBroadcastType
    from ..models.scoreboard_market import ScoreboardMarket
    from ..models.scoreboard_media import ScoreboardMedia


T = TypeVar("T", bound="ScoreboardGeoBroadcast")


@_attrs_define
class ScoreboardGeoBroadcast:
    """
    Attributes:
        market (Union[Unset, ScoreboardMarket]):
        media (Union[Unset, ScoreboardMedia]):
        type (Union[Unset, ScoreboardGeoBroadcastType]):
        lang (Union[Unset, str]):
        region (Union[Unset, str]):
    """

    market: Union[Unset, "ScoreboardMarket"] = UNSET
    media: Union[Unset, "ScoreboardMedia"] = UNSET
    type: Union[Unset, "ScoreboardGeoBroadcastType"] = UNSET
    lang: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        market: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market, Unset):
            market = self.market.to_dict()

        media: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.media, Unset):
            media = self.media.to_dict()

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        lang = self.lang

        region = self.region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market
        if media is not UNSET:
            field_dict["media"] = media
        if type is not UNSET:
            field_dict["type"] = type
        if lang is not UNSET:
            field_dict["lang"] = lang
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_geo_broadcast_type import ScoreboardGeoBroadcastType
        from ..models.scoreboard_market import ScoreboardMarket
        from ..models.scoreboard_media import ScoreboardMedia

        d = src_dict.copy()
        _market = d.pop("market", UNSET)
        market: Union[Unset, ScoreboardMarket]
        if isinstance(_market, Unset):
            market = UNSET
        else:
            market = ScoreboardMarket.from_dict(_market)

        _media = d.pop("media", UNSET)
        media: Union[Unset, ScoreboardMedia]
        if isinstance(_media, Unset):
            media = UNSET
        else:
            media = ScoreboardMedia.from_dict(_media)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ScoreboardGeoBroadcastType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ScoreboardGeoBroadcastType.from_dict(_type)

        lang = d.pop("lang", UNSET)

        region = d.pop("region", UNSET)

        scoreboard_geo_broadcast = cls(
            market=market,
            media=media,
            type=type,
            lang=lang,
            region=region,
        )

        scoreboard_geo_broadcast.additional_properties = d
        return scoreboard_geo_broadcast

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
