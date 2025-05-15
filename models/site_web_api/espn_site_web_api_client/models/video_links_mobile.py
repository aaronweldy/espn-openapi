from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.href_link import HrefLink


T = TypeVar("T", bound="VideoLinksMobile")


@_attrs_define
class VideoLinksMobile:
    """
    Attributes:
        href (Union[Unset, str]):
        alert (Union[Unset, HrefLink]):
        progressive_download (Union[Unset, HrefLink]):
        source (Union[Unset, HrefLink]):
        streaming (Union[Unset, HrefLink]):
    """

    href: Union[Unset, str] = UNSET
    alert: Union[Unset, "HrefLink"] = UNSET
    progressive_download: Union[Unset, "HrefLink"] = UNSET
    source: Union[Unset, "HrefLink"] = UNSET
    streaming: Union[Unset, "HrefLink"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        alert: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alert, Unset):
            alert = self.alert.to_dict()

        progressive_download: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.progressive_download, Unset):
            progressive_download = self.progressive_download.to_dict()

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        streaming: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.streaming, Unset):
            streaming = self.streaming.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if alert is not UNSET:
            field_dict["alert"] = alert
        if progressive_download is not UNSET:
            field_dict["progressiveDownload"] = progressive_download
        if source is not UNSET:
            field_dict["source"] = source
        if streaming is not UNSET:
            field_dict["streaming"] = streaming

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href_link import HrefLink

        d = src_dict.copy()
        href = d.pop("href", UNSET)

        _alert = d.pop("alert", UNSET)
        alert: Union[Unset, HrefLink]
        if isinstance(_alert, Unset):
            alert = UNSET
        else:
            alert = HrefLink.from_dict(_alert)

        _progressive_download = d.pop("progressiveDownload", UNSET)
        progressive_download: Union[Unset, HrefLink]
        if isinstance(_progressive_download, Unset):
            progressive_download = UNSET
        else:
            progressive_download = HrefLink.from_dict(_progressive_download)

        _source = d.pop("source", UNSET)
        source: Union[Unset, HrefLink]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = HrefLink.from_dict(_source)

        _streaming = d.pop("streaming", UNSET)
        streaming: Union[Unset, HrefLink]
        if isinstance(_streaming, Unset):
            streaming = UNSET
        else:
            streaming = HrefLink.from_dict(_streaming)

        video_links_mobile = cls(
            href=href,
            alert=alert,
            progressive_download=progressive_download,
            source=source,
            streaming=streaming,
        )

        video_links_mobile.additional_properties = d
        return video_links_mobile

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
