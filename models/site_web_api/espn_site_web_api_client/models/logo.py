from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Logo")


@_attrs_define
class Logo:
    """
    Attributes:
        href (Union[Unset, str]):
        width (Union[None, Unset, int]):
        height (Union[None, Unset, int]):
        alt (Union[None, Unset, str]):
        rel (Union[List[str], None, Unset]):
    """

    href: Union[Unset, str] = UNSET
    width: Union[None, Unset, int] = UNSET
    height: Union[None, Unset, int] = UNSET
    alt: Union[None, Unset, str] = UNSET
    rel: Union[List[str], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        width: Union[None, Unset, int]
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        height: Union[None, Unset, int]
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        alt: Union[None, Unset, str]
        if isinstance(self.alt, Unset):
            alt = UNSET
        else:
            alt = self.alt

        rel: Union[List[str], None, Unset]
        if isinstance(self.rel, Unset):
            rel = UNSET
        elif isinstance(self.rel, list):
            rel = self.rel

        else:
            rel = self.rel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if alt is not UNSET:
            field_dict["alt"] = alt
        if rel is not UNSET:
            field_dict["rel"] = rel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        href = d.pop("href", UNSET)

        def _parse_width(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        width = _parse_width(d.pop("width", UNSET))

        def _parse_height(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        height = _parse_height(d.pop("height", UNSET))

        def _parse_alt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alt = _parse_alt(d.pop("alt", UNSET))

        def _parse_rel(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rel_type_0 = cast(List[str], data)

                return rel_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        rel = _parse_rel(d.pop("rel", UNSET))

        logo = cls(
            href=href,
            width=width,
            height=height,
            alt=alt,
            rel=rel,
        )

        logo.additional_properties = d
        return logo

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
