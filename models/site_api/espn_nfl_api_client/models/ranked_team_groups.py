from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ranked_team_groups_parent import RankedTeamGroupsParent


T = TypeVar("T", bound="RankedTeamGroups")


@_attrs_define
class RankedTeamGroups:
    """Conference/group information

    Attributes:
        id (Union[Unset, str]): Conference/group ID
        short_name (Union[Unset, str]): Conference short name
        parent (Union[Unset, RankedTeamGroupsParent]):
        is_conference (Union[Unset, bool]): Whether this is a conference
    """

    id: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    parent: Union[Unset, "RankedTeamGroupsParent"] = UNSET
    is_conference: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        short_name = self.short_name

        parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        is_conference = self.is_conference

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if parent is not UNSET:
            field_dict["parent"] = parent
        if is_conference is not UNSET:
            field_dict["isConference"] = is_conference

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ranked_team_groups_parent import RankedTeamGroupsParent

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        short_name = d.pop("shortName", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, RankedTeamGroupsParent]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = RankedTeamGroupsParent.from_dict(_parent)

        is_conference = d.pop("isConference", UNSET)

        ranked_team_groups = cls(
            id=id,
            short_name=short_name,
            parent=parent,
            is_conference=is_conference,
        )

        ranked_team_groups.additional_properties = d
        return ranked_team_groups

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
