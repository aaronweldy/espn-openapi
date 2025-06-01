from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FantasyStatistic")


@_attrs_define
class FantasyStatistic:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        abbreviation (Union[Unset, str]):
        type (Union[Unset, str]):
        recipient_type (Union[Unset, str]):
        slug (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    recipient_type: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        abbreviation = self.abbreviation

        type = self.type

        recipient_type = self.recipient_type

        slug = self.slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if type is not UNSET:
            field_dict["type"] = type
        if recipient_type is not UNSET:
            field_dict["recipientType"] = recipient_type
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        type = d.pop("type", UNSET)

        recipient_type = d.pop("recipientType", UNSET)

        slug = d.pop("slug", UNSET)

        fantasy_statistic = cls(
            id=id,
            name=name,
            abbreviation=abbreviation,
            type=type,
            recipient_type=recipient_type,
            slug=slug,
        )

        fantasy_statistic.additional_properties = d
        return fantasy_statistic

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
