from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.href_link import HrefLink


T = TypeVar("T", bound="VideoLinksApi")


@_attrs_define
class VideoLinksApi:
    """
    Attributes:
        artwork (Union[Unset, HrefLink]):
        self_ (Union[Unset, HrefLink]):
    """

    artwork: Union[Unset, "HrefLink"] = UNSET
    self_: Union[Unset, "HrefLink"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        artwork: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.artwork, Unset):
            artwork = self.artwork.to_dict()

        self_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if artwork is not UNSET:
            field_dict["artwork"] = artwork
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href_link import HrefLink

        d = src_dict.copy()
        _artwork = d.pop("artwork", UNSET)
        artwork: Union[Unset, HrefLink]
        if isinstance(_artwork, Unset):
            artwork = UNSET
        else:
            artwork = HrefLink.from_dict(_artwork)

        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, HrefLink]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = HrefLink.from_dict(_self_)

        video_links_api = cls(
            artwork=artwork,
            self_=self_,
        )

        video_links_api.additional_properties = d
        return video_links_api

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
