from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.odds_value import OddsValue


T = TypeVar("T", bound="OddsTeamCurrent")


@_attrs_define
class OddsTeamCurrent:
    """
    Attributes:
        point_spread (Union[Unset, OddsValue]):
        spread (Union[Unset, OddsValue]):
        money_line (Union[Unset, OddsValue]):
    """

    point_spread: Union[Unset, "OddsValue"] = UNSET
    spread: Union[Unset, "OddsValue"] = UNSET
    money_line: Union[Unset, "OddsValue"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        point_spread: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.point_spread, Unset):
            point_spread = self.point_spread.to_dict()

        spread: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spread, Unset):
            spread = self.spread.to_dict()

        money_line: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.money_line, Unset):
            money_line = self.money_line.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if point_spread is not UNSET:
            field_dict["pointSpread"] = point_spread
        if spread is not UNSET:
            field_dict["spread"] = spread
        if money_line is not UNSET:
            field_dict["moneyLine"] = money_line

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.odds_value import OddsValue

        d = src_dict.copy()
        _point_spread = d.pop("pointSpread", UNSET)
        point_spread: Union[Unset, OddsValue]
        if isinstance(_point_spread, Unset):
            point_spread = UNSET
        else:
            point_spread = OddsValue.from_dict(_point_spread)

        _spread = d.pop("spread", UNSET)
        spread: Union[Unset, OddsValue]
        if isinstance(_spread, Unset):
            spread = UNSET
        else:
            spread = OddsValue.from_dict(_spread)

        _money_line = d.pop("moneyLine", UNSET)
        money_line: Union[Unset, OddsValue]
        if isinstance(_money_line, Unset):
            money_line = UNSET
        else:
            money_line = OddsValue.from_dict(_money_line)

        odds_team_current = cls(
            point_spread=point_spread,
            spread=spread,
            money_line=money_line,
        )

        odds_team_current.additional_properties = d
        return odds_team_current

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
