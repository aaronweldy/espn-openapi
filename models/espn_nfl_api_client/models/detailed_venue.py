from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.venue_image import VenueImage


T = TypeVar("T", bound="DetailedVenue")


@_attrs_define
class DetailedVenue:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 3622.
        full_name (Union[Unset, str]):  Example: GEHA Field at Arrowhead Stadium.
        address (Union[Unset, Address]):
        grass (Union[Unset, bool]):
        indoor (Union[Unset, bool]):
        images (Union[Unset, list['VenueImage']]):
    """

    id: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    address: Union[Unset, "Address"] = UNSET
    grass: Union[Unset, bool] = UNSET
    indoor: Union[Unset, bool] = UNSET
    images: Union[Unset, list["VenueImage"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        full_name = self.full_name

        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        grass = self.grass

        indoor = self.indoor

        images: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if address is not UNSET:
            field_dict["address"] = address
        if grass is not UNSET:
            field_dict["grass"] = grass
        if indoor is not UNSET:
            field_dict["indoor"] = indoor
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.venue_image import VenueImage

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        full_name = d.pop("fullName", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, Address]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        grass = d.pop("grass", UNSET)

        indoor = d.pop("indoor", UNSET)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = VenueImage.from_dict(images_item_data)

            images.append(images_item)

        detailed_venue = cls(
            id=id,
            full_name=full_name,
            address=address,
            grass=grass,
            indoor=indoor,
            images=images,
        )

        detailed_venue.additional_properties = d
        return detailed_venue

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
