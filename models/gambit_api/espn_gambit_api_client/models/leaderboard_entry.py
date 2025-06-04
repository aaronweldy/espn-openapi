from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LeaderboardEntry")


@_attrs_define
class LeaderboardEntry:
    """
    Attributes:
        id (Union[Unset, str]):
        rank (Union[Unset, int]):
        score (Union[Unset, float]):
        percentile (Union[Unset, float]):
        user_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        profile_image_url (Union[None, Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    rank: Union[Unset, int] = UNSET
    score: Union[Unset, float] = UNSET
    percentile: Union[Unset, float] = UNSET
    user_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    profile_image_url: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        rank = self.rank

        score = self.score

        percentile = self.percentile

        user_name = self.user_name

        display_name = self.display_name

        profile_image_url: Union[None, Unset, str]
        if isinstance(self.profile_image_url, Unset):
            profile_image_url = UNSET
        else:
            profile_image_url = self.profile_image_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if rank is not UNSET:
            field_dict["rank"] = rank
        if score is not UNSET:
            field_dict["score"] = score
        if percentile is not UNSET:
            field_dict["percentile"] = percentile
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if profile_image_url is not UNSET:
            field_dict["profileImageUrl"] = profile_image_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        rank = d.pop("rank", UNSET)

        score = d.pop("score", UNSET)

        percentile = d.pop("percentile", UNSET)

        user_name = d.pop("userName", UNSET)

        display_name = d.pop("displayName", UNSET)

        def _parse_profile_image_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        profile_image_url = _parse_profile_image_url(d.pop("profileImageUrl", UNSET))

        leaderboard_entry = cls(
            id=id,
            rank=rank,
            score=score,
            percentile=percentile,
            user_name=user_name,
            display_name=display_name,
            profile_image_url=profile_image_url,
        )

        leaderboard_entry.additional_properties = d
        return leaderboard_entry

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
