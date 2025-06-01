from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standing_group import StandingGroup


T = TypeVar("T", bound="SoccerStandingsGroup")


@_attrs_define
class SoccerStandingsGroup:
    """Soccer standings group (overall or by group)

    Attributes:
        id (str): Group ID
        name (str): Group name (e.g., "overall", "Group A")
        abbreviation (str): Group abbreviation
        standings (StandingGroup):
        uid (Union[Unset, str]): Unique identifier for the group
    """

    id: str
    name: str
    abbreviation: str
    standings: "StandingGroup"
    uid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        abbreviation = self.abbreviation

        standings = self.standings.to_dict()

        uid = self.uid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "abbreviation": abbreviation,
                "standings": standings,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.standing_group import StandingGroup

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        abbreviation = d.pop("abbreviation")

        standings = StandingGroup.from_dict(d.pop("standings"))

        uid = d.pop("uid", UNSET)

        soccer_standings_group = cls(
            id=id,
            name=name,
            abbreviation=abbreviation,
            standings=standings,
            uid=uid,
        )

        soccer_standings_group.additional_properties = d
        return soccer_standings_group

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
