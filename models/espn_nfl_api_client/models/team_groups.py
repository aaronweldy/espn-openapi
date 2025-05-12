from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_groups_parent import TeamGroupsParent


T = TypeVar("T", bound="TeamGroups")


@_attrs_define
class TeamGroups:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 6.
        parent (Union[Unset, TeamGroupsParent]):
        is_conference (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    parent: Union[Unset, "TeamGroupsParent"] = UNSET
    is_conference: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        is_conference = self.is_conference

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if parent is not UNSET:
            field_dict["parent"] = parent
        if is_conference is not UNSET:
            field_dict["isConference"] = is_conference

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_groups_parent import TeamGroupsParent

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, TeamGroupsParent]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = TeamGroupsParent.from_dict(_parent)

        is_conference = d.pop("isConference", UNSET)

        team_groups = cls(
            id=id,
            parent=parent,
            is_conference=is_conference,
        )

        team_groups.additional_properties = d
        return team_groups

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
