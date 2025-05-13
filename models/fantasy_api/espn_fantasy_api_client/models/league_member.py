from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LeagueMember")


@_attrs_define
class LeagueMember:
    """
    Attributes:
        id (str): Member ID Example: {123456789-ABCD-EF12-3456-7890ABCDEF12}.
        display_name (str): Display name Example: User123.
        first_name (Union[Unset, str]): First name Example: John.
        last_name (Union[Unset, str]): Last name Example: Doe.
        is_league_manager (Union[Unset, bool]): Whether member is league manager Example: True.
        is_league_creator (Union[Unset, bool]): Whether member created the league Example: True.
        email (Union[Unset, str]): Member email Example: user@example.com.
    """

    id: str
    display_name: str
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    is_league_manager: Union[Unset, bool] = UNSET
    is_league_creator: Union[Unset, bool] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        display_name = self.display_name

        first_name = self.first_name

        last_name = self.last_name

        is_league_manager = self.is_league_manager

        is_league_creator = self.is_league_creator

        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "displayName": display_name,
            }
        )
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if is_league_manager is not UNSET:
            field_dict["isLeagueManager"] = is_league_manager
        if is_league_creator is not UNSET:
            field_dict["isLeagueCreator"] = is_league_creator
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        display_name = d.pop("displayName")

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        is_league_manager = d.pop("isLeagueManager", UNSET)

        is_league_creator = d.pop("isLeagueCreator", UNSET)

        email = d.pop("email", UNSET)

        league_member = cls(
            id=id,
            display_name=display_name,
            first_name=first_name,
            last_name=last_name,
            is_league_manager=is_league_manager,
            is_league_creator=is_league_creator,
            email=email,
        )

        league_member.additional_properties = d
        return league_member

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
