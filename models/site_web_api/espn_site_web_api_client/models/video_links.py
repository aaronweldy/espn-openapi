from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.href_link import HrefLink
    from ..models.self_link import SelfLink
    from ..models.video_links_api import VideoLinksApi
    from ..models.video_links_mobile import VideoLinksMobile
    from ..models.video_links_source import VideoLinksSource


T = TypeVar("T", bound="VideoLinks")


@_attrs_define
class VideoLinks:
    """
    Attributes:
        sportscenter (Union[Unset, HrefLink]):
        web (Union[Unset, SelfLink]):
        mobile (Union[Unset, VideoLinksMobile]):
        api (Union[Unset, VideoLinksApi]):
        source (Union[Unset, VideoLinksSource]):
    """

    sportscenter: Union[Unset, "HrefLink"] = UNSET
    web: Union[Unset, "SelfLink"] = UNSET
    mobile: Union[Unset, "VideoLinksMobile"] = UNSET
    api: Union[Unset, "VideoLinksApi"] = UNSET
    source: Union[Unset, "VideoLinksSource"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sportscenter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sportscenter, Unset):
            sportscenter = self.sportscenter.to_dict()

        web: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.web, Unset):
            web = self.web.to_dict()

        mobile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mobile, Unset):
            mobile = self.mobile.to_dict()

        api: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.api, Unset):
            api = self.api.to_dict()

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sportscenter is not UNSET:
            field_dict["sportscenter"] = sportscenter
        if web is not UNSET:
            field_dict["web"] = web
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if api is not UNSET:
            field_dict["api"] = api
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href_link import HrefLink
        from ..models.self_link import SelfLink
        from ..models.video_links_api import VideoLinksApi
        from ..models.video_links_mobile import VideoLinksMobile
        from ..models.video_links_source import VideoLinksSource

        d = src_dict.copy()
        _sportscenter = d.pop("sportscenter", UNSET)
        sportscenter: Union[Unset, HrefLink]
        if isinstance(_sportscenter, Unset):
            sportscenter = UNSET
        else:
            sportscenter = HrefLink.from_dict(_sportscenter)

        _web = d.pop("web", UNSET)
        web: Union[Unset, SelfLink]
        if isinstance(_web, Unset):
            web = UNSET
        else:
            web = SelfLink.from_dict(_web)

        _mobile = d.pop("mobile", UNSET)
        mobile: Union[Unset, VideoLinksMobile]
        if isinstance(_mobile, Unset):
            mobile = UNSET
        else:
            mobile = VideoLinksMobile.from_dict(_mobile)

        _api = d.pop("api", UNSET)
        api: Union[Unset, VideoLinksApi]
        if isinstance(_api, Unset):
            api = UNSET
        else:
            api = VideoLinksApi.from_dict(_api)

        _source = d.pop("source", UNSET)
        source: Union[Unset, VideoLinksSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = VideoLinksSource.from_dict(_source)

        video_links = cls(
            sportscenter=sportscenter,
            web=web,
            mobile=mobile,
            api=api,
            source=source,
        )

        video_links.additional_properties = d
        return video_links

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
