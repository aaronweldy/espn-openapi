from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.geo_broadcast_market import GeoBroadcastMarket
    from ..models.geo_broadcast_media import GeoBroadcastMedia
    from ..models.geo_broadcast_type import GeoBroadcastType


T = TypeVar("T", bound="GeoBroadcast")


@_attrs_define
class GeoBroadcast:
    """
    Attributes:
        type_ (GeoBroadcastType):
        market (GeoBroadcastMarket):
        media (Union[Unset, GeoBroadcastMedia]):
        lang (Union[Unset, str]):  Example: en.
        region (Union[Unset, str]):  Example: us.
    """

    type_: "GeoBroadcastType"
    market: "GeoBroadcastMarket"
    media: Union[Unset, "GeoBroadcastMedia"] = UNSET
    lang: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.to_dict()

        market = self.market.to_dict()

        media: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.media, Unset):
            media = self.media.to_dict()

        lang = self.lang

        region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "market": market,
            }
        )
        if media is not UNSET:
            field_dict["media"] = media
        if lang is not UNSET:
            field_dict["lang"] = lang
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.geo_broadcast_market import GeoBroadcastMarket
        from ..models.geo_broadcast_media import GeoBroadcastMedia
        from ..models.geo_broadcast_type import GeoBroadcastType

        d = dict(src_dict)
        type_ = GeoBroadcastType.from_dict(d.pop("type"))

        market = GeoBroadcastMarket.from_dict(d.pop("market"))

        _media = d.pop("media", UNSET)
        media: Union[Unset, GeoBroadcastMedia]
        if isinstance(_media, Unset):
            media = UNSET
        else:
            media = GeoBroadcastMedia.from_dict(_media)

        lang = d.pop("lang", UNSET)

        region = d.pop("region", UNSET)

        geo_broadcast = cls(
            type_=type_,
            market=market,
            media=media,
            lang=lang,
            region=region,
        )

        geo_broadcast.additional_properties = d
        return geo_broadcast

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
