from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_response_details_item import ErrorResponseDetailsItem


T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """
    Attributes:
        messages (Union[Unset, List[str]]):
        details (Union[Unset, List['ErrorResponseDetailsItem']]):
    """

    messages: Union[Unset, List[str]] = UNSET
    details: Union[Unset, List["ErrorResponseDetailsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        messages: Union[Unset, List[str]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = self.messages

        details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()
                details.append(details_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if messages is not UNSET:
            field_dict["messages"] = messages
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_response_details_item import ErrorResponseDetailsItem

        d = src_dict.copy()
        messages = cast(List[str], d.pop("messages", UNSET))

        details = []
        _details = d.pop("details", UNSET)
        for details_item_data in _details or []:
            details_item = ErrorResponseDetailsItem.from_dict(details_item_data)

            details.append(details_item)

        error_response = cls(
            messages=messages,
            details=details,
        )

        error_response.additional_properties = d
        return error_response

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
