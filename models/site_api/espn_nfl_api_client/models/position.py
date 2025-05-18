from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.position_name import PositionName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roster_athlete import RosterAthlete


T = TypeVar("T", bound="Position")


@_attrs_define
class Position:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, PositionName]): The position category name (e.g., offense, defense, special teams)
        items (Union[Unset, List['RosterAthlete']]): List of athletes in this position category
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, PositionName] = UNSET
    items: Union[Unset, List["RosterAthlete"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.roster_athlete import RosterAthlete

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, PositionName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = PositionName(_name)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = RosterAthlete.from_dict(items_item_data)

            items.append(items_item)

        position = cls(
            id=id,
            name=name,
            items=items,
        )

        position.additional_properties = d
        return position

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
