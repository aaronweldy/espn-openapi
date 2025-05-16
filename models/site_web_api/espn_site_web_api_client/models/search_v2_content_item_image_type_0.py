from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchV2ContentItemImageType0")


@_attrs_define
class SearchV2ContentItemImageType0:
    """
    Attributes:
        default (Union[None, Unset, str]):
        default_dark (Union[None, Unset, str]):
    """

    default: Union[None, Unset, str] = UNSET
    default_dark: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default: Union[None, Unset, str]
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        default_dark: Union[None, Unset, str]
        if isinstance(self.default_dark, Unset):
            default_dark = UNSET
        else:
            default_dark = self.default_dark

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default is not UNSET:
            field_dict["default"] = default
        if default_dark is not UNSET:
            field_dict["defaultDark"] = default_dark

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_default(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default = _parse_default(d.pop("default", UNSET))

        def _parse_default_dark(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default_dark = _parse_default_dark(d.pop("defaultDark", UNSET))

        search_v2_content_item_image_type_0 = cls(
            default=default,
            default_dark=default_dark,
        )

        search_v2_content_item_image_type_0.additional_properties = d
        return search_v2_content_item_image_type_0

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
