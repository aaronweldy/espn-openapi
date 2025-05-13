from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.leader_entry import LeaderEntry


T = TypeVar("T", bound="LeaderCategory")


@_attrs_define
class LeaderCategory:
    """
    Attributes:
        name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        leaders (Union[Unset, List['LeaderEntry']]):
    """

    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    leaders: Union[Unset, List["LeaderEntry"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        leaders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.leaders, Unset):
            leaders = []
            for leaders_item_data in self.leaders:
                leaders_item = leaders_item_data.to_dict()
                leaders.append(leaders_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if leaders is not UNSET:
            field_dict["leaders"] = leaders

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.leader_entry import LeaderEntry

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        leaders = []
        _leaders = d.pop("leaders", UNSET)
        for leaders_item_data in _leaders or []:
            leaders_item = LeaderEntry.from_dict(leaders_item_data)

            leaders.append(leaders_item)

        leader_category = cls(
            name=name,
            display_name=display_name,
            leaders=leaders,
        )

        leader_category.additional_properties = d
        return leader_category

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
