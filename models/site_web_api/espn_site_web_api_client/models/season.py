from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Season")


@_attrs_define
class Season:
    """
    Attributes:
        year (Union[Unset, int]):  Example: 2023.
        type (Union[Unset, int]): Season type (1=preseason, 2=regular, 3=postseason) Example: 2.
        display_name (Union[Unset, str]):  Example: 2023 Regular Season.
        ref (Union[None, Unset, str]):
    """

    year: Union[Unset, int] = UNSET
    type: Union[Unset, int] = UNSET
    display_name: Union[Unset, str] = UNSET
    ref: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        year = self.year

        type = self.type

        display_name = self.display_name

        ref: Union[None, Unset, str]
        if isinstance(self.ref, Unset):
            ref = UNSET
        else:
            ref = self.ref

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if year is not UNSET:
            field_dict["year"] = year
        if type is not UNSET:
            field_dict["type"] = type
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if ref is not UNSET:
            field_dict["$ref"] = ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        year = d.pop("year", UNSET)

        type = d.pop("type", UNSET)

        display_name = d.pop("displayName", UNSET)

        def _parse_ref(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ref = _parse_ref(d.pop("$ref", UNSET))

        season = cls(
            year=year,
            type=type,
            display_name=display_name,
            ref=ref,
        )

        season.additional_properties = d
        return season

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
