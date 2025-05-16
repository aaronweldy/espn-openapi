from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nfl_standings_group import NflStandingsGroup


T = TypeVar("T", bound="NflStandings")


@_attrs_define
class NflStandings:
    """
    Attributes:
        abbreviation (Union[Unset, str]):
        group_id (Union[Unset, int]):
        groups (Union[Unset, List['NflStandingsGroup']]):
        name (Union[Unset, str]):
        uid (Union[Unset, str]):
    """

    abbreviation: Union[Unset, str] = UNSET
    group_id: Union[Unset, int] = UNSET
    groups: Union[Unset, List["NflStandingsGroup"]] = UNSET
    name: Union[Unset, str] = UNSET
    uid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        abbreviation = self.abbreviation

        group_id = self.group_id

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        name = self.name

        uid = self.uid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if groups is not UNSET:
            field_dict["groups"] = groups
        if name is not UNSET:
            field_dict["name"] = name
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_standings_group import NflStandingsGroup

        d = src_dict.copy()
        abbreviation = d.pop("abbreviation", UNSET)

        group_id = d.pop("groupId", UNSET)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = NflStandingsGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        name = d.pop("name", UNSET)

        uid = d.pop("uid", UNSET)

        nfl_standings = cls(
            abbreviation=abbreviation,
            group_id=group_id,
            groups=groups,
            name=name,
            uid=uid,
        )

        nfl_standings.additional_properties = d
        return nfl_standings

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
