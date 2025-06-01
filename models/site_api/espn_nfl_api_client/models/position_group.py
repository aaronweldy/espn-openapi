from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.roster_athlete import RosterAthlete


T = TypeVar("T", bound="PositionGroup")


@_attrs_define
class PositionGroup:
    """Group of athletes by position category

    Attributes:
        position (str): Position category name (e.g., offense, defense, Pitcher, Forward)
        items (List['RosterAthlete']): List of athletes in this position category
    """

    position: str
    items: List["RosterAthlete"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.roster_athlete import RosterAthlete

        d = src_dict.copy()
        position = d.pop("position")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = RosterAthlete.from_dict(items_item_data)

            items.append(items_item)

        position_group = cls(
            position=position,
            items=items,
        )

        position_group.additional_properties = d
        return position_group

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
