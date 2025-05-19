from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mlb_roster_athlete_position_parent import MlbRosterAthletePositionParent


T = TypeVar("T", bound="MlbRosterAthletePosition")


@_attrs_define
class MlbRosterAthletePosition:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        abbreviation (Union[Unset, str]):
        leaf (Union[Unset, bool]):
        parent (Union[Unset, MlbRosterAthletePositionParent]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    leaf: Union[Unset, bool] = UNSET
    parent: Union[Unset, "MlbRosterAthletePositionParent"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        display_name = self.display_name

        abbreviation = self.abbreviation

        leaf = self.leaf

        parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if leaf is not UNSET:
            field_dict["leaf"] = leaf
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.mlb_roster_athlete_position_parent import MlbRosterAthletePositionParent

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        leaf = d.pop("leaf", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, MlbRosterAthletePositionParent]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = MlbRosterAthletePositionParent.from_dict(_parent)

        mlb_roster_athlete_position = cls(
            id=id,
            name=name,
            display_name=display_name,
            abbreviation=abbreviation,
            leaf=leaf,
            parent=parent,
        )

        mlb_roster_athlete_position.additional_properties = d
        return mlb_roster_athlete_position

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
