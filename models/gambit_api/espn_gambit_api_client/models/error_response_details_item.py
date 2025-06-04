from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_response_details_item_meta_data_type_0 import ErrorResponseDetailsItemMetaDataType0


T = TypeVar("T", bound="ErrorResponseDetailsItem")


@_attrs_define
class ErrorResponseDetailsItem:
    """
    Attributes:
        message (Union[Unset, str]):
        short_message (Union[Unset, str]):
        resolution (Union[None, Unset, str]):
        type (Union[Unset, str]):
        meta_data (Union['ErrorResponseDetailsItemMetaDataType0', None, Unset]):
    """

    message: Union[Unset, str] = UNSET
    short_message: Union[Unset, str] = UNSET
    resolution: Union[None, Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    meta_data: Union["ErrorResponseDetailsItemMetaDataType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.error_response_details_item_meta_data_type_0 import ErrorResponseDetailsItemMetaDataType0

        message = self.message

        short_message = self.short_message

        resolution: Union[None, Unset, str]
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        else:
            resolution = self.resolution

        type = self.type

        meta_data: Union[Dict[str, Any], None, Unset]
        if isinstance(self.meta_data, Unset):
            meta_data = UNSET
        elif isinstance(self.meta_data, ErrorResponseDetailsItemMetaDataType0):
            meta_data = self.meta_data.to_dict()
        else:
            meta_data = self.meta_data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if short_message is not UNSET:
            field_dict["shortMessage"] = short_message
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if type is not UNSET:
            field_dict["type"] = type
        if meta_data is not UNSET:
            field_dict["metaData"] = meta_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_response_details_item_meta_data_type_0 import ErrorResponseDetailsItemMetaDataType0

        d = src_dict.copy()
        message = d.pop("message", UNSET)

        short_message = d.pop("shortMessage", UNSET)

        def _parse_resolution(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        type = d.pop("type", UNSET)

        def _parse_meta_data(data: object) -> Union["ErrorResponseDetailsItemMetaDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_data_type_0 = ErrorResponseDetailsItemMetaDataType0.from_dict(data)

                return meta_data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ErrorResponseDetailsItemMetaDataType0", None, Unset], data)

        meta_data = _parse_meta_data(d.pop("metaData", UNSET))

        error_response_details_item = cls(
            message=message,
            short_message=short_message,
            resolution=resolution,
            type=type,
            meta_data=meta_data,
        )

        error_response_details_item.additional_properties = d
        return error_response_details_item

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
