from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entry_response_picks_item import EntryResponsePicksItem


T = TypeVar("T", bound="EntryResponse")


@_attrs_define
class EntryResponse:
    """
    Attributes:
        id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        challenge_id (Union[Unset, str]):
        group_ids (Union[Unset, List[str]]):
        picks (Union[Unset, List['EntryResponsePicksItem']]):
        score (Union[Unset, float]):
        rank (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    challenge_id: Union[Unset, str] = UNSET
    group_ids: Union[Unset, List[str]] = UNSET
    picks: Union[Unset, List["EntryResponsePicksItem"]] = UNSET
    score: Union[Unset, float] = UNSET
    rank: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        user_id = self.user_id

        challenge_id = self.challenge_id

        group_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        picks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.picks, Unset):
            picks = []
            for picks_item_data in self.picks:
                picks_item = picks_item_data.to_dict()
                picks.append(picks_item)

        score = self.score

        rank = self.rank

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if challenge_id is not UNSET:
            field_dict["challengeId"] = challenge_id
        if group_ids is not UNSET:
            field_dict["groupIds"] = group_ids
        if picks is not UNSET:
            field_dict["picks"] = picks
        if score is not UNSET:
            field_dict["score"] = score
        if rank is not UNSET:
            field_dict["rank"] = rank

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entry_response_picks_item import EntryResponsePicksItem

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        user_id = d.pop("userId", UNSET)

        challenge_id = d.pop("challengeId", UNSET)

        group_ids = cast(List[str], d.pop("groupIds", UNSET))

        picks = []
        _picks = d.pop("picks", UNSET)
        for picks_item_data in _picks or []:
            picks_item = EntryResponsePicksItem.from_dict(picks_item_data)

            picks.append(picks_item)

        score = d.pop("score", UNSET)

        rank = d.pop("rank", UNSET)

        entry_response = cls(
            id=id,
            user_id=user_id,
            challenge_id=challenge_id,
            group_ids=group_ids,
            picks=picks,
            score=score,
            rank=rank,
        )

        entry_response.additional_properties = d
        return entry_response

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
