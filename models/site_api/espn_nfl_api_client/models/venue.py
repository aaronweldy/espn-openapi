from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.image import Image


T = TypeVar("T", bound="Venue")


@_attrs_define
class Venue:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 1.
        full_name (Union[Unset, str]):  Example: State Farm Stadium.
        address (Union[Unset, Address]):
        capacity (Union[Unset, int]):  Example: 63400.
        grass (Union[Unset, bool]):
        indoor (Union[Unset, bool]):
        images (Union[Unset, List['Image']]):
    """

    id: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    address: Union[Unset, "Address"] = UNSET
    capacity: Union[Unset, int] = UNSET
    grass: Union[Unset, bool] = UNSET
    indoor: Union[Unset, bool] = UNSET
    images: Union[Unset, List["Image"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        full_name = self.full_name

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        capacity = self.capacity

        grass = self.grass

        indoor = self.indoor

        images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if address is not UNSET:
            field_dict["address"] = address
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if grass is not UNSET:
            field_dict["grass"] = grass
        if indoor is not UNSET:
            field_dict["indoor"] = indoor
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.image import Image

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        full_name = d.pop("fullName", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, Address]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        capacity = d.pop("capacity", UNSET)

        grass = d.pop("grass", UNSET)

        indoor = d.pop("indoor", UNSET)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = Image.from_dict(images_item_data)

            images.append(images_item)

        venue = cls(
            id=id,
            full_name=full_name,
            address=address,
            capacity=capacity,
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
