from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.author_links_type_0 import AuthorLinksType0
    from ..models.image import Image


T = TypeVar("T", bound="Author")


@_attrs_define
class Author:
    """
    Attributes:
        display_name (Union[None, Unset, str]):
        source_line (Union[None, Unset, str]):
        images (Union[List['Image'], None, Unset]):
        links (Union['AuthorLinksType0', None, Unset]):
    """

    display_name: Union[None, Unset, str] = UNSET
    source_line: Union[None, Unset, str] = UNSET
    images: Union[List["Image"], None, Unset] = UNSET
    links: Union["AuthorLinksType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.author_links_type_0 import AuthorLinksType0

        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        source_line: Union[None, Unset, str]
        if isinstance(self.source_line, Unset):
            source_line = UNSET
        else:
            source_line = self.source_line

        images: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.images, Unset):
            images = UNSET
        elif isinstance(self.images, list):
            images = []
            for images_type_0_item_data in self.images:
                images_type_0_item = images_type_0_item_data.to_dict()
                images.append(images_type_0_item)

        else:
            images = self.images

        links: Union[Dict[str, Any], None, Unset]
        if isinstance(self.links, Unset):
            links = UNSET
        elif isinstance(self.links, AuthorLinksType0):
            links = self.links.to_dict()
        else:
            links = self.links

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if source_line is not UNSET:
            field_dict["sourceLine"] = source_line
        if images is not UNSET:
            field_dict["images"] = images
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.author_links_type_0 import AuthorLinksType0
        from ..models.image import Image

        d = src_dict.copy()

        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        def _parse_source_line(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_line = _parse_source_line(d.pop("sourceLine", UNSET))

        def _parse_images(data: object) -> Union[List["Image"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                images_type_0 = []
                _images_type_0 = data
                for images_type_0_item_data in _images_type_0:
                    images_type_0_item = Image.from_dict(images_type_0_item_data)

                    images_type_0.append(images_type_0_item)

                return images_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["Image"], None, Unset], data)

        images = _parse_images(d.pop("images", UNSET))

        def _parse_links(data: object) -> Union["AuthorLinksType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                links_type_0 = AuthorLinksType0.from_dict(data)

                return links_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AuthorLinksType0", None, Unset], data)

        links = _parse_links(d.pop("links", UNSET))

        author = cls(
            display_name=display_name,
            source_line=source_line,
            images=images,
            links=links,
        )

        author.additional_properties = d
        return author

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
