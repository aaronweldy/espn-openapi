from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standing_group import StandingGroup


T = TypeVar("T", bound="Conference")


@_attrs_define
class Conference:
    """
    Attributes:
        id (str):  Example: 8.
        name (str):  Example: American Football Conference.
        standings (StandingGroup):
        uid (Union[Unset, str]):  Example: s:20~l:28~g:8.
        abbreviation (Union[Unset, str]):  Example: AFC.
        is_conference (Union[Unset, bool]):  Example: True.
    """

    id: str
    name: str
    standings: "StandingGroup"
    uid: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    is_conference: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        standings = self.standings.to_dict()

        uid = self.uid

        abbreviation = self.abbreviation

        is_conference = self.is_conference

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "standings": standings,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if is_conference is not UNSET:
            field_dict["isConference"] = is_conference

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.standing_group import StandingGroup

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        standings = StandingGroup.from_dict(d.pop("standings"))

        uid = d.pop("uid", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        is_conference = d.pop("isConference", UNSET)

        conference = cls(
            id=id,
            name=name,
            standings=standings,
            uid=uid,
            abbreviation=abbreviation,
            is_conference=is_conference,
        )

        conference.additional_properties = d
        return conference

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
