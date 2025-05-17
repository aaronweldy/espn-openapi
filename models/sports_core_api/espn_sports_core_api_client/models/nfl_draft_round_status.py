from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.nfl_draft_pick_status import NflDraftPickStatus


T = TypeVar("T", bound="NflDraftRoundStatus")


@_attrs_define
class NflDraftRoundStatus:
    """
    Attributes:
        round_ (int):
        type (NflDraftPickStatus):
    """

    round_: int
    type: "NflDraftPickStatus"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        round_ = self.round_

        type = self.type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "round": round_,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_draft_pick_status import NflDraftPickStatus

        d = src_dict.copy()
        round_ = d.pop("round")

        type = NflDraftPickStatus.from_dict(d.pop("type"))

        nfl_draft_round_status = cls(
            round_=round_,
            type=type,
        )

        nfl_draft_round_status.additional_properties = d
        return nfl_draft_round_status

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
