from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DraftRank")


@_attrs_define
class DraftRank:
    """
    Attributes:
        auction_value (Union[Unset, float]): Auction draft value
        published (Union[Unset, bool]): Whether the rank is published
        rank (Union[Unset, int]): Draft rank
        rank_source_id (Union[Unset, int]): Source ID for the ranking
        rank_type (Union[Unset, str]): Type of ranking (STANDARD, PPR, etc.)
        slot_id (Union[Unset, int]): Slot ID
    """

    auction_value: Union[Unset, float] = UNSET
    published: Union[Unset, bool] = UNSET
    rank: Union[Unset, int] = UNSET
    rank_source_id: Union[Unset, int] = UNSET
    rank_type: Union[Unset, str] = UNSET
    slot_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auction_value = self.auction_value

        published = self.published

        rank = self.rank

        rank_source_id = self.rank_source_id

        rank_type = self.rank_type

        slot_id = self.slot_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auction_value is not UNSET:
            field_dict["auctionValue"] = auction_value
        if published is not UNSET:
            field_dict["published"] = published
        if rank is not UNSET:
            field_dict["rank"] = rank
        if rank_source_id is not UNSET:
            field_dict["rankSourceId"] = rank_source_id
        if rank_type is not UNSET:
            field_dict["rankType"] = rank_type
        if slot_id is not UNSET:
            field_dict["slotId"] = slot_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auction_value = d.pop("auctionValue", UNSET)

        published = d.pop("published", UNSET)

        rank = d.pop("rank", UNSET)

        rank_source_id = d.pop("rankSourceId", UNSET)

        rank_type = d.pop("rankType", UNSET)

        slot_id = d.pop("slotId", UNSET)

        draft_rank = cls(
            auction_value=auction_value,
            published=published,
            rank=rank,
            rank_source_id=rank_source_id,
            rank_type=rank_type,
            slot_id=slot_id,
        )

        draft_rank.additional_properties = d
        return draft_rank

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
