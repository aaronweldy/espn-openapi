from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.competition_status_type import CompetitionStatusType


T = TypeVar("T", bound="CompetitionStatus")


@_attrs_define
class CompetitionStatus:
    """Competition status object (clock, period, state, etc) for a specific competition (game).

    Attributes:
        ref (str):
        clock (float):
        display_clock (str):
        period (int):
        type (CompetitionStatusType):
    """

    ref: str
    clock: float
    display_clock: str
    period: int
    type: "CompetitionStatusType"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref

        clock = self.clock

        display_clock = self.display_clock

        period = self.period

        type = self.type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "clock": clock,
                "displayClock": display_clock,
                "period": period,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.competition_status_type import CompetitionStatusType

        d = src_dict.copy()
        ref = d.pop("$ref")

        clock = d.pop("clock")

        display_clock = d.pop("displayClock")

        period = d.pop("period")

        type = CompetitionStatusType.from_dict(d.pop("type"))

        competition_status = cls(
            ref=ref,
            clock=clock,
            display_clock=display_clock,
            period=period,
            type=type,
        )

        competition_status.additional_properties = d
        return competition_status

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
