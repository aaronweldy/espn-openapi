from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.draft_type import DraftType


T = TypeVar("T", bound="DraftStatusResponse")


@_attrs_define
class DraftStatusResponse:
    """Draft status information including current round and type

    Attributes:
        ref (str): API reference URL
        round_ (int): Current draft round number Example: 7.
        type (DraftType): Draft type information
    """

    ref: str
    round_: int
    type: "DraftType"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        round_ = self.round_

        type = self.type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "round": round_,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.draft_type import DraftType

        d = src_dict.copy()
        ref = d.pop("$ref")

        round_ = d.pop("round")

        type = DraftType.from_dict(d.pop("type"))

        draft_status_response = cls(
            ref=ref,
            round_=round_,
            type=type,
        )

        draft_status_response.additional_properties = d
        return draft_status_response

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
