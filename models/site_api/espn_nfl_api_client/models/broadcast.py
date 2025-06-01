from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.broadcast_media import BroadcastMedia
    from ..models.broadcast_type import BroadcastType


T = TypeVar("T", bound="Broadcast")


@_attrs_define
class Broadcast:
    """
    Attributes:
        market (Union[Unset, str]):  Example: national.
        names (Union[Unset, List[str]]):
        type (Union[Unset, BroadcastType]):
        media (Union[Unset, BroadcastMedia]):
        lang (Union[Unset, str]):  Example: en.
        region (Union[Unset, str]):  Example: us.
    """

    market: Union[Unset, str] = UNSET
    names: Union[Unset, List[str]] = UNSET
    type: Union[Unset, "BroadcastType"] = UNSET
    media: Union[Unset, "BroadcastMedia"] = UNSET
    lang: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        market = self.market

        names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.names, Unset):
            names = self.names

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        media: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.media, Unset):
            media = self.media.to_dict()

        lang = self.lang

        region = self.region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market
        if names is not UNSET:
            field_dict["names"] = names
        if type is not UNSET:
            field_dict["type"] = type
        if media is not UNSET:
            field_dict["media"] = media
        if lang is not UNSET:
            field_dict["lang"] = lang
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.broadcast_media import BroadcastMedia
        from ..models.broadcast_type import BroadcastType

        d = src_dict.copy()
        market = d.pop("market", UNSET)

        names = cast(List[str], d.pop("names", UNSET))

        _type = d.pop("type", UNSET)
        type: Union[Unset, BroadcastType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = BroadcastType.from_dict(_type)

        _media = d.pop("media", UNSET)
        media: Union[Unset, BroadcastMedia]
        if isinstance(_media, Unset):
            media = UNSET
        else:
            media = BroadcastMedia.from_dict(_media)

        lang = d.pop("lang", UNSET)

        region = d.pop("region", UNSET)

        broadcast = cls(
            market=market,
            names=names,
            type=type,
            media=media,
            lang=lang,
            region=region,
        )

        broadcast.additional_properties = d
        return broadcast

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
