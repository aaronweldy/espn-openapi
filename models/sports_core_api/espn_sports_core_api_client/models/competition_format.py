from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.competition_overtime import CompetitionOvertime


T = TypeVar("T", bound="CompetitionFormat")


@_attrs_define
class CompetitionFormat:
    """
    Attributes:
        regulation (CompetitionOvertime):
        overtime (CompetitionOvertime):
    """

    regulation: "CompetitionOvertime"
    overtime: "CompetitionOvertime"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        regulation = self.regulation.to_dict()

        overtime = self.overtime.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "regulation": regulation,
                "overtime": overtime,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.competition_overtime import CompetitionOvertime

        d = src_dict.copy()
        regulation = CompetitionOvertime.from_dict(d.pop("regulation"))

        overtime = CompetitionOvertime.from_dict(d.pop("overtime"))

        competition_format = cls(
            regulation=regulation,
            overtime=overtime,
        )

        competition_format.additional_properties = d
        return competition_format

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
