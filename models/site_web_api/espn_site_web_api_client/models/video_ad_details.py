from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VideoAdDetails")


@_attrs_define
class VideoAdDetails:
    """
    Attributes:
        sport (Union[Unset, str]):
        bundle (Union[Unset, str]):
    """

    sport: Union[Unset, str] = UNSET
    bundle: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sport = self.sport

        bundle = self.bundle

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sport is not UNSET:
            field_dict["sport"] = sport
        if bundle is not UNSET:
            field_dict["bundle"] = bundle

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sport = d.pop("sport", UNSET)

        bundle = d.pop("bundle", UNSET)

        video_ad_details = cls(
            sport=sport,
            bundle=bundle,
        )

        video_ad_details.additional_properties = d
        return video_ad_details

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
