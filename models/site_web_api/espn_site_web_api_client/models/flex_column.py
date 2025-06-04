from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.flex_item import FlexItem


T = TypeVar("T", bound="FlexColumn")


@_attrs_define
class FlexColumn:
    """
    Attributes:
        name (str): Column identifier (e.g., leftcolumn, middlecolumn, rightcolumn)
        description (str): Human-readable column description
        items (List['FlexItem']): Content items in this column
    """

    name: str
    description: str
    items: List["FlexItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.flex_item import FlexItem

        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = FlexItem.from_dict(items_item_data)

            items.append(items_item)

        flex_column = cls(
            name=name,
            description=description,
            items=items,
        )

        flex_column.additional_properties = d
        return flex_column

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
