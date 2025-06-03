from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.draft_rank import DraftRank


T = TypeVar("T", bound="FantasyPlayerDraftRanksByRankType")


@_attrs_define
class FantasyPlayerDraftRanksByRankType:
    """Draft rankings by type (STANDARD, PPR, etc.)"""

    additional_properties: Dict[str, "DraftRank"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.draft_rank import DraftRank

        d = src_dict.copy()
        fantasy_player_draft_ranks_by_rank_type = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = DraftRank.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        fantasy_player_draft_ranks_by_rank_type.additional_properties = additional_properties
        return fantasy_player_draft_ranks_by_rank_type

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "DraftRank":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "DraftRank") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
