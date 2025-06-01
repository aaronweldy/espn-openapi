from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FantasyBroadcast")


@_attrs_define
class FantasyBroadcast:
    """
    Attributes:
        type (Union[Unset, str]): Broadcast type (TV, Streaming, etc.)
        lang (Union[Unset, str]): Language code
        region (Union[Unset, str]): Region code
        type_id (Union[Unset, int]): Type ID
        is_national (Union[Unset, bool]): Whether broadcast is national
        short_name (Union[Unset, str]): Broadcast network short name
    """

    type: Union[Unset, str] = UNSET
    lang: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    type_id: Union[Unset, int] = UNSET
    is_national: Union[Unset, bool] = UNSET
    short_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        lang = self.lang

        region = self.region

        type_id = self.type_id

        is_national = self.is_national

        short_name = self.short_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if lang is not UNSET:
            field_dict["lang"] = lang
        if region is not UNSET:
            field_dict["region"] = region
        if type_id is not UNSET:
            field_dict["typeId"] = type_id
        if is_national is not UNSET:
            field_dict["isNational"] = is_national
        if short_name is not UNSET:
            field_dict["shortName"] = short_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        lang = d.pop("lang", UNSET)

        region = d.pop("region", UNSET)

        type_id = d.pop("typeId", UNSET)

        is_national = d.pop("isNational", UNSET)

        short_name = d.pop("shortName", UNSET)

        fantasy_broadcast = cls(
            type=type,
            lang=lang,
            region=region,
            type_id=type_id,
            is_national=is_national,
            short_name=short_name,
        )

        fantasy_broadcast.additional_properties = d
        return fantasy_broadcast

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
