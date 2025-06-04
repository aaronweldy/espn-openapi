from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flex_image_attributes import FlexImageAttributes


T = TypeVar("T", bound="FlexImage")


@_attrs_define
class FlexImage:
    """
    Attributes:
        href (Union[Unset, str]):
        rels (Union[Unset, List[str]]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        attributes (Union[Unset, FlexImageAttributes]):
    """

    href: Union[Unset, str] = UNSET
    rels: Union[Unset, List[str]] = UNSET
    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    attributes: Union[Unset, "FlexImageAttributes"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        rels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rels, Unset):
            rels = self.rels

        width = self.width

        height = self.height

        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if rels is not UNSET:
            field_dict["rels"] = rels
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.flex_image_attributes import FlexImageAttributes

        d = src_dict.copy()
        href = d.pop("href", UNSET)

        rels = cast(List[str], d.pop("rels", UNSET))

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, FlexImageAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = FlexImageAttributes.from_dict(_attributes)

        flex_image = cls(
            href=href,
            rels=rels,
            width=width,
            height=height,
            attributes=attributes,
        )

        flex_image.additional_properties = d
        return flex_image

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
