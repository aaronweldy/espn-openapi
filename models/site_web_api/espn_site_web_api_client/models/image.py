from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Image")


@_attrs_define
class Image:
    """
    Attributes:
        width (Union[None, Unset, int]):
        height (Union[None, Unset, int]):
        url (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
        alt (Union[None, Unset, str]):
        caption (Union[None, Unset, str]):
        peers (Union[List['Image'], None, Unset]):
        source (Union[None, Unset, str]):
    """

    width: Union[None, Unset, int] = UNSET
    height: Union[None, Unset, int] = UNSET
    url: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    alt: Union[None, Unset, str] = UNSET
    caption: Union[None, Unset, str] = UNSET
    peers: Union[List["Image"], None, Unset] = UNSET
    source: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        alt: Union[None, Unset, str]
        if isinstance(self.alt, Unset):
            alt = UNSET
        else:
            alt = self.alt

        caption: Union[None, Unset, str]
        if isinstance(self.caption, Unset):
            caption = UNSET
        else:
            caption = self.caption

        peers: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.peers, Unset):
            peers = UNSET
        elif isinstance(self.peers, list):
            peers = []
            for peers_type_0_item_data in self.peers:
                peers_type_0_item = peers_type_0_item_data.to_dict()
                peers.append(peers_type_0_item)

        else:
            peers = self.peers

        source: Union[None, Unset, str]
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if url is not UNSET:
            field_dict["url"] = url
        if name is not UNSET:
            field_dict["name"] = name
        if alt is not UNSET:
            field_dict["alt"] = alt
        if caption is not UNSET:
            field_dict["caption"] = caption
        if peers is not UNSET:
            field_dict["peers"] = peers
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

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

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_alt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alt = _parse_alt(d.pop("alt", UNSET))

        def _parse_caption(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        caption = _parse_caption(d.pop("caption", UNSET))

        def _parse_peers(data: object) -> Union[List["Image"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                peers_type_0 = []
                _peers_type_0 = data
                for peers_type_0_item_data in _peers_type_0:
                    peers_type_0_item = Image.from_dict(peers_type_0_item_data)

                    peers_type_0.append(peers_type_0_item)

                return peers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["Image"], None, Unset], data)

        peers = _parse_peers(d.pop("peers", UNSET))

        def _parse_source(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source = _parse_source(d.pop("source", UNSET))

        image = cls(
            width=width,
            height=height,
            url=url,
            name=name,
            alt=alt,
            caption=caption,
            peers=peers,
            source=source,
        )

        image.additional_properties = d
        return image

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
