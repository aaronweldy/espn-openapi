from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AthleteReference")


@_attrs_define
class AthleteReference:
    """
    Attributes:
        id (str):  Example: 3139477.
        full_name (str):  Example: Patrick Mahomes.
        display_name (Union[Unset, str]):  Example: Patrick Mahomes.
        headshot (Union[Unset, str]):  Example: https://a.espncdn.com/i/headshots/nfl/players/full/3139477.png.
    """

    id: str
    full_name: str
    display_name: Union[Unset, str] = UNSET
    headshot: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        full_name = self.full_name

        display_name = self.display_name

        headshot = self.headshot

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fullName": full_name,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if headshot is not UNSET:
            field_dict["headshot"] = headshot

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        full_name = d.pop("fullName")

        display_name = d.pop("displayName", UNSET)

        headshot = d.pop("headshot", UNSET)

        athlete_reference = cls(
            id=id,
            full_name=full_name,
            display_name=display_name,
            headshot=headshot,
        )

        athlete_reference.additional_properties = d
        return athlete_reference

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
