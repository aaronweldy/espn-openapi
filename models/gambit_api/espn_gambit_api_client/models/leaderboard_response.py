from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.leaderboard_entry import LeaderboardEntry


T = TypeVar("T", bound="LeaderboardResponse")


@_attrs_define
class LeaderboardResponse:
    """
    Attributes:
        challenge_id (Union[Unset, str]):
        group_id (Union[None, Unset, str]):
        size (Union[Unset, int]): Total number of entries
        locked (Union[Unset, bool]):
        entries (Union[Unset, List['LeaderboardEntry']]):
        featured_entry_ids (Union[Unset, List[str]]):
    """

    challenge_id: Union[Unset, str] = UNSET
    group_id: Union[None, Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    locked: Union[Unset, bool] = UNSET
    entries: Union[Unset, List["LeaderboardEntry"]] = UNSET
    featured_entry_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        challenge_id = self.challenge_id

        group_id: Union[None, Unset, str]
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        else:
            group_id = self.group_id

        size = self.size

        locked = self.locked

        entries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        featured_entry_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.featured_entry_ids, Unset):
            featured_entry_ids = self.featured_entry_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if challenge_id is not UNSET:
            field_dict["challengeId"] = challenge_id
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if size is not UNSET:
            field_dict["size"] = size
        if locked is not UNSET:
            field_dict["locked"] = locked
        if entries is not UNSET:
            field_dict["entries"] = entries
        if featured_entry_ids is not UNSET:
            field_dict["featuredEntryIds"] = featured_entry_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.leaderboard_entry import LeaderboardEntry

        d = src_dict.copy()
        challenge_id = d.pop("challengeId", UNSET)

        def _parse_group_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        group_id = _parse_group_id(d.pop("groupId", UNSET))

        size = d.pop("size", UNSET)

        locked = d.pop("locked", UNSET)

        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = LeaderboardEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        featured_entry_ids = cast(List[str], d.pop("featuredEntryIds", UNSET))

        leaderboard_response = cls(
            challenge_id=challenge_id,
            group_id=group_id,
            size=size,
            locked=locked,
            entries=entries,
            featured_entry_ids=featured_entry_ids,
        )

        leaderboard_response.additional_properties = d
        return leaderboard_response

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
