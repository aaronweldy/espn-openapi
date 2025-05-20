from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.broadcast_market import BroadcastMarket
    from ..models.broadcast_media import BroadcastMedia
    from ..models.broadcast_type import BroadcastType
    from ..models.reference import Reference


T = TypeVar("T", bound="CompetitionBroadcastItem")


@_attrs_define
class CompetitionBroadcastItem:
    """
    Attributes:
        type (BroadcastType):
        channel (int):
        station (str):
        slug (str):
        priority (int):
        market (BroadcastMarket):
        media (BroadcastMedia):
        lang (str):
        region (str):
        competition (Reference):
        partnered (bool):
    """

    type: "BroadcastType"
    channel: int
    station: str
    slug: str
    priority: int
    market: "BroadcastMarket"
    media: "BroadcastMedia"
    lang: str
    region: str
    competition: "Reference"
    partnered: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.to_dict()

        channel = self.channel

        station = self.station

        slug = self.slug

        priority = self.priority

        market = self.market.to_dict()

        media = self.media.to_dict()

        lang = self.lang

        region = self.region

        competition = self.competition.to_dict()

        partnered = self.partnered

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "channel": channel,
                "station": station,
                "slug": slug,
                "priority": priority,
                "market": market,
                "media": media,
                "lang": lang,
                "region": region,
                "competition": competition,
                "partnered": partnered,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.broadcast_market import BroadcastMarket
        from ..models.broadcast_media import BroadcastMedia
        from ..models.broadcast_type import BroadcastType
        from ..models.reference import Reference

        d = src_dict.copy()
        type = BroadcastType.from_dict(d.pop("type"))

        channel = d.pop("channel")

        station = d.pop("station")

        slug = d.pop("slug")

        priority = d.pop("priority")

        market = BroadcastMarket.from_dict(d.pop("market"))

        media = BroadcastMedia.from_dict(d.pop("media"))

        lang = d.pop("lang")

        region = d.pop("region")

        competition = Reference.from_dict(d.pop("competition"))

        partnered = d.pop("partnered")

        competition_broadcast_item = cls(
            type=type,
            channel=channel,
            station=station,
            slug=slug,
            priority=priority,
            market=market,
            media=media,
            lang=lang,
            region=region,
            competition=competition,
            partnered=partnered,
        )

        competition_broadcast_item.additional_properties = d
        return competition_broadcast_item

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
