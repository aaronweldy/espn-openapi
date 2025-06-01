from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.filter_option import FilterOption


T = TypeVar("T", bound="StatsFilter")


@_attrs_define
class StatsFilter:
    """
    Attributes:
        display_name (str): Display name for filter
        name (str): Filter parameter name
        value (str): Current filter value
        options (List['FilterOption']):
    """

    display_name: str
    name: str
    value: str
    options: List["FilterOption"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name

        name = self.name

        value = self.value

        options = []
        for options_item_data in self.options:
            options_item = options_item_data.to_dict()
            options.append(options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "name": name,
                "value": value,
                "options": options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_option import FilterOption

        d = src_dict.copy()
        display_name = d.pop("displayName")

        name = d.pop("name")

        value = d.pop("value")

        options = []
        _options = d.pop("options")
        for options_item_data in _options:
            options_item = FilterOption.from_dict(options_item_data)

            options.append(options_item)

        stats_filter = cls(
            display_name=display_name,
            name=name,
            value=value,
            options=options,
        )

        stats_filter.additional_properties = d
        return stats_filter

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
