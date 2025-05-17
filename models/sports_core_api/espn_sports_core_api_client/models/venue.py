from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.logo import Logo


T = TypeVar("T", bound="Venue")


@_attrs_define
class Venue:
    """
    Attributes:
        ref (str):
        id (str):
        full_name (str):
        address (Address):
        grass (bool):
        indoor (bool):
        images (List['Logo']):
    """

    ref: str
    id: str
    full_name: str
    address: "Address"
    grass: bool
    indoor: bool
    images: List["Logo"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        id = self.id

        full_name = self.full_name

        address = self.address.to_dict()

        grass = self.grass

        indoor = self.indoor

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "id": id,
                "fullName": full_name,
                "address": address,
                "grass": grass,
                "indoor": indoor,
                "images": images,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.logo import Logo

        d = src_dict.copy()
        ref = d.pop("$ref")

        id = d.pop("id")

        full_name = d.pop("fullName")

        address = Address.from_dict(d.pop("address"))

        grass = d.pop("grass")

        indoor = d.pop("indoor")

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = Logo.from_dict(images_item_data)

            images.append(images_item)

        venue = cls(
            ref=ref,
            id=id,
            full_name=full_name,
            address=address,
            grass=grass,
            indoor=indoor,
            images=images,
        )

        venue.additional_properties = d
        return venue

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
