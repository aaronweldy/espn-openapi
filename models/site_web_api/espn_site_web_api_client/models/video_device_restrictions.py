from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VideoDeviceRestrictions")


@_attrs_define
class VideoDeviceRestrictions:
    """
    Attributes:
        type (Union[Unset, str]):
        devices (Union[Unset, List[str]]):
    """

    type: Union[Unset, str] = UNSET
    devices: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        devices: Union[Unset, List[str]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = self.devices

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if devices is not UNSET:
            field_dict["devices"] = devices

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        devices = cast(List[str], d.pop("devices", UNSET))

        video_device_restrictions = cls(
            type=type,
            devices=devices,
        )

        video_device_restrictions.additional_properties = d
        return video_device_restrictions

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
