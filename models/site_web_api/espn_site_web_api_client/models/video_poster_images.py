from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.href_link import HrefLink
    from ..models.image_link_with_size import ImageLinkWithSize


T = TypeVar("T", bound="VideoPosterImages")


@_attrs_define
class VideoPosterImages:
    """
    Attributes:
        square (Union[Unset, HrefLink]):
        default (Union[Unset, ImageLinkWithSize]):
        wide (Union[Unset, HrefLink]):
        full (Union[Unset, HrefLink]):
    """

    square: Union[Unset, "HrefLink"] = UNSET
    default: Union[Unset, "ImageLinkWithSize"] = UNSET
    wide: Union[Unset, "HrefLink"] = UNSET
    full: Union[Unset, "HrefLink"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        square: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.square, Unset):
            square = self.square.to_dict()

        default: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default, Unset):
            default = self.default.to_dict()

        wide: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.wide, Unset):
            wide = self.wide.to_dict()

        full: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.full, Unset):
            full = self.full.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if square is not UNSET:
            field_dict["square"] = square
        if default is not UNSET:
            field_dict["default"] = default
        if wide is not UNSET:
            field_dict["wide"] = wide
        if full is not UNSET:
            field_dict["full"] = full

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href_link import HrefLink
        from ..models.image_link_with_size import ImageLinkWithSize

        d = src_dict.copy()
        _square = d.pop("square", UNSET)
        square: Union[Unset, HrefLink]
        if isinstance(_square, Unset):
            square = UNSET
        else:
            square = HrefLink.from_dict(_square)

        _default = d.pop("default", UNSET)
        default: Union[Unset, ImageLinkWithSize]
        if isinstance(_default, Unset):
            default = UNSET
        else:
            default = ImageLinkWithSize.from_dict(_default)

        _wide = d.pop("wide", UNSET)
        wide: Union[Unset, HrefLink]
        if isinstance(_wide, Unset):
            wide = UNSET
        else:
            wide = HrefLink.from_dict(_wide)

        _full = d.pop("full", UNSET)
        full: Union[Unset, HrefLink]
        if isinstance(_full, Unset):
            full = UNSET
        else:
            full = HrefLink.from_dict(_full)

        video_poster_images = cls(
            square=square,
            default=default,
            wide=wide,
            full=full,
        )

        video_poster_images.additional_properties = d
        return video_poster_images

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
