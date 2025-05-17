from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemBroadcastsItem")


@_attrs_define
class ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemBroadcastsItem:
    """
    Attributes:
        type_id (Union[Unset, int]):
        priority (Union[Unset, int]):
        type (Union[Unset, str]):
        is_national (Union[Unset, bool]):
        broadcaster_id (Union[Unset, int]):
        broadcast_id (Union[Unset, int]):
        name (Union[Unset, str]):
        short_name (Union[Unset, str]):
        call_letters (Union[Unset, str]):
        station (Union[Unset, str]):
        lang (Union[Unset, str]):
        region (Union[Unset, str]):
        slug (Union[Unset, str]):
    """

    type_id: Union[Unset, int] = UNSET
    priority: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    is_national: Union[Unset, bool] = UNSET
    broadcaster_id: Union[Unset, int] = UNSET
    broadcast_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    call_letters: Union[Unset, str] = UNSET
    station: Union[Unset, str] = UNSET
    lang: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type_id = self.type_id

        priority = self.priority

        type = self.type

        is_national = self.is_national

        broadcaster_id = self.broadcaster_id

        broadcast_id = self.broadcast_id

        name = self.name

        short_name = self.short_name

        call_letters = self.call_letters

        station = self.station

        lang = self.lang

        region = self.region

        slug = self.slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_id is not UNSET:
            field_dict["typeId"] = type_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if type is not UNSET:
            field_dict["type"] = type
        if is_national is not UNSET:
            field_dict["isNational"] = is_national
        if broadcaster_id is not UNSET:
            field_dict["broadcasterId"] = broadcaster_id
        if broadcast_id is not UNSET:
            field_dict["broadcastId"] = broadcast_id
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if call_letters is not UNSET:
            field_dict["callLetters"] = call_letters
        if station is not UNSET:
            field_dict["station"] = station
        if lang is not UNSET:
            field_dict["lang"] = lang
        if region is not UNSET:
            field_dict["region"] = region
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type_id = d.pop("typeId", UNSET)

        priority = d.pop("priority", UNSET)

        type = d.pop("type", UNSET)

        is_national = d.pop("isNational", UNSET)

        broadcaster_id = d.pop("broadcasterId", UNSET)

        broadcast_id = d.pop("broadcastId", UNSET)

        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        call_letters = d.pop("callLetters", UNSET)

        station = d.pop("station", UNSET)

        lang = d.pop("lang", UNSET)

        region = d.pop("region", UNSET)

        slug = d.pop("slug", UNSET)

        scoreboard_header_response_sports_item_leagues_item_events_item_broadcasts_item = cls(
            type_id=type_id,
            priority=priority,
            type=type,
            is_national=is_national,
            broadcaster_id=broadcaster_id,
            broadcast_id=broadcast_id,
            name=name,
            short_name=short_name,
            call_letters=call_letters,
            station=station,
            lang=lang,
            region=region,
            slug=slug,
        )

        scoreboard_header_response_sports_item_leagues_item_events_item_broadcasts_item.additional_properties = d
        return scoreboard_header_response_sports_item_leagues_item_events_item_broadcasts_item

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
