from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VideoGeoRestrictions")


@_attrs_define
class VideoGeoRestrictions:
    """
    Attributes:
        type (Union[Unset, str]):
        countries (Union[Unset, List[str]]):
    """

    type: Union[Unset, str] = UNSET
    countries: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        countries: Union[Unset, List[str]] = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if countries is not UNSET:
            field_dict["countries"] = countries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        countries = cast(List[str], d.pop("countries", UNSET))

        video_geo_restrictions = cls(
            type=type,
            countries=countries,
        )

        video_geo_restrictions.additional_properties = d
        return video_geo_restrictions

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
