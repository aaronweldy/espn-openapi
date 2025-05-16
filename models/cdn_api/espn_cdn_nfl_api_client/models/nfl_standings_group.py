from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nfl_standings_group_division import NflStandingsGroupDivision
    from ..models.nfl_standings_group_standings import NflStandingsGroupStandings


T = TypeVar("T", bound="NflStandingsGroup")


@_attrs_define
class NflStandingsGroup:
    """
    Attributes:
        uid (Union[Unset, str]):
        group_id (Union[Unset, int]):
        name (Union[Unset, str]):
        abbreviation (Union[Unset, str]):
        groups (Union[Unset, List['NflStandingsGroupDivision']]):
        standings (Union[Unset, NflStandingsGroupStandings]):
    """

    uid: Union[Unset, str] = UNSET
    group_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    groups: Union[Unset, List["NflStandingsGroupDivision"]] = UNSET
    standings: Union[Unset, "NflStandingsGroupStandings"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uid = self.uid

        group_id = self.group_id

        name = self.name

        abbreviation = self.abbreviation

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        standings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standings, Unset):
            standings = self.standings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uid is not UNSET:
            field_dict["uid"] = uid
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if name is not UNSET:
            field_dict["name"] = name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if groups is not UNSET:
            field_dict["groups"] = groups
        if standings is not UNSET:
            field_dict["standings"] = standings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nfl_standings_group_division import NflStandingsGroupDivision
        from ..models.nfl_standings_group_standings import NflStandingsGroupStandings

        d = src_dict.copy()
        uid = d.pop("uid", UNSET)

        group_id = d.pop("groupId", UNSET)

        name = d.pop("name", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = NflStandingsGroupDivision.from_dict(groups_item_data)

            groups.append(groups_item)

        _standings = d.pop("standings", UNSET)
        standings: Union[Unset, NflStandingsGroupStandings]
        if isinstance(_standings, Unset):
            standings = UNSET
        else:
            standings = NflStandingsGroupStandings.from_dict(_standings)

        nfl_standings_group = cls(
            uid=uid,
            group_id=group_id,
            name=name,
            abbreviation=abbreviation,
            groups=groups,
            standings=standings,
        )

        nfl_standings_group.additional_properties = d
        return nfl_standings_group

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
