from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.flex_column import FlexColumn


T = TypeVar("T", bound="FlexResponse")


@_attrs_define
class FlexResponse:
    """
    Attributes:
        columns (List['FlexColumn']): Layout columns containing content items
    """

    columns: List["FlexColumn"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()
            columns.append(columns_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columns": columns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.flex_column import FlexColumn

        d = src_dict.copy()
        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = FlexColumn.from_dict(columns_item_data)

            columns.append(columns_item)

        flex_response = cls(
            columns=columns,
        )

        flex_response.additional_properties = d
        return flex_response

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
