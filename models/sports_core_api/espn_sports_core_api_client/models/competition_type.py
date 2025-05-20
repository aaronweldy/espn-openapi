from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CompetitionType")


@_attrs_define
class CompetitionType:
    """
    Attributes:
        id (str):
        text (str):
        abbreviation (str):
        slug (str):
        type (str):
    """

    id: str
    text: str
    abbreviation: str
    slug: str
    type: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        text = self.text

        abbreviation = self.abbreviation

        slug = self.slug

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "text": text,
                "abbreviation": abbreviation,
                "slug": slug,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        text = d.pop("text")

        abbreviation = d.pop("abbreviation")

        slug = d.pop("slug")

        type = d.pop("type")

        competition_type = cls(
            id=id,
            text=text,
            abbreviation=abbreviation,
            slug=slug,
            type=type,
        )

        competition_type.additional_properties = d
        return competition_type

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
