from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.href_link import HrefLink


T = TypeVar("T", bound="VideoLinksSourceHLS")


@_attrs_define
class VideoLinksSourceHLS:
    """
    Attributes:
        href (Union[Unset, str]):
        hd (Union[Unset, HrefLink]):
    """

    href: Union[Unset, str] = UNSET
    hd: Union[Unset, "HrefLink"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        hd: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hd, Unset):
            hd = self.hd.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if hd is not UNSET:
            field_dict["HD"] = hd

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href_link import HrefLink

        d = src_dict.copy()
        href = d.pop("href", UNSET)

        _hd = d.pop("HD", UNSET)
        hd: Union[Unset, HrefLink]
        if isinstance(_hd, Unset):
            hd = UNSET
        else:
            hd = HrefLink.from_dict(_hd)

        video_links_source_hls = cls(
            href=href,
            hd=hd,
        )

        video_links_source_hls.additional_properties = d
        return video_links_source_hls

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
