from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.odds_value import OddsValue


T = TypeVar("T", bound="OddsItemCurrent")


@_attrs_define
class OddsItemCurrent:
    """
    Attributes:
        over (Union[Unset, OddsValue]):
        under (Union[Unset, OddsValue]):
        total (Union[Unset, OddsValue]):
    """

    over: Union[Unset, "OddsValue"] = UNSET
    under: Union[Unset, "OddsValue"] = UNSET
    total: Union[Unset, "OddsValue"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        over: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.over, Unset):
            over = self.over.to_dict()

        under: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.under, Unset):
            under = self.under.to_dict()

        total: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total, Unset):
            total = self.total.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if over is not UNSET:
            field_dict["over"] = over
        if under is not UNSET:
            field_dict["under"] = under
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.odds_value import OddsValue

        d = src_dict.copy()
        _over = d.pop("over", UNSET)
        over: Union[Unset, OddsValue]
        if isinstance(_over, Unset):
            over = UNSET
        else:
            over = OddsValue.from_dict(_over)

        _under = d.pop("under", UNSET)
        under: Union[Unset, OddsValue]
        if isinstance(_under, Unset):
            under = UNSET
        else:
            under = OddsValue.from_dict(_under)

        _total = d.pop("total", UNSET)
        total: Union[Unset, OddsValue]
        if isinstance(_total, Unset):
            total = UNSET
        else:
            total = OddsValue.from_dict(_total)

        odds_item_current = cls(
            over=over,
            under=under,
            total=total,
        )

        odds_item_current.additional_properties = d
        return odds_item_current

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
