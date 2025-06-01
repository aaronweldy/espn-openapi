from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.odds_value_with_outcome_outcome import OddsValueWithOutcomeOutcome


T = TypeVar("T", bound="OddsValueWithOutcome")


@_attrs_define
class OddsValueWithOutcome:
    """
    Attributes:
        alternate_display_value (str):
        american (str):
        value (Union[Unset, float]):
        display_value (Union[Unset, str]):
        decimal (Union[Unset, float]):
        fraction (Union[Unset, str]):
        outcome (Union[Unset, OddsValueWithOutcomeOutcome]):
    """

    alternate_display_value: str
    american: str
    value: Union[Unset, float] = UNSET
    display_value: Union[Unset, str] = UNSET
    decimal: Union[Unset, float] = UNSET
    fraction: Union[Unset, str] = UNSET
    outcome: Union[Unset, "OddsValueWithOutcomeOutcome"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alternate_display_value = self.alternate_display_value

        american = self.american

        value = self.value

        display_value = self.display_value

        decimal = self.decimal

        fraction = self.fraction

        outcome: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alternateDisplayValue": alternate_display_value,
                "american": american,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value
        if decimal is not UNSET:
            field_dict["decimal"] = decimal
        if fraction is not UNSET:
            field_dict["fraction"] = fraction
        if outcome is not UNSET:
            field_dict["outcome"] = outcome

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.odds_value_with_outcome_outcome import OddsValueWithOutcomeOutcome

        d = src_dict.copy()
        alternate_display_value = d.pop("alternateDisplayValue")

        american = d.pop("american")

        value = d.pop("value", UNSET)

        display_value = d.pop("displayValue", UNSET)

        decimal = d.pop("decimal", UNSET)

        fraction = d.pop("fraction", UNSET)

        _outcome = d.pop("outcome", UNSET)
        outcome: Union[Unset, OddsValueWithOutcomeOutcome]
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = OddsValueWithOutcomeOutcome.from_dict(_outcome)

        odds_value_with_outcome = cls(
            alternate_display_value=alternate_display_value,
            american=american,
            value=value,
            display_value=display_value,
            decimal=decimal,
            fraction=fraction,
            outcome=outcome,
        )

        odds_value_with_outcome.additional_properties = d
        return odds_value_with_outcome

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
