from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.odds_value_with_outcome_outcome_type import OddsValueWithOutcomeOutcomeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OddsValueWithOutcomeOutcome")


@_attrs_define
class OddsValueWithOutcomeOutcome:
    """
    Attributes:
        type (Union[Unset, OddsValueWithOutcomeOutcomeType]):
    """

    type: Union[Unset, OddsValueWithOutcomeOutcomeType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, OddsValueWithOutcomeOutcomeType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OddsValueWithOutcomeOutcomeType(_type)

        odds_value_with_outcome_outcome = cls(
            type=type,
        )

        odds_value_with_outcome_outcome.additional_properties = d
        return odds_value_with_outcome_outcome

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
