from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.linescore_source import LinescoreSource


T = TypeVar("T", bound="LinescoreItem")


@_attrs_define
class LinescoreItem:
    """
    Attributes:
        ref (str): Reference URL for this linescore
        value (float): Score value for this period
        display_value (str): Display value of the score
        source (LinescoreSource):
        period (int): Period/quarter number
    """

    ref: str
    value: float
    display_value: str
    source: "LinescoreSource"
    period: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        value = self.value

        display_value = self.display_value

        source = self.source.to_dict()

        period = self.period

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "value": value,
                "displayValue": display_value,
                "source": source,
                "period": period,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.linescore_source import LinescoreSource

        d = src_dict.copy()
        ref = d.pop("$ref")

        value = d.pop("value")

        display_value = d.pop("displayValue")

        source = LinescoreSource.from_dict(d.pop("source"))

        period = d.pop("period")

        linescore_item = cls(
            ref=ref,
            value=value,
            display_value=display_value,
            source=source,
            period=period,
        )

        linescore_item.additional_properties = d
        return linescore_item

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
