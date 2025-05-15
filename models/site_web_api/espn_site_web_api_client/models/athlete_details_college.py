from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AthleteDetailsCollege")


@_attrs_define
class AthleteDetailsCollege:
    """
    Attributes:
        id (Union[None, Unset, str]):
        mascot (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
        short_name (Union[None, Unset, str]):
    """

    id: Union[None, Unset, str] = UNSET
    mascot: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    short_name: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        mascot: Union[None, Unset, str]
        if isinstance(self.mascot, Unset):
            mascot = UNSET
        else:
            mascot = self.mascot

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        short_name: Union[None, Unset, str]
        if isinstance(self.short_name, Unset):
            short_name = UNSET
        else:
            short_name = self.short_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if mascot is not UNSET:
            field_dict["mascot"] = mascot
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_mascot(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mascot = _parse_mascot(d.pop("mascot", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_short_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        short_name = _parse_short_name(d.pop("shortName", UNSET))

        athlete_details_college = cls(
            id=id,
            mascot=mascot,
            name=name,
            short_name=short_name,
        )

        athlete_details_college.additional_properties = d
        return athlete_details_college

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
