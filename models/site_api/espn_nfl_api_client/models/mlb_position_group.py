from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mlb_roster_athlete import MlbRosterAthlete


T = TypeVar("T", bound="MlbPositionGroup")


@_attrs_define
class MlbPositionGroup:
    """Group of athletes by position category (MLB)

    Attributes:
        position (str): The position category name (e.g., Pitcher, Catcher, Infield, Outfield, etc.)
        items (List['MlbRosterAthlete']): List of athletes in this position category
    """

    position: str
    items: List["MlbRosterAthlete"]
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
        from ..models.mlb_roster_athlete import MlbRosterAthlete

        d = src_dict.copy()
        position = d.pop("position")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = MlbRosterAthlete.from_dict(items_item_data)

            items.append(items_item)

        mlb_position_group = cls(
            position=position,
            items=items,
        )

        mlb_position_group.additional_properties = d
        return mlb_position_group

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
