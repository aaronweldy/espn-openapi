from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.nhl_position_group_position import NhlPositionGroupPosition
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nhl_athlete import NhlAthlete


T = TypeVar("T", bound="NhlPositionGroup")


@_attrs_define
class NhlPositionGroup:
    """Group of NHL athletes by position

    Attributes:
        position (Union[Unset, NhlPositionGroupPosition]):
        items (Union[Unset, List['NhlAthlete']]):
    """

    position: Union[Unset, NhlPositionGroupPosition] = UNSET
    items: Union[Unset, List["NhlAthlete"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position: Union[Unset, str] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.value

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nhl_athlete import NhlAthlete

        d = src_dict.copy()
        _position = d.pop("position", UNSET)
        position: Union[Unset, NhlPositionGroupPosition]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = NhlPositionGroupPosition(_position)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = NhlAthlete.from_dict(items_item_data)

            items.append(items_item)

        nhl_position_group = cls(
            position=position,
            items=items,
        )

        nhl_position_group.additional_properties = d
        return nhl_position_group

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
