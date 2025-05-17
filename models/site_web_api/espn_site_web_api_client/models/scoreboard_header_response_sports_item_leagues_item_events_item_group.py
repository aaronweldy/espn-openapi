from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemGroup")


@_attrs_define
class ScoreboardHeaderResponseSportsItemLeaguesItemEventsItemGroup:
    """
    Attributes:
        group_id (Union[Unset, str]):
        name (Union[Unset, str]):
        abbreviation (Union[Unset, str]):
        short_name (Union[Unset, str]):
    """

    group_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_id = self.group_id

        name = self.name

        abbreviation = self.abbreviation

        short_name = self.short_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if name is not UNSET:
            field_dict["name"] = name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if short_name is not UNSET:
            field_dict["shortName"] = short_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_id = d.pop("groupId", UNSET)

        name = d.pop("name", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        short_name = d.pop("shortName", UNSET)

        scoreboard_header_response_sports_item_leagues_item_events_item_group = cls(
            group_id=group_id,
            name=name,
            abbreviation=abbreviation,
            short_name=short_name,
        )

        scoreboard_header_response_sports_item_leagues_item_events_item_group.additional_properties = d
        return scoreboard_header_response_sports_item_leagues_item_events_item_group

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
