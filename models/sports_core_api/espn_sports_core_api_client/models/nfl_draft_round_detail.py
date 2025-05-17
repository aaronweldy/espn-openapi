from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.nfl_draft_pick import NflDraftPick
    from ..models.nfl_draft_round_status import NflDraftRoundStatus


T = TypeVar("T", bound="NflDraftRoundDetail")


@_attrs_define
class NflDraftRoundDetail:
    """
    Attributes:
        number (int):
        display_name (str):
        short_display_name (str):
        picks (List['NflDraftPick']):
        status (NflDraftRoundStatus):
    """

    number: int
    display_name: str
    short_display_name: str
    picks: List["NflDraftPick"]
    status: "NflDraftRoundStatus"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number

        display_name = self.display_name

        short_display_name = self.short_display_name

        picks = []
        for picks_item_data in self.picks:
            picks_item = picks_item_data.to_dict()
            picks.append(picks_item)

        status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
                "displayName": display_name,
                "shortDisplayName": short_display_name,
                "picks": picks,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_draft_pick import NflDraftPick
        from ..models.nfl_draft_round_status import NflDraftRoundStatus

        d = src_dict.copy()
        number = d.pop("number")

        display_name = d.pop("displayName")

        short_display_name = d.pop("shortDisplayName")

        picks = []
        _picks = d.pop("picks")
        for picks_item_data in _picks:
            picks_item = NflDraftPick.from_dict(picks_item_data)

            picks.append(picks_item)

        status = NflDraftRoundStatus.from_dict(d.pop("status"))

        nfl_draft_round_detail = cls(
            number=number,
            display_name=display_name,
            short_display_name=short_display_name,
            picks=picks,
            status=status,
        )

        nfl_draft_round_detail.additional_properties = d
        return nfl_draft_round_detail

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
