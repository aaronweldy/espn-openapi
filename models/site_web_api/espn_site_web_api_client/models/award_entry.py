from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwardEntry")


@_attrs_define
class AwardEntry:
    """
    Attributes:
        id (str): Award ID
        name (str): Award name
        league (Union[Unset, str]): League abbreviation
        display_count (Union[Unset, str]): Display string for count (e.g., "4x")
        seasons (Union[Unset, List[int]]): Years won
    """

    id: str
    name: str
    league: Union[Unset, str] = UNSET
    display_count: Union[Unset, str] = UNSET
    seasons: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        league = self.league

        display_count = self.display_count

        seasons: Union[Unset, List[int]] = UNSET
        if not isinstance(self.seasons, Unset):
            seasons = self.seasons

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if league is not UNSET:
            field_dict["league"] = league
        if display_count is not UNSET:
            field_dict["displayCount"] = display_count
        if seasons is not UNSET:
            field_dict["seasons"] = seasons

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        league = d.pop("league", UNSET)

        display_count = d.pop("displayCount", UNSET)

        seasons = cast(List[int], d.pop("seasons", UNSET))

        award_entry = cls(
            id=id,
            name=name,
            league=league,
            display_count=display_count,
            seasons=seasons,
        )

        award_entry.additional_properties = d
        return award_entry

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
