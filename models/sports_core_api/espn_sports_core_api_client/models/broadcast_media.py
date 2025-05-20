from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.broadcast_logo import BroadcastLogo


T = TypeVar("T", bound="BroadcastMedia")


@_attrs_define
class BroadcastMedia:
    """
    Attributes:
        ref (str):
        id (str):
        call_letters (str):
        name (str):
        short_name (str):
        slug (str):
        logos (List['BroadcastLogo']):
    """

    ref: str
    id: str
    call_letters: str
    name: str
    short_name: str
    slug: str
    logos: List["BroadcastLogo"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        id = self.id

        call_letters = self.call_letters

        name = self.name

        short_name = self.short_name

        slug = self.slug

        logos = []
        for logos_item_data in self.logos:
            logos_item = logos_item_data.to_dict()
            logos.append(logos_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "id": id,
                "callLetters": call_letters,
                "name": name,
                "shortName": short_name,
                "slug": slug,
                "logos": logos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.broadcast_logo import BroadcastLogo

        d = src_dict.copy()
        ref = d.pop("$ref")

        id = d.pop("id")

        call_letters = d.pop("callLetters")

        name = d.pop("name")

        short_name = d.pop("shortName")

        slug = d.pop("slug")

        logos = []
        _logos = d.pop("logos")
        for logos_item_data in _logos:
            logos_item = BroadcastLogo.from_dict(logos_item_data)

            logos.append(logos_item)

        broadcast_media = cls(
            ref=ref,
            id=id,
            call_letters=call_letters,
            name=name,
            short_name=short_name,
            slug=slug,
            logos=logos,
        )

        broadcast_media.additional_properties = d
        return broadcast_media

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
