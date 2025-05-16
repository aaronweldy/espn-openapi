from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoreboard_regulation import ScoreboardRegulation


T = TypeVar("T", bound="ScoreboardFormat")


@_attrs_define
class ScoreboardFormat:
    """
    Attributes:
        regulation (Union[Unset, ScoreboardRegulation]):
    """

    regulation: Union[Unset, "ScoreboardRegulation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        regulation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.regulation, Unset):
            regulation = self.regulation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if regulation is not UNSET:
            field_dict["regulation"] = regulation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scoreboard_regulation import ScoreboardRegulation

        d = src_dict.copy()
        _regulation = d.pop("regulation", UNSET)
        regulation: Union[Unset, ScoreboardRegulation]
        if isinstance(_regulation, Unset):
            regulation = UNSET
        else:
            regulation = ScoreboardRegulation.from_dict(_regulation)

        scoreboard_format = cls(
            regulation=regulation,
        )

        scoreboard_format.additional_properties = d
        return scoreboard_format

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
