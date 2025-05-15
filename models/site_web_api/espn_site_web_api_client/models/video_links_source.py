from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.href_link import HrefLink
    from ..models.video_links_source_hls import VideoLinksSourceHLS


T = TypeVar("T", bound="VideoLinksSource")


@_attrs_define
class VideoLinksSource:
    """
    Attributes:
        href (Union[Unset, str]):
        flash (Union[Unset, HrefLink]):
        full (Union[Unset, HrefLink]):
        hds (Union[Unset, HrefLink]):
        mezzanine (Union[Unset, HrefLink]):
        hd (Union[Unset, HrefLink]):
        hls (Union[Unset, VideoLinksSourceHLS]):
    """

    href: Union[Unset, str] = UNSET
    flash: Union[Unset, "HrefLink"] = UNSET
    full: Union[Unset, "HrefLink"] = UNSET
    hds: Union[Unset, "HrefLink"] = UNSET
    mezzanine: Union[Unset, "HrefLink"] = UNSET
    hd: Union[Unset, "HrefLink"] = UNSET
    hls: Union[Unset, "VideoLinksSourceHLS"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        flash: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.flash, Unset):
            flash = self.flash.to_dict()

        full: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.full, Unset):
            full = self.full.to_dict()

        hds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hds, Unset):
            hds = self.hds.to_dict()

        mezzanine: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mezzanine, Unset):
            mezzanine = self.mezzanine.to_dict()

        hd: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hd, Unset):
            hd = self.hd.to_dict()

        hls: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hls, Unset):
            hls = self.hls.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if flash is not UNSET:
            field_dict["flash"] = flash
        if full is not UNSET:
            field_dict["full"] = full
        if hds is not UNSET:
            field_dict["hds"] = hds
        if mezzanine is not UNSET:
            field_dict["mezzanine"] = mezzanine
        if hd is not UNSET:
            field_dict["HD"] = hd
        if hls is not UNSET:
            field_dict["HLS"] = hls

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href_link import HrefLink
        from ..models.video_links_source_hls import VideoLinksSourceHLS

        d = src_dict.copy()
        href = d.pop("href", UNSET)

        _flash = d.pop("flash", UNSET)
        flash: Union[Unset, HrefLink]
        if isinstance(_flash, Unset):
            flash = UNSET
        else:
            flash = HrefLink.from_dict(_flash)

        _full = d.pop("full", UNSET)
        full: Union[Unset, HrefLink]
        if isinstance(_full, Unset):
            full = UNSET
        else:
            full = HrefLink.from_dict(_full)

        _hds = d.pop("hds", UNSET)
        hds: Union[Unset, HrefLink]
        if isinstance(_hds, Unset):
            hds = UNSET
        else:
            hds = HrefLink.from_dict(_hds)

        _mezzanine = d.pop("mezzanine", UNSET)
        mezzanine: Union[Unset, HrefLink]
        if isinstance(_mezzanine, Unset):
            mezzanine = UNSET
        else:
            mezzanine = HrefLink.from_dict(_mezzanine)

        _hd = d.pop("HD", UNSET)
        hd: Union[Unset, HrefLink]
        if isinstance(_hd, Unset):
            hd = UNSET
        else:
            hd = HrefLink.from_dict(_hd)

        _hls = d.pop("HLS", UNSET)
        hls: Union[Unset, VideoLinksSourceHLS]
        if isinstance(_hls, Unset):
            hls = UNSET
        else:
            hls = VideoLinksSourceHLS.from_dict(_hls)

        video_links_source = cls(
            href=href,
            flash=flash,
            full=full,
            hds=hds,
            mezzanine=mezzanine,
            hd=hd,
            hls=hls,
        )

        video_links_source.additional_properties = d
        return video_links_source

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
